# McGraw Hill K–12 International — Notion Marketing Ops
## Central Source of Truth (full build)

**Maintainer:** Hammad Khilji — Marketing Director, MHE K–12 International (Dubai)
**Last updated:** 2026-06-06 (rev 4) · **Reconciliation status:** complete (entire system verified live)
**Companion:** `notion_marketing_ops_handoff_for_claude.md` (deep architecture rationale)

> This is the single living reference for the whole Notion build — model, decisions, current state, IDs, conventions, learnings, and the open backlog. Working state lives here in `.md`; system architecture lives in Notion (System Map, Glossary, guides). Where this file and Notion ever disagree, Notion wins — update here.

---

## 0. Orientation

- **Purpose:** marketing operations hub for MHE K–12 International — connects intake → campaigns → work → hours → outcomes, with controlled vocab and budget governance.
- **Fiscal year:** April–March (FY27 = Apr 2026 – Mar 2027).
- **Working hours (SLA basis):** Sunday–Thursday, 09:00–18:00 Dubai time.
- **Build status:** core architecture is **live and richly built**. Pre-launch polish session completed 2026-06-05. All broken rollups repaired 2026-06-06. **System is launch-ready** — DB locks + vocab field population on demo records remain before Monday team access. Remaining backlog is post-launch hygiene and external integrations (see §9).

---

## 1. Team roster

| Person | Role | Base |
|---|---|---|
| Hammad Khilji | Marketing Director (MEA, UK/NECE/I, Asia, Australia) | Dubai |
| Andrew Teo | Creative Lead | Singapore |
| Autumn Chen | Marketing Manager (Intervention/Supplemental) | Singapore |
| Fatemah Alibrahim | Brand & Content (on leave) | KSA |
| Lawrasari Suardy | Portfolio PM | Singapore |
| Lisa McNeil | Marketing Manager | Sydney |
| Rudy Galera | Growth Marketing Manager, K-12 INTL | Dubai |
| Sanah Varsi | Coordinator | Noida |
| Sehrish Shuja | Marketing Manager | UK |
| Vikas Tripathi | Salesforce Admin (not yet on Notion) | Noida |

Team onboarding (including Vikas) will happen together as a group post-launch — not a pre-launch blocker.

---

## 2. The system model (authoritative)

**Lifecycle (the spine):**

```
💡 Ideas  →  🎯 Master Campaigns  →  📡 Channel Campaigns  →  ✅ Tasks  →  ⏱️ Time Entries
                                          ↘ 🎙️ Webinars (created post-event)
```

- **Two intakes feed the lifecycle:**
  - **💡 Ideas** — the front door for any request (Sales, CS, Distributors, Leadership). Request Type + status flow New → Reviewing → Approved / Declined / On Hold → Promoted. Weekly triage by Hammad. *(Downstream relations to Master/Projects are intentionally deferred.)*
  - **🎪 External Events** — research/shortlist pipeline for sponsorships (Researching → Shortlisted → Approved → Confirmed). When **Confirmed**, promote to a Channel Campaign (Medium = In-Person Event); the event record persists as research history.
- **🚀 Projects is a *sibling* to Master Campaigns**, not a layer above it. Projects is the home for **non-pipeline** work, tagged by a **Workstream** property: Campaign / System Build / Research & Strategy / Content Creation / Internal Comms & Ops / Event (Internal) / Development. Both Projects and Master Campaigns roll up Tasks + Hours (same plumbing, different purpose).
- **There is no "Goals" database.**

**The Master-vs-Project decision:** *Does this work directly generate pipeline through external marketing channels?* Yes → **Master Campaign** (Event / Content / Nurture template). No → **Project**.

**Reference databases (tags attached to lifecycle records, not part of the flow):** 📦 Products, 🌍 Regions, 📚 Disciplines, 🎤 Experts & Presenters, 📊 Database Segments, 💰 Budget Ledger. Plus 🌴 Team Leave (visibility layer; Workday is system of record).

**Budget (two layers):** 🏦 **Budget Allocations** = top-down Finance-approved annual envelopes (Category × Region); **14 FY27 allocations total ~$691,977**, with Forecasted/Actuals rollups and % Forecast Committed / % Actual Spent variance formulas. 💰 **Budget Ledger** = bottom-up forecast/actual transactions, each linked to an allocation.

