# Candidates for the Vibe Coding Guide

Things we've learned that **might** belong in the main guide once we've validated them in real-world use. Each entry: what we learned, evidence it works, what's still uncertain, suggested home in the guide if/when promoted.

---

## 1. Event-driven sidecar pattern for orchestrating long-running subprocess agents (2026-05-20)

**What we learned:** When a "parent" coding agent (Claude Code, Cursor, etc.) launches one or more "child" agents (Codex CLI, sub-Claude, ad-hoc scripts) in tmux sessions for parallel work, **don't rely on single-shot timers (`ScheduleWakeup`-style) to detect completion or hangs.** Timers get preempted by user input, get lost if you forget to chain them, and tell you nothing about whether the child is stuck vs working.

**Working pattern**: A `Bash(run_in_background: true)` sidecar that polls a state file the child writes on exit, plus log-mtime-based idle detection that captures pane content before killing. The sidecar's bash exit produces a real harness completion event — durable, doesn't get preempted by user messages.

**Evidence:** Verified live 2026-05-20. Three parallel Codex sessions (CollabLists/WIT/Noos) — all completed cleanly, the sidecar fired a clean task-notification when one of them ended.

**Still uncertain:**
- Optimal `idle_limit` defaults — current rule says 15min for bulk-execute, 5min for quick. Needs more runs to tune.
- Whether the pattern degrades when running 5+ parallel agents (terminal/tmux limits, system load).
- How to handle the case where the child agent silently goes wrong (writes wrong code, commits something destructive) — the sidecar only detects process state, not work correctness.

**Suggested home:** Probably a new section in `tmux-guide.md` titled "Orchestrating other agents from a coding agent" — describes the pattern, gives the shell skeleton, lists failure modes. Belongs alongside the existing tmux content about managing dev servers.

**Full reference (Jacob's internal stack):** `~/.claude/rules/tool-codex.md` has the production-ready bash skeleton with state files, idle detection, pane forensics.

**Why mention in the public guide:** Anyone using Claude Code / Cursor / Codex CLI in 2026+ will eventually try to fan out parallel agents. The naive approach (timers + sleep) breaks. The pattern here is the durable answer + Codex-vetted.

---

## How to use this file

When something works repeatedly and friends start asking "how do you do that?" — promote the candidate into the main `README.md` or an appropriate sub-guide. When something turns out to be only-Jacob-specific or has too many caveats, leave it here as a cautionary note.

Add new candidates to the top so the newest learnings are easiest to find. Date everything.
