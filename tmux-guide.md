# tmux Guide for Claude Code

Run Claude Code, your server, and logs side-by-side — and keep them running even when you disconnect.

---

## What is tmux?

A terminal multiplexer. Split your terminal into panes, create tabs (windows), and keep everything running in the background.

---

## Getting Started

### Create a session
```bash
tmux new -s dev
```
You're now inside tmux (green bar at bottom).

### The prefix key: `Ctrl+b`
All tmux commands start with `Ctrl+b`, then release, then press another key.

---

## Splitting Your Screen (Panes)

| Keys | Action |
|------|--------|
| `Ctrl+b %` | Split vertical (side by side) |
| `Ctrl+b "` | Split horizontal (top/bottom) |
| `Ctrl+b arrow` | Move between panes |
| `Ctrl+b z` | Zoom/unzoom pane (toggle fullscreen) |
| `Ctrl+b x` | Kill current pane |

---

## Windows (Tabs)

| Keys | Action |
|------|--------|
| `Ctrl+b c` | Create new window |
| `Ctrl+b n` | Next window |
| `Ctrl+b p` | Previous window |
| `Ctrl+b 0-9` | Jump to window by number |
| `Ctrl+b ,` | Rename window |

**Panes** = splits you see simultaneously
**Windows** = tabs you switch between

---

## Session Management

```bash
tmux ls                  # List all sessions
tmux a -t dev            # Attach to named session
tmux a -t 0              # Attach to session 0 (unnamed)
tmux a                   # Attach to most recent session
tmux kill-session -t 0   # Kill specific session
tmux kill-server         # Kill ALL sessions
```

### Detach (leave running)
```
Ctrl+b d
```
Session keeps running. Come back later with `tmux a`.

---

## Example Setup: Claude Code + Server + Logs

```
┌─────────────────┬─────────────────┐
│                 │                 │
│  Claude Code    │  Server         │
│  (claude)       │  (npm run dev)  │
│                 │                 │
│                 ├─────────────────┤
│                 │  Logs           │
│                 │  (tail -f ...)  │
└─────────────────┴─────────────────┘
```

**Step by step:**
1. `tmux new -s dev` — start session
2. Run `claude` (this is pane 0)
3. `Ctrl+b %` — split right (now in pane 1)
4. Run `npm run dev 2>&1 | tee server.log`
5. `Ctrl+b "` — split below (now in pane 2)
6. Run `tail -f server.log`
7. `Ctrl+b ←` — go back to Claude pane

**One-liner to create layout:**
```bash
tmux new -s dev \; split-window -h \; split-window -v \; select-pane -t 0
```

---

## Let Claude See Server Output

### Option A: Log to a file
```bash
npm run dev 2>&1 | tee server.log
```
Then tell Claude: "read server.log"

### Option B: Capture tmux pane
Tell Claude which pane has the server, then:
```bash
tmux capture-pane -p -t 0.1 -S -100
```
- `0.1` = window 0, pane 1
- `-S -100` = last 100 lines

### Option C: Continuous logging
```bash
tmux pipe-pane -o 'cat >> ~/session.log'
```
Logs everything in that pane to a file.

---

## Quick Reference

| Task | Command |
|------|---------|
| Start session | `tmux new -s name` |
| List sessions | `tmux ls` |
| Attach | `tmux a` or `tmux a -t name` |
| Detach | `Ctrl+b d` |
| Split vertical | `Ctrl+b %` |
| Split horizontal | `Ctrl+b "` |
| Move panes | `Ctrl+b arrow` |
| Zoom toggle | `Ctrl+b z` |
| New window | `Ctrl+b c` |
| Next/prev window | `Ctrl+b n` / `Ctrl+b p` |
| Kill pane | `Ctrl+b x` |
| Kill session | `tmux kill-session -t name` |

---

## Copy & Paste

### Copy within tmux
1. `Ctrl+b [` — enter copy mode
2. Navigate with arrow keys or vim keys (h/j/k/l)
3. `Space` — start selection
4. Move to end of text
5. `Enter` or `y` — copy (exits copy mode)

### Paste within tmux
- `Ctrl+b ]`

### Copy to system clipboard (macOS)

**Mouse method:** Start dragging, THEN hold `Shift` or `Option` to maintain selection → copies to system clipboard (bypasses tmux).

**Config method:** Add to `~/.tmux.conf`:
```bash
set -g mode-keys vi
bind -T copy-mode-vi y send-keys -X copy-pipe-and-cancel "pbcopy"
bind -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "pbcopy"
```
Reload: `tmux source-file ~/.tmux.conf`

Now `y` or `Enter` in copy mode copies to system clipboard.

**Manual method:** `tmux show-buffer | pbcopy`

### Copy mode navigation

| Keys | Action |
|------|--------|
| `q` | Exit copy mode |
| `Ctrl+u` / `Ctrl+d` | Page up/down |
| `/` | Search forward |
| `?` | Search backward |
| `n` / `N` | Next/previous match |
