const state = {
  tasks: [],
  notes: [],
  chatLog: [],
  terminalPanes: [],
  layout: {
    horizontalRatio: 0.46,
    verticalRatio: 0.55
  },
  allowUnsafe: false
};

const els = {
  taskList: document.querySelector("#taskList"),
  noteList: document.querySelector("#noteList"),
  addTaskBtn: document.querySelector("#addTaskBtn"),
  addNoteBtn: document.querySelector("#addNoteBtn"),
  chatLog: document.querySelector("#chatLog"),
  chatForm: document.querySelector("#chatForm"),
  chatInput: document.querySelector("#chatInput"),
  modeSelect: document.querySelector("#modeSelect"),
  surfaceTitle: document.querySelector("#surfaceTitle"),
  surfaceContent: document.querySelector("#surfaceContent"),
  terminalGrid: document.querySelector("#terminalGrid"),
  terminalTemplate: document.querySelector("#terminalTemplate"),
  newPaneBtn: document.querySelector("#newPaneBtn"),
  newPaneBtnSecondary: document.querySelector("#newPaneBtnSecondary"),
  allowUnsafeToggle: document.querySelector("#allowUnsafeToggle"),
  horizontalSplit: document.querySelector("#horizontalSplit"),
  verticalSplit: document.querySelector("#verticalSplit")
};

function escapeHtml(input) {
  return String(input)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

async function api(path, payload, method = "POST") {
  const response = await fetch(path, {
    method,
    headers: {
      "Content-Type": "application/json"
    },
    body: method === "GET" ? undefined : JSON.stringify(payload || {})
  });

  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.error || "Request failed");
  }

  return data;
}

function renderTasks() {
  els.taskList.innerHTML = "";

  for (const task of state.tasks) {
    const card = document.createElement("article");
    card.className = `item ${task.done ? "done" : ""}`;

    const top = document.createElement("div");
    top.className = "row";

    const label = document.createElement("label");
    label.style.display = "flex";
    label.style.gap = "8px";

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = task.done;
    checkbox.addEventListener("change", async () => {
      await api("/api/tasks", { op: "toggle", taskId: task.id });
      const found = state.tasks.find((item) => item.id === task.id);
      if (found) found.done = !found.done;
      renderTasks();
    });

    const text = document.createElement("span");
    text.textContent = task.title;

    label.append(checkbox, text);

    const removeBtn = document.createElement("button");
    removeBtn.className = "ghost";
    removeBtn.textContent = "x";
    removeBtn.addEventListener("click", async () => {
      const response = await api("/api/tasks", { op: "delete", taskId: task.id });
      state.tasks = response.tasks;
      renderTasks();
    });

    top.style.display = "flex";
    top.style.justifyContent = "space-between";
    top.style.alignItems = "center";
    top.append(label, removeBtn);

    card.append(top);
    els.taskList.append(card);
  }
}

function renderNotes() {
  els.noteList.innerHTML = "";

  for (const note of state.notes) {
    const card = document.createElement("article");
    card.className = "item";
    card.innerHTML = `<p>${escapeHtml(note.text)}</p>`;

    const removeBtn = document.createElement("button");
    removeBtn.className = "ghost";
    removeBtn.textContent = "Delete";
    removeBtn.addEventListener("click", async () => {
      const response = await api("/api/notes", { op: "delete", noteId: note.id });
      state.notes = response.notes;
      renderNotes();
    });

    card.append(removeBtn);
    els.noteList.append(card);
  }
}

function renderChat() {
  els.chatLog.innerHTML = "";

  for (const message of state.chatLog.slice(-120)) {
    const block = document.createElement("article");
    block.className = `chat-msg ${message.role}`;
    block.textContent = message.content;
    els.chatLog.append(block);
  }

  els.chatLog.scrollTop = els.chatLog.scrollHeight;
}

