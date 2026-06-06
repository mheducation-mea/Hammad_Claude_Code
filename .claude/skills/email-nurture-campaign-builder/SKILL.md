---
name: email-nurture-campaign-builder
description: Generate complete, flexible-length B2B email nurture sequences for educational products targeting international schools. Use when the user asks to build a nurture sequence, an email drip or multi-touch series, or a buyer-journey email campaign for a product or curriculum. Produces a sequence planning table, stage-by-stage emails (awareness, consideration, sale), 3 subject-line options each, UTM and technical specs, and regional customization. Enforces one CTA per email, brevity-first drafting, and case-study localisation. Composes with and always applies the hammad-b2b-copywriting skill to every email.
---

# Email Nurture Campaign Builder for Educational Products

<!--
Skill metadata (ported from the original Claude.ai skill):
  version: 2.0  ·  last updated: April 2026
  domain: EdTech Marketing / Email Campaign Strategy  ·  complexity: Advanced
  tags: email marketing, nurture campaigns, educational technology, sales enablement, buyer journey

Composition: this skill depends on the hammad-b2b-copywriting skill. When this skill
runs, load that skill and apply its standards to every email; its rules win on any conflict.
-->


---

## Skill Overview

This skill enables you to generate complete, strategic nurture sequences for educational products and programs targeting international schools. It combines proven buyer journey frameworks (awareness, consideration, decision) with educational market expertise to create high-converting email campaigns.

**Use this skill when:**
- Launching new educational products or curricula
- Building lead nurture campaigns for K-12 programs
- Creating multi-touch email sequences for EdTech solutions
- Developing buyer journey campaigns for international school markets
- You need a structured, research-backed approach to educational marketing

---

## Critical Rules

These rules override any conflicting guidance elsewhere in this skill. They are non-negotiable.

### 1. COPYWRITING STANDARDS INTEGRATION

All email copy produced by this skill MUST comply with the B2B copywriting standards defined in the `hammad-b2b-copywriting` skill. Specifically:
- Lead with customer benefits, not company claims
- Use "you-phrasing" (the word "you" must appear more than the company/product name)
- Write with confidence, no hedging ("we believe," "may help," "perhaps")
- Eliminate company-centric language (never open with the company name)
- Kill jargon ("synergy," "leverage," "best-in-class," "holistic," "innovative")
- Never use em dashes in any email copy
- Professional but warm tone: a knowledgeable colleague, not a brochure

If any guidance in this skill conflicts with the copywriting standards, the copywriting standards win.

### 2. ONE CTA PER EMAIL

Every email must have exactly one primary call-to-action button. No exceptions. Do not offer "2-3 CTA options" as suggested in older frameworks. Multiple buttons dilute focus and reduce click-through rates.

A passive footer link ("Want to speak to someone on our team? Get in touch") is acceptable as a standing option across all emails, but it must never be styled as a button competing with the primary CTA.

### 3. BREVITY FIRST

Awareness-stage emails must be scannable in under 60 seconds. If a draft feels like it's doing the work of two or three emails, it is, and it needs to be cut.

Guidelines by stage:
- Awareness emails: 150-250 words. Short paragraphs. One core idea.
- Consideration emails: 200-350 words. Evidence and proof points earn more space, but stay tight.
- Decision emails: 150-250 words. The final email should be the shortest in the sequence: personal, direct, no fluff.

### 4. INTERNAL DOCUMENTS ARE NEVER CUSTOMER-FACING

Any file whose name begins with `INTERNAL_` or contains "INTERNAL ONLY" or "Internal" in its title is strictly for informing strategy, positioning, objection-handling, and messaging decisions. Content from these documents must NEVER be shared with prospects, linked in emails, offered as downloads, or referenced in any customer-facing communication. They are behind-the-scenes resources only.

### 5. CASE STUDY LOCALISATION FOR INTERNATIONAL MARKETS

When using case studies originating from the US for international audiences:
- Lead with outcomes and data in email copy, never school names or geographic identifiers
- Remove or replace US-specific language: "districts" becomes "school networks" or "school groups," "state standards" becomes "national or curriculum standards," "state assessments" becomes "standardised assessments"
- School names, city names, and state names must not appear in the email body copy
- The downloadable PDF or linked case study may contain these details, and that is acceptable. The principle is: the email sells the outcome, the asset provides the context
- When referencing case study results, use phrasing like "a network of 77 schools" or "a middle school study" rather than naming the institution

