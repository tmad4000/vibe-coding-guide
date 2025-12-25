# Vibe Coding Guide

Tips for getting the most out of Claude Code and AI-assisted development.

**New to the terminal?** Start with the [Minimal Terminal Guide](terminal-guide.md) first.

**Running Claude Code + server + logs?** See the [tmux Guide](tmux-guide.md) for managing multiple terminals.

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

**Other AI coding tools worth trying:**

- **Codex CLI** - OpenAI's coding agent with extra thinking capabilities
- **Gemini CLI** - Google's coding assistant
  ```bash
  gemini --model gemini-2.5-pro --yolo
  ```

**Gemini CLI not working with your Workspace account?** "Google AI Ultra for Business" doesn't support Gemini 3 in CLI yet. Workaround: use a direct API key from [AI Studio](https://aistudio.google.com/), then `export GEMINI_API_KEY="your_key"`.

**Pro tip:** If you're just getting started and want to try it out, ask a friend who's already using Claude Code - they might be able to share access or help you get set up.

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

## 6. Project-Specific Instructions (CLAUDE.md)

Put a `CLAUDE.md` in your project root for project-specific context:

- Tech stack and conventions
- How to run/test the project
- Architecture decisions
- Links to relevant docs

Claude reads this automatically when working in that directory.

---

## 7. Let Claude Plan Complex Tasks

For big features, let Claude use its todo/planning tools. Say things like:
- "Plan out how we'd implement X"
- "Break this into steps"

This helps Claude stay organized and gives you visibility into progress.

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

**Block rm in iCloud (works in zsh and bash):**
```bash
# Add to ~/.zshrc or ~/.bash_profile
function rm() {
  if [[ "$PWD" == *"Mobile Documents"* ]] || [[ "$PWD" == *"iCloud Drive"* ]]; then
    echo "⛔ Refusing to run rm in an iCloud directory"
    return 1
  fi
  command rm "$@"
}
```

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

*Last updated: 2025-12-14*
