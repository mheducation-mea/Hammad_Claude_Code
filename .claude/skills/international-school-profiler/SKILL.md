---
name: international-school-profiler
description: Create comprehensive, structured profiles of international schools to support ABM (Account-Based Marketing) campaigns. Use this skill whenever a user asks to profile, research, or create detailed intelligence on any international school. Triggers include school name + location requests, school website URLs provided, existing school documentation submitted, or general requests to "research a school," "create a school profile," or "gather school intelligence." Always use this skill for international school intelligence gathering regardless of the school's name, location, or educational framework.
---

# International School Profiler

A skill for researching and creating comprehensive business intelligence profiles of international schools to support Account-Based Marketing campaigns.

> **Requires tools:** this skill uses Claude Code's `WebSearch` and `WebFetch` tools for live research.

## Overview

International schools are complex organizations with specific decision-making structures, challenges, and opportunities. This skill enables Claude to transform school research into actionable, structured profiles that support personalized outreach and solution positioning.

The skill outputs a 3,000-5,000 word profile organized into 16 strategic sections designed to identify decision-makers, understand challenges, and align educational solutions.

---

## When to Use This Skill

**Explicit triggers:**
- User provides a school name and location
- User shares a school website URL
- User uploads school documentation
- User requests "create a profile for [school]"
- User asks to "research" or "intelligence gather" on a school

**Contextual triggers:**
- ABM campaign planning targeting educational institutions
- Need to understand school structure, challenges, or decision-makers
- Solution positioning for educational technology or programs
- Competitive analysis of international school networks
- Lead research for education sector sales/partnerships

---

## Research Process

### Step 1: Initial Web Search

Execute comprehensive web search using school name + location to gather foundational intelligence:

```
[School Name] international school [City/Country]
```

From official and third-party sources, collect:
- Official school website and key pages
- Wikipedia entries
- International school directories (ISS, AISA, FOBISSEA, etc.)
- Education news and press releases
- Accreditation body records
- Social media profiles (LinkedIn, Facebook, Instagram)
- Local education ministry records
- Local news coverage

**Action:** Run 2-3 broad web searches to triangulate school information.

### Step 2: Deep Dive Searches

Conduct 4-6 targeted searches for specific intelligence categories:

**History & Background:**
```
"[School Name]" founded history established
```

**Curriculum & Academic Programs:**
```
"[School Name]" curriculum IB AP programs
"[School Name]" PYP MYP DP accreditation
```

**Admissions, Tuition & Demographics:**
```
"[School Name]" admissions tuition fees enrollment
"[School Name]" tuition costs student body
```

**Facilities & Campus Infrastructure:**
```
"[School Name]" facilities campus athletics
"[School Name]" campus size buildings
```

**Leadership & Decision-Makers:**
```
"[School Name]" head of school principal leadership
"[School Name]" board of directors governance
```

**Athletics & Extracurriculars:**
```
"[School Name]" athletics sports conference
"[School Name]" clubs activities
```

**Action:** Execute 5-8 targeted searches minimum. Use `WebFetch` to capture full content from official school pages and credible education news sources.

### Step 3: Verify & Cross-Reference

- Cross-check facts across multiple sources
- Prioritize official school sources (website, official publications)
- Use most recent information available (within last 2 years for static facts, current year for enrollment/tuition)
- Flag conflicting information with source notation
- Note when information is unavailable or approximate
- Verify leadership names and titles against current LinkedIn profiles

---

## Profile Output Structure