function renderSurface(surface) {
  if (!surface || surface.type === "none") return;

  els.surfaceTitle.textContent = surface.title || "Programmable Surface";

  if (surface.type === "html") {
    els.surfaceContent.innerHTML = surface.content;
    return;
  }

  if (surface.type === "table") {
    const columns = Array.isArray(surface.columns) ? surface.columns : [];
    const rows = Array.isArray(surface.rows) ? surface.rows : [];

    const head = `<thead><tr>${columns.map((column) => `<th>${escapeHtml(column)}</th>`).join("")}</tr></thead>`;
    const body = `<tbody>${rows
      .map((row) => `<tr>${row.map((value) => `<td>${escapeHtml(value)}</td>`).join("")}</tr>`)
      .join("")}</tbody>`;

    els.surfaceContent.innerHTML = `<table>${head}${body}</table>`;
    return;
  }

  const markdown = escapeHtml(surface.content || "").replaceAll("\n", "<br>");
  els.surfaceContent.innerHTML = `<div>${markdown}</div>`;
}

function runAction(action) {
  if (!action || typeof action !== "object") return;

  if (action.type === "create_terminal_pane") {
    const count = Number(action.count || 1);
    for (let i = 0; i < count; i += 1) {
      const pane = {
        id: crypto.randomUUID(),
        title: `Pane ${state.terminalPanes.length + 1}`,
        cwd: "/Users/jacobcole/code",
        lastCommand: "",
        lastOutput: "Ready"
      };
      state.terminalPanes.push(pane);
    }
    renderTerminalGrid();
  }

  if (action.type === "add_task" && action.title) {
    state.tasks.unshift({
      id: crypto.randomUUID(),
      title: action.title,
      done: false,
      createdAt: new Date().toISOString()
    });
    renderTasks();
  }
}

function renderTerminalGrid() {
  els.terminalGrid.innerHTML = "";

  for (const pane of state.terminalPanes) {
    const fragment = els.terminalTemplate.content.cloneNode(true);
    const card = fragment.querySelector(".terminal-card");
    const titleInput = fragment.querySelector(".pane-title");
    const cwdInput = fragment.querySelector(".pane-cwd");
    const commandInput = fragment.querySelector(".pane-command");
    const output = fragment.querySelector(".terminal-output");
    const runButton = fragment.querySelector(".pane-run");

    card.dataset.paneId = pane.id;
    titleInput.value = pane.title;
    cwdInput.value = pane.cwd || "/Users/jacobcole/code";
    commandInput.value = pane.lastCommand || "";
    output.textContent = pane.lastOutput || "Ready";

    titleInput.addEventListener("change", () => {
      pane.title = titleInput.value.trim() || pane.title;
    });

    runButton.addEventListener("click", async () => {
      const command = commandInput.value.trim();
      if (!command) return;

      output.textContent = "Running...";

      try {
        const response = await api("/api/execute", {
          command,
          cwd: cwdInput.value.trim(),
          paneId: pane.id,
          allowUnsafe: state.allowUnsafe
        });

        pane.cwd = cwdInput.value.trim();
        pane.lastCommand = command;
        pane.lastOutput = [response.result.stdout, response.result.stderr]
          .filter(Boolean)
          .join("\n") || "Command completed with no output.";

        output.textContent = `${pane.lastOutput}\n\n(exit ${response.result.exitCode}, ${response.result.durationMs}ms)`;
      } catch (error) {
        output.textContent = error.message;
      }
    });

    commandInput.addEventListener("keydown", (event) => {
      if (event.key === "Enter") {
        event.preventDefault();
        runButton.click();
      }
    });

    els.terminalGrid.append(fragment);
  }
}

async function sendChat(message) {
  if (!message.trim()) return;

  state.chatLog.push({
    role: "user",
    content: message,
    createdAt: new Date().toISOString()
  });
  renderChat();

  const mode = els.modeSelect.value;

  try {
    const response = await api("/api/chat", { message, mode });
    state.chatLog = response.state.chatLog;
    state.tasks = response.state.tasks;
    state.notes = response.state.notes;
    state.terminalPanes = response.state.terminalPanes;

    renderChat();
    renderTasks();
    renderNotes();
    renderTerminalGrid();

    if (response.reply.surface) {
      renderSurface(response.reply.surface);
    }
  } catch (error) {
    state.chatLog.push({
      role: "assistant",
      content: `Error: ${error.message}`,
      createdAt: new Date().toISOString()
    });
    renderChat();
  }
}

