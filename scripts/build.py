#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build the McGraw Hill Campaign Portal.

Single source of truth for the internal sales nurture-reference page.
  1. Generates branded .eml files (emails/) for every authored email.
  2. Injects the portal data into scripts/template.html -> index.html (self-contained).

Run:  python3 scripts/build.py
"""
import json, os, re, html
from email.message import EmailMessage
from email.utils import formatdate, make_msgid

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL_DIR = os.path.join(ROOT, "emails")
TEMPLATE = os.path.join(ROOT, "scripts", "template.html")
OUT = os.path.join(ROOT, "index.html")

# ----- brand stage colours -----
STAGE_COLOR = {"Awareness": "#0B48BC", "Consideration": "#5F14C1", "Decision": "#E21A23", "Other": "#6A7180"}

def body(raw):
    """Triple-quoted raw block -> list of non-empty paragraph lines."""
    return [ln.strip() for ln in raw.strip("\n").split("\n") if ln.strip()]

# =====================================================================
#  DATA  (faithful to the Notion source of truth)
# =====================================================================

CONFIG = {
    # Relative: works on the live preview (raw.githack.com keeps the directory structure),
    # on GitHub Pages, and when index.html + emails/ are co-hosted on Marketo.
    "emlBase": "emails/",
    "heroLede": ("Your single reference for every pre-sale email nurture we're running across International K-12 "
                 "for the coming academic year. Browse each program, see exactly what every email does, preview the "
                 "full creative, track progress in Salesforce, and grab the .eml whenever you want to send one to your own contacts."),
}

PRODUCTS = []

# ---------------------------------------------------------------- LEVEL UP
PRODUCTS.append({
    "id": "level-up", "name": "Level Up", "color": "#5F14C1",
    "status": "In-Progress",
    "audience": "School leaders & ICT coordinators",
    "regions": "MEA · Asia · EU · ANZ · CA · SAF · KSA",
    "salesforceReport": "",
    "description": ("The full K-12 ICT and AI-literacy nurture for ‘Level Up Through Digital Discoveries’. It moves "
        "international school leaders and ICT coordinators from the problem (the AI-literacy gap and the failure of "
        "patchwork coding tools), through consideration (teacher support, standards alignment, proof), to a decision-stage "
        "push to adopt a single progressive K-12 computing curriculum in time for 2026/27. Nine emails across Awareness → "
        "Consideration → Decision."),
    "ctaUrl": "https://info.mheducation.com/int_ict",
    "emails": [
        {"code":"AW01","stage":"Awareness","title":"Is Your ICT Curriculum Ready for AI?",
         "blurb":"Opens the nurture by framing the AI-literacy gap and the failure of patchwork coding tools, positioning Level Up as the only K-12 ICT curriculum with AI woven in from Grade 1 to 12. Invites readers to explore the program, download the brochure, and request sample lessons.",
         "subject":"Is your school preparing students for an AI-powered world?",
         "greeting":"Hi [First Name],","cta_text":"Explore the Full Program",
         "body": body(r'''
How is your school teaching students to navigate AI?
If you’re not sure where to start (or if computing education hasn’t been a priority yet) you’re not alone. Research shows that two-thirds of countries still lack comprehensive computing curricula, and AI literacy is rarely integrated at all grade levels.[1]
But here’s what’s changed: By 2030, 85% of jobs will require some level of AI fluency.[2] The question isn’t whether schools need to teach computing and AI. It’s how to do it well across all grades, not just high school.
Here’s the problem most schools face: They cobble together free tools. Scratch for elementary, Code.org for middle school, maybe some Python tutorials in high school. But these fragmented approaches lack progression, overwhelm teachers, and fail to prepare students for the AI-driven careers they’ll enter.
What if there was a better way?
Level Up Through Digital Discoveries is the only K-12 ICT curriculum that integrates AI literacy from Grade 1 through Grade 12. It’s built on a progressive “spiral learning” model that ensures students don’t just learn to code, but learn to think computationally in an AI-powered world.
Here’s what makes it different:
✓ Complete K-12 continuity – Not a patchwork. One seamless curriculum from digital citizenship in kindergarten to machine learning in Grade 12.
✓ AI integration at every grade – Grade 1 students explore AI basics through Scratch. Grade 7 students dive into generative AI and prompt engineering. Grade 12 students build predictive models and study natural language processing.
✓ Standards-aligned globally – Independently reviewed to meet ISTE, CSTA, and UN SDG 4 frameworks. Prepares students for Cambridge IGCSE, IB, and AP pathways.
✓ Teacher support you can rely on – Ready-to-teach lesson plans, pacing guides, and comprehensive teacher editions. No CS degree required.
✓ Bilingual classroom support – Designed to support diverse language backgrounds and promote equity in learning. Critical for international schools with multilingual students.
✓ Flexible delivery – Works in traditional, hybrid, or remote settings. Print materials available now, with adaptive digital platform launching later this year.
I’d like to show you how Level Up can bring comprehensive computing education to your school.
Here are three ways to learn more:
[Explore the Full Program →]
[Download the Program Brochure (PDF) →]
[See How AI is Integrated Across All Grades (PDF) →]
Or, if you’d prefer to see sample lessons from specific grade levels, simply reply to this email and let me know which grades you’re most interested in.
P.S. — If you’re planning curriculum for 2026/27, now is the time to explore your options. Many schools finalize adoptions by May/June. Let’s make sure you have everything you need to make an informed decision.
''')},
        {"code":"AW02","stage":"Awareness","title":"Why Fragmented Coding Tools Are Failing",
         "blurb":"Dramatizes the pain of the patchwork approach (Scratch, Code.org, YouTube Python) and argues computing deserves the same curricular rigor as maths or science. Offers Grade 2 and Grade 5 sample packages so readers can see real K-12 progression.",
         "subject":"Why piecing together Scratch + Code.org + Python isn’t working",
         "greeting":"Hi [First Name],","cta_text":"Explore the Full K-12 Curriculum",
         "body": body(r'''
You know the drill.
Grade 3 teachers use Scratch because it’s free and visual.
Grade 6 switches to Code.org because someone found it online.
Grade 9 cobbles together Python tutorials from YouTube.
Grade 12? Good luck finding anything that connects to what came before.
This is how most international schools teach computing. And it’s breaking down.
Here’s what happens with the patchwork approach:
Teachers are overwhelmed. Every year, they’re hunting for new resources, figuring out what to teach next, and wondering if students actually retained anything from last year. There’s no continuity, no scope and sequence, no teacher support.
Students are confused. They learn Scratch blocks in Grade 6, but when they hit Python in Grade 9, it feels like starting over. The concepts don’t build. The skills don’t transfer. They’re learning tools, not computational thinking.
Schools can’t measure progress. Without a unified curriculum, how do you know if a Grade 8 student is on track? What does “proficient in computing” even mean when every grade uses different tools with different learning objectives?
And nobody’s teaching AI literacy. Free platforms like Scratch and Code.org are great for basic coding. But they don’t address the elephant in the room: students graduating into an AI-powered workforce with zero understanding of how AI works, how to use it, or how to evaluate it critically.
There’s a better way.
Comprehensive K-12 curricula exist for math, science, and language arts. Why? Because progression matters. Because teacher support matters. Because you can’t build mastery by stitching together random resources.
Computing deserves the same rigor.
Level Up Through Digital Discoveries is built like a traditional curriculum, but for the modern computing landscape:
✓ Spiral learning from K-12 – Concepts introduced early, revisited and deepened every year
✓ Teacher editions and lesson plans – No hunting for resources or guessing what to teach next
✓ Integrated assessments – Track student progress across all grades with consistent benchmarks
✓ AI literacy built in – From Grade 1 awareness to Grade 12 machine learning, progressively integrated
✓ Standards-aligned – ISTE, CSTA, UN SDG 4 frameworks, independently reviewed every 2 years
It’s not about replacing the free tools. It’s about having a foundation that actually prepares students for the next grade, the next year, and the careers they’ll enter.
See what a comprehensive K-12 computing curriculum actually looks like:
We’ve put together complete teaching packages for Grade 2 and Grade 5 so you can see exactly how Level Up delivers progression, teacher support, and student engagement.
Grade 2 Sample Package:
→ Table of Contents
→ Sample Chapter (Student Edition)
→ Sample Lesson (Teacher Edition)
→ Pacing Guide
Grade 5 Sample Package:
→ Table of Contents
→ Sample Chapter (Student Edition)
→ Sample Lesson (Teacher Edition)
→ Pacing Guide
Compare the two and you’ll see how foundational concepts in Grade 2 evolve into more sophisticated computational thinking by Grade 5 — and that’s just the elementary years.
[Explore the Full K-12 Curriculum →]
Or reply to this email and let me know which other grade levels you’d like to see. We have sample packages for Grades K-12.
P.S. — If your school is still piecing together free tools year after year, ask yourself: Would we accept this approach for math? For science? Why do we accept it for computing?
''')},
        {"code":"AW03","stage":"Awareness","title":"The Full K-12 Journey to AI Mastery",
         "blurb":"Walks through the complete K-12 progression band by band (digital citizenship through machine learning) to show Level Up's spiral-learning pathway versus restart-every-few-years programs. Drives downloads of the K-12 progression overview and sample lessons.",
         "subject":"From digital citizenship to AI mastery: The K-12 journey",
         "greeting":"Hi [First Name],","cta_text":"Download: K-12 Progression Overview (PDF)",
         "body": body(r'''
Most computing curricula are built for a specific age range.
You’ve got elementary programs (K-5).
Middle school programs (6-8).
High school electives (9-12).
But they rarely connect. Students finish Grade 5 strong, then start over in Grade 6 with a completely different curriculum. By Grade 9, nobody remembers what they learned in elementary school.
What if computing education worked like math? Or science? Or language arts?
Those subjects don’t restart every few years. They build. Concepts introduced in Grade 1 become the foundation for Grade 6, which becomes the foundation for Grade 12.
That’s how Level Up Through Digital Discoveries is designed.
Here’s what the full K-12 journey looks like:
Grades K-2: Digital Citizenship + Foundations
Students learn what technology is, how to use it responsibly, and begin exploring basic concepts like patterns, sequences, and algorithms through age-appropriate activities.
Grades 3-5: Computational Thinking + Introduction to Coding
Students start coding with Scratch, learning loops, conditionals, and variables. They explore how computers process information and begin understanding AI basics through interactive projects.
Grades 6-8: Application + Creation
Students transition to text-based coding with Python. They dive into generative AI and prompt engineering (Grade 7 focus). They build real projects, from chatbots to games, understanding how AI tools work and their limitations.
Grades 9-12: Problem-Solving + Career Readiness
Students tackle advanced topics: machine learning, natural language processing, image recognition, data science. They study AI ethics, bias, and societal impact. They prepare for Cambridge IGCSE, IB, AP exams, and industry certifications.
This is spiral learning. Concepts aren’t taught once and forgotten. They’re introduced early, revisited regularly, and deepened over time.
By Grade 12, students don’t just know how to code. They understand computational thinking. They can work with AI tools critically. They’re prepared for university CS programs and tech-centered careers.
That’s the difference between a patchwork and a pathway.
Want to see how this progression works in practice?
[Download: K-12 Progression Overview (PDF) →]
[Explore Sample Lessons Across Grade Levels →]
[See Standards Alignment (ISTE/CSTA) →]
Or reply to this email with the grade levels most relevant to your school, and I’ll send you specific materials.
P.S. — If you’re planning curriculum for 2026/27, now is the time to think about progression, not just individual grade levels. Most schools finalize adoptions by May/June. Let’s make sure you have what you need to make the right decision.
''')},
        {"code":"CO04","stage":"Consideration","title":"Teach ICT Without a CS Degree",
         "blurb":"Addresses the top adoption barrier — ‘our teachers aren’t computer scientists’ — by detailing Level Up's teacher editions, ready-to-teach lesson plans, pacing guides and PD. Drives sample teacher-edition downloads and webinar registration.",
         "subject":"“I teach science, not computer science. Here’s how I’m teaching coding with confidence.”",
         "greeting":"Hi [First Name],","cta_text":"Download: Sample Teacher Edition (Grade 5)",
         "body": body(r'''
Here’s what we hear from international schools all the time:
“We want to teach computing, but our teachers aren’t computer scientists.”
It’s the biggest barrier to implementing K-12 computing programs. And it’s completely understandable.
Most teachers didn’t study computer science in university. They’re science teachers, math teachers, primary generalists. The idea of teaching Python or AI feels overwhelming. So schools either:
- Hire expensive CS specialists (hard to find, especially internationally)
- Ask existing teachers to “figure it out” (recipe for stress and burnout)
- Skip computing altogether (students lose out)
What if there was a fourth option?
What if computing could be taught like any other subject: with comprehensive teacher support, ready-to-use lesson plans, and resources that don’t assume you have a CS degree?
That’s exactly how Level Up Through Digital Discoveries is designed.
Here’s what teacher support actually looks like in Level Up:
Comprehensive Teacher Editions — point-of-use guidance for every lesson, background knowledge sections, common student misconceptions and how to address them, extension activities, and answers to all exercises and assessments.
Ready-to-Teach Lesson Plans — clear learning objectives aligned to standards, a step-by-step teaching sequence, suggested timing and pacing, discussion prompts, and formative assessment checks. No hunting for resources or wondering “what do I teach next?”
Flexible Pacing Guides — whether you have 1 hour per week or 2, the pacing guides show you exactly how to sequence lessons across the school year. Customize to fit your schedule.
Professional Development Resources — video tutorials, getting-started guides, and ongoing support to build your confidence. You’re not expected to know everything on Day 1.
Digital Teacher Dashboard (Launching 2026) — access all resources, track student progress, assign work, and get real-time insights, all in one place.
Here’s what teachers are saying:
“I teach science, not computer science. Level Up’s teacher guides made implementation seamless. Everything I needed was right there — no guessing, no scrambling for resources.” — Primary Teacher, International School
“The point-of-use support in the Teacher Edition was a game-changer. I felt confident teaching topics I’d never taught before.” — ICT Coordinator, Middle East
You don’t need a CS degree. You need good curriculum and strong support. Level Up provides both.
Want to see the teacher support resources for yourself?
[Download: Sample Teacher Edition (Grade 5) →]
[View: Teacher Support Overview (PDF) →]
[Register for Webinar: Teaching ICT Without a CS Degree →]
Or reply to this email and let me know what grade levels you’re most concerned about. I’ll send you the specific teacher resources for those grades.
P.S. — We’re hosting a live webinar in 2 weeks: “Teaching ICT Without a CS Degree: A Teacher’s Guide.” Register above to join educators from across your region who are making computing accessible in their schools.
''')},
        {"code":"CO05","stage":"Consideration","title":"Standards Alignment: ISTE, CSTA, SDG 4",
         "blurb":"Answers the ‘how does this align with our standards?’ question by mapping Level Up to ISTE, CSTA K-12, UN SDG 4 and Cambridge/IB/AP pathways, noting independent biennial review. Offers downloadable standards-mapping docs and a leadership pitch brief.",
         "subject":"How to answer “Is this aligned with ISTE and CSTA?”",
         "greeting":"Hi [First Name],","cta_text":"Download: Complete ISTE Standards Mapping (PDF)",
         "body": body(r'''
Every curriculum decision eventually faces this question:
“How does this align with our standards?”
School boards want to know. Accreditation bodies require it. Parents ask about it. And rightfully so: standards alignment ensures students are learning what they need to succeed, whether they’re preparing for university, international exams, or future careers.
For computing education, the key standards are ISTE (International Society for Technology in Education), CSTA K-12 CS (Computer Science Teachers Association), and UN SDG 4 (Quality Education) — plus regional requirements like Cambridge IGCSE, IB, and AP pathways.
Here’s how Level Up Through Digital Discoveries delivers:
Independently Reviewed Every 2 Years — Level Up isn’t just self-proclaimed “standards-aligned.” It’s independently reviewed by education experts every two years to ensure alignment with evolving standards and best practices.
Built on ISTE Standards — every lesson maps to the ISTE standards for students: Empowered Learner, Digital Citizen, Knowledge Constructor, Innovative Designer, Computational Thinker, Creative Communicator, and Global Collaborator.
Aligned with the CSTA K-12 CS Framework — Level Up covers all five core concepts: Computing Systems; Networks and the Internet; Data and Analysis; Algorithms and Programming; and Impacts of Computing. Progression follows CSTA’s developmental approach.
Supports UN SDG 4 (Quality Education) — equitable access to computing education, digital literacy as a fundamental skill, and support for bilingual and multilingual learners.
Prepares Students for Global Pathways — Cambridge IGCSE Computer Science, IB Computer Science (SL/HL), AP Computer Science Principles, and AP Computer Science A.
Want proof? We’ve created detailed mapping documents that show exactly where each standard is addressed across the K-12 curriculum.
[Download: Complete ISTE Standards Mapping (PDF) →]
[Download: Complete CSTA Standards Mapping (PDF) →]
[Download: How to Pitch Level Up to Your Leadership (1-Page Brief) →]
These documents are designed for exactly the conversation you’ll have with your school board, head of school, or curriculum committee. They answer the alignment question definitively.
P.S. — The “How to Pitch Level Up to Your Leadership” brief includes talking points, FAQs, and the business case for comprehensive K-12 computing education. Use it to make the case internally.
''')},
        {"code":"CO06","stage":"Consideration","title":"Athens School Success Story",
         "blurb":"A case-study email showing how an international school in Athens replaced fragmented tools with Level Up and saw gains for students, teachers and the school. Drives a case study download and an implementation call.",
         "subject":"Real results: How an Athens school implemented K-12 computing in one year",
         "greeting":"Hi [First Name],","cta_text":"Download: Complete Case Study (PDF)",
         "body": body(r'''
Let me introduce you to [School Name] in Athens, Greece. Like many international schools, they were facing a familiar challenge.
The Problem: Computing education was fragmented. Elementary used Scratch. Middle school had some Code.org activities. High school offered a Python elective. But nothing connected. Teachers were overwhelmed hunting for resources. Students weren’t building on previous learning. And the school had no way to measure computing proficiency across grades.
Sound familiar?
The Decision: After evaluating several options, [School Name] decided to implement a comprehensive K-12 computing curriculum and chose Level Up Through Digital Discoveries — for its complete K-12 continuity, built-in teacher support, standards alignment (ISTE, CSTA, Cambridge IGCSE prep), AI literacy across all grades, and flexible implementation.
The Implementation: [School Name] rolled out Level Up across all grades, starting with professional development and ongoing support. Students transitioned to the new curriculum seamlessly.
The Results:
For students — increased engagement in computing classes, successful completion of first machine-learning projects, and stronger performance on Cambridge IGCSE Computer Science.
For teachers — reduced prep time with ready-to-use lesson plans, and confidence teaching advanced topics they’d never taught before.
For the school — computing is now a signature program that attracts new families, and leadership can finally track computing proficiency across all grades with integrated assessments.
Want to see the full story? The case study includes the school’s challenge and decision process, implementation timeline and approach, detailed results and outcomes, lessons learned, and sample student work.
[Download: Complete Case Study (PDF) →]
[Schedule a Call: Discuss Implementation at Your School →]
If you’re facing similar challenges and want to explore what comprehensive K-12 computing education could look like at your school, let’s talk.
P.S. — [School Name] started with a pilot and expanded from there. You don’t have to implement K-12 all at once. We can work with whatever approach makes sense for your school.
''')},
        {"code":"DE07","stage":"Decision","title":"What's Inside Your Adoption Package",
         "blurb":"Itemizes everything included in a Level Up adoption — print curriculum, the 2026 digital platform, implementation support, ongoing updates and exam pathways — to show it’s a full ecosystem, not just textbooks. Drives requests for pricing and a 1-on-1 consultation.",
         "subject":"Everything included in your Level Up adoption package",
         "greeting":"Hi [First Name],","cta_text":"Request: Detailed Pricing & Implementation Timeline",
         "body": body(r'''
We’ve spent the past several weeks showing you why comprehensive K-12 computing education matters and how Level Up delivers it. Now let’s talk about what you actually get when you adopt Level Up Through Digital Discoveries. Because it’s more than just textbooks.
PRINT CURRICULUM (AVAILABLE NOW)
Student materials: consumable student worktexts for Grades K-12, age-appropriate content with hands-on activities, project-based learning throughout, available in 1-year or multi-year subscriptions.
Teacher materials: comprehensive Teacher Editions for every grade, point-of-use teaching guidance, lesson plans with flexible pacing, assessment tools and answer keys, and background knowledge for non-CS teachers.
DIGITAL PLATFORM (LAUNCHING 2026)
For students: SmartBook® adaptive learning (Grades 6-12), robotics eBook lessons with interactive activities, self-grading assessments, video tutorials, a mobile app with eBook, and a Career Center exploring tech careers (Grades 6-12).
For teachers: a digital dashboard to track student progress across all grades, assign work and assessments, access all digital resources in one place, and get real-time insights on performance.
IMPLEMENTATION SUPPORT
Professional development: getting-started training, grade-level specific workshops, ongoing support, and access to an educator community.
Curriculum support: scope and sequence documents, standards alignment mapping (ISTE, CSTA), pacing guides for 1-2 hours per week, and implementation timeline planning.
ONGOING VALUE
Continuous updates: curriculum reviewed and updated every 2 years, new topics added as technology evolves (AI, emerging tech), and refreshed content to keep pace with industry.
Flexibility: works in traditional, hybrid, or remote settings, adaptable pacing, multiple subscription options, and bilingual classroom support.
STANDARDS & PATHWAYS
Prepares students for Cambridge IGCSE Computer Science, IB Computer Science (SL/HL), AP Computer Science Principles, AP Computer Science A, industry certifications, and university CS programs.
This isn’t just a curriculum purchase. It’s a complete K-12 computing education ecosystem.
Ready to discuss what this looks like for your school?
[Request: Detailed Pricing & Implementation Timeline →]
[Download: Complete Package Overview (PDF) →]
[Schedule: 1-on-1 Consultation with an Implementation Specialist →]
Or reply with your number of students per grade level, preferred start date, and any specific questions, and we’ll send you a customized proposal tailored to your school’s needs.
P.S. — Schools planning for 2026/27 implementation are finalizing decisions now. Let’s make sure you have all the information you need to move forward confidently.
''')},
        {"code":"DE08","stage":"Decision","title":"Your Peers Are Switching to Level Up",
         "blurb":"Uses social proof and momentum — international schools across regions adopting Level Up for 2026/27 — plus a tightening regional timeline to spur action. Drives an implementation planning call, customized proposal request, and a decision-criteria download.",
         "subject":"Schools in [Region] are preparing for 2026/27. Here’s who’s already committed.",
         "greeting":"Hi [First Name],","cta_text":"Schedule Your Implementation Planning Call",
         "body": body(r'''
In the past few months, we’ve seen significant momentum: international schools across Europe, Asia, the Middle East, Africa, Australia, and New Zealand are making decisions about their 2026/27 computing curricula. And many are choosing Level Up Through Digital Discoveries.
Here’s what we’re seeing:
Schools are moving away from patchwork approaches. The days of cobbling together Scratch + Code.org + random YouTube tutorials are ending. Schools recognize that comprehensive K-12 curricula deliver clearer progression, stronger teacher support, and measurable results.
AI literacy is now a requirement, not an option. With 85% of future jobs requiring AI fluency, schools can’t afford to treat computing as an afterthought. Level Up’s K-12 AI integration addresses this directly.
Teachers need support, not just content. Schools are prioritizing curricula with strong teacher editions, lesson plans, and professional development.
Standards alignment matters to boards and accreditors. ISTE, CSTA, Cambridge IGCSE, IB pathways — Level Up delivers this out of the box.
What educators are saying:
“Level Up has transformed our approach to teaching computing. Students are more engaged and ready for future challenges.” — School Leader, Athens
“The teacher support made all the difference. I felt confident teaching topics I’d never taught before.” — ICT Coordinator, Middle East
“We needed a curriculum that would take students from kindergarten through Grade 12 with real progression. Level Up was the only option that delivered.” — Primary Coordinator, Asia
The timeline is tightening:
- Australia/NZ: schools finalizing Term 1 2027 adoptions by April
- Middle East/Asia: 2026/27 decisions happening now through May
- Europe: planning windows for September 2026 start closing in June
If you’re still evaluating options, now is the time to move forward.
[Schedule Your Implementation Planning Call →]
[Request Your Customized Proposal →]
[Download: Why Schools Choose Level Up (PDF) →]
Don’t let your students fall behind while other schools move forward.
P.S. — Schools that wait until June/July often miss their implementation window for 2026/27. Let’s talk this month.
''')},
        {"code":"DE09","stage":"Decision","title":"Final Call for 2026/27 Adoption",
         "blurb":"The closing, urgency-driven email laying out region-by-region decision deadlines and the cost of waiting another fragmented year. Pushes hard for a 30-minute call to map the school's timeline and confirm next steps.",
         "subject":"Your 2026/27 window closes in 4-6 weeks",
         "greeting":"Hi [First Name],","cta_text":"Book a 30-minute call",
         "body": body(r'''
Your window for 2026/27 implementation is closing. Here's what you need to know.
The timeline: If you're planning to implement a new computing curriculum for 2026/27, decisions need to happen now.
Australia/New Zealand: Term 1 2027 starts in late January. You need curriculum decisions finalized within 4-6 weeks to ensure materials arrive, teachers are trained, and you're ready for Day 1.
Middle East/Asia: the academic year starts in August/September. Procurement, shipping, and teacher training mean decisions need to be finalized by May — that's 8-10 weeks.
Europe: September 2026 start dates require decisions by June at the latest — that's 10-12 weeks.
What happens if you wait: You'll miss your 2026/27 window. Your students will spend another year with fragmented tools that don't connect, teachers scrambling between 7+ different platforms, no AI literacy integration, and no measurable computing progression. Another year of "we'll fix this next year" — except next year is already here.
You already know this isn't working. Your students deserve better.
What comes next: Book a 30-minute call this week. We'll map your specific timeline, show you what 2026/27 looks like for your school, and confirm next steps.
[Book a 30-minute call →]
If a call doesn't work right now, reply to this email. Tell me where you are in the decision and I'll personally respond and connect you with the right person to move forward. But please book the call. You're past the research phase — this needs a conversation.
Let's make 2026/27 the year your school transforms computing education.
P.S. — If you're not ready to implement now, that's fine. But don't let another year pass without a plan. The decision window is real. Make the call.
''')},
    ],
})

# ---------------------------------------------------------------- ALEKS
PRODUCTS.append({
    "id": "aleks", "name": "ALEKS", "color": "#0B48BC",
    "status": "Planning",
    "audience": "School leaders & maths HoDs",
    "regions": "MEA · Asia · EU · ANZ · UK · CA · KSA · SAF",
    "salesforceReport": "",
    "description": ("The pre-sale nurture for ALEKS, McGraw Hill's adaptive maths programme, aimed at international school "
        "leaders, curriculum coordinators and maths heads of department who are new to ALEKS. It frames the problem of "
        "invisible, compounding maths gaps, challenges the ‘more practice’ instinct, paints the vision of personalised "
        "learning, and anchors everything in the Knowledge Space Theory research behind ALEKS — before moving into "
        "consideration and a free-trial push. Awareness and Consideration emails are authored; later stages are in production."),
    "ctaUrl": "https://hub.mheducation.com/share/ALEKS",
    "emails": [
        {"code":"AW01","stage":"Awareness","title":"The Invisible Maths Gaps Problem",
         "blurb":"An empathetic, problem-focused opener that frames invisible, compounding maths gaps and names ALEKS and Knowledge Space Theory as the answer. CTA drives a download of the Knowledge Space Theory whitepaper.",
         "subject":"Your students have maths gaps you can't see yet",
         "preview":"The gaps are invisible. But they're compounding every term.",
         "greeting":"Hi {{First Name}},","cta_text":"Download the Knowledge Space Theory Whitepaper",
         "cta_url":"https://hub.mheducation.com/share/ALEKS",
         "body": body(r'''
Right now, students in your school are sitting in maths lessons that assume they understood last year's content. Many of them didn't.
Research consistently shows that roughly half of students enter a new maths course missing prerequisite knowledge. Not because they weren't taught. Because knowledge gaps from earlier years went undetected, and each new topic made them harder to close.
These gaps are invisible in a traditional classroom. A student who struggles with fractions won't just struggle with fractions. They'll hit a wall in algebra, then geometry, then everything that follows. The gap doesn't stay the same size. It compounds.
And without a way to diagnose exactly what each student knows and doesn't know, your teachers are left teaching to the middle of the room. Struggling students fall further behind. Strong students lose the chance to accelerate.
Knowledge isn't linear. It's a complex web of interrelated topics, and every student navigates it differently. This is the foundation of Knowledge Space Theory, a field of research developed at the University of California. It's also the science behind ALEKS (Assessment and Learning in Knowledge Spaces): an adaptive maths programme that maps each student's unique knowledge state and builds a personalised path from there, with a mastery rate above 90%.
The whitepaper explains how it works, why traditional approaches miss the mark, and what becomes possible when you can see every student's knowledge map in real time.
[Download the Knowledge Space Theory Whitepaper →]
''')},
        {"code":"AW02","stage":"Awareness","title":"Why More Practice Isn't Working",
         "blurb":"Validates the reader's intervention efforts, then explains why one-size-fits-all practice fails — shifting the thinking from ‘more practice’ to ‘smarter, adaptive practice.’ CTA drives a watch of the 4-minute animated explainer.",
         "subject":"Why extra practice isn't closing the gap",
         "preview":"Practice without precision is just repetition. Here's the difference.",
         "greeting":"Hi {{First Name}},","cta_text":"Watch the 4-minute explainer",
         "cta_url":"https://hub.mheducation.com/share/ALEKS",
         "body": body(r'''
When students fall behind in maths, the instinct is to give them more. More worksheets. More revision sessions. More intervention hours after school.
It's the right instinct. But it often doesn't work.
Here's why: practice only helps when it's matched to what the student is genuinely ready to learn. Hand a student more questions on a topic they're already missing the prerequisites for, and they don't get better at it. They get more frustrated. They start to believe they're "bad at maths." The gap stays where it is, sometimes wider than before.
Meanwhile, the strong students sit through revision they don't need. Disengagement follows.
This is the limitation of one-size-fits-all practice. It assumes every student in the room is at the same starting point. They never are.
Adaptive learning works differently. Instead of giving every student the same content, it identifies what each individual student knows, what they don't, and what they're ready to learn next. The practice they receive is precisely matched to their position on their own knowledge map.
This short animated explainer walks through how adaptive learning differs from traditional practice, and why the shift matters more than most schools realise.
[Watch the 4-minute explainer →]
''')},
        {"code":"AW03","stage":"Awareness","title":"What An ALEKS Classroom Looks Like",
         "blurb":"Bridges from problem to product by painting the vision of personalised learning through the assess–learn–reassess cycle and the student and teacher experience. CTA drives a 3-minute product walkthrough video.",
         "subject":"What an ALEKS maths classroom actually looks like",
         "preview":"Assess. Learn. Reassess. The cycle that changes everything.",
         "greeting":"Hi {{First Name}},","cta_text":"See ALEKS in action (3-min walkthrough)",
         "cta_url":"https://hub.mheducation.com/share/ALEKS",
         "body": body(r'''
Imagine 30 students working on maths at the same time, each on a different topic, each at the right level of challenge, each receiving feedback the moment they need it.
That's what ALEKS makes possible. Here's how.
1. Assess. Every student starts with an adaptive Knowledge Check. In a few dozen questions, ALEKS pinpoints exactly what each student knows and doesn't know, mapping their position on the curriculum from a trillion possible knowledge states.
2. Learn. ALEKS then shows each student a personalised set of topics they are genuinely ready to learn. The student chooses what to work on next. As they practise, they get immediate feedback, step-by-step explanations, and, where relevant, short instructional videos.
3. Reassess. Periodically, ALEKS checks back to confirm what's been mastered and identify topics that need reinforcement. This is the spaced retrieval practice that turns short-term gains into long-term retention.
For teachers, the system handles the diagnostic and personalisation work that would be impossible to do manually for 30 individual learners. The teacher dashboard shows exactly where every student is and where they need support, freeing teachers to do what only they can do: targeted small-group instruction, conferencing, and intervention.
This is what a classroom looks like when every student gets the right work at the right time.
[See ALEKS in action (3-min walkthrough) →]
''')},
        {"code":"AW04","stage":"Awareness","title":"The Science Behind 90% Mastery",
         "blurb":"Establishes scientific credibility, positioning ALEKS as the only adaptive maths platform built on 30+ years of peer-reviewed Knowledge Space Theory research from the University of California with NSF support. CTA re-offers the whitepaper.",
         "subject":"The science behind 90% maths mastery",
         "preview":"30+ years of peer-reviewed research. One adaptive learning platform.",
         "greeting":"Hi {{First Name}},","cta_text":"Download the Knowledge Space Theory Whitepaper",
         "cta_url":"https://hub.mheducation.com/share/ALEKS",
         "body": body(r'''
Most adaptive learning tools are built on rules. If a student gets question A wrong, show them question B. If they get B right, jump to C. It works in a basic way, but it can't tell you anything meaningful about where the student actually is on a curriculum, or what they're genuinely ready to learn next.
ALEKS is built on something fundamentally different: Knowledge Space Theory.
Developed over 30 years at the University of California with funding from the National Science Foundation, Knowledge Space Theory is a branch of mathematical cognitive science. It models knowledge not as a linear sequence of topics, but as a vast network of interrelated concepts. For a single maths course, this network contains over a trillion possible "knowledge states" — each one a different combination of what a student does and doesn't know.
ALEKS uses adaptive Knowledge Checks to locate every student's precise position in that network, then identifies the topics in their "learning fringe" — the small set of topics they are genuinely ready to learn next.
This is why ALEKS students master topics at a rate above 90%. They are never asked to learn something they're not ready for, and they are never asked to revisit something they already know.
The full whitepaper explains the research, the methodology, and the evidence behind the approach. It's the most detailed look at the science underpinning ALEKS, and it's available below.
[Download the Knowledge Space Theory Whitepaper →]
''')},
        {"code":"CO05","stage":"Consideration","title":"Less Prep, More Teaching, Better Data",
         "blurb":"Tackles the top adoption barrier — teacher workload — by showing ALEKS' AI handles diagnostics, personalisation and reassessment, with Insights reports flagging at-risk students, plus the ST4S data-safety badge. CTA drives a free trial sign-up.",
         "subject":"Less prep. More teaching. Better data.",
         "preview":"Plus: see why ALEKS holds the ST4S safety badge for schools.",
         "greeting":"Hi {{First Name}},","cta_text":"Start Your Free Trial",
         "cta_url":"https://www.aleks.com/free_trial/instructor",
         "body": body(r'''
When schools evaluate a new maths programme, the question that decides the outcome is rarely "is the content good?" It's almost always: will my teachers have the time to make this work?
It's a fair concern. Most adaptive tools shift the work from textbook design to teacher configuration: setting up student paths, monitoring progress, deciding what to assign next. The teacher becomes the system administrator.
ALEKS is built the other way around.
The AI handles diagnostics. The AI handles personalisation. The AI handles reassessment. Teachers don't decide what each student should work on next. ALEKS does. What teachers see is a clear, real-time picture of where every student is and where they need help.
And ALEKS goes further: the Insights reports proactively alert teachers when a student is exhibiting one of four risk behaviours: failed topics, decreased learning rate, unusually fast learning (possible copying), or procrastination. Teachers don't have to go looking for problems. ALEKS surfaces them.
The result is that teachers spend less time managing the platform and more time doing what only they can do: small-group instruction, one-to-one conferencing, and targeted intervention.
One more thing schools tell us matters: ALEKS holds the Safer Technologies 4 Schools (ST4S) badge, having been independently assessed against the nationally consistent privacy and security framework for school technology. Data safety is verified, not just claimed.
The fastest way to see how this works in your context is to spend 20 minutes inside ALEKS as both a student and a teacher. The free trial is below.
[Start Your Free Trial →]
''')},
    ],
})

# ---------------------------------------------------------------- READING LABS ONLINE (draft)
PRODUCTS.append({
    "id": "reading-labs", "name": "Reading Labs Online", "color": "#E21A23",
    "status": "In-Progress",
    "audience": "Literacy & primary coordinators",
    "regions": "MEA · Asia · EU · ANZ · UK · CA",
    "salesforceReport": "",
    "description": ("The launch nurture for Reading Labs Online — the international online edition of the proven SRA Reading "
        "Labs literacy programme. It targets existing SRA print customers, recent literacy opportunities, and literacy-webinar "
        "registrants, moving them from awareness through consideration to decision and driving them to the Reading Labs Online "
        "landing page. The nine-email structure is mapped across all three stages; full creative is in production."),
    "ctaUrl": "https://info.mheducation.com/int_rlo",
    "draftNoteDefault": "Full copy for this email is in production. The summary above captures its role, stage and message in the sequence; the live creative will be added here once approved.",
    "emails": [
        {"code":"AW01","stage":"Awareness","title":"Are Your Reading Interventions Working?","hasCopy":False,
         "subject":"Are your reading interventions actually working for every student?",
         "blurb":"Opens the series by challenging schools on whether their reading interventions truly work for every K-8 student, positioning Reading Labs Online as a globally proven program used by 100M+ students. Drives readers to the overview brochure and landing page."},
        {"code":"AW02","stage":"Awareness","title":"See the Student Reading Journey","hasCopy":False,
         "blurb":"Spotlights the student journey and experience inside Reading Labs Online via a student demo. Encourages readers to visit the page to see how the program works for learners."},
        {"code":"AW03","stage":"Awareness","title":"The Systemic Reading Challenge","hasCopy":False,
         "blurb":"Frames the systemic challenges schools face in delivering differentiated reading practice at scale, and points to Reading Labs Online as the system-wide solution."},
        {"code":"CO04","stage":"Consideration","title":"Explore the Interactive Showcase","hasCopy":False,
         "blurb":"Moves engaged readers into consideration with an interactive showcase/demo of the platform. Invites them to explore the product experience in depth."},
        {"code":"CO05","stage":"Consideration","title":"Inside the Technology Platform","hasCopy":False,
         "blurb":"Demonstrates the technology and platform capabilities that power Reading Labs Online. Drives prospects to take a closer look at the product."},
        {"code":"CO06","stage":"Consideration","title":"Resources to Evaluate RLO","hasCopy":False,
         "blurb":"Points prospects to a resource page of supporting materials and screenshots for evaluating Reading Labs Online, encouraging deeper research."},
        {"code":"DE07","stage":"Decision","title":"Your RLO Questions Answered","hasCopy":False,
         "blurb":"A decision-stage email answering common FAQs and objections about adopting Reading Labs Online, removing purchase barriers for ready buyers."},
        {"code":"DE08","stage":"Decision","title":"Start Your Free Trial / Pilot","hasCopy":False,
         "blurb":"Drives conversion by offering a free trial / pilot of Reading Labs Online, prompting decision-stage prospects to experience the program firsthand."},
        {"code":"DE09","stage":"Decision","title":"Final Call to Adopt RLO","hasCopy":False,
         "blurb":"The closing email, making a final appeal to commit to Reading Labs Online with urgency and a last conversion push."},
    ],
})

# ---------------------------------------------------------------- REVEAL MATH FOR IB PYP (draft, has SF report)
PRODUCTS.append({
    "id": "reveal-math-ib", "name": "Reveal Math for IB PYP", "color": "#5F14C1",
    "status": "In-Progress",
    "audience": "IB PYP maths educators",
    "regions": "MEA · Asia · EU · KSA",
    "salesforceReport": "https://mh.lightning.force.com/lightning/r/Report/00OPB000004Y4rh2AC/view?queryScope=userFolders",
    "description": ("An awareness-stage nurture introducing Reveal Math for IB PYP to IB Primary Years Programme maths "
        "educators and decision-makers. The two-email sequence builds interest with supporting assets — a companion guide "
        "and a flexible implementation model — each driving recipients to the international landing page. Live progress for "
        "this program is tracked in the linked Salesforce report. Email creative is held in Marketo."),
    "ctaUrl": "https://info.mheducation.com/int_ict",
    "draftNoteDefault": "The full creative for this email is built in Marketo (email preview / Live Link). This card captures its role in the sequence; track contacts and leads through the program via the Salesforce report above.",
    "emails": [
        {"code":"AW01","stage":"Awareness","title":"Reveal Math IB PYP: Companion Guide","hasCopy":False,
         "blurb":"Awareness email introducing Reveal Math for IB PYP and offering a companion guide as the lead asset. CTA drives recipients to the McGraw Hill international landing page."},
        {"code":"AW02","stage":"Awareness","title":"A Flexible Implementation Model","hasCopy":False,
         "blurb":"Awareness follow-up highlighting a flexible implementation model for Reveal Math for IB PYP. CTA drives recipients to the international landing page."},
    ],
})

# =====================================================================
#  BODY FORMATTER (shared look with the on-page renderer)
# =====================================================================
def fmt_line_html(raw, cta_url):
    line = (raw or "").strip()
    if not line:
        return ""
    m = re.match(r'^\[(.+?)\]$', line)
    if m:
        lbl = re.sub(r'\s*[→\-–]+\s*$', '', m.group(1)).strip()
        return ('<a href="%s" style="display:inline-block;margin:0 0 8px;padding:9px 15px;'
                'border:1px solid #9EBDF9;background:#D9E5FC;color:#083377;border-radius:8px;'
                'font-weight:700;font-size:14px;text-decoration:none;">%s ↗</a><br>'
                % (html.escape(cta_url or "#"), html.escape(lbl)))
    if line.startswith("✓"):
        t = line[1:].strip()
        parts = t.split(" – ")
        if len(parts) > 1:
            head = html.escape(parts[0]); rest = html.escape(" – ".join(parts[1:]))
            return ('<p style="margin:0 0 9px;color:#2a2f38;"><span style="color:#0B48BC;font-weight:800;">✓</span> '
                    '<b>%s</b> – %s</p>' % (head, rest))
        return ('<p style="margin:0 0 9px;color:#2a2f38;"><span style="color:#0B48BC;font-weight:800;">✓</span> %s</p>'
                % html.escape(t))
    if re.match(r'^[-→•]\s?', line):
        return ('<p style="margin:0 0 7px 16px;color:#2a2f38;">• %s</p>'
                % html.escape(re.sub(r'^[-→•]\s?', '', line)))
    return '<p style="margin:0 0 14px;">%s</p>' % html.escape(line)

# =====================================================================
#  .eml GENERATION
# =====================================================================
def make_eml(product, e):
    color = STAGE_COLOR.get(e["stage"], "#6A7180")
    cta_url = e.get("cta_url") or product.get("ctaUrl") or "#"
    greeting = e.get("greeting", "")
    subject = e.get("subject", "") or e["title"]
    preview = e.get("preview", "") or (e.get("blurb","")[:90])
    cta_text = e.get("cta_text", "")
    signoff = e.get("signoff", "Best regards,\n{{Sender Name}}\n{{Sender Title}}, McGraw Hill")

    # ---- plain text alternative ----
    text_parts = []
    if greeting: text_parts.append(greeting)
    text_parts.append("")
    for ln in e.get("body", []):
        text_parts.append(re.sub(r'^\[(.+?)\]$', r'\1', ln))
    if cta_text:
        text_parts.append("")
        text_parts.append("%s: %s" % (cta_text, cta_url))
    text_parts.append("")
    text_parts.append(signoff)
    text_body = "\n".join(text_parts)

    # ---- html alternative ----
    body_html = "".join(fmt_line_html(ln, cta_url) for ln in e.get("body", []))
    cta_html = ('<a href="%s" style="display:inline-block;background:#E21A23;color:#ffffff;font-weight:700;'
                'padding:13px 22px;border-radius:8px;margin:6px 0 18px;text-decoration:none;font-size:15px;">%s</a>'
                % (html.escape(cta_url), html.escape(cta_text))) if cta_text else ""
    greet_html = ('<p style="margin:0 0 14px;font-weight:700;color:#16181D;">%s</p>' % html.escape(greeting)) if greeting else ""
    sign_html = '<div style="color:#3A3F4A;font-size:14.5px;white-space:pre-line;margin-top:6px;">%s</div>' % html.escape(signoff)

    html_body = """<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0"></head>
