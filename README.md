# Campaign Portal — Internal Sales Reference

A single-page **internal reference** for the McGraw Hill International K-12 sales team. It surfaces every pre-sale
email **nurture program** we're running for the coming academic year, section by section, so a rep can quickly see
what each program is about, what every email does, preview the full creative, jump to the Salesforce report, and
download an `.eml` to forward to their own contacts.

> **Internal use only.** Not for external distribution. Built to McGraw Hill Brand Guidelines v6.1 (Heritage Red
> `#E21A23`, Academic Blue `#0B48BC`, Vibrant Violet `#5F14C1`, Proxima Nova / Mulish, the Cubic Grid).

## What's on the page

- **Hero** — a simple, sales-oriented intro framing the page as a handy portal.
- **One section per program** (Level Up, ALEKS, Reading Labs Online, Reveal Math for IB PYP), each with:
  - the program **heading** + a couple of lines of **description**,
  - a link to the **Salesforce report** that tracks contacts/leads through the full nurture (where one exists),
  - a **carousel of email thumbnails** across Awareness → Consideration → Decision. Each thumbnail has a title
    capturing the email's essence and a couple of lines on the offer / CTA / crux. Click a thumbnail to open a
    **modal** with the full rendered email and a **Download .eml** button.
- **Footer** — evergreen reference links: how-to guides, screencasts, and wikis (add contacts to a nurture, send a
  nurture email to your contacts, naming conventions, brand guidelines, etc.).

Emails that are still in production (copy lives in Marketo, or is being written) appear as **Draft** cards — the
thumbnail and strategic summary still show, and the modal explains where the live creative lives.

## Data source

All content is pulled faithfully from the **Marketing Team workspace in Notion** (Master Campaigns → Channel
Campaigns), the same source of truth used by the nurture-build pipeline.

| Program | Emails on page | Full creative | Salesforce report |
|---|---|---|---|
| Level Up | 9 (AW01–DE09) | ✅ all 9 | pending |
| ALEKS | 5 (AW01–CO05) | ✅ all 5 | pending |
| Reading Labs Online | 9 (AW01–DE09) | draft (in production) | pending |
| Reveal Math for IB PYP | 2 (AW01–AW02) | draft (in Marketo) | ✅ live |

## Project layout

```
index.html              ← the portal (self-contained: inline CSS + JS + data). This is what you host.
emails/*.eml            ← downloadable email files (one per authored email)
scripts/template.html   ← HTML/CSS/JS engine (no data)
scripts/build.py        ← single source of truth (content) → generates emails/ + index.html
```

## Rebuilding

Edit content in `scripts/build.py` (or the engine in `scripts/template.html`), then:

```bash
python3 scripts/build.py
```

This regenerates every `.eml` and rewrites `index.html` with the data injected inline.

## Hosting on Marketo

`index.html` is fully self-contained (the only external dependencies are the Google Fonts CDN and the `.eml`
download files). To host as a Marketo landing page:

1. Paste the contents of `index.html` into a Marketo **custom HTML** landing page (or a Free-Form approver page).
2. Upload the files in `emails/` to Marketo (Design Studio → Files) or any static host, and set
   `config.emlBase` in `scripts/build.py` to that absolute URL, then rebuild. (Defaults to relative `emails/`,
   which works when the `.eml` files sit alongside `index.html`.)
