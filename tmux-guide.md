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

**Simpler alternative:** Use [iTerm2](https://iterm2.com/) with native split panes instead of tmux - standard `Cmd+C`/`Cmd+V` just works. Only use tmux when you need background processes or detach/reattach.

### Copy within tmux
1. `Ctrl+b [` — enter copy mode
2. Navigate with arrow keys or vim keys (h/j/k/l)
3. `Space` — start selection
4. Move to end of text
5. `Enter` or `y` — copy (exits copy mode)

### Paste within tmux
- `Ctrl+b ]`

### Copy to system clipboard (macOS)

**Mouse method (with mouse mode on):**
1. Click and drag to start selection
2. Hold `Shift` while dragging (or tap it mid-selection)
3. Selection completes and copies to system clipboard (bypasses tmux buffer)

**Recommended config for auto-copy:** Add to `~/.tmux.conf`:
```bash
# Enable mouse mode
set -g mouse on

# Vi mode for copy
set -g mode-keys vi

# Auto-copy to system clipboard when mouse selection ends
bind -T copy-mode-vi MouseDragEnd1Pane send-keys -X copy-pipe-and-cancel "pbcopy"

# y and Enter also copy to system clipboard
bind -T copy-mode-vi y send-keys -X copy-pipe-and-cancel "pbcopy"
bind -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "pbcopy"

# v to start selection (like vim)
bind -T copy-mode-vi v send -X begin-selection
```
Reload: `tmux source-file ~/.tmux.conf`

Now:
- Mouse drag → auto-copies to system clipboard on release
- `y` or `Enter` in copy mode → copies to system clipboard
- `v` starts selection (vim-style)

**Manual method:** `tmux show-buffer | pbcopy`

### Copy mode navigation

| Keys | Action |
|------|--------|
| `q` | Exit copy mode |
| `Ctrl+u` / `Ctrl+d` | Page up/down |
| `/` | Search forward |
| `?` | Search backward |
| `n` / `N` | Next/previous match |

---

## Why tmux Over Background Agents?

Mario Zechner's [pi coding agent](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/) makes a strong case for tmux over background processes:

> "There's simply no need for background bash."

**Key arguments:**
- **Observability:** You can always `tmux attach` to see exactly what's running
- **Interactivity:** You can jump into a session and co-debug with the agent
- **No black boxes:** Sub-agents spawned in the background are invisible; tmux sessions are not
- **Simpler debugging:** When something hangs, you can see why

**The pattern:** Instead of background processes, spawn named tmux sessions:
```bash
# Start a dev server in a named session
tmux new-session -d -s backend 'cd ~/project && npm run dev'

# Check on it anytime
tmux attach -t backend

# List all running sessions
tmux ls
```

This gives you the benefits of background execution with full visibility.

---

## Session Persistence: Never Lose Your Layout

By default, tmux sessions disappear when the server restarts (reboot, crash, `tmux kill-server`). Three plugins fix this:

### Install TPM (Tmux Plugin Manager)

```bash
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```

### Configure `~/.tmux.conf`

Add to your config:

```bash
# --- Plugins ---
set -g @plugin "tmux-plugins/tpm"
set -g @plugin "tmux-plugins/tmux-resurrect"
set -g @plugin "tmux-plugins/tmux-continuum"
set -g @plugin "tmux-plugins/tmux-logging"

# Auto-save sessions every 15 minutes
# Auto-restore last saved session on tmux start
set -g @continuum-restore "on"

# Auto-start tmux on boot (macOS)
set -g @continuum-boot "on"

# Log all pane output automatically
set -g @logging-auto-start "on"
set -g @logging-path "$HOME/tmux-logs"

# Initialize TPM (keep at bottom of .tmux.conf)
run "~/.tmux/plugins/tpm/tpm"
```

Install plugins: `Ctrl+b I` (capital I), or run:
```bash
~/.tmux/plugins/tpm/bin/install_plugins
```

Then reload: `tmux source-file ~/.tmux.conf`

### What Each Plugin Does

| Plugin | Purpose |
|--------|---------|
| **tmux-resurrect** | Save/restore sessions manually (`Ctrl+b Ctrl+s` / `Ctrl+b Ctrl+r`) |
| **tmux-continuum** | Auto-saves every 15 min, auto-restores on tmux start |
| **tmux-logging** | Logs all terminal output per-pane to `~/tmux-logs/` |

### What Gets Saved (and What Doesn't)

**Saved by Resurrect/Continuum:**
- Session names, window names, layouts
- Pane splits and positions
- Working directories
- The command name running in each pane

**NOT saved:**
- Terminal scrollback / output history ← **tmux-logging fixes this**
- Running process state (SSH connections, interactive programs)
- Environment variables beyond basics

After a restore, you get the right tabs and pane layout, but every pane starts a fresh shell in the correct directory. Programs need to be restarted.

### Restoring Specific Programs

To auto-restart certain programs on restore, add:

```bash
set -g @resurrect-processes 'ssh mosh node python "npm run dev"'
```

Only works for simple commands — not interactive state.

### Key Bindings

| Keys | Action |
|------|--------|
| `Ctrl+b Ctrl+s` | Save session (Resurrect) |
| `Ctrl+b Ctrl+r` | Restore last saved session |
| `Ctrl+b Shift+P` | Toggle logging on/off for current pane |
| `Ctrl+b Alt+p` | Save visible pane content to file |
| `Ctrl+b Alt+Shift+P` | Save complete pane scrollback history |

### Restore from an Older Snapshot

Continuum saves snapshots to `~/.tmux/resurrect/`. The `last` symlink points to the most recent. To restore an older one:

```bash
# List available snapshots
ls -lt ~/.tmux/resurrect/

# Point to the one you want
ln -sf tmux_resurrect_20260227T225745.txt ~/.tmux/resurrect/last

# Then restore
# Ctrl+b Ctrl+r
```

### Enable Logging on All Existing Panes

New panes auto-log with `@logging-auto-start "on"`, but panes that existed before the plugin was installed need a one-time toggle. Either press `Ctrl+b Shift+P` in each pane, or run this to enable logging on all panes at once:

```bash
tmux list-panes -a -F '#{session_name}:#{window_index}.#{pane_index} #{session_name} #{window_index} #{pane_index}' | while read target sess win pane; do
  file="$HOME/tmux-logs/tmux-${sess}-${win}-${pane}-$(date +%Y%m%dT%H%M%S).log"
  tmux pipe-pane -t "$target" "exec cat - | sed -E 's/(\[([0-9]{1,3}((;[0-9]{1,3})*)?)?[m|K]||]0;[^]+|[[:space:]]+$)//g' >> $file"
  tmux set-option -gq "@${sess}_${win}_${pane}" "logging"
done
```

### The Bottom Line

With this setup, rebooting your machine means:
1. tmux auto-starts on login (Continuum)
2. Your sessions, windows, and pane layouts are restored (Resurrect)
3. Going forward, all terminal output is logged to `~/tmux-logs/` (Logging)

You lose running processes but keep the workspace structure and a full record of what happened.
