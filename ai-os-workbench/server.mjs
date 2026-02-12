import { createServer } from "node:http";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { generateAssistantReply } from "./src/core/agent.mjs";
import { runCommand } from "./src/core/shell.mjs";
import { applyAction, loadState, saveState, updateState } from "./src/core/state.mjs";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const PUBLIC_DIR = path.join(__dirname, "public");

const PORT = Number(process.env.PORT || 4077);
const HOST = process.env.HOST || "127.0.0.1";

function sendJson(res, statusCode, payload) {
  res.writeHead(statusCode, {
    "Content-Type": "application/json; charset=utf-8",
    "Cache-Control": "no-store"
  });
  res.end(JSON.stringify(payload));
}

function sendText(res, statusCode, body, contentType) {
  res.writeHead(statusCode, {
    "Content-Type": contentType,
    "Cache-Control": "no-store"
  });
  res.end(body);
}

async function parseBody(req) {
  const chunks = [];
  for await (const chunk of req) {
    chunks.push(chunk);
  }

  if (chunks.length === 0) {
    return {};
  }

  const raw = Buffer.concat(chunks).toString("utf8");
  try {
    return JSON.parse(raw);
  } catch {
    return {};
  }
}

function contentTypeFromFile(filePath) {
  if (filePath.endsWith(".html")) return "text/html; charset=utf-8";
  if (filePath.endsWith(".css")) return "text/css; charset=utf-8";
  if (filePath.endsWith(".js")) return "text/javascript; charset=utf-8";
  if (filePath.endsWith(".json")) return "application/json; charset=utf-8";
  return "text/plain; charset=utf-8";
}

async function serveStatic(req, res) {
  const safePath = req.url === "/" ? "/index.html" : req.url;
  const filePath = path.join(PUBLIC_DIR, safePath.replace(/^\/+/, ""));

  if (!filePath.startsWith(PUBLIC_DIR)) {
    sendText(res, 403, "Forbidden", "text/plain; charset=utf-8");
    return;
  }

  try {
    const file = await readFile(filePath);
    sendText(res, 200, file, contentTypeFromFile(filePath));
  } catch {
    sendText(res, 404, "Not found", "text/plain; charset=utf-8");
  }
}

const server = createServer(async (req, res) => {
  try {
    if (req.method === "GET" && req.url === "/api/health") {
      sendJson(res, 200, {
        status: "ok",
        mode: process.env.OPENAI_API_KEY ? "openai+local" : "local-fallback"
      });
      return;
    }

    if (req.method === "GET" && req.url === "/api/state") {
      const state = await loadState();
      sendJson(res, 200, { state });
      return;
    }

    if (req.method === "POST" && req.url === "/api/chat") {
      const body = await parseBody(req);
      const message = String(body.message || "").trim();
      const mode = String(body.mode || "assistant");

      if (!message) {
        sendJson(res, 400, { error: "message is required" });
        return;
      }

      const stateBefore = await loadState();
      stateBefore.chatLog.push({
        id: crypto.randomUUID(),
        role: "user",
        content: message,
        mode,
        createdAt: new Date().toISOString()
      });

      const reply = await generateAssistantReply({
        message,
        mode,
        state: stateBefore
      });

      stateBefore.chatLog.push({
        id: crypto.randomUUID(),
        role: "assistant",
        content: reply.message,
        surface: reply.surface,
        actions: reply.actions,
        suggestedCommands: reply.suggestedCommands,
        createdAt: new Date().toISOString()
      });

      for (const action of reply.actions || []) {
        applyAction(stateBefore, action);
      }

      await saveState(stateBefore);
      sendJson(res, 200, {
        reply,
        state: {
          tasks: stateBefore.tasks,
          notes: stateBefore.notes,
          layout: stateBefore.layout,
          terminalPanes: stateBefore.terminalPanes,
          chatLog: stateBefore.chatLog
        }
      });
      return;
    }

    if (req.method === "POST" && req.url === "/api/execute") {
      const body = await parseBody(req);
      const command = String(body.command || "").trim();
      const cwd = String(body.cwd || process.cwd());
      const paneId = String(body.paneId || "default");
      const allowUnsafe = Boolean(body.allowUnsafe);

      if (!command) {
        sendJson(res, 400, { error: "command is required" });
        return;
      }

      const result = await runCommand({
        command,
        cwd,
        allowUnsafe,
        timeoutMs: 30_000
      });

      await updateState((draft) => {
        draft.commandLog.push({
          id: crypto.randomUUID(),
          paneId,
          command,
          cwd,
          ...result,
          createdAt: new Date().toISOString()
        });

        const pane = draft.terminalPanes.find((item) => item.id === paneId);
        if (pane) {
          pane.cwd = cwd;
          pane.lastCommand = command;
          pane.lastOutput = `${result.stdout}${result.stderr ? `\n${result.stderr}` : ""}`;
          pane.updatedAt = new Date().toISOString();
        }
      });

      sendJson(res, 200, { result });
      return;
    }

    if (req.method === "POST" && req.url === "/api/tasks") {
      const body = await parseBody(req);
      const op = String(body.op || "");
      const taskId = String(body.taskId || "");
      const title = String(body.title || "").trim();

      const state = await updateState((draft) => {
        if (op === "add" && title) {
          draft.tasks.unshift({
            id: crypto.randomUUID(),
            title,
            done: false,
            createdAt: new Date().toISOString()
          });
        }

        if (op === "toggle" && taskId) {
          const task = draft.tasks.find((item) => item.id === taskId);
          if (task) task.done = !task.done;
        }

        if (op === "delete" && taskId) {
          draft.tasks = draft.tasks.filter((item) => item.id !== taskId);
        }
      });

      sendJson(res, 200, { tasks: state.tasks });
      return;
    }

    if (req.method === "POST" && req.url === "/api/notes") {
      const body = await parseBody(req);
      const op = String(body.op || "");
      const noteId = String(body.noteId || "");
      const text = String(body.text || "").trim();

      const state = await updateState((draft) => {
        if (op === "add" && text) {
          draft.notes.unshift({
            id: crypto.randomUUID(),
            text,
            createdAt: new Date().toISOString()
          });
        }

        if (op === "delete" && noteId) {
          draft.notes = draft.notes.filter((item) => item.id !== noteId);
        }
      });

      sendJson(res, 200, { notes: state.notes });
      return;
    }

    if (req.method === "POST" && req.url === "/api/layout") {
      const body = await parseBody(req);

      const state = await updateState((draft) => {
        draft.layout = {
          ...draft.layout,
          ...(body.layout || {})
        };
      });

      sendJson(res, 200, { layout: state.layout });
      return;
    }

    await serveStatic(req, res);
  } catch (error) {
    sendJson(res, 500, {
      error: error.message,
      stack: process.env.NODE_ENV === "development" ? error.stack : undefined
    });
  }
});

server.listen(PORT, HOST, () => {
  console.log(`ai-os-workbench listening on http://${HOST}:${PORT}`);
});
