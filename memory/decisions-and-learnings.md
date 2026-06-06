# Decisions & Learnings

> Durable decisions, rules learned, and project state from Claude Code sessions.
> Newest entries at the top. Each entry: date, what, why.

---

## 2026-06-06 — Session: setup and migration

### Environment & access
- **GitHub App "Claude" installed** on the `mheducation-mea` account with Contents read/write. Push to `claude/brave-darwin-CsPEG` works. (Before install, pushes failed with 403.)
- The repo is the home for the work engine: skills, `CLAUDE.md`, and `memory/`. Notion stays the system of record.
- Rudy's reference HTML file was imported for analysis, then deleted from this branch. A copy still exists on `main`.

### Skills
- Ported Hammad's three Claude.ai skills into `.claude/skills/`, kept separate, as a composed set:
  - `hammad-b2b-copywriting` (foundation)
  - `email-nurture-campaign-builder` (loads the copywriting skill; copywriting rules win on conflict)
  - `international-school-profiler` (uses `WebSearch` / `WebFetch`; tool names updated from the originals)
- Frontmatter normalised to `name` + `description`. Original metadata preserved in-file.

### Memory & global rules
- Created root `CLAUDE.md` (auto-loads every session) and this `memory/` system.
- Removed the customer-facing comms items from CLAUDE.md section 2: they belong with copywriting standards, not "how to work with Hammad."

### Automation (memory write-back hook)
- Added a project Stop hook (`.claude/hooks/memory-writeback-check.sh`, wired in `.claude/settings.json`) that nudges Claude to update this log when a session made substantive (non-`memory/`) changes without a write-back. Respects `stop_hook_active` to avoid loops; runs independently of the user-level git-check Stop hook.
- Added a `SessionStart` companion (`.claude/hooks/session-base.sh`) that records the session's base commit under `.git/claude-memory-hook/<session_id>` so the Stop hook can scope "what changed this session." The base ref is per-session and not committed; the nudge becomes effective from the next session onward.

### Notion
- Connector confirmed for **read and write**.
- Validated the edit-safety pattern: surgical `update_content` (old/new), scoped by heading, then re-fetch to verify.
- Dashboard edits made and verified live:
  - Fixed typo: nav toggle "Core DatabasesH" → "Core Databases".
  - Rewrote two mispasted captions (they carried the Ideas caption):
    - Active Channel Campaigns: "Channel campaigns currently live or in progress, across all regions and mediums. Click any row to open its tasks, budget, and tracking."
    - Active Projects by Work Stream: "Active non-pipeline work, grouped by workstream. Click any row to open its tasks and logged hours."
  - Ideas To Triage caption left intact.
- Still open: External Tools links on the dashboard are `example.com` placeholders (backlog).