Present the completed profile using this exact 16-section structure. Use Markdown formatting with H4 (####) headers for each section.

### **[School Name] – [Campus Location]**

#### **School Setup and History**

Include:
- Founding year, founder name, founding mission/story
- Major milestones (expansions, relocations, campus developments)
- Affiliation with networks or educational organizations
- Current enrollment numbers and growth trajectory
- Special designations ("oldest," "first," "largest" in region, etc.)
- Any notable institutional changes or restructuring

**Format example:**
> Founded in 1973 by Edward Ben Adams as a small English-language program, [School] has grown to serve 850 students across three divisions. The school relocated to its current 8.5-acre campus in 2008 and became an accredited member of the AISA in 2010.

#### **Curriculum and Academic Focus**

Include:
- Educational framework (IB, AP, American, British, National curriculum, etc.)
- Grade levels served (PK-12, K-8, 6-12, etc.)
- Specific programs (IB Primary Years Programme, IB Middle Years Programme, IB Diploma, AP Capstone, etc.)
- Number of AP/IB courses offered (specific count, not vague)
- Special academic emphases (STEM, inquiry-based learning, project-based, etc.)
- Language(s) of instruction
- Faculty credentials (% with advanced degrees, average experience)
- Student-teacher ratios and typical class sizes
- Assessment philosophies (standards-based, letter grades, etc.)

**Format example:**
> Curriculum: IB Continuum (PYP, MYP, DP) for grades K-12. Faculty: 87% hold master's degrees or higher. Average class size is 15.2 students. Student-teacher ratio: 8:1.

#### **Regional and Cultural Nuances**

Include:
- Precise address and geographic context
- Proximity to major landmarks, transportation, international districts
- Student body nationality breakdown (% expatriate vs. local)
- Language demographics of student body
- Cultural and religious composition/considerations
- Local regulatory context affecting the school
- Unique regional characteristics (climate, local education ecosystem)
- Community partnerships with local organizations

**Format example:**
> Located in the Gangnam District, 15 minutes from Incheon International Airport. Student body: 92% Korean nationals, 8% expatriate. 98% Korean-speaking, with English as primary instruction language.

#### **Decision-Making Structure**

Include:
- Governance model (private institution, non-profit, proprietary, for-profit, etc.)
- Current leadership names and titles (Head of School, Principal, Executive Director)
- Board composition (names, roles, professional backgrounds if available)
- Key administrative positions and office holders
- Admission policies and decision-making criteria
- Decision-making processes for major initiatives
- Key stakeholder groups in school governance

**Format example:**
> Governance: Private, non-profit. Head of School: Dr. Jennifer Williams (2019-present). Board Chair: Park Min-jun. Admission decision: Rolling basis; competency assessments in English/Math for grades 3+.

#### **Challenges and Growth Opportunities**

Include:
- Current operational or strategic challenges
- Enrollment management issues (growth, decline, retention)
- Faculty recruitment and retention challenges
- Learning support and special education limitations
- Infrastructure or facility gaps
- Regulatory compliance issues
- Technology adoption barriers
- Competitive positioning challenges
- Community engagement gaps

**Format example:**
> Key challenges: Faculty retention in competitive international school market; growing wait lists for junior grades suggesting enrollment demand exceeds capacity; limited learning support staffing; aging science lab facilities requiring upgrade.

#### **Vision and Successes**

Include:
- Mission statement (exact quote from school materials)
- Vision statement (exact quote)
- Core values framework (list key values)
- Notable achievements (last 3-5 years)
- Recognition and awards received
- Accreditation status and dates
- Graduate outcomes and college placement statistics
- Notable alumni or achievements

**Format example:**
> Mission: "To develop globally minded, compassionate learners who contribute meaningfully to their communities."
> Vision: "To be the leading international school in Southeast Asia."
> Accreditation: WASC (2022-2027), IB authorized (since 2015).

#### **Student Body and Educator Profile**

Include:
- Total enrollment by division (Early Years, Elementary, Middle, High School)
- Enrollment trends (growth rate, projections)
- Student demographic details (age range, nationality, socioeconomic range if available)
- Faculty size and hiring practices
- Professional development emphasis and budget allocation
- Support staff (counselors, learning specialists, nurses, etc.)
- Community engagement structures (parent associations, etc.)

**Format example:**
> Total enrollment: 850 students (Early Years: 120, Elementary: 280, Middle: 220, High School: 230). Faculty: 95 full-time staff; recruitment focus on Master's-degree holders. Counseling: 1 full-time counselor + 2 part-time specialists. Learning support team: 4 specialists covering 8% of student body.

#### **Innovation and Signature Initiatives**

Include:
- Unique or distinctive programs
- Technology integration level (1:1 devices, learning management systems, etc.)
- Student agency/voice initiatives
- Special partnerships or collaborative projects
- Research or capstone programs
- Community service/social responsibility requirements
- Leadership development programs (student government, peer mentoring, etc.)

**Format example:**
> Signature initiatives: Environmental Science Research Program (partnerships with local universities); Student-led social enterprises program; 1:1 iPad program for grades 3-12; Required 40-hour service learning for graduation.

#### **Facilities and Campus**

Include:
- Total campus size (acres or square meters)
- Building descriptions (number, age, primary uses)
- Athletic facilities (gymnasiums, pools, sports fields, courts)
- Academic facilities (science labs, technology centers, libraries, theaters, maker spaces)
- Technology infrastructure (network capacity, device ratios)
- Outdoor spaces (playgrounds, gardens, sports fields, green spaces)
- Special facilities (music studios, art centers, performance venues)
- Accessibility and inclusive design features

**Format example:**
> Campus: 8.5 acres in suburban location. 12 buildings including 3 classroom wings, dedicated science/technology center, library (14,000 volumes), 2 athletic facilities. Outdoor: 3 soccer fields, 2 tennis courts, playground area, nature reserve.

#### **Accreditation and Recognition**

Include:
- Primary accrediting bodies with certification dates and next review dates
- Re-accreditation schedule
- Ministry of Education recognition or registration
- Professional association memberships (AISA, FOBISSEA, etc.)
- External rankings or validations
- Awards and distinctions received
- Audit or compliance status

**Format example:**
> Accreditation: WASC (2022-2027 cycle), IB Authorized (Primary, Middle, Diploma), Korean Ministry of Education registered. Member of AISA, EARCOS. Next WASC visit: 2025.

#### **University Placement and Outcomes**

Include:
- Graduation rate (%)
- University acceptance rate (%)
- Geographic distribution of university placements
- Specific universities (name 20-30 institutions where graduates attend)
- Average standardized test scores (AP, IB, SAT, ACT if applicable)
- Scholarship and financial aid success rate
- Career outcomes (if tracked/available)
- College counseling approach and ratio

**Format example:**
> Graduation rate: 98%. College placement: 100% acceptance to university. Top placement institutions: Harvard, Stanford, MIT, Cambridge, Oxford, University of Tokyo, Seoul National University, NUS, HKUST, Erasmus. Average IB score: 36.5/45. College counselor ratio: 1:40.

#### **Admissions and Accessibility**

Include:
- Application fees (in local currency)
- Application deadlines (rolling or fixed)
- Enrollment/registration/acceptance fees
- Eligibility requirements (citizenship restrictions, language proficiency, etc.)
- Assessment requirements by grade level
- Acceptance rate (if publicly available)
- Rolling vs. fixed admissions timeline
- Waitlist policies
- Priority admission categories (siblings, staff children, nationality, etc.)

**Format example:**
> Application fee: ₩100,000. Deadline: Rolling (Early admission through February, regular through June). Assessment required for grades 3+: English reading/writing, Math reasoning. Language requirement: Fluent English. Acceptance rate: ~40%. Priority: Siblings, staff children, Korean nationals.

#### **Tuition and Financial Structure**

Include:
- Annual tuition by grade level (in local currency, clearly marked)
- First-year total costs (including all fees and non-refundable deposits)
- Payment plan options (monthly, quarterly, annual)
- Refund policies and cancellation terms
- Late payment penalties
- Financial aid availability (% receiving aid, average award)
- Sibling discounts or scholarships
- Additional mandatory fees (technology, activities, field trips, etc.)

**Format example:**
> Tuition (2024-2025): Early Years ₩32,000,000/year; Elementary ₩38,000,000/year; Middle ₩42,000,000/year; High School ₩45,000,000/year. First-year total: ~₩50,000,000 (includes registration, activity fees, uniforms). Payment plans: Monthly, quarterly, or annual. Financial aid: 12% of families receive aid averaging ₩8,000,000. Sibling discount: 5%.

#### **Extracurricular Activities and Student Life**

Include:
- School hours and daily schedule
- Club offerings (comprehensive list organized by category)
- Student publications (newspaper, yearbook, literary magazines)
- Student government structure
- Service learning programs
- Arts programs (music, drama, visual arts)
- After-school program availability and costs
- School events and traditions

**Format example:**
> School hours: 7:50 AM - 3:30 PM (M-F), with after-school programs until 5:30 PM. Clubs (25+): Model UN, Debate, Robotics, Environmental Club, Music Ensembles, Art Guild, etc. Publications: Monthly newspaper (English/Korean), annual yearbook. Student government: President, VP, class representatives. Service requirement: 40 hours minimum for graduation.

#### **Athletics and Competition**

Include:
- Athletic conference memberships (KAIAC, AISA, ISL, etc.)
- Sports offered by season (Fall, Winter, Spring)
- Division levels (competitive, recreational, intramural)
- Varsity/JV/Middle School structure
- Competition opponents and league locations
- Athletic philosophy
- Practice schedules and coaching staff

**Format example:**
> Conference: KAIAC (Korean-American Interscholastic Athletic Conference). Sports offered: 18 total. Fall: Soccer, Field Hockey, Cross Country, Golf, Tennis. Winter: Basketball, Volleyball, Swimming, Badminton. Spring: Baseball, Softball, Track. Coaching staff: 12 full-time + 8 part-time. Philosophy: "Athletics for all; emphasis on participation and character development."

#### **Transportation and Support Services**

Include:
- Bus routes and coverage areas served
- Transportation fees (monthly or annual)
- Pick-up/drop-off times and locations
- EAL/ELL program offerings and enrollment
- Learning support services available
- Special education capabilities and IEP support
- Medical/health services (nurse, clinic hours)
- Counseling services (mental health, college advising)
- Library resources (collection size, technology)

**Format example:**
> Transportation: 8 routes serving greater metro area; fees: ₩1,800,000/year. Nurse: Full-time, clinic open 7:30 AM - 4:00 PM. Counseling: College counselor (1:40 ratio), school counselor (1:150 ratio), part-time mental health specialist. EAL support: All grades; 15% of student body in EAL program. Learning support: Individual tutoring, small group instruction for identified students. Library: 14,000+ volumes, digital database access.

---

## Writing Standards

### Tone & Style
- **Factual and objective:** Use no promotional language ("outstanding," "exceptional," "prestigious")
- **Precise:** Include specific numbers, dates, percentages, currency
- **Comprehensive:** Aim for 3,500-5,000 words across all sections
- **Structured:** Maintain consistent formatting throughout
- **Professional:** Suitable for business intelligence and sales enablement

### Data Presentation
- Always cite specific numbers (not "many," "several," "most")
- Include currency symbols (₩, $, £, €, etc.) for all financial figures
- Use consistent date formats (2024-2025 academic year, established 1997, etc.)
- Specify units (meters, acres, students, percent, etc.)
- Use approximate notation (~) only when explicitly stated as estimate

**Good examples:**
- "Founded in 1973 by Edward Ben Adams"
- "Current enrollment: 850 students across three divisions"
- "Tuition: ₩45,000,000 (High School, 2024-2025 academic year)"
- "87% of faculty hold master's degrees"
- "Average class size: 15.2 students"

**Avoid:**
- "Founded many years ago"
- "Large student population"
- "Expensive tuition"
- "Highly qualified faculty"
- "Small classes"

### Handling Information Gaps

When critical information is unavailable:
- Note explicitly: "Information not publicly available"
- Don't invent or assume details
- Suggest contacting school directly when appropriate
- Use "approximately" or "estimated at" when making educated estimates from incomplete data

### Source Attribution

- Prioritize official school sources (website, publications, official statements)
- Use most recent information available
- When sources conflict, note the discrepancy with dates: "Per 2023 website [X], though 2024 LinkedIn profile states [Y]"
- Include website URLs for key facts if multiple sources exist

---

## ABM Application Framework

This profile supports Account-Based Marketing by enabling:

### **Persona Mapping**
- **Decision-makers by role:** Head of School, Director of Curriculum, Technology Director, Admissions Director, Business Manager
- **Influencers:** Faculty leaders, department heads, subject specialists
- **Budget holders:** CFO, COO, Board members

### **Challenge Identification**
Use the "Challenges and Growth Opportunities" section to identify:
- Operational gaps (technology, learning support, enrollment management)
- Expansion needs (facilities, programs, staff capacity)
- Competitive pressures (enrollment decline, student retention, college placement)
- Regulatory pressures (accreditation, local education requirements)

### **Solution Alignment**
Match McGraw Hill or other education solutions to:
- **Curriculum frameworks:** IB, AP, specific subject areas
- **Student demographics:** EAL student numbers, special education needs, diversity
- **Current programs:** Existing initiatives that solutions can enhance or extend
- **Innovation priorities:** Programs mentioned in "Signature Initiatives"
- **Operational challenges:** Technology, assessment, learning support, professional development

### **Personalization Points**
- School history for credibility building ("Since 1997, [school] has...")
- Recent achievements for congratulation hook ("Congratulations on [achievement]...")
- Specific challenges for consultative approach ("I noticed [school] is growing enrollment by [X]%, which creates...")
- Named programs for direct references ("Your environmental science research program...")
- Faculty leadership for relationship building (direct outreach to specific department heads)

### **Contact Strategy**
- **Timing:** Application deadlines guide enrollment discussions; accreditation cycles suggest curriculum review timing
- **Level:** Large schools (600+ students) = need to engage department heads before approaching leadership
- **Topic:** Match solution to identified challenge area (learning support, technology, curriculum, assessment)
- **Frame:** Use specific school data to build credibility ("Your high school has [X] AP courses and [Y]% placement to Tier-1 universities...")

---

## Quality Assurance Checklist

Before delivering the profile, verify:

- [ ] School name, location, and contact info are accurate
- [ ] All 16 sections present with proper H4 (####) headers
- [ ] Founding year and key historical dates confirmed from 2+ sources
- [ ] Curriculum framework clearly identified (IB/AP/other)
- [ ] Current enrollment numbers included with division breakdown
- [ ] Tuition fees specified by grade level with currency symbol
- [ ] Key leadership names, titles, and tenure dates accurate
- [ ] Mission and vision statements quoted exactly (verbatim from school sources)
- [ ] Accreditation details complete with next review dates
- [ ] All numbers cross-referenced across sources
- [ ] No promotional language present
- [ ] Consistent formatting throughout
- [ ] Word count: 3,500-5,000 words minimum
- [ ] No assumptions made; gaps noted explicitly
- [ ] Web search results used (minimum 5-8 searches documented)

---

## Delivery Format

Present the completed profile as:

1. Clean Markdown document
2. Properly formatted with **bold** school name in opening
3. Proper header hierarchy (#### for section headers)
4. Bullet points only where appropriate (lists, not body text)
5. No decorative elements or filler
6. Ready for copy-paste into CRM, documentation systems, or presentation tools
7. Total length: 3,500-5,000 words

---

## Workflow Summary

When a user requests school intelligence:

1. **Acknowledge** the request and note school name/location
2. **Plan** the research approach (identify key search queries)
3. **Execute** web searches (5-8 targeted queries minimum)
4. **Fetch** full content from official school pages and credible sources
5. **Synthesize** findings into structured profile format
6. **Verify** against quality checklist
7. **Deliver** complete profile in Markdown format
8. **Offer** to clarify, expand, or adjust specific sections

---

## Research Depth Guidelines

- **Single-campus school, straightforward case:** 5-8 `WebSearch` queries + 2-3 `WebFetch` calls
- **Multi-campus network or complex history:** 10-15 `WebSearch` queries + 4-6 `WebFetch` calls
- **School with limited public information:** 8-12 searches focused on news, directory listings, education ministry records
- **Profile with significant gaps:** Note explicitly what information requires direct school contact

Invest time in source verification and cross-referencing — the profile's value depends on accuracy for stakeholder relationships and sales positioning.
