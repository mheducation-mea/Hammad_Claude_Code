# CLAUDE.md — McGraw Hill K-12 International Marketing

> Global context for every Claude Code session in this repo. Auto-loaded at session start.
> This is durable memory. Keep it accurate. When a rule changes, update it here.
> Last updated: 2026-06-06.

---

## 1. Who this is for

- **Maintainer:** Hammad Khilji, **Marketing Director**, McGraw Hill K-12 International, based in Dubai.
- **Scope:** K-12 International marketing across MEA, UK/NECE/I, EU, Asia, ANZ/Australia, Canada, Oceania.
- **Fiscal year:** April to March (FY27 = Apr 2026 to Mar 2027).
- **Working hours (SLA basis):** Sunday to Thursday, 09:00 to 18:00 Dubai time.

## 2. How to work with Hammad (verified from his ops doc)

- Be **direct and decision-oriented**. Get to the point.
- Give **options plus a clear recommendation**. Do not take unilateral action on anything significant.
- Prefer **surgical edits over bulk replacements**.
- **Always confirm before deleting** anything.
- Anchor to the **current date** when creating or reasoning about records (avoid date drift).
- He catches precise errors: property-name confusion, date drift, placeholder leakage, conflated formulas. Hold that bar.

### Communication preferences (to confirm with Hammad)
*These were observed secondhand and are not yet ratified. Confirm before treating as rules.*
- Lead with a number.
- Keep briefs tight (around 300 words).
- Pair every flag or problem with a proposed solution.
- Every campaign line should pass the "competitor swap" test (if a competitor's name fits, the line is too generic).

## 3. Copywriting standards (customer-facing copy)

The authoritative source is the **`hammad-b2b-copywriting`** skill. Always apply it to any
customer-facing copy. The hard rules:

- Lead with customer benefits, not company claims.
- Use "you-phrasing": "you" appears more than the company or product name.
- Write with confidence. No hedging ("we believe", "may help", "perhaps").
- Never open with the company name or "We".
- Kill jargon ("synergy", "leverage", "best-in-class", "holistic", "innovative").
- **Never use em dashes.** Use colons, commas, periods, or restructure.
- One clear CTA per email.

## 4. Skills in this repo

Located in `.claude/skills/`. They auto-invoke from their descriptions.

| Skill | Use it for | Depends on |
|---|---|---|
| `hammad-b2b-copywriting` | Writing or reviewing any B2B customer-facing copy | None (foundation) |
| `email-nurture-campaign-builder` | Multi-touch nurture sequences for educational products | Loads `hammad-b2b-copywriting` |
| `international-school-profiler` | ABM research profiles of international schools | `WebSearch`, `WebFetch` |

## 5. Notion (the marketing operations system)

- **Notion is the system of record.** Where this repo and Notion disagree, **Notion wins**, then update the repo.
- **Marketing Team Dashboard ID:** `1be31abc-8070-8038-8742-c15dd49bd26c`
- Access is via the Notion MCP connector (read and write confirmed).
- Full architecture, all database IDs, conventions, and API learnings live in Hammad's
  **Notion Marketing Ops source-of-truth doc** (to be added to `memory/`). Treat that as the deep reference.

### Notion edit-safety rules (always apply)
- **Never** use `replace_content` with `allow_deleting_content=true` on hub or dashboard pages, or any page with child pages or databases. It trashes children.
- If `replace_content` warns about child deletion, **stop and ask Hammad**.
- Prefer **`update_content`** (`old_str` / `new_str`) for dashboard edits. Scope each edit narrowly (include a heading) so identical text elsewhere is not affected.
- After any write, **re-fetch and verify** the change actually landed.

### Core vocabulary (for consistency)
- **Regions (7):** MEA, ANZ, UK, EU, ASIA, CA, OCEANIA.
- **Disciplines (7):** Literacy, Math, Science, ICT, Intervention, Uncategorized, Leadership.
- **Buyer stages:** AW (Awareness), CO (Consideration), DE (Decision), RT/PS (Retention/Post-sale).
- **Status vocab:** Planning, In-Progress, Launched, Paused, Completed, Cancelled.

## 6. Memory discipline

- Memory here is **deliberate, not automatic.** Nothing is saved unless written to a file.
- Durable state lives in two places: **Notion** (architecture and live data) and **this repo** (`CLAUDE.md` plus `memory/`).
- **Close every substantive session with a write-back**: record new decisions, rules, and project state in `memory/`, and update this file when a global rule changes.

## 7. Repo and workflow

- Development branch: `claude/brave-darwin-CsPEG`.
- Commit work with clear messages. Push to the development branch.
- Do not open pull requests unless Hammad asks.

## 8. Pending / to set up

- `memory/` folder (decisions, learnings, project state). Not yet created.
- Brand assets (logo, exact colours, fonts) for brand-locked outputs. Not yet provided.
- Confirm the communication preferences in section 2.
