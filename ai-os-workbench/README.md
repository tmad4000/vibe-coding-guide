# AI OS Workbench

A two-phase local prototype for an AI-first operating workbench that combines:

- Persistent chat orchestration
- Tmux-style split workspace (chat + programmable surface + command grid)
- Task and ideaflow sidebars
- Optional OpenAI responses integration
- Local shell execution from pane cards

## Why this stack

You asked for something that can become your daily driver rather than a raw terminal.
This build uses a dependency-free Node server plus a polished web UI so it can run immediately and still feel like a native desktop shell.

## Phase 1 delivered

- Desktop-grade UI shell with sidebar + multi-pane workspace
- Resizable split panes (horizontal + vertical)
- Persistent state (tasks, notes, chat log, pane layout)
- Command panes with cwd and output logs

## Phase 2 delivered

- Agent action model (`actions`) to mutate UI state from chat
- Programmable output surface rendering markdown, table, or HTML
- Optional OpenAI backend (`OPENAI_API_KEY`) with strict JSON envelope parsing
- Safety policy for command execution with opt-in unsafe toggle

## Run

```bash
cd /Users/jacobcole/code/ai-os-workbench
npm start
```

Open: [http://localhost:4077](http://localhost:4077)

## Optional OpenAI integration

```bash
export OPENAI_API_KEY="your_key"
export OPENAI_MODEL="gpt-5-mini"
npm start
```

Without an API key, the app runs on deterministic local fallback intelligence.

## Tests

```bash
npm test
```

Covers:

- command safety detection
- shell command execution contract
- agent envelope parsing and fallback behavior
- surface normalization and markdown conversion

## Architecture

- `/Users/jacobcole/code/ai-os-workbench/server.mjs` API server and static serving
- `/Users/jacobcole/code/ai-os-workbench/public` UI app
- `/Users/jacobcole/code/ai-os-workbench/src/core` state, shell, formatting, agent logic
- `/Users/jacobcole/code/ai-os-workbench/tests` core tests

## Next extensions

- native shell embedding via Swift `WKWebView` wrapper + `NSTerminal`
- workspace presets ("Coding", "Planning", "Review")
- background agents for inbox synthesis and issue triage
- integrations for ideaflow and iMessage overlays
