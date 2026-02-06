# Vibe Coding Guide

Tips for getting the most out of Claude Code and AI-assisted development.

**New to the terminal?** Start with the [Minimal Terminal Guide](terminal-guide.md) first.

**Running Claude Code + server + logs?** See the [tmux Guide](tmux-guide.md) for managing multiple terminals, or use **iTerm2** with split panes (simpler copy/paste).

**Terminal Recommendation: iTerm2**

For macOS, [iTerm2](https://iterm2.com/) is better than the default Terminal.app:
- Native split panes (`Cmd+D` vertical, `Cmd+Shift+D` horizontal) - run server + Claude Code side by side
- Standard macOS copy/paste (`Cmd+C`/`Cmd+V`) - no tmux clipboard gymnastics
- Hotkey window (drop-down terminal with a keystroke)
- Better search, autocomplete, and shell integration
- Window titles can show current directory (see setup below)

**Show current directory in window/tab titles:**
1. Go to **iTerm2 → Preferences → Profiles → General**
2. Under "Title", select **PWD** from the dropdown
3. You can select multiple options (e.g., "Job Name" + "PWD") to show both the running command and directory

**When you still need tmux:**
- Background processes that survive terminal close
- SSH sessions you want to detach/reattach
- Sharing sessions between multiple users
- Scripted layouts that auto-setup on connect

For visual-only multi-pane work, iTerm2 splits are simpler. For persistent background processes, tmux is still the way.

**Opinionated take on agents and tmux:** Mario Zechner's [pi coding agent](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/) argues against background bash and sub-agents in favor of tmux for observability. Key points:
- Use tmux instead of background processes - you can see and interact with what's running
- Avoid sub-agents (black boxes within black boxes) - spawn visible tmux sessions instead
- Full observability beats convenience - you can always `tmux attach` to see what's happening

---

## 0. Get API Access & Use the Best Model

Before anything else, you need API access to use Claude Code:

1. **Get an Anthropic API key** at [console.anthropic.com](https://console.anthropic.com)
2. **Or use Claude Pro/Max subscription** - Claude Code works with your subscription
3. **Set your API key:**
   ```bash
   export ANTHROPIC_API_KEY=your-key-here
   # Or add to your ~/.zshrc or ~/.bashrc for persistence
   ```

**Switch to the latest model (Opus 4.5):**

By default, Claude Code uses Sonnet. To use Opus 4.5 (the most capable model):

```bash
# In Claude Code, run:
/model opus
```

Or set it permanently in `~/.claude/settings.json`:
```json
{
  "model": "opus"
}
```

**Skip permissions for faster workflow:**

By default, Claude Code asks permission for many actions. To skip these prompts:

```bash
claude --dangerously-skip-permissions
```

**Pro tip:** Use TextExpander (or similar) to expand a short snippet like `cld` into the full command. Much faster than typing it every time.

**Extended thinking mode:**

For complex problems, enable extended thinking to let Claude reason more deeply:

```bash
# In Claude Code:
/think
```

This gives Claude more "thinking time" for harder tasks.

**Keyboard shortcut: Clear input line** `#shortcut`

Use `Ctrl+U` to clear the entire input line without interrupting Claude. This is the standard readline shortcut - deletes the whole line while staying in the session.

- `Ctrl+U` = clear line (keep session running)
- `Ctrl+C` = interrupt/cancel current operation

If you typed something and want to start over, `Ctrl+U` is cleaner than `Ctrl+C` which treats it as an interrupt action.

**Other AI coding tools worth trying:**

- **Codex CLI** - OpenAI's coding agent with extra thinking capabilities
- **Gemini CLI** - Google's coding assistant
  ```bash
  gemini --model gemini-2.5-pro --yolo
  ```

**Gemini CLI not working with your Workspace account?** "Google AI Ultra for Business" doesn't support Gemini 3 in CLI yet. Workaround: use a direct API key from [AI Studio](https://aistudio.google.com/), then `export GEMINI_API_KEY="your_key"`.

**Pro tip:** If you're just getting started and want to try it out, ask a friend who's already using Claude Code - they might be able to share access or help you get set up.

**Mobile input - Willow Voice:**

When vibe coding from your phone (dictating prompts to Claude Code via SSH, remote sessions, or mobile apps), [Willow Voice](https://willowvoice.com/) is excellent:

- **Full keyboard + dictation** - Unlike competitors that only show a numeric keyboard during voice input, Willow has a full keyboard so you can quickly edit words without switching keyboards
- **Context-aware formatting** - Automatically formats messages based on the app context (code, email, chat)
- **100+ languages** - Great for multilingual workflows
- **Custom vocabulary** - Define technical terms, project names, function names

Free tier: 2,000 words/week. Unlimited: $12/month.

This matters for vibe coding because you often need to mix dictation with quick typed edits - saying "add a function called" then typing `handleUserAuth` is faster than spelling it out loud.

---

## 1. Use Playwright MCP for Browser Automation

**This is the game-changer.** Install the Playwright MCP server to let Claude directly interact with browsers - click, type, navigate, screenshot, and test your web apps.

**Global install (recommended for web devs):** Add to `~/.claude/mcp.json`:
```json
{
  "mcpServers": {
    "playwright": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}
```

Now Claude can:
- Run end-to-end tests
- Debug UI issues by actually seeing and interacting with your app
- Automate repetitive browser tasks

**Global vs. per-project MCPs:**
- `~/.claude/mcp.json` = available in ALL projects (good for Playwright if you do web dev)
- Project-level = configured per-project in Claude Code settings

**Downsides of global MCPs:** Minimal. The MCP only launches a browser when you actually use it. Slight startup overhead and extra tools in context, but negligible for 1-2 MCPs.

---

## 2. Chrome DevTools MCP for Debugging

Connect Claude directly to Chrome DevTools for real-time debugging:

- Inspect network requests and responses
- View console logs and errors
- Take snapshots of page state
- Debug performance issues with traces
- See exactly what your users see

This is incredibly powerful for debugging issues where you need to see what's actually happening in the browser.

**Setup:** Best as a per-project MCP (not global) since it requires a running Chrome instance with debugging enabled:
```bash
# Launch Chrome with debugging
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
```

**When to use which:**
- **Playwright** = automated testing, CI/CD, headless browser work → good as global
- **Chrome DevTools** = active debugging sessions → enable per-project when needed

### Auto-Detect Electron Apps (Provisional)

Chrome DevTools MCP normally launches its own Chrome instance. But Electron apps also expose DevTools! Use this wrapper script to auto-detect and connect to whatever's running:

**Create `~/.claude/scripts/devtools-mcp-wrapper.sh`:**
```bash
#!/bin/bash
# Auto-detect DevTools endpoint and launch chrome-devtools-mcp

# Check common ports for DevTools
for port in 9222 9223 9224 9225; do
  if curl -s "http://127.0.0.1:$port/json/version" >/dev/null 2>&1; then
    TARGET=$(curl -s "http://127.0.0.1:$port/json/list" 2>/dev/null | head -1 | grep -o '"title":"[^"]*"' | head -1 | cut -d'"' -f4)
    echo "[devtools-wrapper] Connecting to existing DevTools on port $port (${TARGET:-unknown})" >&2
    exec npx chrome-devtools-mcp@latest --browserUrl "http://127.0.0.1:$port" "$@"
  fi
done

# No existing DevTools found, launch Chrome normally
echo "[devtools-wrapper] No existing DevTools found, launching Chrome" >&2
exec npx chrome-devtools-mcp@latest "$@"
```

```bash
chmod +x ~/.claude/scripts/devtools-mcp-wrapper.sh
```

**Update `~/.claude/mcp.json`:**
```json
"chrome-devtools": {
  "command": "/Users/yourusername/.claude/scripts/devtools-mcp-wrapper.sh",
  "args": []
}
```

**Behavior:**
| Scenario | What happens |
|----------|--------------|
| No DevTools running | Launches Chrome normally |
| Electron app running on 9223 | Connects to Electron |
| Chrome with DevTools on 9222 | Connects to existing Chrome |

**Gotcha:** If Electron is running and you want a fresh Chrome, either kill Electron first or run `npx chrome-devtools-mcp@latest` directly. The wrapper always prefers existing DevTools.

---

## 2.5. Native App Debugging: Build a CLI

**For Swift/macOS/iOS apps**, Chrome DevTools won't help you. The solution: **build a CLI wrapper** so AI agents can test your app programmatically.

**Why this matters:**
- Web apps have Chrome DevTools MCP - agents can inspect, click, navigate
- Native apps are opaque to AI without a programmatic interface
- Screenshots + OCR is slow and unreliable
- A CLI makes debugging 10x faster

**What to expose via CLI:**
```bash
# Example CLI for a notes app
myapp list                    # List items (JSON output)
myapp create --title "Test"   # Create item
myapp show <id>               # Show item details
myapp test-connection         # Verify API connectivity
```

**Key requirements:**
1. **JSON output** - AI can parse structured data, not just text
2. **Error codes** - Return non-zero on failure
3. **Screen recording permissions** - Grant to Terminal.app for screenshot tools

**Setup screen recording (macOS):**
1. System Preferences → Privacy & Security → Screen Recording
2. Enable for Terminal.app (or iTerm, Warp, etc.)
3. Restart terminal

**When to use which:**
| App Type | Debugging Tool |
|----------|---------------|
| Web apps | Chrome DevTools MCP, Playwright |
| Backend/API | Server logs, curl |
| Native macOS/iOS | CLI wrapper + Peekaboo MCP |
| Electron | Chrome DevTools (it's web under the hood) |

**Pro tip:** [Peekaboo](https://github.com/steipete/peekaboo) is an MCP server for macOS accessibility inspection - useful for seeing UI state without screenshots.

---

## 3. Alternative: Server Logs for Backend Debugging

If you're debugging backend issues or don't need browser interaction, simply:

- Tail your server logs in a terminal
- Copy/paste relevant errors to Claude
- Or point Claude at your log files directly

Sometimes simpler is better. Not everything needs an MCP - for backend work, logs + Claude's code understanding is often enough.

---

## 4. Global Claude Instructions (~/.claude/CLAUDE.md)

Create `~/.claude/CLAUDE.md` to set rules that apply to ALL your projects:

```markdown
# Example global instructions

# Auto-commit after tasks
- Automatically commit after completing each task
- Use conventional commits (feat:, fix:, docs:, etc.)

# Keep requirements updated
- When I mention product specs, update REQUIREMENTS.md
```

This saves you from repeating yourself across projects.

---

## 5. Sound Notifications When Claude Needs Input

Don't babysit Claude! Set up sound alerts so you can context-switch while Claude works:

**Add to `~/.claude/settings.json`:**
```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "idle_prompt",
        "hooks": [
          {
            "type": "command",
            "command": "afplay /System/Library/Sounds/Glass.aiff"
          }
        ]
      },
      {
        "matcher": "permission_prompt",
        "hooks": [
          {
            "type": "command",
            "command": "afplay /System/Library/Sounds/Ping.aiff"
          }
        ]
      }
    ]
  }
}
```

**What this does:**
- **Glass sound** = Claude is done and waiting for input
- **Ping sound** = Claude needs permission for something

**Customize sounds:** Browse `/System/Library/Sounds/` for options (Submarine, Blow, Funk, etc.)

**Bonus - add desktop notification too:**
```bash
# Create ~/bin/claude-alert.sh
#!/bin/bash
afplay /System/Library/Sounds/Glass.aiff
osascript -e 'display notification "Claude Code needs input" with title "Claude Code"'
```

Then use `"command": "~/bin/claude-alert.sh"` in your hook.

**Linux users:** Replace `afplay` with `paplay` or `aplay`.

---

## 5.5. Keep Mac Awake for Long Sessions (Lid Closed)

Running a long Claude Code session and want to close your laptop lid? By default, Macs sleep when the lid closes, killing your terminal sessions. Here's how to prevent that.

**The Problem:**
- `caffeinate` only prevents *idle* sleep, not lid-close sleep
- Apps like Amphetamine + Amphetamine Enhancer work but require manual toggling
- You need `sudo pmset -a disablesleep 1` but it requires password every time

**The Solution: `nosleep` script with passwordless sudo**

**1. Set up passwordless pmset (one-time):**
```bash
echo 'YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/pmset' | sudo tee /etc/sudoers.d/pmset
sudo chmod 0440 /etc/sudoers.d/pmset
```

Replace `YOUR_USERNAME` with your actual username. This allows only pmset without password, not all sudo commands.

**2. Install the nosleep script:**

Download [`nosleep.sh`](./nosleep.sh) from this repo, or:

```bash
curl -o /usr/local/bin/nosleep https://raw.githubusercontent.com/tmad4000/vibe-coding-guide/main/nosleep.sh
chmod +x /usr/local/bin/nosleep
```

**3. Usage:**
```bash
nosleep              # 30 minutes (default)
nosleep 3600         # 1 hour
nosleep --on         # Indefinitely (until --off)
nosleep --off        # Re-enable sleep
nosleep --status     # Check current settings
nosleep --help       # Full documentation
```

**Key features:**
- **Trap for cleanup:** If you Ctrl+C, sleep is automatically re-enabled
- **Timed mode:** Set specific duration, sleep re-enables when done
- **Status check:** See current sleep settings

**Workflow for long Claude Code sessions:**
```bash
# Start a long session
nosleep --on
claude --dangerously-skip-permissions

# When done (or Ctrl+C will clean up)
nosleep --off
```

**Why not Amphetamine?** Amphetamine + Amphetamine Enhancer works great for GUI workflows, but for terminal-heavy vibe coding, a script is faster and can be automated. Use whichever fits your workflow.

### Enable Wake for Wi-Fi Network Access

For remote access (SSH) when you're away, enable `networkoversleep` so your Mac can wake from sleep for network requests:

```bash
# Enable only when plugged in (recommended)
sudo pmset -c networkoversleep 1

# Or enable for both battery and AC power
sudo pmset -a networkoversleep 1
```

**The flags:**
- `-c` = charger/AC only
- `-b` = battery only
- `-a` = all (both)

**Battery impact:** Minimal (~0.5% extra per day). The Wi-Fi radio stays in low-power listening mode. If you already have Power Nap enabled, this adds negligible drain on top of that.

**When to use what:**

| Scenario | Solution |
|----------|----------|
| Active Claude Code session, closing lid | `nosleep --on` |
| Away from home, want SSH access if Mac sleeps | `networkoversleep 1` |
| Both (belt and suspenders) | Use both |

**Note about `caffeinate`:** Standard `caffeinate` only prevents *idle* sleep. It does NOT prevent lid-close (clamshell) sleep, and it doesn't help the Mac wake for incoming SSH connections. For remote access, you need either `nosleep` or `networkoversleep`.

---

## 6. Project-Specific Instructions (CLAUDE.md)

Put a `CLAUDE.md` in your project root for project-specific context:

- Tech stack and conventions
- How to run/test the project
- Architecture decisions
- Links to relevant docs

Claude reads this automatically when working in that directory.

---

## 6.5. Always Display Version Numbers

**Show your app version** in the user interface - ideally in the account menu, settings, or footer. This helps with:

- **Debugging**: "What version are you on?" is the first support question
- **Deployment verification**: Confirm changes actually deployed
- **User awareness**: People like knowing they have the latest

**Implementation:**

```typescript
// Define version (sync with package.json)
const APP_VERSION = '1.0.0';

// Display in user dropdown footer
<div className="text-xs text-muted text-center py-1">
  v{APP_VERSION}
</div>
```

**Best locations** (in order of preference):
1. User account dropdown (bottom)
2. App sidebar footer
3. Settings page
4. Page footer

For multi-app ecosystems (like microservices), displaying version helps users know which service has an issue.

---

## 7. Let Claude Plan Complex Tasks

For big features, let Claude use its todo/planning tools. Say things like:
- "Plan out how we'd implement X"
- "Break this into steps"

This helps Claude stay organized and gives you visibility into progress.

---

## 7.5. Use Beads for Multi-Session Issue Tracking

**[Beads](https://github.com/steveyegge/beads)** is a git-backed issue tracker designed for AI-assisted workflows. Great for tracking work across sessions, managing dependencies, and keeping context when Claude's memory resets.

**Install:**
```bash
npm install -g @anthropic-ai/beads
```

**Initialize in your project:**
```bash
bd init myproject
```

**Critical setup (do this once globally):**
```bash
bd setup claude
```

This installs Claude Code hooks that auto-inject `bd prime` (beads workflow context) at session start and after compaction. **Without this, Claude won't know the beads best practices** and may use commands incorrectly.

**Basic workflow:**
```bash
bd create "Add login feature" --type feature    # Create issue
bd create "Fix auth bug" --parent myproj-abc    # Subtask under epic
bd ready                                         # Find unblocked work
bd update myproj-123 --status in_progress       # Claim work
bd close myproj-123                             # Complete work
```

**Why use beads over TodoWrite:**
- Persists across sessions (survives context compaction)
- Tracks dependencies between tasks
- Works with multiple Claude instances/agents
- Git-synced for collaboration

**Pro tip:** For epics with subtasks, always use `--parent`:
```bash
bd create "Epic: OAuth" --type epic
bd create "Research providers" --parent myproj-abc
bd create "Implement OAuth flow" --parent myproj-abc
```

**Regression tracking:** When you tell Claude "we lost the ability to X" or "X stopped working", it should immediately create a P1 bug ticket. Regressions are easy to forget mid-conversation - tracking them ensures they get fixed. Add this to your CLAUDE.md:
```markdown
## Regression Tracking
When the user reports "we lost the ability to X" or "X stopped working":
1. Immediately create a bug ticket with priority P1
2. Include what worked before and when it stopped (if known)
```

**Recurring issues pattern:** Some bugs keep coming back — the fix works, but the underlying conditions that caused the bug recur (timing issues, race conditions, state management edge cases). Use beads labels to track these, with a focus on documenting *why* they recur, not just *that* they recur.

```bash
# When debugging, check for known recurring issues first
bd list --label recurring

# When a bug recurs:
bd reopen <id> --reason "recurred: <context>"  # If closed
bd label add <id> recurring                     # Add label if not already
```

**The key insight:** A recurring label without root cause notes is just a list of frustrations. When marking something recurring, add a "Why this recurs" section to the ticket description. This helps future sessions skip re-diagnosis and go straight to the architectural issue.

Document the pattern (not the individual issues) in your project's CLAUDE.md:
```markdown
## Recurring Issues Pattern

When debugging, first check for known recurring issues:
bd list --label recurring

When a bug recurs:
1. If closed, reopen: `bd reopen <id> --reason "recurred: <context>"`
2. Add label if not already: `bd label add <id> recurring`
3. Add/update a "Why this recurs" section in the ticket description
4. Fix the issue, then close normally

When closing a recurring issue:
- Document what fixed it THIS time
- Note whether the root cause was addressed or just the symptom
- If only the symptom was fixed, note what a permanent fix would require
```

This keeps beads as the source of truth — no separate markdown file to maintain. The `recurring` label is the canonical list, and the ticket descriptions carry the institutional memory.

---

## 8. Be Specific About What You Want

Good: "Add a login form with email/password fields, validation, and error states"
Less good: "Add login"

The more context upfront, the fewer back-and-forth iterations.

---

## 9. Use "Don't Commit" When Experimenting

If you have auto-commit enabled but want to experiment:
- "Try this but don't commit"
- "Make this change, no commit"

You stay in control.

---

## 10. Ask Claude to Explain Before Changing

If you're learning or want to understand:
- "Explain this code before we change it"
- "What does this function do?"
- "Walk me through the data flow here"

Great for onboarding to new codebases.

---

## 11. Managing Local Dev Servers with Caddy

When you're running multiple projects on localhost, it's easy to forget which port is which. **Caddy** gives you friendly `.localhost` URLs with automatic HTTPS.

**Why Caddy:**
- `.localhost` domains auto-resolve (no `/etc/hosts` editing)
- Auto-generates trusted HTTPS certs
- Simple config, actively maintained
- Your apps still work on their original ports too

**Install:**
```bash
brew install caddy
```

**Create `~/Caddyfile`:**
```
# Use http:// prefix to avoid HTTPS cert issues

http://myapp.localhost {
    reverse_proxy localhost:5173
}

http://api.localhost {
    reverse_proxy localhost:8080
}

# Add more as needed
```

**Run:**
```bash
caddy run --config ~/Caddyfile
```

**Access:**
- `http://myapp.localhost` → your app on 5173
- `http://localhost:5173` still works too

**Adding new projects with Claude:**

Just say: "Add this project to Caddy" — Claude will check the port and update your Caddyfile.

To make this work reliably, add to your `~/.claude/CLAUDE.md`:
```markdown
# Local Dev Server Routing (Caddy)

I use Caddy for local dev subdomains. Config is at `~/Caddyfile`.

When adding a project to Caddy:
1. Use `.localhost` domains (NOT `.local`) — they auto-resolve, no /etc/hosts needed
2. Use `http://` prefix to avoid HTTPS certificate issues
3. Check what port the app runs on (grep config files or use `lsof -iTCP -sTCP:LISTEN | grep node` if running)
4. Add to `~/Caddyfile`:
   http://projectname.localhost {
       reverse_proxy localhost:PORT
   }
5. Reload with: `caddy reload --config ~/Caddyfile`
```

**List registered projects:**
```bash
cat ~/Caddyfile
```

**Reload after changes:**
```bash
caddy reload --config ~/Caddyfile
```

---

## 12. Permission Tiers: Choose Your Safety Level

Speed up your workflow by choosing a permission tier that matches your trust level. Three pre-configured tiers available:

### Tier 1: Read-Only (140+ permissions)
**For:** Exploring unfamiliar code, learning, maximum safety

Zero modifications. Pure exploration:
- ✅ All file reading (cat, grep, find, rg)
- ✅ Git inspection (status, log, diff, blame)
- ✅ System info (ps, lsof, uptime)
- ❌ No Write/Edit operations
- ❌ No git add/commit/push

```bash
cp ~/Documents/vibe-coding-guide/permissions-read-only.json ~/.claude/settings.local.json
```

### Tier 2: Create-Only (200+ permissions) ⭐ RECOMMENDED
**For:** Active development on trusted projects

Can add/modify, but **never delete**. Perfect for git-tracked development:
- ✅ Everything from Read-Only
- ✅ Write, Edit (file operations)
- ✅ Git write ops (add, commit, push, merge)
- ✅ File creation (mkdir, touch, cp, mv)
- ✅ Package install (npm install, pip install)
- ✅ Build/test (npm run, cargo test, pytest)
- ❌ **Blocks all rm commands**
- ❌ **Blocks git reset --hard, git clean**
- ❌ **Blocks git push --force**
- ❌ **Blocks package uninstall**

```bash
cp ~/Documents/vibe-coding-guide/permissions-create-only.json ~/.claude/settings.local.json
```

**Why Create-Only is safe:** Every change is tracked in git. You can always revert:
```bash
git reset --hard HEAD  # Undo all changes
git clean -fd          # Remove untracked files
```

### Tier 3: Development (coming soon)
Full development including controlled deletions with PreToolUse hooks.

### Quick Comparison

| Operation | Read-Only | Create-Only | Development |
|-----------|-----------|-------------|-------------|
| Read files | ✅ | ✅ | ✅ |
| Git status/log/diff | ✅ | ✅ | ✅ |
| Edit files | ❌ | ✅ | ✅ |
| Git add/commit/push | ❌ | ✅ | ✅ |
| Install packages | ❌ | ✅ | ✅ |
| Delete files (rm) | ❌ | ❌ | ⚠️ |
| Force push | ❌ | ❌ | ❌ |

⚠️ = Allowed with restrictions

**Full documentation:** See [PERMISSIONS.md](PERMISSIONS.md) for complete details, safety tips, and customization.

**Switch anytime:**
```bash
# More restrictive for sensitive work
cp ~/Documents/vibe-coding-guide/permissions-read-only.json ~/.claude/settings.local.json

# More permissive for trusted projects
cp ~/Documents/vibe-coding-guide/permissions-create-only.json ~/.claude/settings.local.json
```

Changes take effect immediately.

---

## 13. Safety: Protect Against Accidental Deletions

**Critical if using `--dangerously-skip-permissions`:** When you skip permission prompts for faster workflow, you lose the safety net. Add PreToolUse hooks to block catastrophic commands.

**Real incidents:** Multiple users have accidentally wiped home directories with `rm -rf` commands when Claude misunderstood cleanup tasks. [See GitHub issues](https://github.com/anthropics/claude-code/issues?q=rm+-rf+deleted).

### Quick Setup

Copy [`validate-bash-command.sh`](./validate-bash-command.sh) to intercept dangerous commands before execution:

```bash
mkdir -p ~/.claude/hooks
cp validate-bash-command.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/validate-bash-command.sh
```

The script blocks:

1. **Catastrophic patterns:** `rm -rf /`, `rm -rf ~`, `rm -rf $HOME`, `rm -rf *`
2. **Home directory paths:** Anything starting with `~/`, `/Users/`, `/home/`
3. **Current directory deletion:** `rm -rf .` or `rm -rf ..`
4. **Recursive rm from home:** If you're in `~`, blocks ALL `rm -r` commands
5. **iCloud Drive:** ANY deletion from `~/Library/Mobile Documents/`

**Config in `~/.claude/settings.json`:**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/validate-bash-command.sh"
          }
        ]
      }
    ]
  }
}
```

The hook receives JSON on stdin, checks patterns, and returns exit code 2 to block dangerous commands.

**What's still allowed:**
- `rm -rf node_modules` from project directories
- `rm -rf dist`, `.next`, `build` (relative paths from projects)
- Normal file operations

**If a command is blocked but you need it:**
- Run it manually in your terminal
- Use relative paths instead of absolute (`./folder` vs `~/code/folder`)
- Move to trash: `mv ~/old-project ~/.Trash/`

**Version control your Claude config:** Put `~/.claude` in a private GitHub repo so you can track changes and rollback if needed.

### Gemini CLI Safety

**Gemini CLI doesn't support PreToolUse hooks**, so it can't intercept commands before execution. Instead, add safety rules to `~/.gemini/GEMINI.md`:

```markdown
# Critical: Protect Against Accidental Deletions

**NEVER run these commands:**
- `rm -rf /`, `rm -rf ~`, `rm -rf $HOME`
- `rm -rf *`, `rm -rf .`, `rm -rf ..`
- Any `rm` on paths starting with `~/`, `/Users/`, `/home/`
- ANY deletion from iCloud Drive (`~/Library/Mobile Documents/`)

**When in home directory:**
- Do NOT use recursive `rm` commands
- Ask user to confirm first

**If deletion requested from important paths:**
1. Ask user to confirm the exact path
2. Suggest safer alternatives (move to trash)
3. Remind that manual terminal deletion is safer
```

This relies on the AI following instructions rather than technical enforcement. Less reliable than hooks, but better than nothing.

### Shell-Level Protection (Manual Commands)

Add these functions to your shell profile for protection even when typing commands manually:

**Block catastrophic rm patterns + iCloud (works in zsh and bash):**
```bash
# Add to ~/.zshrc or ~/.bash_profile
function rm() {
  # Block catastrophic patterns (use /bin/rm to bypass if truly needed)
  case "$*" in
    *-rf\ /*|*-rf\ ~*|*-rf\ \$HOME*|*-rf\ .)
      echo "⛔ Blocked catastrophic rm. Use /bin/rm if you really mean it."
      return 1 ;;
  esac
  # Block in iCloud directories
  if [[ "$PWD" == *"Mobile Documents"* ]] || [[ "$PWD" == *"iCloud Drive"* ]]; then
    echo "⛔ No rm in iCloud directories"
    return 1
  fi
  command rm "$@"
}
```

This blocks patterns you'd never intentionally type (`rm -rf /`, `rm -rf ~`, `rm -rf .`) while allowing normal operations like `rm -rf node_modules`.

**Visual iCloud warning in prompt (zsh):**
```bash
# Add to ~/.zshrc
function in_icloud() {
  [[ "$PWD" == *"Mobile Documents"* ]] || [[ "$PWD" == *"iCloud Drive"* ]]
}

setopt PROMPT_SUBST
PROMPT='%F{cyan}%n@%m%f %F{yellow}%~%f $(in_icloud && echo "%F{red}⚠️ iCloud%f") %# '
```

**Visual iCloud warning in prompt (bash):**
```bash
# Add to ~/.bash_profile
function in_icloud() {
  [[ "$PWD" == *"Mobile Documents"* ]] || [[ "$PWD" == *"iCloud Drive"* ]]
}

PS1='\[\033[36m\]\u@\h\[\033[0m\] \[\033[33m\]\w\[\033[0m\]$(in_icloud && echo " \[\033[31m\]⚠️ iCloud\[\033[0m\]") \$ '
```

These protect you from accidentally running dangerous commands yourself, not just when AI does it.

**Start new shells in ~/code (not home):**
```bash
# Add to ~/.zshrc or ~/.bash_profile
# Reduces risk of accidentally running commands in home directory
if [[ $PWD == $HOME ]]; then
  cd ~/code  # or your preferred projects directory
fi
```

**Keep API keys out of shell configs:**
```bash
# In ~/.zshrc or ~/.bash_profile - add this line:
[[ -f ~/.secrets ]] && source ~/.secrets

# Then create ~/.secrets (never commit this file):
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
```

This way your `.zshrc` is safe to share/commit, and secrets stay in a separate file.

---

## 14. MCP Servers Worth Exploring

- **Playwright** - Browser automation and testing
- **Chrome DevTools** - Real-time browser debugging
- **Filesystem** - Enhanced file operations
- **GitHub** - PR and issue management
- **Postgres/SQLite** - Direct database access
- **Gemini CLI** - Use Google's Gemini AI from within Claude Code

### Gemini CLI MCP Setup

Want to use Gemini (Google's AI) from within Claude Code? Install the Gemini CLI MCP:

```bash
claude mcp add gemini-cli -- npx -y gemini-mcp-tool
```

This adds Gemini as a tool that Claude can call. Useful for:
- Cross-referencing answers between AI models
- Tasks where Gemini might have different/complementary capabilities
- Having Claude orchestrate multiple AI models

**Prerequisites:**
1. Gemini CLI installed: `npm install -g @anthropic-ai/gemini-cli`
2. Authenticated with Google: `gemini login`

Check available MCPs at: https://github.com/modelcontextprotocol/servers

---

## 15. Fetching JavaScript-Heavy Pages (Gemini shares, etc.)

Some URLs can't be fetched with `curl` or standard web tools because they require JavaScript to render the content. Examples:
- Gemini share links (`gemini.google.com/share/...`)
- ChatGPT share links
- Many modern SPAs

**The problem:** `curl` just returns an empty HTML shell with JavaScript loaders.

**The solution:** Use Chrome DevTools MCP to navigate with a real browser:

```
# In Claude Code, just ask:
"Fetch the content from https://gemini.google.com/share/abc123"
```

Claude will:
1. Open the URL in Chrome via DevTools MCP
2. Wait for content to load
3. Take a snapshot of the rendered page
4. Extract and summarize the content

**Why this works:**
- Uses your real Chrome session (not a headless browser)
- No automation detection issues since it's your actual browser
- Can access pages that require authentication (if you're logged in)

**Setup:** Make sure Chrome DevTools MCP is configured (see section 2).

---

## 16. Meta: Keep This Guide Updated

This guide itself is maintained using Claude Code! Here's the workflow:

**How this guide stays current:**
- The guide lives at `~/Documents/vibe-coding-guide/README.md`
- When I learn new tips, I just tell Claude "update the vibe guide with X"
- Claude edits, commits, and pushes automatically
- Friends see updates in real-time at this repo

**To set this up yourself:**
Add to your `~/.claude/CLAUDE.md`:
```markdown
# Vibe Coding Guide
- The vibe coding guide lives at `~/Documents/vibe-coding-guide/README.md`
- When updating the guide, commit and push changes to GitHub so friends can see updates
```

---

## Contributing

Got tips to add? **Pull requests welcome!**

1. Fork this repo
2. Add your tips
3. Submit a PR

Or just open an issue with your suggestion.

---

*Last updated: 2026-02-05*
