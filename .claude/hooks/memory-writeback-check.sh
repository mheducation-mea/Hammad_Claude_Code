#!/usr/bin/env bash
# Stop hook: if substantive changes were made this session but the memory log
# (memory/decisions-and-learnings.md) was not updated, ask Claude to write a
# memory entry before finishing.
#
# Loop guard: if stop_hook_active is true we are already continuing because of a
# previous block, so allow the stop and exit immediately.
# Independent of the user-level git-check Stop hook; both run separately.
set -uo pipefail
input=$(cat || true)

active=$(printf '%s' "$input" | jq -r '.stop_hook_active // false' 2>/dev/null || echo false)
[ "$active" = "true" ] && exit 0

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)" || exit 0
cd "$ROOT" || exit 0

sid=$(printf '%s' "$input" | jq -r '.session_id // "default"' 2>/dev/null || echo default)
base_file=".git/claude-memory-hook/$sid"
base=""
[ -f "$base_file" ] && base=$(cat "$base_file" 2>/dev/null)

mem="memory/decisions-and-learnings.md"

# Files changed this session = committed since the session base + anything still uncommitted.
changed=""
if [ -n "$base" ] && git rev-parse --verify "$base" >/dev/null 2>&1; then
  changed=$(git diff --name-only "$base" HEAD 2>/dev/null)
fi
changed="$changed
$(git status --porcelain 2>/dev/null | sed 's/^...//')"

# Substantive = any changed path outside memory/. The memory log itself is the "updated" signal.
substantive=$(printf '%s\n' "$changed" | sed '/^[[:space:]]*$/d' | grep -v '^memory/' | head -n1 || true)
mem_updated=$(printf '%s\n' "$changed" | grep -x "$mem" | head -n1 || true)

if [ -n "$substantive" ] && [ -z "$mem_updated" ]; then
  printf '%s' '{"decision":"block","reason":"Substantive changes were made this session, but memory/decisions-and-learnings.md was not updated. Before finishing: append a dated entry (newest at top) summarizing the decisions, rules, or state changes from this session, then commit and push. If nothing this session is worth recording, briefly say so and stop."}'
fi
exit 0
