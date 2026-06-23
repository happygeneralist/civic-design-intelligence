# Safe research ingestion MVP

This document defines the minimum repository conventions needed to start breaking real research into structured knowledge objects without overclaiming, losing traceability or introducing semantic drift.

The immediate goal is not to complete the whole repository model. The goal is to make it safe to ingest SEND pathway-planning research samples and learn from practice.

Use this document with `docs/Non_linear_research_ingestion.md`. This MVP describes safe object creation defaults. The non-linear ingestion guide describes how knowledge may enter before the full source-to-evidence-to-object chain is complete.

## Scope

Use this MVP for structured ingestion from SEND pathway-planning research.

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

Capture is allowed before full traceability when useful knowledge is available in a partial form. Traceability remains the preferred state, and any gaps in provenance, evidence linkage or review status should remain visible.

## Non-linear ingestion

Research material will not always arrive in a clean linear sequence.

The preferred mature chain is:

```text
source
→ evidence
→ derived object
```

But useful knowledge may also enter as:

- need-shaped input
- behaviour-shaped input
- pain-point-shaped input
- research summaries
- workshop outputs
- collaborator observations
- generated candidate objects
- older notes that need later evidence linking

These inputs may be research-derived even when they are not yet linked to specific evidence objects or research-study records.

Do not copy partially structured inputs directly into canonical folders without ingestion and reconciliation. Use them to generate a full ingestion slice, then check the slice against evidence, source records and existing objects.

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

1. Capture or identify the input material.
2. Create or link source and evidence notes where the material is useful, safe to use and sufficiently anonymised.
3. Extract candidate behaviours, pain points and needs from the material.
4. Mark candidate objects conservatively.
5. Link each object back to supporting, contextual or limiting evidence where possible.
6. Compare candidate objects with existing user needs, behaviours, pain points, civic needs, insights, themes and evidence.
7. Decide whether each candidate should be created, linked, used to update an existing object, split, merged, superseded, left in the inbox or deferred.
8. Preserve uncertainty explicitly.
9. Record material meaning changes in the object change log.
10. Leave metadata-only and formatting-only changes to Git history and the pull request summary.

## Reconciliation notes

Each ingestion PR should include a short reconciliation note.

Use a lightweight structure such as:

```markdown
## Reconciliation notes

- New objects created:
- Existing objects linked:
- Existing objects updated:
- Candidate objects not created because they overlapped:
- Objects needing future split, merge or supersession review:
- Severity, scope or lifecycle judgements that remain relative or uncertain:
- Evidence or source links still unresolved:
- Material left in the inbox:
```

This is a quality-control step. It is not a maturity gate.

## User needs during ingestion

User needs are first-class problem-space objects. Follow `docs/User_needs_writing_rules.md` when deriving, refining or reconciling candidate user needs.

A user need may be functional, emotional, social, relational, experiential, decision-making, access-oriented or civic-adjacent.

Do not force emotional, social or identity needs into purely functional task language if doing so removes meaning.

Do not create solution-shaped user needs.

Before creating or materially changing a user need, check neighbouring user needs and related objects. The question is not only whether the wording is plausible. It is also whether the candidate occupies the right conceptual space in the existing repository.

## What to create first

Start with objects that help answer value and coverage questions:

- What needs are visible in the evidence or partially structured input?
- Where is unresolved pain blocking value?
- Which civic obligations or public outcomes may be unsupported?
- Which evidence is weak, indicative, traceable or substantiated?
- Which areas of the pathway are under-researched?
- Which objects already exist and should be linked or adjusted rather than duplicated?

## What not to create yet

Do not add heavy structure during the first ingestion passes:

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

- SEND pathway-planning research samples can be broken into structured objects
- partially structured knowledge can be captured without pretending it is more mature or traceable than it is
- each object has conservative status and review metadata
- each evidence-derived object links back to source evidence where possible
- unresolved source or evidence-linking gaps are visible
- candidate objects are reconciled against nearby existing objects before finalising an ingestion PR
- semantic changes are recorded in a human-readable object change log
- formatting and metadata-only changes are left to Git history and pull request summaries
- no object is marked reviewed or validated unless human review has happened
- the resulting objects support basic questions about need, pain, evidence and value coverage

## Relationship to later roadmap phases

This MVP supports the early roadmap phases only. It should not try to solve repository-wide validation, dashboarding, cross-government generalisation or mature schema enforcement.

Tighten the schema only after several worked examples show which fields are useful, which fields create friction and where semantic risk appears.
