# Ingestion slice workflow

This document defines the lightweight workflow for running a bounded ingestion slice.

Use it when turning evidence, source material, need-shaped input, research summaries or other partially structured knowledge into repository objects.

This is a practical workflow, not a heavy governance process.

## Purpose

An ingestion slice should help the repository take in useful knowledge without creating object sprawl, losing provenance or making immature knowledge look settled.

An ingestion slice should produce:

- selected evidence or source links where possible
- candidate user needs, civic needs, behaviours, pain points, insights or themes
- reconciliation with existing objects
- clear uncertainty and review status
- a small reviewable PR

## Core rule

```text
Ingestion is extraction plus reconciliation.
```

Do not only ask what new objects can be created. Also ask how the material relates to existing objects.

## When to use this workflow

Use this workflow for:

- a small group of evidence quotes
- a transcript excerpt
- a need-shaped research summary
- a workshop output
- a collaborator observation
- a secondary-source extract
- a small report section
- an existing inbox note that needs structuring

Do not use this workflow for large uncontrolled bulk ingestion.

## Recommended slice size

Start small.

A good first slice might include:

- 1 to 5 evidence quotes
- 1 short section of a report
- 1 coherent cluster of need-shaped inputs
- 1 tightly scoped theme, such as parent/carer navigation burden

If the slice produces too many candidate objects or unresolved questions, split it.

## Stage 1: Prepare the slice

Define the slice before using tools.

Capture:

- the input material
- why this slice is useful now
- known source or evidence links
- likely actor or beneficiary
- likely service or pathway context
- any sensitive interpretation risks
- expected existing objects to check

Example:

```markdown
## Slice scope

Topic: Parent/carer navigation burden in SEND pathway planning
Input material: EVID_003 and related need-shaped research summaries
Likely objects to check: UN_015, BEH_009, PP_002
Goal: Test whether navigation-burden evidence supports additional links, refinements or candidate objects
```

## Stage 2: ChatGPT sensemaking

Use ChatGPT for semantic framing before editing files.

Ask for:

- possible user needs
- possible civic needs
- possible behaviours
- possible pain points
- possible insights or themes
- existing objects likely to overlap
- wording risks
- object-boundary risks
- unresolved evidence questions

Do not treat this as repository truth. Treat it as a candidate interpretation.

## Stage 3: Codex repository reconnaissance

Use Codex to inspect the repository at scale before implementation.

Codex instruction pattern:

```text
Do not edit files yet.

Read:
- docs/Non_linear_research_ingestion.md
- docs/Safe_research_ingestion_MVP.md
- docs/User_needs_writing_rules.md
- docs/Ingestion_slice_workflow.md

Inspect existing user needs, civic needs, behaviours, pain points, insights, themes, evidence and research studies related to [slice topic].

Produce a reconciliation brief only. Do not create or modify files.
```

Codex should return:

- existing objects checked
- likely duplicates or overlaps
- candidate objects that may be new
- existing objects that may need links or updates
- evidence/source gaps
- questions needing human judgement

## Stage 4: Reconciliation brief

Create or review a reconciliation brief before implementation.

Use this structure:

```markdown
# Reconciliation brief

## Slice scope

## Input material

## Existing objects checked

### User needs

### Civic needs

### Behaviours

### Pain points

### Evidence and sources

## Candidate decisions

### Create

### Link

### Update

### Do not create

### Leave in inbox

### Needs later review

## User need wording checks

## Severity, scope or lifecycle checks

## Evidence and provenance gaps

## Human review questions
```

This brief is the main quality-control artefact.

## Stage 5: Human or ChatGPT review

Review the reconciliation brief before files are changed.

Check:

- whether candidate user needs follow `docs/User_needs_writing_rules.md`
- whether emotional, social, relational or experiential meaning has been preserved
- whether any user need contains solution-shaped wording
- whether candidates duplicate existing objects
- whether behaviours are too broad or too granular
- whether pain point severity or lifecycle claims are overconfident
- whether civic needs are justified by the evidence
- whether source or evidence gaps are visible
- whether any material should remain in the inbox

This review does not need to validate objects. It only needs to make the implementation safe enough to try.

## Stage 6: Codex implementation

Only after the reconciliation brief has been reviewed should Codex edit files.

Codex instruction pattern:

```text
Implement the reviewed ingestion slice.

Use only the create, link, update, do-not-create and defer decisions in the approved reconciliation brief.

Do not mark anything reviewed or validated.
Use conservative metadata.
Preserve source and evidence uncertainty.
Add reconciliation notes to the PR body.
Run validation.
Open a small PR.
```

Keep implementation bounded.

## Stage 7: PR review

The PR should explain:

- what changed
- what did not change
- which existing objects were checked
- which candidate objects were not created
- what remains unresolved
- whether an object change log or LLM intervention log was needed
- expected validation effect

No ingestion PR should silently promote confidence, evidence strength, maturity or review state.

## Required PR reconciliation notes

Every ingestion PR should include:

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

## Tool use summary

### Use ChatGPT for

- initial sensemaking
- semantic review
- object-boundary discussion
- user need wording review
- reviewing Codex reconciliation briefs

### Use Codex for

- repository search
- file inspection
- reconciliation brief generation from files
- implementation
- validation
- PR creation

### Use humans for

- semantic acceptance
- review and merge
- decisions about maturity, review status or validation
- sensitive interpretation
- public or partner-facing judgement

## Guardrails

Do not:

- ask Codex to ingest broad research without a bounded slice
- copy need-shaped input directly into canonical user need objects
- create new objects without checking nearby existing objects
- rewrite user needs into task language when the evidence is emotional, social or relational
- create solution-shaped user needs
- mark anything reviewed or validated unless human review has happened
- change lifecycle, severity or maturity states without explicit review
- add large new schemas or validators during an ingestion slice

## Done criteria

An ingestion slice is complete when:

- the slice scope is clear
- candidate objects have been compared with existing objects
- new or updated objects are traceable where possible
- unresolved provenance gaps are visible
- uncertainty and review status remain conservative
- the PR contains reconciliation notes
- the changed file set is small enough to review
