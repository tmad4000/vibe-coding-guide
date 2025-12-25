#!/bin/bash
# Claude Code PreToolUse hook to block dangerous rm commands
#
# How it works:
# - Receives JSON on stdin with tool call details
# - Extracts the command from .tool_input.command
# - Blocks dangerous patterns with exit code 2
# - Allows safe commands with exit code 0

# Read JSON from stdin
input=$(cat)

# Extract the command using jq
command=$(echo "$input" | jq -r '.tool_input.command // ""')

# If we couldn't extract a command, allow (fail open)
if [ -z "$command" ]; then
  exit 0
fi

# Patterns that are ALWAYS blocked (catastrophic)
# Using case statement for exact pattern matching
case "$command" in
  *"rm -rf /"*|*"rm -rf /*"*|*"rm -rf ~"*|*"rm -rf \$HOME"*|*"rm -rf \"\$HOME\""*)
    echo "🚫 BLOCKED: Extremely dangerous command detected" >&2
    echo "   Command: $command" >&2
    echo "   This could delete your entire home directory or system files." >&2
    exit 2
    ;;
esac

# Check for rm -rf with wildcard or current directory
if echo "$command" | grep -qE 'rm\s+(-[a-zA-Z]*r[a-zA-Z]*f|--recursive)\s+\*'; then
  echo "🚫 BLOCKED: rm -rf with wildcard is too dangerous" >&2
  echo "   Command: $command" >&2
  exit 2
fi

# Check for rm -rf on common important directories
if echo "$command" | grep -qE 'rm\s+(-[a-zA-Z]*r[a-zA-Z]*f|--recursive)\s+(~/|/Users/|/home/)'; then
  echo "🚫 BLOCKED: rm -rf on home/user directory" >&2
  echo "   Command: $command" >&2
  exit 2
fi

# Block rm -rf . and rm -rf ..
if echo "$command" | grep -qE 'rm\s+(-[a-zA-Z]*r[a-zA-Z]*f|--recursive)\s+\.\.?\s*$'; then
  echo "🚫 BLOCKED: rm -rf on current or parent directory" >&2
  echo "   Command: $command" >&2
  exit 2
fi

# Block ANY rm command targeting iCloud Drive
if echo "$command" | grep -qE 'rm\s+.*Library/Mobile Documents'; then
  echo "🚫 BLOCKED: Cannot delete files from iCloud Drive" >&2
  echo "   Command: $command" >&2
  echo "   Tip: iCloud files should not be deleted by automated tools." >&2
  exit 2
fi

# If running from home directory, block ALL recursive rm commands
cwd=$(echo "$input" | jq -r '.cwd // ""')
if [[ "$cwd" == "$HOME" ]]; then
  if echo "$command" | grep -qE 'rm\s+.*-[a-zA-Z]*r'; then
    echo "🚫 BLOCKED: No recursive rm allowed when running from home directory" >&2
    echo "   Command: $command" >&2
    echo "   Tip: cd into a project directory first, or run this command manually." >&2
    exit 2
  fi
fi

# Allow the command
exit 0