<body style="margin:0;padding:0;background:#f0f2f6;font-family:'Proxima Nova',Mulish,'Segoe UI',Arial,sans-serif;color:#222;">
<span style="display:none!important;opacity:0;color:#f0f2f6;font-size:1px;line-height:1px;max-height:0;max-width:0;overflow:hidden;">{preview}</span>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f0f2f6;"><tr><td align="center" style="padding:24px 12px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#ffffff;border-radius:14px;overflow:hidden;border:1px solid #e4e7ec;">
<tr><td style="height:8px;background:{color};font-size:0;line-height:0;">&nbsp;</td></tr>
<tr><td style="padding:22px 30px 0;"><div style="font-size:17px;font-weight:800;color:#E21A23;letter-spacing:-.01em;">McGraw Hill</div></td></tr>
<tr><td style="padding:16px 30px 28px;font-size:15px;line-height:1.62;color:#222;">
{greet}{body}{cta}{sign}
</td></tr>
<tr><td style="border-top:1px solid #eef0f4;padding:16px 30px;background:#f6f7f9;font-size:11.5px;color:#6A7180;">
McGraw Hill International &middot; You are receiving this because you engaged with McGraw Hill.
Manage preferences or unsubscribe anytime.
</td></tr>
</table>
<div style="font-size:11px;color:#9AA3BC;margin-top:14px;">Internal reference copy &middot; {product} nurture &middot; {code}</div>
</td></tr></table></body></html>""".format(
        preview=html.escape(preview), color=color, greet=greet_html, body=body_html,
        cta=cta_html, sign=sign_html, product=html.escape(product["name"]), code=html.escape(e["code"]))

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "McGraw Hill International <marketing@mheducation.com>"
    msg["To"] = "{{First Name}} {{Last Name}} <prospect@school.edu>"
    msg["Date"] = formatdate(localtime=True)
    msg["Message-ID"] = make_msgid(domain="mheducation.com")
    msg["X-Campaign"] = "%s / %s" % (product["name"], e["code"])
    msg["X-Preheader"] = preview
    msg.set_content(text_body)
    msg.add_alternative(html_body, subtype="html")
    return msg.as_bytes()

# =====================================================================
#  BUILD
# =====================================================================
def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

def build():
    os.makedirs(EMAIL_DIR, exist_ok=True)
    portal = {"config": CONFIG, "products": [], "resources": RESOURCES}
    eml_count = 0

    for p in PRODUCTS:
        pj = {k: p[k] for k in ("id","name","color","status","audience","regions","salesforceReport","description")}
        pj["emails"] = []
        for e in p["emails"]:
            has_copy = e.get("hasCopy", bool(e.get("body")))
            ej = {
                "code": e["code"], "stage": e["stage"], "title": e["title"],
                "blurb": e.get("blurb",""), "subject": e.get("subject",""),
                "preview": e.get("preview",""), "hasCopy": has_copy,
                "cta": {"text": e.get("cta_text",""), "url": e.get("cta_url") or p.get("ctaUrl","")},
            }
            if not has_copy:
                ej["draftNote"] = e.get("draftNote") or p.get("draftNoteDefault","")
            if has_copy:
                ej["greeting"] = e.get("greeting","")
                ej["body"] = e.get("body",[])
                ej["signoff"] = e.get("signoff","Best regards,\n{{Sender Name}}\n{{Sender Title}}, McGraw Hill")
                fname = "%s-%s.eml" % (slugify(p["name"]), e["code"])
                with open(os.path.join(EMAIL_DIR, fname), "wb") as f:
                    f.write(make_eml(p, e))
                ej["eml"] = fname
                eml_count += 1
            pj["emails"].append(ej)
        portal["products"].append(pj)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        tpl = f.read()
    data_js = "window.PORTAL_DATA = " + json.dumps(portal, ensure_ascii=False) + ";"
    data_js = data_js.replace("</", "<\\/")  # never let content break the <script> tag
    out = tpl.replace("/*__PORTAL_DATA__*/", data_js)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(out)

    n_emails = sum(len(p["emails"]) for p in PRODUCTS)
    print("Built index.html (%d bytes)" % len(out))
    print("Products: %d | Email cards: %d | .eml files: %d" % (len(PRODUCTS), n_emails, eml_count))

# =====================================================================
#  FOOTER RESOURCES
# =====================================================================
RESOURCES = [
    {"title": "How-to guides", "links": [
        {"label": "Add contacts to a nurture program", "url": "#"},
        {"label": "Send a nurture email to your own contacts", "url": "#"},
        {"label": "Request a new segment or list", "url": "#"},
        {"label": "Marketo program quick-start", "url": "#"},
    ]},
    {"title": "Watch & learn (screencasts)", "links": [
        {"label": "Screencast: adding contacts to a nurture", "url": "#"},
        {"label": "Screencast: sending an email to your contacts", "url": "#"},
        {"label": "Screencast: reading a Salesforce nurture report", "url": "#"},
    ]},
    {"title": "Reference & wiki", "links": [
        {"label": "Nurture program playbook (Notion)", "url": "https://app.notion.com/p/36531abc807081589995d71ffd41bd62"},
        {"label": "Brand Guidelines v6.1 (Notion)", "url": "https://app.notion.com/p/36331abc8070815cb7ceea1740cf1c68"},
        {"label": "Campaign naming conventions", "url": "https://app.notion.com/p/35731abc807081a2b0c4d2c7ea267b3a"},
        {"label": "Glossary of terms", "url": "https://app.notion.com/p/36231abc807081e69617e7713ed3e1b1"},
    ]},
]

if __name__ == "__main__":
    build()
