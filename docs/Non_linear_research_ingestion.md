# Non-linear research ingestion

This document describes how research knowledge can enter the repository when it does not arrive in a clean source-to-evidence-to-object sequence.

The repository should support live, messy and partially structured knowledge while still moving towards traceability, defensibility and reviewable object quality.

## Core principle

```text
Capture is allowed before full traceability. Traceability remains the preferred state.
```

The repository should make gaps in provenance, evidence linkage, object maturity and review status visible. It should not block useful knowledge from entering simply because the ideal chain is not complete yet.

## Preferred mature state

The preferred mature chain is:

```text
source
→ evidence
→ derived object
→ pattern or insight
```

This is still the most defensible state. It supports audit, challenge, comparison and later reuse.

However, this chain is an end state to work towards. It is not the only acceptable entry route.

## Real working state

Research knowledge may enter the repository as partial knowledge first:

```text
partial knowledge
→ structured capture
→ backward evidence linking
→ reconciliation
→ improved traceability
```

This is intentional. The system is being used in a live institutional context, where useful knowledge may appear before all provenance and object relationships have been resolved.

## Possible entry states

Knowledge may enter as:

- a raw source
- a selected evidence extract
- a transcript extract
- a research summary
- a need-shaped input
- a behaviour-shaped input
- a pain-point-shaped input
- a workshop output
- a collaborator observation
- a thematic synthesis
- an LLM-assisted candidate object
- an existing note that needs later evidence linking

Entry state is not the same as evidence strength, object quality or maturity.

For example:

- a need-shaped input may be research-derived but not yet linked to a specific evidence object
- a quote may be strong evidence but not yet interpreted
- a report may be authoritative but not yet broken into selected evidence extracts
- a generated candidate object may be well structured but still weakly grounded
- a synthesis may be useful but need backward evidence-linking before it is relied on heavily

## Need-shaped inputs

A need-shaped input is material that appears to express a user need, but has not yet been processed into a first-class user need object.

Need-shaped inputs may be real research-derived material. They should not be treated as invalid simply because they are not yet linked to specific evidence or research-study records.

They should also not be copied directly into the user needs folder without a fuller ingestion and reconciliation process.

A useful workflow is:

```text
need-shaped input
→ LLM-assisted ingestion slice
→ candidate user needs, behaviours, pain points, civic needs or insights
→ object landscape check
→ evidence/source linking where possible
→ unresolved provenance questions made visible
→ create, link, update, split, merge or leave in inbox
```

Do not introduce a formal object type called anchor need or anchor summary from this pattern. Those terms may mean something else later.

## Ingestion is not only extraction

Ingestion includes both extraction and reconciliation.

Extraction asks:

- what evidence, needs, behaviours, pain points, civic needs or insights might this material imply?
- what source or evidence records are needed?
- what uncertainty needs to be preserved?

Reconciliation asks:

- does an equivalent object already exist?
- is this a narrower or broader version of an existing object?
- is it a sibling in the same conceptual space?
- should an existing object be linked, updated, split, merged or superseded?
- should the material stay in the inbox until the evidence basis is clearer?
- do relative judgements such as severity or scope need comparison with nearby objects?

The repository should avoid avoidable object sprawl. The aim is not to dump many disconnected objects into the system. The aim is to increase useful coverage while keeping the knowledge graph coherent.

## Reconciliation before finalising a slice

Before finalising an ingestion PR, check nearby existing objects:

- user needs
- civic needs
- behaviours
- pain points
- insights
- themes
- evidence records
- research studies or source records

The PR summary should record reconciliation notes, such as:

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

## User needs during non-linear ingestion

User needs are first-class research objects. They must follow `docs/User_needs_writing_rules.md` during both direct extraction and backward structuring from need-shaped input.

A user need may be functional, emotional, social, relational, experiential, decision-making, access-oriented or civic-adjacent.

Do not force emotional, social or identity needs into purely functional task language if doing so removes meaning.

Do not create solution-shaped user needs.

When deriving or refining a user need, check:

- what kind of need the evidence or input supports
- whether the wording preserves functional, emotional and social meaning
- whether the actor or beneficiary is correct
- whether the need level is right
- whether a wording change would alter the conceptual space
- whether the candidate overlaps with existing user needs
- whether it is actually a behaviour, pain point, insight or civic need
- whether solution-shaped material has been separated from the canonical user need

## Backward evidence-linking

Backward evidence-linking is the process of taking partially structured knowledge and connecting it back to source or evidence records after capture.

Use this when:

- a need-shaped input is known to be research-derived but not yet linked to the specific extract
- a synthesis exists before the evidence objects have been created
- a collaborator contributes knowledge from known work but the repository does not yet contain the source trail
- older notes contain useful knowledge but need source/evidence reconstruction

Backward evidence-linking should make the current state explicit. Use conservative status and review metadata until the provenance is clearer.

Do not silently upgrade confidence, evidence strength or review status just because a backward link has been added.

## Source capture and cross-repository use

Where the input is a public secondary source, the preferred split remains:

```text
civic-design-secondary-research
→ raw or lightly processed public source material
→ source-level documentation
→ candidate extracts
→ evidence maps back to structured objects

civic-design-intelligence
→ source records
→ selected evidence extracts
→ structured knowledge objects
```

However, non-linear ingestion means structured knowledge may sometimes exist before the source archive is complete. In those cases, add source archive references later and make the provenance gap visible until resolved.

Future upload or source-capture workflows should help create:

- a companion source folder
- source-level metadata
- an evidence-map stub
- a matching source record in this repository
- selected evidence extract stubs where useful
- reviewable links between the two repositories

Automation should support capture and traceability. It should not automatically validate interpretation, evidence strength, review status or maturity.

## What this changes

This model changes the ingestion emphasis from a strictly linear process to a flexible, live knowledge process.

The repository should support:

- getting useful knowledge in
- marking uncertainty honestly
- working backwards to evidence where needed
- reconciling new material with existing objects
- improving traceability over time
- avoiding premature validation
- avoiding uncontrolled object sprawl

## What this does not change

This does not change the core governance principles:

- Git remains the technical audit trail.
- Object change logs record meaningful knowledge evolution.
- LLM intervention logs remain reserved for material semantic risk.
- LLMs must not mark objects as reviewed or validated unless human review has happened.
- User needs remain solution-free problem-space objects.
- Raw public source material should not be bulk imported into the structured intelligence repository.
- Traceability remains the preferred state.

## Near-term use

Use this model for the next ingestion work:

1. Take existing evidence quotes and need-shaped research summaries.
2. Generate full ingestion slices rather than direct object copies.
3. Compare candidate objects with the existing object landscape.
4. Create, link, update, split, merge or defer objects based on reconciliation.
5. Record unresolved provenance or object-boundary questions in the PR.
6. Keep maturity and review status conservative unless explicit human review has happened.