### 6. FORMAT DECISION: EMAIL BODY VS. DOWNLOADABLE ASSET

Before creating a downloadable PDF or gated asset for any email, apply this test:

- If the content is fewer than 3 stats, 1 core insight, or 1 short framework: put it in the email body. Do not create a download. The friction of clicking to download outweighs the value of gating thin content.
- If the content offers genuine depth the email cannot contain (a whitepaper, a full case study, a detailed research report, a multi-page implementation guide): create or link to a downloadable asset.
- If in doubt, put it in the email. You can always offer a deeper-dive asset as a secondary resource.

### 7. PRODUCT INTRODUCTION TIMING

The product may be named in Email 1, but only after the problem has been fully framed. The product arrives as the answer to a question the reader is already asking, not as an unsolicited pitch. The structure is: problem → insight → product as the research-backed answer → CTA.

Do NOT withhold the product name until Email 3 or later. Cold prospects who recognise their problem want to know what solves it. Delaying the reveal creates frustration, not curiosity.

---

## Flexible Email Count

This skill does NOT prescribe a fixed number of emails. The sequence length should match the complexity of the product, the depth of available proof points, and the length of the buying cycle.

Guidelines:
- Minimum: 3 emails per buyer journey stage (9 total)
- Typical: 3-4 emails per stage (9-12 total)
- Complex/high-ticket products: 4-5 emails per stage (12-15 total)
- Simple/low-ticket products: 2-3 emails per stage (6-9 total)

The number per stage does not need to be equal. A product with strong research but limited case studies might have 4 awareness emails, 3 consideration emails, and 3 decision emails.

---

## Core Workflow

### PHASE 1: DISCOVERY (15-20 minutes)

Start by gathering essential information. Ask the user structured questions organized in five categories:

#### 1. PRODUCT & PROGRAM INFORMATION

```
PRODUCT BASICS
   - Product name (exact branding/capitalisation):
   - Target audience (grade levels, subject areas, buyer personas):
   - Core problem it solves (the gap or need):
   - Top 3-5 differentiators:
   - Why is this different/better?

GEOGRAPHIC MARKETS
   - Which regions are you targeting? (e.g., Asia, Middle East, Europe, ANZ)
   - What are the school buying cycle timelines in each region?
```

#### 2. AVAILABLE ASSETS

```
ASSETS YOU HAVE
   - Product brochures/flyers (PDFs):
   - Sample materials (student editions, teacher editions):
   - Standards alignment documents:
   - Case studies or testimonials:
   - Pricing/package information:
   - Landing page URL:
   - Video content (if available):
   - Trust signals or certifications (e.g., ST4S, ISO, data privacy badges):
   - On-demand webinars or recorded sessions:
   - Internal-only documents (objection guides, competitive analyses, sales playbooks):
```

#### 3. CAMPAIGN PARAMETERS

```
CAMPAIGN GOALS & TIMELINE
   - Database size (how many contacts to reach?):
   - Specific conversion targets (MQLs, opportunities, sales?):
   - Budget constraints (affects asset creation):
   - Campaign timeline/urgency:
   - Existing performance data from past campaigns:
   - Landing page bandwidth (can you create multiple pages, or do you need a single page?):
```

#### 4. MARKET CONTEXT

```
COMPETITIVE & MARKET CONTEXT
   - What approach are schools currently using?
   - Main barriers to adoption (cost, training, time, integration?):
   - Who are the main competitors/alternatives?
   - What industry trends are creating demand?
   - Which buying decision-makers are you targeting (teacher, principal, admin)?
```

#### 5. EXISTING CAMPAIGNS (NEW)

```
EXISTING CAMPAIGNS
   - Are there any existing email campaigns for this product (from any region)?
   - If yes, can you share them for audit?
   - What worked or didn't work in previous campaigns?
```

If existing campaign emails are provided, audit them against the B2B copywriting standards before drafting new emails. Document specific failures (company-centric openings, multiple CTAs, broken merge tags, generic language) and ensure the new sequence corrects them.

---

### PHASE 2: STRATEGIC PLANNING (10 minutes)

Based on discovery, synthesize:

