# First bounded Ofsted SEND ingestion slice plan

Status: proposed
Related issue: #79
Related execution-model issue: #80
Source domain: SEND pathway planning
Source locality: Essex

## Purpose

This note defines the first bounded public-source ingestion slice for the Civic Design Intelligence repository.

It is a planning note only. It does not create evidence objects, user needs, civic needs, pain points, insights, themes or other research objects.

The goal is to make the first Ofsted SEND ingestion test small enough to inspect, while preserving enough public-safe reasoning for future repository users to understand the source boundary, evidence selection rationale and uncertainty.

## Execution model

Use the hybrid public reasoning trail with private method support.

This means:

- human and ChatGPT-led reasoning define the slice, interpret the public source and decide what public-safe rationale needs to be captured;
- Codex or repository tooling may later support mechanical work such as file creation, template application, link checking and validation;
- Codex should not be the sole reasoning agent for this first substantial Ofsted report;
- private orchestration may support ingestion, but the public CDI repo must contain enough source-to-object rationale to inspect the resulting knowledge objects without access to the private repo;
- no private prompts, protected rubrics, scoring logic, ontology/navigation inference logic or reusable orchestration playbooks should be committed publicly.

## Source

### Source title

Area SEND inspection of Essex Local Area Partnership

### Source type

Public Ofsted and Care Quality Commission area SEND inspection report.

This is secondary/system evidence. It is not direct user research and must not be treated as validated evidence of user needs on its own.

### Source location

Source archive repository:

```text
happygeneralist/civic-design-secondary-research
sources/SRC_001_ofsted_essex_area_send_inspection_jan_2026
```

Working source used during planning:

```text
Essex_Area_SEND_Full_inspection_Jan26.pdf
```

### Public and reuse status

The source is a public inspection report. The report states that the publication is Crown copyright 2026 and that information may be reused under the Open Government Licence, excluding logos.

Structured CDI use should cite the public source and avoid copying unnecessary branded or presentational material.

## Proposed slice boundary

### Slice name

Communication with families while waiting for assessments or services.

### In scope

Only report material directly concerned with:

- inconsistent frequency or quality of communication from the local area partnership;
- children, young people and families not being aware of what support is available;
- families needing more help to understand available community activities or support;
- insufficient communication with individual families about plans and support;
- communication that does not resolve families' questions and anxieties while they wait;
- the area-for-improvement recommendation about improving communication with children, young people and parents, including while families wait for assessments or services.

Likely report locations to inspect during the next step:

- page 2: communication frequency and quality are inconsistent; children, young people and families are sometimes not aware of available support;
- page 5: communication between services and individual families about plans and support is often insufficient to resolve questions and anxieties;
- pages 6 to 7: area for improvement requiring more consistent communication about available support and improved communication with individual families while they wait.

### Out of scope

Do not include the whole report by default.

Exclude from this first slice unless strictly needed as limited context:

- the full EHC needs assessment backlog;
- EHC plan quality issues, including health and social care accuracy;
- neurodevelopmental assessment waiting times as a whole;
- speech and language identification or therapy access;
- ADHD medication pathway arrangements;
- mental health service equity and therapeutic support waits;
- preparation for adulthood;
- alternative provision;
- leadership, governance and strategy findings;
- all positive practice examples;
- full report-level outcome coding.

These can become later bounded slices if needed.

## Why this slice is useful

This slice is small, coherent and directly relevant to SEND pathway planning.

It tests whether CDI can represent an important public-service problem without converting an inspection finding into a validated user need or prematurely turning it into a solution requirement.

The slice should help test:

- inspection findings as evidence;
- communication breakdown as a pathway condition;
- waiting as an experience context, not only an operational delay;
- the distinction between user needs, civic needs, pain points, evidence and service mechanisms;
- how a local evidence instance can support a reusable or umbrella object without creating a national prevalence claim;
- how uncertainty, scope and review status should remain visible.

## General objects and local evidence

The underlying need for families to communicate, coordinate and stay oriented in SEND pathways is not inherently Essex-specific.

The Essex report should be treated as a local evidence instance showing how this need, pain or service condition appears in Essex. It should not be used on its own to claim that the same issue has the same prevalence, severity or pattern across the UK.