function setupSplit(splitEl) {
  const axis = splitEl.classList.contains("horizontal") ? "x" : "y";
  const divider = splitEl.querySelector('.divider[data-axis="' + axis + '"]');
  const isHorizontal = axis === "x";

  const applyRatio = (ratio) => {
    const clamped = Math.max(0.22, Math.min(0.78, ratio));
    splitEl.style.setProperty("--primary-size", `${Math.round(clamped * 100)}%`);
    splitEl.dataset.ratio = String(clamped);
  };

  applyRatio(Number(splitEl.dataset.ratio || 0.5));

  divider.addEventListener("pointerdown", (event) => {
    event.preventDefault();

    const rect = splitEl.getBoundingClientRect();

    function onMove(moveEvent) {
      const ratio = isHorizontal
        ? (moveEvent.clientX - rect.left) / rect.width
        : (moveEvent.clientY - rect.top) / rect.height;
      applyRatio(ratio);
    }

    function onUp() {
      window.removeEventListener("pointermove", onMove);
      window.removeEventListener("pointerup", onUp);

      state.layout.horizontalRatio = Number(els.horizontalSplit.dataset.ratio);
      state.layout.verticalRatio = Number(els.verticalSplit.dataset.ratio);
      api("/api/layout", { layout: state.layout }).catch(() => {});
    }

    window.addEventListener("pointermove", onMove);
    window.addEventListener("pointerup", onUp);
  });
}

function bindEvents() {
  els.chatForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const message = els.chatInput.value;
    els.chatInput.value = "";
    sendChat(message);
  });

  els.chatInput.addEventListener("keydown", (event) => {
    if ((event.metaKey || event.ctrlKey) && event.key === "Enter") {
      event.preventDefault();
      els.chatForm.requestSubmit();
    }
  });

  const addPane = () => {
    state.terminalPanes.push({
      id: crypto.randomUUID(),
      title: `Pane ${state.terminalPanes.length + 1}`,
      cwd: "/Users/jacobcole/code",
      lastCommand: "",
      lastOutput: "Ready"
    });
    renderTerminalGrid();
  };

  els.newPaneBtn.addEventListener("click", addPane);
  els.newPaneBtnSecondary.addEventListener("click", addPane);

  els.allowUnsafeToggle.addEventListener("change", () => {
    state.allowUnsafe = els.allowUnsafeToggle.checked;
  });

  els.addTaskBtn.addEventListener("click", async () => {
    const title = prompt("Task title:");
    if (!title) return;
    const response = await api("/api/tasks", { op: "add", title });
    state.tasks = response.tasks;
    renderTasks();
  });

  els.addNoteBtn.addEventListener("click", async () => {
    const text = prompt("Capture note:");
    if (!text) return;
    const response = await api("/api/notes", { op: "add", text });
    state.notes = response.notes;
    renderNotes();
  });

  window.addEventListener("keydown", (event) => {
    if ((event.metaKey || event.ctrlKey) && event.shiftKey && event.key.toLowerCase() === "k") {
      event.preventDefault();
      addPane();
    }
  });
}

async function init() {
  const payload = await api("/api/state", null, "GET");
  state.tasks = payload.state.tasks;
  state.notes = payload.state.notes;
  state.chatLog = payload.state.chatLog;
  state.terminalPanes = payload.state.terminalPanes;
  state.layout = payload.state.layout;

  els.horizontalSplit.dataset.ratio = String(state.layout.horizontalRatio || 0.46);
  els.verticalSplit.dataset.ratio = String(state.layout.verticalRatio || 0.55);

  bindEvents();
  setupSplit(els.horizontalSplit);
  setupSplit(els.verticalSplit);
  renderTasks();
  renderNotes();
  renderChat();
  renderTerminalGrid();
}

init().catch((error) => {
  els.chatLog.innerHTML = `<article class="chat-msg assistant">Boot error: ${escapeHtml(error.message)}</article>`;
});