**Meetings:** 👥 **Team Meetings** (on the dashboard; agendas, AI summaries, decisions, action items → Tasks). 🤝 **1:1 Meetings** (Hammad's private workspace; alternating Thursday Group A/B cycles; not on the team dashboard).

**Monthly Newsletter:** 📰 **Monthly Newsletters** DB — a simple, standalone DB holding one record per month. Each record captures all content for the internal business-wide email sent on the 1st of each month. Content is AI-generated via a Claude skill (see §4.3) and covers: last month's highlights, upcoming campaigns/events, and standing resource links/reminders. Not part of the campaign lifecycle; classified as Internal Comms & Ops.

---

## 3. Architecture decisions (confirmed — do not reopen)

1. **Single unified Channel Campaigns DB** (not per-channel DBs); Channel/Medium/Format are properties, with templates + filtered views for the channel-specific feel.
2. **Projects ↔ Master Campaigns dual model** — sibling or umbrella by initiative shape; the audience-based rule decides edge cases (internal audience → Project; external/pipeline → Master Campaign).
3. **Master Type doesn't constrain channel mix** — any Master (Content/Event/Nurture) can hold any-medium Channel Campaigns.
4. **Two-name model:** **Suggested Name** (human-readable, copied into the Name title) vs **Child Campaign Name** (technical identifier flowing to Salesforce/Marketo). Different formulas, different outputs — never conflate.
5. **Database locks (not trust-based permissions)** for access control (~30 DBs; checklist documented).
6. **CTA left blank** rather than placeholder URLs (keeps UTM/Name formulas clean).
7. **Projects hours = Campaign Hours + Task Hours** via a formula (avoids Notion's rollup-of-a-rollup limit).
8. **Completion (Projects) = direct-task % only** — does not transitively roll up children; read umbrella progress from children's bars + Status.
9. **Task linkage rule:** a Task links to a Channel Campaign **or** a Project — never both. Linking both causes hours double-counting across rollups.
10. **"Week Of" formula on Time Entries: formally dropped.** Notion's native date grouping (Group By → Date → Week) handles weekly bucketing in views without a separate formula field.
11. **Linked 1:1 Meetings relation on Master Campaigns: dropped.** Never populated; 1:1s are private and should not surface as a property on team-visible records. Linked Team Meetings relation retained on both Master Campaigns and Channel Campaigns.
12. **Ideas DB — two product fields:** `Product (as submitted)` = free text on the form (Notion forms cannot link to non-public DBs); `Related Product (Triage)` = relation to Products DB, populated by Hammad during weekly triage. Priority field removed from the form — set by Hammad during triage only.
13. **Dashboard Quick Capture + Navigation merged into a single column.** The freed space in the second column holds a "This Week" linked view of all Tasks and Channel Campaigns due or active in the current week — added by Hammad via UI.
14. **Monthly Newsletters is a standalone DB**, not part of the campaign lifecycle. It is not related to Master Campaigns or Channel Campaigns. Content is composed externally (Claude skill) and pasted in. The DB is housed under Admin & Reference (or alongside Team Meetings) and linked from the dashboard Navigation section.
15. **Vocab relations on Channel Campaigns — seven required fields per record.** All seven code rollups (Region Code, Medium Code, Product Code, Channel Code, Channel Format Code, Asset Type Code, FY Code) are driven by direct relations to their respective vocab DBs. The relation fields must be populated per campaign record for codes (and downstream formulas) to resolve. This is a data-entry step, not a schema issue — the schema is fully wired.
16. **Paid Media Campaign Name formula is UI-created only.** The API cannot handle the nested-quote formula expression. Formula must be created manually in Channel Campaigns via Notion UI. Expression documented in §4.4.
17. **Search Objective is a user-editable select** (options: Conversion / Traffic / Reach / Lead Gen). It is NOT a rollup. The rollup from Paid Search Benchmark is named `Search Bench Objective` and is read-only. The formula references `Search Objective` (select) for Paid Search campaigns and `Social Objective` (rollup from Social Benchmark) for Social campaigns.
18. **Social Objective is a rollup from Social Benchmark** — requires the `Social Benchmark` relation to be populated on the record before it resolves. This is the most common reason `Paid Media Campaign Name` returns blank on a Social campaign.

---

## 4. Current build state (live)

**Lifecycle DBs**

- **Ideas** — intake form + status flow live; downstream relations deferred. Schema updated 2026-06-05: `Related Product` (text) replaced by two fields: `Product (as submitted)` (text, on form) + `Related Product (Triage)` (relation to Products DB, internal). Priority removed from form. Dashboard now has **💡 Ideas to Triage** section with linked view filtered to Status is not Declined / not Promoted. 5 realistic dummy idea records seeded for demo. Default page template exists ("New Idea").
- **Master Campaigns** — Status (Planning→Cancelled), Start/End Date rollups, unified (Total) actuals/est/targets, ROI, Initiative + FY relations, Products/Regions, Webinars, Budget Ledger. `Linked 1:1 Meetings` property dropped 2026-06-05.
- **Channel Campaigns** — the executional engine (~100+ properties): two-name model (Suggested + Child Campaign Name), full Est_ + Actual metric set, Email & Social & Paid Search benchmark rollups, seven vocab code rollups (all repaired 2026-06-06), UTM formulas, Paid Media Campaign Name formula (UI step pending), Source Idea, Budget Ledger, Segments. **4 templates:** default, Social, Event-Webinar, Event-In-Person.
- **Tasks** — `Campaigns` property renamed to `Linked Channel Campaign` (2026-06-05). Body template exists. Hours helper feeds Channel/Project rollups. Orphaned placeholder "Task" records and "Email Template" record deleted by Hammad. ALEKS demo tasks (21) and standing Operations tasks (Admin/planning, Training & learning) retained.
- **Time Entries** — Date, Hours, Person, Tasks, Notes, Work Type (12-option select). `Channel Campaign` rollup added (2026-06-05) — pulls campaign name through from linked Task, read-only. No "Week Of" formula (formally dropped). Page template created (content staged at `37631abc-8070-81e9-b87d-e2c31ec4bf9f`, copied into DB template by Hammad). All placeholder time entry records deleted by Hammad.
- **Projects** — swept; 18-prop schema; hours fix (Campaign Hours + Task Hours + Hours Logged); Workstream + Parent Project nesting.
- **Webinars** — full DB (Attendance/Registrations/Attendance-Rate, Presenters/Products/Regions/Disciplines/Buyer-Stage/Master/Channel relations; 6 views incl. Library/Upcoming/Past). Page template created and set as default by Hammad (staged from `37631abc-8070-8120-af3e-dca5467af52d`).
- **External Events** — enriched + parked; see §4.1. Page template created and set as default by Hammad (staged from `37631abc-8070-81b3-b015-cc9dffa9c1ec` in Admin & Reference).

**Reference / vocab DBs** — Products (code + override), Regions (7 territories), Disciplines (7), Experts & Presenters (roster, 4 views; page template created and set as default by Hammad, staged from `37631abc-8070-810b-b4a0-c61c5dee24d2`), Database Segments, Team Leave; Buyer Stage / FY / Initiatives vocab; Email & Social & Paid Search Benchmarks (all wired into Channel Campaigns).

**Budget** — Allocations (14 FY27, ~$691,977, variance formulas) + Ledger (bottom-up), both live. `Forecast Remaining` and `Actual Remaining` formula fields: dollar currency formatting to be applied via UI (API does not support FORMAT on formula fields).

**Reference hub (under Admin & Reference)** — System Map (updated 2026-06-05), Team Guide (updated 2026-06-05), Glossary of Terms, Team Onboarding & Adoption Plan, Time Entries Guidance (updated 2026-06-05: Week Of note added), Web-vs-Marketo guide, Synced Blocks Library, Campaign References, Monthly Newsletter Prompt, Regional Calendar Overview, Event Certificate Generator Guide, Org Chart & Territories, Notion Crash Course, Marketing Team SLAs (+ Approval SLAs sub-page), Monday Review, Nurture Mapping Guide, Campaign Thinking, Post-Launch Improvements. **Staging template pages** also live here (see §4.2).

**Dashboard layout** — welcome callout; flow line; **Single-column Quick Capture + Navigation block** (merged 2026-06-05 rev 3: Quick Capture buttons + Navigation links in one column; second column reserved for Hammad to add "This Week" linked view); Action Required (Overdue Tasks + approvals); **💡 Ideas to Triage**; Active Master Campaigns; Active Projects by Work Stream; Active Events Pipeline (⚠ filters to ~next 60 days); FY27 Budget Health (by % spent). External Tools links still `example.com` placeholders.

**Team Meetings** — page template created and set as default by Hammad (staged from `37631abc-8070-8149-b0b1-eb29563d4541`).

**Monthly Newsletters DB** — *(planned, not yet built)* — see §4.3 for spec. ID to be captured once created.

### 4.1 External Events — enriched & parked (12 promoted, mixed stages)

| Event | Stage | Date | Location |
|---|---|---|---|
| ResearchED London | Confirmed | 5 Sep 2026 | London |
| Festival of Education | Approved | 2–3 Jul 2026 | Wellington College |
| ERDI Jasper | Approved | 15–18 Oct 2026 | Jasper |
| uLead | Approved | 18–20 Apr 2027 | Banff |
| ERDI Calgary | Approved | Mar 2027 (TBC) | Calgary |
| CPCO | Approved | Apr 2027 (TBC) | Niagara |
| OPSOA | Approved | Mar 2027 (TBC) | Toronto |
| CEC | Approved | Dec 2026 (TBC) | Toronto |
| ResearchEd Toronto | Approved | Oct 2026 (TBC) | Toronto |
| World Literacy Summit | Shortlisted | 31 Mar–3 Apr 2027 | Oxford |
| SGIS | Shortlisted | 12–13 Mar 2027 | Zurich |
| OCSTA | Shortlisted | Late Apr/May 2027 (TBC) | — |

### 4.2 Staging template pages — all resolved ✅

All DB default templates were created and registered by Hammad on 2026-06-05. Staging pages in Admin & Reference should be deleted once confirmed.

| DB | Staging page ID | Status |
|---|---|---|
| ⏱️ Time Entries | 37631abc-8070-81e9-b87d-e2c31ec4bf9f | ✅ Copied & template set |
| 👥 Team Meetings | 37631abc-8070-8149-b0b1-eb29563d4541 | ✅ Copied & template set |
| 🎥 Webinars | 37631abc-8070-8120-af3e-dca5467af52d | ✅ Copied & template set |
| 🎤 Experts & Presenters | 37631abc-8070-810b-b4a0-c61c5dee24d2 | ✅ Copied & template set |
| 🎪 External Events | 37631abc-8070-81b3-b015-cc9dffa9c1ec | ✅ Copied & template set |
| 💡 Ideas | 37631abc-8070-819a-a1bb-c70bae847e38 | ✅ Redundant — deleted (existing "New Idea" template used) |

### 4.3 Monthly Newsletters DB — spec (planned)

**Purpose:** One record per calendar month. Houses all content for the internal business-wide email that goes out on the 1st of each month. Audience = entire MHE business (not external). Content is AI-generated via the Monthly Newsletter Claude skill and pasted in by Hammad or his coordinator.

**Schema (proposed — confirm before build):**

| Property | Type | Notes |
|---|---|---|
| Newsletter Name | Title | e.g. "June 2026 — Marketing Newsletter" |
| Month | Date | First day of the month (e.g. 2026-06-01) |
| Status | Select | Draft · Ready · Sent |
| Send Date | Date | Target send: 1st of month |
| Sent By | Person | |
| Last Month Highlights | Text | AI-generated section: what shipped/launched |
| Coming Up This Month | Text | AI-generated section: upcoming campaigns, events, launches |
| Resources & Reminders | Text | Standing links; updated manually each issue |
| Notes | Text | Internal only |

**Placement:** housed alongside Team Meetings in the dashboard, or under Admin & Reference. Add a linked view to the dashboard Navigation block.

**Content generation workflow (Claude skill):**
1. Hammad runs the "Monthly Newsletter Builder" skill prompt in Claude.
2. The skill queries (via Notion MCP): active/completed Channel Campaigns, Master Campaigns, Tasks, Projects, and External Events for the prior month and current month.
3. Claude synthesises output into the agreed newsletter format (sections: Last Month's Highlights · Coming Up · Resources & Reminders).
4. Hammad reviews, edits, pastes into the Notion record, marks Status → Ready, then sends on 1st of month.

**Skill location:** `/mnt/skills/user/monthly-newsletter-builder/SKILL.md` *(to be created).*

**Newsletter format (agreed standard — to be finalised in skill build):**

```
SUBJECT: Marketing Update — [Month Year]

Hi team,

Here's your monthly marketing update from the K–12 International team.

─────────────────────────────────────
🏁 LAST MONTH — WHAT WE DID
─────────────────────────────────────
[Bullet summary of campaigns launched, events attended, content published,
 projects completed — pulled from Notion]

─────────────────────────────────────
📅 THIS MONTH — WHAT'S COMING
─────────────────────────────────────
[Bullet summary of upcoming campaign launches, webinars, events,
 key milestones — pulled from Notion]

─────────────────────────────────────
🔗 RESOURCES & REMINDERS
─────────────────────────────────────
[Standing links: Marketing Dashboard · Campaign Brief form ·
 Brand Assets · Marketo · Salesforce · Regional Calendar]
[Any standing reminders: SLA turnarounds, Ideas intake form link, etc.]

─────────────────────────────────────
Questions? Reply to this email or ping Hammad directly.
```

### 4.4 Paid Media Campaign Name formula (UI-only — pending)

Must be created manually in Channel Campaigns via Notion UI (API cannot handle nested-quote formula expressions). Property name: `Paid Media Campaign Name`. Expression:

```
if(prop("Medium") == "Social",
  prop("Platform") + "_" + prop("Region Code") + "_" + prop("Product Code") + "_" + prop("Asset") + "_" + prop("Social Objective"),
  if(prop("Medium") == "Paid Search",
    prop("Platform") + "_" + prop("Region Code") + "_" + prop("Product Code") + "_" + prop("Asset") + "_" + prop("Search Objective"),
    ""
  )
)
```

**Dependencies for this formula to produce output:**
- Social campaigns: `Platform` (select) + `Region` relation populated → `Region Code` resolves + `Product` relation populated → `Product Code` resolves + `Asset` (text) filled + `Social Benchmark` relation populated → `Social Objective` resolves.
- Paid Search campaigns: same except `Search Objective` (select, user-editable) replaces `Social Objective` — no benchmark link needed.

---

## 5. Conventions & rules

- **Status vocabulary:** Planning · In-Progress · Launched · Paused · Completed · Cancelled (hyphen: "In-Progress"). *Note: Webinars currently uses "In progress" — standardize.*
- **Buyer stages:** AW (Awareness) · CO (Consideration) · DE (Decision) · RT/PS (Retention/Post-sale).
- **Regions (7):** MEA · ANZ · UK · EU · ASIA · CA · OCEANIA.
- **Disciplines (7):** Literacy · Math · Science · ICT · Intervention · Uncategorized · Leadership.
- **Two-name model** (see §3.4); **CTA blank** (§3.6).
- **Date discipline:** confirm launch/event dates are in the future before creating records.
- **Task linkage rule** (see §3.9): a Task links to a Channel Campaign **or** a Project — never both.
- **Ideas triage filter:** Ideas to Triage view shows Status is not Declined AND Status is not Promoted (i.e. shows New + Reviewing + Approved + On Hold).
- **Ideas form:** Priority is not on the form — set by Hammad during triage only. Product (as submitted) is on the form as optional free text. Related Product (Triage) is internal, populated during triage via the Products DB relation.
- **Monthly Newsletter send date:** always 1st of the month. One record per month. Status must be Ready before send.
- **Seven vocab relation fields per Channel Campaign record** must be populated for code rollups and naming formulas to resolve: `Region`, `Product`, `Medium (Vocab)`, `Channel (Vocab)`, `Channel Format (Vocab)`, `Asset Type (Vocab)`, `FY (Vocab)`. These are data-entry steps — the schema is fully wired.
- **Social Benchmark relation** must be populated on Social campaign records for `Social Objective` to resolve (and therefore for `Paid Media Campaign Name` to output a result).

---

## 6. Notion MCP / API learnings (permanent)

**Property writes** — `notion-update-page` cmd `update_properties`: dates use `date:{Prop}:start` / `:end` / `:is_datetime` (0/1); checkboxes `"__YES__"`/`"__NO__"`; numbers as JS numbers; multi-select as a JSON-array string `"[\"X\"]"`; properties literally named `id`/`url` need a `userDefined:` prefix.

**Schema edits** — `notion-update-data-source` (SQL DDL): `ADD/DROP/RENAME COLUMN`, `ALTER COLUMN SET`, `ROLLUP/FORMULA/SELECT/MULTI_SELECT`. Batches are **atomic**.
- **Cannot roll up a rollup through a relation** → roll up a **FORMULA** instead.
- `ALTER COLUMN SET` on a select reconciles options **by name**, preserves data, but **errors on changing an existing option's color**.
- A FORMULA referencing other props must be added **after** they exist (separate DDL call).
- **Formula fields cannot have FORMAT applied via DDL** (e.g. `FORMAT 'dollar'`) — number format on formula fields is UI-only.
- **Relation fields cannot be used in Notion forms if the target DB is not public** — use a free-text field for form intake and a separate relation field for internal triage.
- **DDL rollup syntax requires all three arguments in single quotes:** `ROLLUP('relation-name', 'target-field', 'aggregation-function')` — unquoted function names cause parse failures.
- **Broken rollup pattern:** when a relation is dropped from a DB, rollups that referenced it retain a stale `relationPropertyUrl` pointing at the old property ID. The rollup shows `<omitted />` on records. Fix: add the relation back (new property ID), then `ALTER COLUMN SET ROLLUP(...)` to repoint. The stale property ID is visible when fetching `collection://` directly.
- **Complex formula expressions with nested double quotes in `FORMULA('...')` DDL consistently fail** regardless of escaping — must be created in the Notion UI.

**Links** — `notion://` is stripped to `https://` on save; use inline `<mention-page url="https://www.notion.so/<id>">Label</mention-page>` for in-app opening.

**Templates** — `apply_template` is unreliable (verify; fall back to inline). Creating a page inside a DB data source does **not** automatically register it as a DB template — this is a UI-only step (open DB → arrow next to `+ New` → `+ New Template` → paste content → Set as default). Use staging pages in Admin & Reference as copy sources when direct DB template creation is blocked by the API.

**Page creation into some data sources** may be blocked by the API (permissions quirk) — fall back to creating a staging page elsewhere and having Hammad copy the content manually.

**UI-only (no API):** property icons, property ordering, side-panel grouping, visibility/hide/pin, layout, **buttons**, existing-view filter/column changes, formula field number formatting, formula expressions with nested quotes → Claude specs, Hammad executes.

---

## 7. Notion edit-safety rules (always apply)

- **NEVER** `replace_content` with `allow_deleting_content=true` on hub/dashboard pages or any page with child pages/DBs (it trashes children).
- If `replace_content` warns about child deletion → **STOP and ask Hammad**.
- **Prefer `update_content` (`old_str`/`new_str`)** for dashboard edits; for broken embeds, update the specific block only.

---

## 8. Key IDs

```
# Dashboard & containers
Marketing Team Dashboard:   1be31abc-8070-8038-8742-c15dd49bd26c
Core Databases (page):      18531abc-8070-8026-b8e1-e2e81c69cadb
Admin & Reference (page):   35731abc-8070-81a2-b0c4-d2c7ea267b3a
Vocab Databases (container): 27c31abc-8070-8074-86fe-eecb06a8be97

# Lifecycle DBs            page : data source
Ideas:        31b1c1057bf7481dbd704d201f0d452d : collection://0f974715-0e1a-4cdf-b6c7-2b23157fc62a
Master Campaigns: 27c31abc807080058e9ae40524316322 : collection://27c31abc-8070-803f-b35f-000b3ca18963   (tmpl 27c31abc80708017baddf9ff38d086bf)
Channel Campaigns: 1c031abc8070804c9155dfc779d5c137 : collection://1c031abc-8070-8005-87ff-000b528f1a30
Tasks:        18531abc807081f9a310d6d7953f750c : collection://18531abc-8070-81f7-9303-000b3bec418e   (body tmpl 18531abc-8070-81bb-b502-c2965a4b4b79)
Time Entries: 27c31abc8070803a9367d09456db7359 : collection://27c31abc-8070-80b4-b3b2-000b803d9f18
Projects:     18531abc807081888d53e03b4309c6aa : collection://18531abc-8070-8126-ab7c-000bebf17898   (tmpl 18531abc-8070-815f-aa66-c00f49845c04)
Webinars:     28f31abc8070805c84abf923b4f3d3db : collection://28f31abc-8070-806c-80ac-000b99788cbb
External Events: bbfa2a44d5a34d718f82d6310fb682c4 : collection://82aee770-bc51-4b5c-9665-44105ed26230
Monthly Newsletters: (ID TBC — capture once created)

# Channel Campaign templates
default 1c031abc807080e2b0fdd9d05cf48dba · Social 28331abc807080739580de6560f73f85 · Event-Webinar 36131abc80708038a758fc17c60cb6aa · Event-In-Person 36131abc807080dd8b34e2a976a30ddc

# Budget
Budget Allocations: 9ca3656eea7f4150894cc3aff404e993 : collection://3c0725e9-9463-46bf-af5b-b7e030a7d433
Budget Ledger:      28031abc807080f4ba96dfc256e875f9 : collection://28031abc-8070-80b8-a009-000bfb4e3cd4

# Reference / vocab DBs   page : data source
Products:    27b31abc807080fbbb4acdb4f41d5c96 : collection://27b31abc-8070-8020-a324-000b7955c538
Regions:     27c31abc8070802eb8b7f5a7a1591731 : collection://27c31abc-8070-8026-9227-000b4cd616e8
Disciplines: 4ae1788fd90e4165a3383fb14b3ffa34 : collection://f1c122b4-2f32-4c63-8d7a-7a8fa18d98eb
Experts & Presenters: 28031abc80708053a016e3b2c4c55836 : collection://28031abc-8070-80ef-bd4b-000b3a60bb99
Database Segments: 22131abc807080908af2e1294cfbdbc7 : collection://22131abc-8070-80ee-8cc9-000b9fc5cb66
Team Leave:  d60d8944050640baa417b98936699c75
Buyer Stage (vocab): collection://27c31abc-8070-8002-894c-000bfe93d183
FY (vocab):          collection://27c31abc-8070-80dd-9818-000b9f3807b7
Initiatives:         collection://30131abc-8070-80a2-b983-000b71dc7e90
Email Benchmark:     collection://22131abc-8070-80f7-adfb-000baa14b6c5
Social Benchmark:    collection://28031abc-8070-80d3-8e7d-000bc8821e11
Paid Search Benchmarks: page 0d128542f301409fa1d815215591b8e0 : collection://8ec79224-1f16-4581-b3ce-4c23697ac4aa

# Vocab DBs (Channel Campaigns relations — all wired as of 2026-06-06)
Channel:        collection://27c31abc-8070-80f5-97ed-000b188c9767
Channel Format: collection://27c31abc-8070-80a4-b7ad-000b016b360e
Asset Type:     collection://27c31abc-8070-80e8-ba18-000b4c90bdee
Medium:         collection://27c31abc-8070-801b-beb7-000b387c5220

# Meetings
Team Meetings: 81d0f221c6424bb79376c7978f29ac24 : collection://763d4599-3989-45d3-a681-5b31b27bc5d8
1:1 Meetings (private):                          collection://732b913d-a077-4227-a37a-20c15203b997

# Reference hub pages (under Admin & Reference)
System Map: 36231abc8070811da3dcc25821dda697 · Team Guide: 36131abc807081f596e0f240a62de9a6
Glossary: 36231abc807081e69617e7713ed3e1b1 · Onboarding & Adoption Plan: 36231abc80708197b890d600644851dc
Time Entries Guidance: 36431abc807081c4b63bccfb7404658b · Web vs Marketo: 36331abc8070819ebe0bf46f9b2ecf6d
Synced Blocks Library: 22131abc80708092910be0bc70fdcd4f · Campaign References: 35d31abc807081e3a44cc6cdadee3454
Monthly Newsletter Prompt: 36131abc8070817ab9f9da0c3c94e8f3 · Regional Calendar Overview: 36231abc807081778409d56d3a3b82d9
Event Certificate Generator: 36231abc80708130b1eec166794a7969 · Org Chart & Territories: 36331abc807081cc9d58e776a5f26c28
Notion Crash Course: 36331abc80708112ae3dc9599e8b1c9f · Marketing Team SLAs (parent): 36331abc80708145996afc24956ba8f4
Approval SLAs (sub): 36631abc-8070-8170-a85b-e3cad33c42e6 · Monday Review: 36131abc8070817c9451c87c0b21eae4
Nurture Mapping Guide: 36531abc807081589995d71ffd41bd62 · Campaign Thinking: 36931abc8070810696def67a8c1fbba3
Post-Launch Improvements (backlog): 36231abc8070819989bcc190f3257231

# Dashboard inline views
Overdue Tasks 36531abc807081a48567d0e76e1b48a4 · Tasks(2) 36531abc8070817aa976f28f05f9c615
Active Master Campaigns 36531abc807081e78557f7131d1cd408 · Active Projects 36531abc80708028b352cd401f894462
Active Events Pipeline 36531abc80708165a1b9cb8925fa6c08 · FY27 Budget Health 36531abc8070814aa34bd90acb3c7a61

# ALEKS demo
Master Campaign: 36931abc-8070-80fc-ac9d-c278f6af9f7a · Budget envelope: 37331abc-8070-81dc-966c-f58c7eb30879
LinkedIn Organic AW01 37331abc-8070-8193-862f-de05cd9622bd · LinkedIn Carousel DE02 37331abc-8070-8158-8da8-f32a2d962e81
Instagram Reel AW03 37331abc-8070-815b-bc08-caa94f9022b8 · Webinar CO01 37331abc-8070-81ab-8a54-cd28e8ea9cd5
Event GESS Dubai CO01 37331abc-8070-8116-bb29-f898ec44a018 · Email1 37331abc-8070-8143-927e-d76de7124798 · Email2 37331abc-8070-81e2-9667-c7dcd1d7233c (3–5 created, URLs uncaptured)

# Ideas — demo records seeded 2026-06-05
ALEKS Webinar (John Doe): 37631abc-8070-810a-870e-ef24c7a13a53
Reveal Math SEA Comparison (Priya Sharma): 37631abc-8070-817d-9d40-fe414a16efe1
ANZ Intervention Email (Lisa McNeil): 37631abc-8070-8192-98b4-f930f1457bcf
KSA Vision 2030 Whitepaper (Rudy Galera): 37631abc-8070-815e-9cab-d6d5359d2261
Inspire Science LinkedIn (Sehrish Shuja): 37631abc-8070-81d8-b746-d31fa1efce2b

# Projects of note
Salesforce Optimization FY27: 36531abc-8070-8176-ab34-f3f7bdee0f9a
Throwaway TEST page (delete): 37331abc-8070-8186-b276-c8a44be67ae8
```

---

## 9. Remaining work — single prioritized backlog

**Pre-launch (must complete before Monday team access):**

| Pri | Area | Item | Notes |
|---|---|---|---|
| **1** | Formula | Create `Paid Media Campaign Name` formula property in Channel Campaigns UI | Expression in §4.4. API cannot handle nested-quote formulas. |
| **1** | Demo data | Populate seven vocab relation fields on ALEKS demo campaign records | `Region`, `Product`, `Medium (Vocab)`, `Channel (Vocab)`, `Channel Format (Vocab)`, `Asset Type (Vocab)`, `FY (Vocab)` — per record in UI |
| **1** | Demo data | Populate `Social Benchmark` on Social demo campaign records | Unblocks `Social Objective` → unblocks `Paid Media Campaign Name` output |
| **1** | Permissions | Apply DB locks across ~30 DBs (UI) | Do this last, after all demo data is verified |

**Post-launch — first week:**

| Pri | Area | Item | Notes |
|---|---|---|---|
| **2** | Demo data | Seed realistic dummy time entries | 2–3 entries per team member; use ALEKS demo tasks as anchor |
| **2** | Hygiene | Products placeholder fill (~19 records) | Needed before Ideas form product field is useful to submitters |
| **2** | Dashboard | Add "This Week" linked view in second column (UI) | Spec confirmed in §3.13; column already freed |
| **2** | New DB | Build Monthly Newsletters DB (schema in §4.3) | Simple build; no relations needed; add to dashboard Navigation |

**Post-launch — ongoing hygiene:**

| Pri | Area | Item | Notes |
|---|---|---|---|
| **3** | Hygiene | `Actual  Launch Date` double-space/type; align "In-Progress" vs "In progress" in Webinars | Minor but visible |
| **3** | Hygiene | Vocab "Purpose" standardize; Benchmark row check | |
| **3** | Hygiene | Initiatives — decouple rollups, then deprecate; Ideas downstream relations (deferred) | Initiatives still load-bearing |
| **3** | Housekeeping | Delete TEST page; clean SF FY27 body; ALEKS demo verify (Ledger/phantom/CTA) | Time entries already cleared |
| **3** | Budget | Budget Mix chart Count → Sum | |
| **3** | Events | Widen Active Events Pipeline view >60 days; Promote-to-Channel-Campaign button | FY27 events won't surface until widened |
| **3** | Skills | Build Monthly Newsletter Builder skill (`/mnt/skills/user/monthly-newsletter-builder/SKILL.md`) | Skill queries Notion MCP for prior-month + current-month activity; outputs standard newsletter format; see §4.3 |

**Post-launch — deferred:**

| Pri | Area | Item | Notes |
|---|---|---|---|
| **4** | Onboarding | Full team onboarding including Vikas — run together as a group | Onboarding & Adoption Plan already exists |
| **4** | Enablement | Refine webinar/meeting/expert templates based on real usage | Templates built; adoption comes with use |
| **4** | Integrations | External Tools real URLs (Marketo/SF/Looker/Drive) | currently example.com |
| **4** | Integrations | Salesforce + Marketo campaign-sync fields | |
| **4** | Reporting | Looker Studio / Power BI feeds (Power BI web; Mac) | |
| **4** | Ops | Backup/export routine; formal ERD page | |

---

## 10. Workflow & context learnings

1. **Notion = durable architecture; `.md` (this file) = durable state.** Close every substantive chat with a write-back to one or the other.
2. **`apply_template` unreliable** — verify, fall back to inline.
3. **Anchor the current date** in any campaign/record creation (other Claudes drift to past dates).
4. **Schema reads are large** — sweep in focused passes; don't assert un-opened areas.
5. **Hammad's working style:** direct, decision-oriented; wants options + a clear recommendation, not unilateral action; prefers surgical edits over bulk replacements; catches precise errors (property-name confusion, date drift, placeholder leakage, conflated formulas). Always confirms before deletion.
6. **Formula field formatting is UI-only** — DDL `FORMAT` keyword not supported on formula fields.
7. **Notion form relations require public DB** — if the target DB is not publicly shared, relation fields cannot be added to forms. Use free-text intake + internal relation triage pattern instead.
8. **Page creation into some data sources blocked by API** — fall back to staging pages in Admin & Reference; Hammad copies content into DB templates manually.
9. **DB template registration is UI-only** — creating a page inside a DB via API does not register it as a template. Must open DB → arrow next to `+ New` → `+ New Template` → paste → Set as default.
10. **Broken rollup diagnosis pattern** — fetch the DB via `collection://` ID; stale `relationPropertyUrl` with no matching active relation in the schema confirms the relation was dropped. Fix: add relation back → `ALTER COLUMN SET ROLLUP(...)` to repoint. Do not attempt to reuse the old property ID.
11. **DDL rollup syntax** — all three arguments must be single-quoted: `ROLLUP('relation-name', 'target-field', 'aggregation-function')`. Unquoted aggregation tokens (e.g. `max`, `average`) cause parse failures at position ~37–69.

---

*Provenance: demo build 2026-06-02 · DB sweeps + dashboard + events enrichment 2026-06-03 · full live reconciliation 2026-06-04 · pre-launch polish session 2026-06-05 rev 1 (Tasks rename, Team Guide rule, System Map edits, Week Of dropped, 1:1 Meeting relation dropped, Time Entries Channel Campaign rollup + template, meeting/webinar/expert/event/ideas templates, Ideas schema refactor, 5 dummy idea records, dashboard Ideas to Triage section) · rev 2 (External Events template done, Ideas staging deleted, Ideas form updated, Budget Allocations currency format applied, property icons + ordering applied — system now launch-ready pending DB locks only) · rev 3 2026-06-05 (dashboard Quick Capture + Navigation merged into single column; "This Week" view spec added; Monthly Newsletters DB specced in §4.3 with schema, workflow, and newsletter format standard; Monthly Newsletter Builder skill added to backlog; architecture decisions §3.13–14 added) · rev 4 2026-06-06 (Paid Search Benchmarks DB created and populated with 9 rows; Paid Search Benchmark relation + 8 rollups added to Channel Campaigns; Search Objective renamed to Search Bench Objective as rollup; new Search Objective added as user-editable select; Paid Media Campaign Name formula documented in §4.4 — UI creation pending; seven broken rollups diagnosed and repaired: Region Code, Medium Code, Product Code, Channel Code, Channel Format Code, Asset Type Code, FY Code — all had stale relationPropertyUrl values; fixed by restoring direct relations and repointing rollups; Social Objective / Social Benchmark behaviour documented; broken rollup diagnosis pattern added to learnings §10).*