1. **Core messaging angle** - The single biggest problem/opportunity to lead with
2. **Credibility foundation** - What proof points matter most to this audience
3. **Urgency lever** - What creates genuine time sensitivity (fiscal year end, adoption cycles, etc.)
4. **Decision sequence** - Which objections/questions appear in which email
5. **Asset audit** - What exists, what needs to be created, what's internal-only

Create a Campaign Strategy Summary and a Sequence Planning Table.

#### SEQUENCE PLANNING TABLE (Required Output)

Before writing any email copy, produce a table with the following columns:

| Column | Description |
|--------|-------------|
| Buyer Journey Stage | Awareness / Consideration / Sale |
| Email # | Sequential number |
| Purpose & Funnel Movement | What the email does, what it contains, how it moves the prospect forward |
| Source Documents | Which internal files informed the email content (for reference, not for the customer) |
| Customer-Facing Assets | The exact file names, videos, or links that serve as the CTA or downloadable |

This table must be approved by the user before any email copy is drafted.

---

### PHASE 3: VIDEO ASSESSMENT (NEW)

If video assets are available, assess each one before placing it in the sequence:

| Criteria | Guidance |
|----------|----------|
| Under 4 minutes | Suitable as a primary email CTA. Short enough to watch in full. |
| 4-10 minutes | Suitable as a secondary CTA or landing page embed. |
| Over 10 minutes | Landing page only. Position as "on-demand session" or "webinar recording." Too long for an email CTA. |
| Animated explainer | Best for awareness stage. Explains concepts without requiring prior product knowledge. |
| Classroom/teacher video | Best for social proof emails (consideration stage). Real voices carry more weight than animation. |
| US school prominently named in title | Usable on landing page but avoid as a primary email CTA for international campaigns. If the content is strong, the video can be embedded without drawing attention to the US origin. |

---

### PHASE 4: LANDING PAGE STRATEGY (NEW)

Determine the landing page approach before writing emails, because CTAs depend on where they point.

