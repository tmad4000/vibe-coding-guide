import { mkdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.join(__dirname, "..", "..");
const DATA_DIR = path.join(ROOT, "data");
const STATE_PATH = path.join(DATA_DIR, "state.json");

const defaultState = {
  version: 1,
  tasks: [
    {
      id: "task-seed-1",
      title: "Capture one operating-system-level workflow to automate",
      done: false,
      createdAt: new Date().toISOString()
    },
    {
      id: "task-seed-2",
      title: "Open a split terminal pane and run a command",
      done: false,
      createdAt: new Date().toISOString()
    }
  ],
  notes: [
    {
      id: "note-seed-1",
      text: "Ideaflow sync idea: each note can become an executable action card.",
      createdAt: new Date().toISOString()
    }
  ],
  chatLog: [],
  commandLog: [],
  layout: {
    horizontalRatio: 0.46,
    verticalRatio: 0.55
  },
  terminalPanes: [
    {
      id: "pane-1",
      title: "System Pane",
      cwd: process.cwd(),
      lastCommand: "",
      lastOutput: "",
      updatedAt: new Date().toISOString()
    }
  ]
};

function mergeDefaults(state) {
  return {
    ...defaultState,
    ...state,
    layout: {
      ...defaultState.layout,
      ...(state.layout || {})
    },
    tasks: Array.isArray(state.tasks) ? state.tasks : defaultState.tasks,
    notes: Array.isArray(state.notes) ? state.notes : defaultState.notes,
    chatLog: Array.isArray(state.chatLog) ? state.chatLog : defaultState.chatLog,
    commandLog: Array.isArray(state.commandLog) ? state.commandLog : defaultState.commandLog,
    terminalPanes: Array.isArray(state.terminalPanes) && state.terminalPanes.length > 0
      ? state.terminalPanes
      : defaultState.terminalPanes
  };
}

async function ensureStateFile() {
  await mkdir(DATA_DIR, { recursive: true });

  try {
    await readFile(STATE_PATH, "utf8");
  } catch {
    await writeFile(STATE_PATH, JSON.stringify(defaultState, null, 2));
  }
}

export async function loadState() {
  await ensureStateFile();
  const raw = await readFile(STATE_PATH, "utf8");
  const parsed = JSON.parse(raw);
  return mergeDefaults(parsed);
}

export async function saveState(state) {
  await ensureStateFile();
  const merged = mergeDefaults(state);
  await writeFile(STATE_PATH, JSON.stringify(merged, null, 2));
}

export async function updateState(mutator) {
  const state = await loadState();
  await mutator(state);
  await saveState(state);
  return state;
}

export function applyAction(state, action) {
  if (!action || typeof action !== "object") {
    return;
  }

  if (action.type === "create_terminal_pane") {
    const paneCount = Number(action.count || 1);
    for (let i = 0; i < paneCount; i += 1) {
      state.terminalPanes.push({
        id: crypto.randomUUID(),
        title: `Pane ${state.terminalPanes.length + 1}`,
        cwd: process.cwd(),
        lastCommand: "",
        lastOutput: "",
        updatedAt: new Date().toISOString()
      });
    }
  }

  if (action.type === "add_task" && action.title) {
    state.tasks.unshift({
      id: crypto.randomUUID(),
      title: String(action.title),
      done: false,
      createdAt: new Date().toISOString()
    });
  }
}
