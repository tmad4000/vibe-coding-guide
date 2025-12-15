# Claude Code Permission Tiers

Three permission profiles for different workflows. Choose based on your trust level and task.

## Quick Start

Copy the contents of your chosen tier into `~/.claude/settings.local.json`:

```bash
# Read-Only: Safe exploration, no modifications
cp ~/Documents/vibe-coding-guide/permissions-read-only.json ~/.claude/settings.local.json

# Create-Only: Development with git, but no deletions (RECOMMENDED)
cp ~/Documents/vibe-coding-guide/permissions-create-only.json ~/.claude/settings.local.json

# Development: Full development including controlled deletions
# (coming soon)
```

---

## Tier 1: Read-Only (140+ permissions)

**Use when:** Exploring unfamiliar codebases, learning, or maximum safety

**Philosophy:** Zero modifications. Pure exploration and analysis.

**Includes:**
- ✅ All file reading (cat, head, tail, less, more, grep, find, rg)
- ✅ Git inspection (status, log, diff, show, blame, reflog)
- ✅ System info (ps, lsof, netstat, uptime, whoami)
- ✅ Package inspection (npm list, pip list, brew list)
- ✅ Version checks (all --version flags)
- ✅ Data tools (jq, yq, xmllint)
- ✅ Archive inspection (tar -t, unzip -l, zipinfo)
- ✅ Tmux read operations

**Excludes:**
- ❌ All Write/Edit operations
- ❌ Git write operations (add, commit, push)
- ❌ File creation/modification
- ❌ Package installation
- ❌ Any system modifications

**Safety:** Maximum. Impossible to modify anything.

---

## Tier 2: Create-Only (200+ permissions) ⭐ RECOMMENDED

**Use when:** Active development on trusted projects

**Philosophy:** You can add and modify, but never remove. Git-tracked projects are safe because changes can be reverted.

**Everything from Read-Only, plus:**
- ✅ Write, Edit (Claude Code file operations)
- ✅ Git write ops (add, commit, push, stash, merge, pull, fetch)
- ✅ File creation (mkdir, touch, cp, mv, echo)
- ✅ Package install (npm install, pip install, cargo build)
- ✅ Build/test (npm run, make, cargo test, pytest, jest)
- ✅ Archive extraction (tar -x, unzip, gunzip)
- ✅ wget for downloads
- ✅ chmod, chown for permissions

**Explicitly denies:**
- ❌ rm (all file deletion)
- ❌ git reset --hard, git clean (destructive git)
- ❌ git push --force (history rewriting)
- ❌ git branch -D (branch deletion)
- ❌ npm uninstall, pip uninstall (package removal)

**Safety:** High. Can create/modify but never delete. Combined with git, all changes are reversible:
```bash
# Undo any changes
git reset --hard HEAD
git clean -fd
```

**Why this is safe:**
- Every change is tracked in git
- No ability to delete files
- No ability to delete git history
- Force push blocked
- Can always revert to previous state

---

## Tier 3: Development (coming soon)

**Use when:** Full-trust scenarios on your own projects

**Philosophy:** Complete development workflow with smart guardrails.

**Everything from Create-Only, plus:**
- Controlled rm operations (project files only, with hooks)
- git reset, git clean (with warnings)
- Package uninstall operations
- More sudo commands

**Still blocked:**
- rm -rf ~, rm -rf /, rm -rf *
- Operations on system directories
- Deletion in iCloud Drive

**Requires:** PreToolUse hooks for safety (see vibe-coding-guide README.md section 13)

---

## Comparison Table

| Operation | Read-Only | Create-Only | Development |
|-----------|-----------|-------------|-------------|
| Read files | ✅ | ✅ | ✅ |
| Git status, log, diff | ✅ | ✅ | ✅ |
| System info | ✅ | ✅ | ✅ |
| Edit files | ❌ | ✅ | ✅ |
| Git add/commit/push | ❌ | ✅ | ✅ |
| Create files/dirs | ❌ | ✅ | ✅ |
| Install packages | ❌ | ✅ | ✅ |
| Run build/test | ❌ | ✅ | ✅ |
| Delete files (rm) | ❌ | ❌ | ⚠️ |
| Uninstall packages | ❌ | ❌ | ⚠️ |
| git reset --hard | ❌ | ❌ | ⚠️ |
| Force push | ❌ | ❌ | ❌ |

⚠️ = Allowed with restrictions/hooks

---

## Switching Between Tiers

You can switch tiers anytime by copying a different file:

```bash
# Switch to Read-Only for exploring new codebase
cp ~/Documents/vibe-coding-guide/permissions-read-only.json ~/.claude/settings.local.json

# Switch back to Create-Only for development
cp ~/Documents/vibe-coding-guide/permissions-create-only.json ~/.claude/settings.local.json
```

Changes take effect immediately (no restart needed).

---

## Per-Project Overrides

For specific projects, create `.claude/settings.local.json` in the project directory:

```bash
cd ~/my-trusted-project
mkdir -p .claude
cp ~/Documents/vibe-coding-guide/permissions-create-only.json .claude/settings.local.json
```

This overrides your global `~/.claude/settings.local.json` for that project only.

---

## Customizing

Start with a tier and add project-specific permissions:

```json
{
  "permissions": {
    "allow": [
      "... (copy from tier file) ...",
      "Bash(docker:*)",
      "Bash(kubectl:*)",
      "Bash(./deploy.sh)"
    ],
    "deny": [],
    "ask": []
  }
}
```

---

## Safety Tips

1. **Start restrictive** - Use Read-Only first, upgrade to Create-Only when comfortable
2. **Git is your safety net** - Create-Only is safe because git tracks everything
3. **Combine with hooks** - Add PreToolUse hooks (README section 13) for extra safety
4. **Review before pushing** - Always `git diff` before pushing to remote
5. **Project-specific** - Use stricter permissions for sensitive projects

---

## Why These Tiers?

**Read-Only exists because:**
- Perfect for exploring unfamiliar code
- No risk of accidental modifications
- Great for learning and code review

**Create-Only exists because:**
- Normal development doesn't need deletions
- Git tracks all changes, making them reversible
- Blocking rm prevents catastrophic mistakes
- Ideal balance of productivity + safety

**Development exists because:**
- Some workflows genuinely need rm (cleaning build artifacts)
- Advanced users with proper hooks can be safe
- Full-featured development without constant prompts

---

Last updated: 2025-12-15
