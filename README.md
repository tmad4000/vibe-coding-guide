# Vibe Coding Guide

Tips for getting the most out of Claude Code and AI-assisted development.

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

## 5. Project-Specific Instructions (CLAUDE.md)

Put a `CLAUDE.md` in your project root for project-specific context:

- Tech stack and conventions
- How to run/test the project
- Architecture decisions
- Links to relevant docs

Claude reads this automatically when working in that directory.

---

## 6. Let Claude Plan Complex Tasks

For big features, let Claude use its todo/planning tools. Say things like:
- "Plan out how we'd implement X"
- "Break this into steps"

This helps Claude stay organized and gives you visibility into progress.

---

## 7. Be Specific About What You Want

Good: "Add a login form with email/password fields, validation, and error states"
Less good: "Add login"

The more context upfront, the fewer back-and-forth iterations.

---

## 8. Use "Don't Commit" When Experimenting

If you have auto-commit enabled but want to experiment:
- "Try this but don't commit"
- "Make this change, no commit"

You stay in control.

---

## 9. Ask Claude to Explain Before Changing

If you're learning or want to understand:
- "Explain this code before we change it"
- "What does this function do?"
- "Walk me through the data flow here"

Great for onboarding to new codebases.

---

## 10. MCP Servers Worth Exploring

- **Playwright** - Browser automation and testing
- **Chrome DevTools** - Real-time browser debugging
- **Filesystem** - Enhanced file operations
- **GitHub** - PR and issue management
- **Postgres/SQLite** - Direct database access

Check available MCPs at: https://github.com/modelcontextprotocol/servers

---

## 11. Meta: Keep This Guide Updated

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

*Last updated: 2025-11-25*