**Single-page approach (recommended for resource-constrained teams):**
- One primary landing page serves as the central hub for the entire sequence
- Each email CTA deep-links to a specific section (e.g., #results, #resources, #free-trial)
- The page should include: benefit-led hero section, short explainer video, results section with key stats, downloadable resources hub, trust signals/badges, and a consultation request form
- All downloadable assets (whitepapers, case studies, brochures) live in a resources section on this page

**Multi-page approach (if bandwidth allows):**
- Consider a dedicated admin/leadership variant for the consideration stage (when the email shifts focus from teachers to decision-makers)
- Event-specific landing pages if the campaign includes webinar promotions

Always specify the landing page approach in the planning output so email CTAs can be written with the correct destination in mind.

---

### PHASE 5: TRUST SIGNALS ASSESSMENT (NEW)

Prompt the user to identify any certifications, safety badges, compliance credentials, or third-party validations the product holds. Examples:
- Safer Technologies 4 Schools (ST4S) badge
- ISO certifications
- Data privacy compliance (GDPR, COPPA, FERPA equivalents)
- Independent efficacy studies or third-party research
- Industry awards (CODiE, EdTech awards)

Place trust signals in:
- Consideration stage emails (where adoption concerns and risk aversion surface)
- The final "complete picture" email (where you summarise the full value proposition)
- The landing page footer or trust signals bar

---

### PHASE 6: EMAIL GENERATION (30-45 minutes)

Generate all emails using the framework below. For each email, provide:

```
SUBJECT LINE (provide 3 options: A/B/C)
Option A: [Problem/question-focused]
Option B: [Stat or curiosity-driven]
Option C: [Direct benefit or solution]

---

EMAIL BODY

[Greeting - use first name]

[Opening paragraph - Hook with the reader's situation or pain point]

[Body paragraphs - 2-3 short paragraphs, 2-4 sentences each]

[Product/solution positioning - earned, not forced]

[CTA paragraph - One clear action]

[Closing - Professional but warm]

---

COPYWRITING SELF-CHECK
- Does it lead with a customer benefit? [Y/N]
- Is "you" used more than the company name? [Y/N]
- Any hedging phrases? [Y/N - list them]
- No em dashes? [Y/N]
- One clear CTA? [Y/N]
- Appropriate for buyer stage? [Y/N]
- Scannable in under 60 seconds (awareness) or 90 seconds (consideration)? [Y/N]
- Would a school leader actually want to read this? [Y/N]

---

TECHNICAL SPECS
- Send timing: Week [X], [Day] at 9 AM recipient timezone
- Audience: [Segment definition]
- Exclude: [Who should NOT receive]
- Required asset: [What needs to exist - specify if it already exists or needs creation]
- CTA link with UTM: [Full parameters]
- Expected performance: [Open/CTR/conversion targets]
```

---

## The Email Framework

### STAGE 1: AWARENESS (Minimum 3 emails)
**Goal:** Frame the problem, shift thinking, introduce the product as the research-backed answer

#### EMAIL 1: The Problem
- **Opening:** Lead with the reader's classroom reality. Make them feel seen.
- **Body:** Introduce 1-2 sharp statistics that quantify the problem. Keep it tight.
- **Product introduction:** Name the product in the bottom third of the email, after the problem is framed. The product arrives as the answer, not the pitch.
- **CTA:** One substantive next step (whitepaper, research report, explainer video). Must offer genuine depth.
- **Tone:** Problem-focused, empathetic, research-backed.
- **Length:** 150-250 words.

#### EMAIL 2: Why Current Approaches Fail
- **Opening:** Validate the reader's current efforts, then explain why they fall short.
- **Body:** Introduce a conceptual shift (e.g., knowledge is non-linear, practice must be matched to readiness).
- **CTA:** Animated explainer video or concept-level educational resource.
- **Tone:** Empathetic then challenging. Respect their effort, redirect their thinking.
- **Length:** 150-250 words.

#### EMAIL 3: The Vision
- **Opening:** Paint a picture of what the solution looks like in practice.
- **Body:** Describe the product experience (the cycle, the approach, the student journey) without drowning in features.
- **CTA:** Short product walkthrough video or programme overview.
- **Tone:** Visionary but grounded. Show what's possible, not what's theoretical.
- **Length:** 200-300 words.

#### EMAIL 4 (if needed): Research Credibility
- **Opening:** Anchor the product in its research foundation.
- **Body:** Explain the science or methodology behind the product. Why it works, not just what it does.
- **CTA:** Research whitepaper or methodology document.
- **Tone:** Authoritative, evidence-based, intellectual.
- **Length:** 200-300 words.

---

### STAGE 2: CONSIDERATION (Minimum 3 emails)
**Goal:** Address objections, build credibility, provide social proof

#### EMAIL 5: Overcoming the #1 Barrier
- **Opening:** Name the biggest adoption obstacle (usually teacher workload, implementation complexity, or cost).
- **Body:** Show specifically how the product addresses this barrier. Include trust signals (certifications, safety badges).
- **CTA:** Free trial, implementation guide, or support overview.
- **Tone:** Solution-focused, practical, reassuring.
- **Length:** 200-350 words.

#### EMAIL 6: Evidence & Outcomes
- **Opening:** Lead with the strongest data point.
- **Body:** Present research findings, efficacy data, or proficiency study results. Use specific numbers.
- **CTA:** Full research report or outcomes study download.
- **Tone:** Data-driven, confident, evidence-led.
- **Length:** 200-350 words.

#### EMAIL 7: Decision-Maker View
- **Opening:** Shift focus from end-users (teachers) to buyers (principals, curriculum coordinators, administrators).
- **Body:** Show what the product looks like from a leadership perspective: reporting dashboards, school-wide visibility, accountability data.
- **CTA:** Admin report sample, on-demand webinar, or leadership-focused walkthrough.
- **Tone:** Strategic, results-oriented, leadership-level.
- **Length:** 200-350 words.

#### EMAIL 8: Social Proof
- **Opening:** Feature case study results, leading with outcomes not geography.
- **Body:** Challenge → Solution → Results structure. Include teacher or leader voice quotes.
- **CTA:** Video case study or full case study PDF download.
- **Tone:** Story-driven, relatable, evidence-backed.
- **Length:** 200-350 words.
- **Case study rule:** Follow the localisation rules in Critical Rules section 5.

---

### STAGE 3: SALE (Minimum 3 emails)
**Goal:** Remove friction, demonstrate total value, drive conversion

#### EMAIL 9: Flexibility & Fit
- **Opening:** Address implementation concerns directly.
- **Body:** Show the product fits their context: grade coverage, device compatibility, instructional models, curriculum alignment.
- **CTA:** Book a consultation call.
- **Tone:** Practical, reassuring, partnership-oriented.
- **Length:** 200-300 words.

#### EMAIL 10: Experience It
- **Opening:** Invite hands-on experience with the product.
- **Body:** Frame the trial or demo as zero-risk. Provide clear steps.
- **CTA:** Start free trial or book personalised demo.
- **Tone:** Inviting, low-pressure, action-oriented.
- **Length:** 150-250 words.

#### EMAIL 11: The Complete Picture
- **Opening:** Summarise the full value proposition.
- **Body:** Everything included: product, support, training, reporting, certifications, ongoing service. Position as an investment, not a cost.
- **CTA:** Request a proposal or pricing conversation.
- **Tone:** Comprehensive, confident, investment-minded.
- **Length:** 200-300 words.

#### EMAIL 12: Final Push
- **Opening:** Personal, direct tone from the regional sales representative.
- **Body:** Brief recap of the journey. Genuine urgency tied to school planning cycles. Direct reply option.
- **CTA:** Reply to this email or click to book a time. No PDFs, no videos. This is a plain-text, personal email.
- **Tone:** Personal, direct, conversational, genuine.
- **Length:** 100-200 words. Shortest email in the sequence.

---

## Email Writing Standards

### FORMATTING RULES

1. **No em dashes** - Use colons, commas, periods, or restructure the sentence
2. **Lead with the reader's situation** - Never open with the company name
3. **One CTA per email** - Non-negotiable (see Critical Rules)
4. **Cite sources** - Use footnote citations [1], [2] when using statistics
5. **Short paragraphs** - 2-4 sentences max for mobile readability
6. **Bold sparingly** - Use bold for key stats or the single most important sentence. Not for emphasis on every other line
7. **Email length** - Follow the word count guidelines per stage in Critical Rules section 3

### SUBJECT LINE FORMULA

Provide 3 options per email (for A/B testing):

| Type | Focus | Example |
|------|-------|---------|
| **Option A** | Problem/question | "Your students have maths gaps you can't see yet" |
| **Option B** | Stat/curiosity | "50% of students start the year missing prerequisite skills" |
| **Option C** | Direct benefit | "How one school network improved maths scores by 25%" |

**Subject Line Best Practices:**
- 40-50 characters (optimal for mobile preview)
- Avoid spam trigger words (Free!, Limited Time!!!)
- Use specificity (numbers, metrics)
- Do not use school names in subject lines for international campaigns

### CTA STRATEGY BY STAGE

| Stage | CTA Type | Example Button Text |
|-------|----------|---------------------|
| **Awareness** | Educational depth | "Download the [Research] Whitepaper" |
| **Consideration** | Evidence & proof | "See the Full Outcomes Report" |
| **Consideration** | Experience | "Start Your Free Trial" |
| **Sale** | Conversion | "Book a Consultation" |
| **Sale** | Personal | "Reply to This Email" (no button needed) |

### TONE & VOICE GUIDELINES

| Dimension | Standard |
|-----------|----------|
| **Professionalism** | Professional but warm, not corporate-speak |
| **Empathy** | Validate before solving |
| **Conciseness** | Respect busy educators' limited time |
| **Evidence** | Back claims with research, stats, case study data |
| **Action** | Every email should move reader toward the single CTA |
| **You-focus** | "You" and "your" must outnumber the company/product name |

---

## Regional Buying Cycle Mapping

### AUSTRALIA & NEW ZEALAND
- **Planning window:** October-December
- **Decision finalization:** April
- **Urgency angle:** Term planning, curriculum adoption deadlines

### MIDDLE EAST
- **Planning window:** March-June
- **Decision finalization:** May
- **Urgency angle:** Academic year planning for the following September start

### ASIA (Singapore, Hong Kong, India, etc.)
- **Planning window:** September-December
- **Decision finalization:** January
- **Urgency angle:** Calendar year planning, January implementation window

### EUROPE
- **Planning window:** April-July
- **Decision finalization:** June
- **Urgency angle:** September academic year start, budget allocation by June

---

## Landing Page Standards

### SINGLE-PAGE APPROACH (Default)

A single enhanced landing page should include:
1. **Hero section:** Benefit-led headline (not a product description). E.g., "Every student on the right path to maths mastery" not "ALEKS is a web-based assessment and learning system."
2. **Explainer video:** Short (under 4 minutes) embedded prominently.
3. **Results section:** 2-3 key stats from efficacy research.
4. **Resources hub:** All downloadable PDFs from the nurture sequence (whitepapers, case studies, programme overviews, research reports).
5. **Trust signals:** Certifications, badges, third-party validations.
6. **Consultation form:** Primary conversion mechanism, always visible.
7. **Secondary CTA:** Free trial link.

Each email CTA should deep-link to the relevant section of this page using anchor links (e.g., #results, #resources, #free-trial).

---

## Source Documentation Requirement

Every email in the planning output must specify:

1. **Source documents (internal reference):** Which files, case studies, research papers, objection guides, or internal documents informed the email's content and messaging. These are never shared with the customer.

2. **Customer-facing assets:** The exact file names, video titles, or URLs that serve as the email's CTA or downloadable offering. Specify whether each asset already exists or needs to be created.

This prevents the common problem of planning emails around assets that don't exist and ensures clear traceability from strategy to execution.

---

## Video Assessment Framework

When video assets are available, evaluate and place them using these criteria:

**For email CTAs (primary use):**
- Must be under 4 minutes
- Animated explainers work best for awareness stage
- Classroom/teacher testimony videos work best for social proof (consideration stage)
- Video case studies showing real results are the most compelling social proof assets

**For landing page only:**
- Full product overview sessions (15+ minutes)
- On-demand webinar recordings
- Videos with US school names prominently in the title (for international campaigns)

**For on-demand/secondary CTA:**
- 5-10 minute deep-dive videos
- "Getting to Know [Product]" walkthroughs

Always note the video's length, view count (if available), and content type when making placement decisions.

---

## Existing Campaign Audit (NEW)

If existing campaign emails are provided (from any region or team), audit them before drafting new emails. Check for:

1. **Company-centric openings** - Does the email start with the company name or "We"?
2. **Multiple competing CTAs** - Are there 2+ buttons fighting for attention?
3. **Broken personalisation** - Unresolved merge tags, US-specific dynamic content for international audiences?
4. **Generic language** - Could this email be about any EdTech product, or is it specific to this one?
5. **Buyer journey progression** - Do the emails feel like a connected sequence or disconnected standalone pitches?
6. **Compliance with copywriting standards** - Run through the full B2B copywriting checklist.

Document specific failures and ensure the new sequence corrects each one.

---

## Quality Assurance Checklist

Before finalizing and delivering the campaign, verify:

### MESSAGING COHERENCE
- [ ] Does each email have a single, clear purpose in the buyer journey?
- [ ] Is there a logical escalation from problem awareness to decision?
- [ ] Does the product introduction feel earned, not forced?
- [ ] Are case study references localised (outcomes-led, no US geography in email copy)?
- [ ] Are internal-only documents excluded from all customer-facing assets?

### COPYWRITING STANDARDS
- [ ] Every email checked against the B2B copywriting self-check?
- [ ] "You/your" outnumbers company/product name in every email?
- [ ] Zero hedging language across the full sequence?
- [ ] Zero em dashes across the full sequence?
- [ ] One CTA per email, no exceptions?

### BREVITY
- [ ] Awareness emails under 250 words?
- [ ] No email tries to do the work of two emails?
- [ ] Final email is the shortest in the sequence?

### TECHNICAL ACCURACY
- [ ] Product name spelled/capitalised correctly throughout?
- [ ] All CTAs have proper UTM parameters?
- [ ] Regional variants match actual buying cycles?
- [ ] Asset list distinguishes "exists" vs. "needs creation"?
- [ ] Source documents column completed for every email?
- [ ] Customer-facing assets column completed for every email?
- [ ] No internal-only documents appear in customer-facing assets?

### LANDING PAGE
- [ ] Landing page approach specified (single vs. multi)?
- [ ] All email CTAs point to a defined destination?
- [ ] Landing page leads with benefit, not product description?

---

## Troubleshooting Guide

### PROBLEM: Low Open Rates (<20%)

**Possible causes:**
- Subject lines not compelling enough
- Email list quality/deliverability issues
- Send time not optimized for audience
- Email sender name not recognized

**Solutions:**
- A/B test stronger subject lines (use Option B or C from framework)
- Clean email list, check spam filtering
- Test different send times (AM vs. PM, mid-week vs. end of week)
- Adjust sender name to person name vs. company name

---

### PROBLEM: Low Click-Through Rate (<2%)

**Possible causes:**
- CTA not clear or compelling
- Asset/offer not relevant to email content
- Email too long/text-heavy
- CTA buried at the bottom

**Solutions:**
- Strengthen CTA button text (action verbs, specificity)
- Ensure email content and CTA are directly connected
- Shorten email, increase white space
- Move CTA higher if the email runs long

---

### PROBLEM: High Unsubscribe Rate (>0.5%)

**Possible causes:**
- Sending too frequently (fatigue)
- Messaging not resonating with audience
- Targeting too broad
- Content feels too sales-heavy too early

**Solutions:**
- Increase gap between emails (add 1 week between sends)
- Reassess messaging fit
- Tighten audience targeting
- Adjust tone: more education, less selling in awareness emails

---

### PROBLEM: Nurture Fatigue Mid-Sequence

**Possible causes:**
- Emails feel repetitive
- Sending too frequently
- Content not valuable enough to justify frequency

**Solutions:**
- Add 1-week gap between awareness and consideration stages
- Increase education/value content relative to selling
- Vary email length and format
- Segment out highly engaged prospects for direct sales conversation (remove from sequence)

---

## Measuring Success

### INDIVIDUAL EMAIL SUCCESS METRICS

| Metric | Awareness | Consideration | Decision | Action If Low |
|--------|-----------|----------------|----------|---------------|
| **Open Rate** | 25-35% | 20-30% | 20-25% | Test subject lines |
| **CTR** | 2-3% | 2.5-3.5% | 3-5% | Strengthen CTA |
| **Conversion Rate** | 0.5-1% | 1-2% | 2-5% | Better targeting |
| **Unsubscribe Rate** | <0.5% | <0.3% | <0.2% | Review messaging |

### RED FLAGS & INTERVENTIONS

| Red Flag | Intervention |
|----------|--------------|
| Email 1 opens <20% | Pause, A/B test subject lines, resend in 3 days |
| Mid-sequence CTR <1.5% | Adjust bridge messaging, strengthen CTA |
| Social proof email <2% CTR | Case study not resonating, try different outcomes or video format |
| Final emails unsubscribes spike | Reduce urgency messaging, too much pressure |
| No opportunities generated | Review lead quality, check CRM sync, audit sales follow-up speed |

---

## Final Pre-Launch Checklist

### CAMPAIGN CONTENT
- [ ] All emails written and reviewed by stakeholders
- [ ] Subject lines tested and finalized
- [ ] All CTAs link to correct landing pages/assets
- [ ] UTM parameters consistent and trackable
- [ ] Spelling/grammar checked, brand names correct

### TECHNICAL SETUP
- [ ] All assets created or sourced (PDFs, landing pages, videos)
- [ ] Landing pages tested and converting (forms working, no broken links)
- [ ] Email template coded and tested in ESP
- [ ] Audience segments defined, clean, and excluding converters
- [ ] Automation workflows configured (send timing, triggers)

### TEAM ALIGNMENT
- [ ] Sales team briefed on campaign, lead routing, SLAs
- [ ] Marketing leadership approval on messaging/positioning
- [ ] All stakeholders sign off on launch date

### MONITORING SETUP
- [ ] Performance tracking dashboard created
- [ ] Red flag thresholds defined and communicated
- [ ] Weekly review cadence scheduled
- [ ] Person assigned to monitor and optimize

### GO/NO-GO
- [ ] All checkboxes above completed?
- [ ] **LAUNCH**

---

**End of Skill**

This Email Nurture Campaign Builder generates complete, strategic nurture sequences for educational products targeting international schools. It enforces single-CTA emails, brevity-first drafting, B2B copywriting standards compliance, and proper localisation of US-origin case studies for international markets.

*Version 2.0 - Updated April 2026*
*Changelog: Flexible email count, single-CTA enforcement, brevity guidelines, internal document protection, case study localisation rules, format decision framework, video assessment, landing page strategy, trust signals, existing campaign audit, copywriting standards integration, source documentation requirement.*
