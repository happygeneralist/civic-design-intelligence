# Safe research ingestion MVP

This document defines the minimum repository conventions needed to start breaking real research into structured knowledge objects without overclaiming, losing traceability or introducing semantic drift.

The immediate goal is not to complete the whole repository model. The goal is to make it safe to ingest a small SEND pathway-planning research sample and learn from practice.

## Scope

Use this MVP for the first structured ingestion pass from SEND pathway-planning research.

Create only the strongest useful objects first:

- evidence
- behaviours
- pain points
- user needs
- civic needs, where relevant
- insights
- themes

Avoid creating opportunities unless they are directly grounded in the problem space and explicitly linked to evidence, pain points or needs.

## Safe-ingestion principle

```text
Structure enough to make research usable, but not enough to make immature knowledge look settled.
```

The repository should support fast capture and cautious interpretation.

## Default metadata for new objects

Use conservative defaults unless there is a clear reason not to.

### Evidence

```yaml
status: captured
analysis_state: captured
review_status: not_reviewed
creation_mode: manual | llm_assisted | imported
llm_generated: false
human_reviewed: false
```

### LLM-assisted candidate analysis object without direct evidence links

Use this for early candidate user needs, civic needs, behaviours, pain points, insights or themes created from research review but not yet linked to specific evidence.

```yaml
status: assumption
analysis_state: candidate
review_status: not_reviewed
evidence_basis: none
evidence_strength: none
confidence: low
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
change_level: none
```

### LLM-assisted candidate analysis object with direct evidence links

Use this when the object has at least one explicit evidence link, but a human has not checked the interpretation.

```yaml
status: draft
analysis_state: evidence_linked
review_status: needs_review
evidence_basis: traceable
evidence_strength: weak
confidence: low | medium
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
change_level: none
```

Do not use `reviewed` or `validated` unless a human has explicitly reviewed the object and the evidence basis supports the status.

## First-pass ingestion workflow

1. Capture or identify the source evidence.
2. Create evidence notes only where the material is useful and anonymised.
3. Extract candidate behaviours, pain points and needs from the evidence.
4. Mark candidate objects conservatively.
5. Link each object back to supporting, contextual or limiting evidence where possible.
6. Preserve uncertainty explicitly.
7. Record material meaning changes in the object change log.
8. Leave metadata-only and formatting-only changes to Git history and the pull request summary.

## What to create first

Start with objects that help answer value and coverage questions:

- What needs are visible in the evidence?
- Where is unresolved pain blocking value?
- Which civic obligations or public outcomes may be unsupported?
- Which evidence is weak, indicative, traceable or substantiated?
- Which areas of the pathway are under-researched?

## What not to create yet

Do not add heavy structure during the first ingestion pass:

- full LLM intervention logs for routine extraction
- strict validators
- dashboards
- coverage scoring
- maturity scoring beyond existing status fields
- journey generation
- persona or segment models
- opportunity pipelines
- cross-service taxonomies

These should be introduced only after worked examples show what is useful.

## Civic needs in the MVP

Treat civic needs as first-class analysis objects when the research points to an institutional obligation, public value, rights issue, accountability concern, access burden or system-level duty.

For the MVP, civic needs may live alongside user needs in `003_User_needs/` while using:

```yaml
type: civic_need
id: CN_000
need_level: civic
```

A later schema review can decide whether civic needs need their own folder.

## Acceptance criteria

The safe-ingestion MVP is working when:

- a small SEND pathway-planning research sample can be broken into structured objects
- each object has conservative status and review metadata
- each evidence-derived object links back to source evidence where possible
- semantic changes are recorded in a human-readable object change log
- formatting and metadata-only changes are left to Git history and pull request summaries
- no object is marked reviewed or validated unless human review has happened
- the resulting objects support basic questions about need, pain, evidence and value coverage

## Relationship to later roadmap phases

This MVP supports the early roadmap phases only. It should not try to solve repository-wide validation, dashboarding, cross-government generalisation or mature schema enforcement.

Tighten the schema only after several worked examples show which fields are useful, which fields create friction and where semantic risk appears.
