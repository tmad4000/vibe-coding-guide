import { normalizeSurface } from "./formatter.mjs";

const SYSTEM_PROMPT = `You are AI OS, an orchestration assistant.\nReturn strict JSON only.\nSchema:\n{\n  "message": "string",\n  "surface": {\n    "type": "none|markdown|html|table",\n    "title": "string",\n    "content": "string",\n    "columns": ["string"],\n    "rows": [["string"]]\n  },\n  "actions": [{"type": "create_terminal_pane", "count": 1}, {"type": "add_task", "title": "..."}],\n  "suggestedCommands": ["pwd", "ls -la"]\n}`;

function extractJsonObject(text) {
  const start = text.indexOf("{");
  if (start === -1) return null;

  let depth = 0;
  let inString = false;
  let escape = false;

  for (let i = start; i < text.length; i += 1) {
    const char = text[i];

    if (inString) {
      if (escape) {
        escape = false;
      } else if (char === "\\") {
        escape = true;
      } else if (char === '"') {
        inString = false;
      }
      continue;
    }

    if (char === '"') {
      inString = true;
      continue;
    }

    if (char === "{") depth += 1;
    if (char === "}") depth -= 1;

    if (depth === 0) {
      return text.slice(start, i + 1);
    }
  }

  return null;
}

export function parseAgentEnvelope(text) {
  const rawText = String(text || "").trim();

  if (!rawText) {
    return null;
  }

  try {
    return JSON.parse(rawText);
  } catch {
    const extracted = extractJsonObject(rawText);
    if (!extracted) return null;
    try {
      return JSON.parse(extracted);
    } catch {
      return null;
    }
  }
}

export function classifyIntent(message) {
  const content = message.toLowerCase();

  if (content.includes("split")) return "split_layout";
  if (content.includes("table") || content.includes("compare") || content.includes("alternatives")) return "comparison";
  if (content.includes("task") || content.includes("todo")) return "task_capture";
  if (content.includes("run") || content.includes("command")) return "command_help";

  return "general";
}

function alternativesTable() {
  return {
    type: "table",
    title: "Terminal + Workbench Alternatives",
    columns: ["Tool", "Strength", "Best For"],
    rows: [
      ["tmux", "Fast split panes + sessions", "Terminal-first control"],
      ["zellij", "Modern pane UX + plugins", "Tmux feel with nicer defaults"],
      ["WezTerm", "GPU terminal + mux", "Terminal + better visuals"],
      ["Warp", "Blocks + command workflows", "Command-centric teams"],
      ["VS Code + terminal", "Integrated editor + tasks", "Code and shell in one space"]
    ],
    content: ""
  };
}

export function buildFallbackReply({ message, mode }) {
  const intent = classifyIntent(message);

  if (intent === "comparison") {
    return {
      message: "I mapped strong alternatives and included where each one fits. If you want, I can generate a migration plan from your current tmux workflow.",
      surface: alternativesTable(),
      actions: [{ type: "add_task", title: "Pick one terminal/workbench stack to trial this week" }],
      suggestedCommands: ["which tmux", "brew info zellij", "wezterm start --always-new-process"]
    };
  }

  if (intent === "split_layout") {
    return {
      message: "I can open multiple terminal panes and keep chat in the primary pane. I created two new panes so you can stage command workflows in parallel.",
      surface: {
        type: mode === "web" ? "html" : "markdown",
        title: "Split Layout Plan",
        content:
          mode === "web"
            ? "<h2>AI OS Split Plan</h2><p>Main chat pane left, programmable surface top-right, shell panes bottom-right.</p>"
            : "## AI OS Split Plan\n- Main chat pane (left)\n- Programmable surface (top-right)\n- Shell panes (bottom-right)"
      },
      actions: [{ type: "create_terminal_pane", count: 2 }],
      suggestedCommands: ["pwd", "ls -la", "git status --short"]
    };
  }

  if (intent === "task_capture") {
    return {
      message: "Captured. I can keep adding your ideas into executable tasks and keep the sidebar synced.",
      surface: {
        type: "markdown",
        title: "Task Flow",
        content: "- Add idea in chat\n- Convert to task action\n- Execute via pane command or surface widget"
      },
      actions: [{ type: "add_task", title: message.slice(0, 120) }],
      suggestedCommands: []
    };
  }

  return {
    message:
      "I can orchestrate your workspace with chat, side tasks, executable commands, and programmable surfaces. Ask me to split panes, run shell workflows, or build a live surface.",
    surface: {
      type: "markdown",
      title: "AI OS Capabilities",
      content:
        "- Persistent task sidebar\n- Multi-pane command runner\n- Optional OpenAI responses integration\n- Surface rendering as markdown, table, or raw HTML"
    },
    actions: [],
    suggestedCommands: ["pwd", "ls -la"]
  };
}

function pullOutputText(responseJson) {
  if (typeof responseJson?.output_text === "string" && responseJson.output_text) {
    return responseJson.output_text;
  }

  const outputs = Array.isArray(responseJson?.output) ? responseJson.output : [];
  const parts = [];

  for (const item of outputs) {
    const content = Array.isArray(item?.content) ? item.content : [];
    for (const block of content) {
      if (typeof block?.text === "string") {
        parts.push(block.text);
      }
    }
  }

  return parts.join("\n").trim();
}

async function fetchOpenAIReply({ message, mode, state }) {
  const apiKey = process.env.OPENAI_API_KEY;
  if (!apiKey) return null;

  const model = process.env.OPENAI_MODEL || "gpt-5-mini";

  const payload = {
    model,
    input: [
      {
        role: "system",
        content: [{ type: "input_text", text: SYSTEM_PROMPT }]
      },
      {
        role: "user",
        content: [
          {
            type: "input_text",
            text: `Mode: ${mode}\nRecent tasks: ${JSON.stringify(state.tasks.slice(0, 4))}\nUser message: ${message}`
          }
        ]
      }
    ],
    reasoning: { effort: "medium" }
  };

  const response = await fetch("https://api.openai.com/v1/responses", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  });

  if (!response.ok) {
    const body = await response.text();
    throw new Error(`OpenAI API error ${response.status}: ${body}`);
  }

  const data = await response.json();
  const text = pullOutputText(data);
  return parseAgentEnvelope(text);
}

export async function generateAssistantReply({ message, mode, state }) {
  let envelope;

  try {
    envelope = await fetchOpenAIReply({ message, mode, state });
  } catch {
    envelope = null;
  }

  if (!envelope) {
    envelope = buildFallbackReply({ message, mode });
  }

  return {
    message: String(envelope.message || "No response generated."),
    surface: normalizeSurface(envelope.surface),
    actions: Array.isArray(envelope.actions) ? envelope.actions : [],
    suggestedCommands: Array.isArray(envelope.suggestedCommands) ? envelope.suggestedCommands : []
  };
}