Candidate objects may be worded at the highest useful level where the underlying need is generalisable. Locality should attach to the source, evidence, severity note, service context or implementation condition unless the evidence shows that local context materially changes the meaning of the object.

Use this working rule:

```text
general or umbrella object
→ supported, challenged or qualified by local evidence instances
→ strengthened, narrowed, split or superseded through comparison
```

Do not create local-only duplicate needs merely because the first evidence instance is from Essex.

Do not create national claims from a single local source.

## Expected evidence types

Expected evidence types include:

- inspection finding;
- contextual evidence;
- secondary interpretation by Ofsted/CQC;
- area-for-improvement recommendation;
- system condition affecting families, children and young people, and professionals.

Candidate evidence should record whether it is:

- direct report evidence;
- secondary interpretation;
- inspection finding;
- contextual evidence;
- improvement recommendation.

## Possible candidate object types

The slice may support candidate recommendations for:

- evidence;
- pain point;
- user need;
- civic need;
- insight;
- theme;
- service context;
- source note;
- loose or inbox material.

Do not assume every extract needs a derived object.

Some selected extracts may remain evidence only.

## Candidate object caution

Inspection findings are not direct user research.

Do not treat inspection findings as validated user needs.

Prefer conservative states such as `captured`, `draft`, `needs_review` or equivalent current schema values.

Do not mark objects as reviewed or validated.

Do not convert policy requirements, service mechanisms, administrative steps or organisational needs into user needs.

When considering a user need, follow `docs/User_needs_writing_rules.md`:

- use action-oriented language;
- describe what a person needs to achieve, preserve, recover or change in context;
- avoid vague cognitive states such as `know` or `understand` unless comprehension itself is the evidenced need;
- preserve emotional, relational, social, civic and experiential meaning where evidence supports it;
- check nearby existing needs before proposing a new need.

## Public-safe reasoning to capture in the next step

For each candidate extract within the agreed slice, capture:

- exact or near-exact extract;
- source location, preferably page and section;
- why the extract matters;
- what candidate object type it may support;
- why that object type is appropriate;
- what uncertainty remains;
- whether it is direct evidence, secondary interpretation, inspection finding or contextual evidence;
- whether it should produce a new object, support an existing object, update an existing object or remain evidence only;
- whether it may connect to an umbrella need or pattern;
- what nearby objects were checked or still need checking;
- why the status should remain conservative;
- what has not been validated.

## Private method details to exclude

Do not include:

- protected prompt chains;
- detailed private rubrics;
- scoring or diagnostic method;
- ontology/navigation inference logic;
- reusable orchestration playbooks;
- private scratch reasoning that is not needed to inspect the public knowledge object.

## Stop or shrink criteria

Stop or shrink the slice if:

- more than 5 to 8 candidate evidence extracts are needed;
- the analysis starts pulling in the whole EHC assessment backlog;
- the analysis starts treating all waiting-time problems as part of this communication slice;
- the analysis starts creating multiple user needs from thin inspection evidence;
- nearby existing objects cannot be checked before object recommendations are made;
- it becomes unclear whether an item is about communication, assessment timeliness, plan quality or service availability;
- the evidence requires direct user research before it can be responsibly modelled;
- public rationale would require private method detail to be intelligible.

Tighter fallback slice:

```text
Communication with individual families while they wait for assessments or services, using only the page 5 finding and the pages 6 to 7 area-for-improvement recommendation.
```

## Proposed next PR after this plan

After this planning PR is merged, create a second small PR containing a candidate evidence table for this slice.

That PR should include:

- selected candidate extracts only from the agreed slice;
- source locations;
- extract rationale;
- possible object type;
- confidence and uncertainty;
- evidence-type classification;
- recommendation to create, link, update, defer or leave as evidence only.

That PR should still avoid creating final research objects unless explicitly approved.

## What this plan does not do

This plan does not:

- ingest the whole Ofsted report;
- scrape or bulk-download material;
- create evidence objects;
- create user needs, civic needs, pain points, insights or themes;
- make national claims from Essex evidence;
- mark anything as reviewed or validated;
- expose private orchestration method.
