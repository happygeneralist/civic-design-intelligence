# Non-linear research ingestion

This document describes how research knowledge can enter the repository when it does not arrive in a clean source-to-evidence-to-object sequence.

The repository should support live, messy and partially structured knowledge while still moving towards traceability, defensibility and reviewable object quality.

## Core principle

```text
Capture is allowed before full traceability. Traceability remains the preferred state.
```

The repository should make gaps in provenance, evidence linkage, object maturity and review status visible. It should not block useful knowledge from entering simply because the ideal chain is not complete yet.

A second practical rule applies:

```text
Capture at the smallest useful level that preserves meaning and relationships.
```

Sometimes that level is one candidate object. Sometimes it is a relationship hypothesis, summary, generated view or whole analytical model. The repository should not force every input through the same route.

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
- a candidate civic need or insight
- a relationship or causal hypothesis
- a workshop output
- a collaborator observation
- a thematic synthesis
- an LLM-assisted candidate object
- a generated journey or service view
- a coherent analytical model or map
- an existing note that needs later evidence linking

Entry state is not the same as evidence strength, object quality or maturity.

For example:

- a need-shaped input may be research-derived but not yet linked to a specific evidence object
- a quote may be strong evidence but not yet interpreted
- a report may be authoritative but not yet broken into selected evidence extracts
- a generated candidate object may be well structured but still weakly grounded
- a synthesis may be useful but need backward evidence-linking before it is relied on heavily
- a relationship may be plausible but still be an analyst hypothesis rather than an established causal link
- a coherent journey view may be useful for inspection while many of its phases or relationships remain assumptive

## Choose treatment by form, basis and maturity

Before deciding how to ingest material, assess three things.

### Form

What is the useful unit that should be preserved?

- source or evidence extract
- candidate object
- object attribute
- relationship or causal hypothesis
- summary or synthesis
- generated or contextual view
- whole model or map

### Basis

What supports the important claims?

- direct lived-experience evidence
- reported or mediated lived experience
- practitioner or expert knowledge
- inspection or institutional evidence
- operational data
- policy, law or statutory material
- current-system analysis
- analyst synthesis
- LLM-assisted inference
- unclear or unresolved provenance

### Maturity

What is the current knowledge state?

- captured
- assumption or candidate
- evidence-linked
- human reviewed
- validated or substantiated where explicitly justified
- superseded, deprecated, dormant or resolved

These are review questions, not a new controlled taxonomy. Do not add schema simply to make every input fit a neat classification.

## Assumptions can exist at different levels

An assumption is an epistemic property, not one kind of object.

Uncertainty may apply to:

- the whole object
- one attribute, such as severity or actor scope
- a relationship between objects
- a causal explanation
- applicability or prevalence
- a journey phase or pattern
- a generated view or whole model

For example, a pain point may have locally evidenced existence while its severity, national applicability and causal explanation remain assumptive.

Do not let one object-level status imply that every claim within the object has the same evidence basis. Use interpretation and review notes to make claim-level uncertainty visible before introducing heavier schema.

## Appropriate first treatments

Different forms of partial knowledge need different first treatments.

### Source or evidence-led material

Use bounded extraction when a source is the useful starting unit.

```text
source
→ source context
→ selected evidence
→ bounded interpretation
→ reconciliation
→ candidate object changes
```

### Individual candidate objects

An assumptive user need, pain point, behaviour, civic need or insight may enter directly as a conservative candidate object when that is the smallest useful level that preserves meaning.

It does not require a whole-model ingestion process.

The object should preserve:

- its original meaning and origin
- unsupported attributes or relationships
- conservative maturity and review metadata
- nearby-object reconciliation
- evidence or provenance gaps

### Relationship or explanation hypotheses

Sometimes the useful knowledge is a proposed connection rather than a new object.

Examples include:

- unclear responsibility may lead to repeated chasing
- support invisibility may compound waiting-related harm
- a funding mechanism may redistribute navigation burden to families

Record the connection as provisional analysis or a review note unless an existing relationship structure is clearly suitable. Do not make an inferred relationship look established.

### Summaries, syntheses and legacy knowledge

Preserve the original input, identify its basis, structure only the useful parts and work backwards towards stronger traceability where proportionate.

Do not require a useful research summary or expert synthesis to be rebuilt from the ground up before it can inform the repository.

### Generated views and whole models

Preserve the whole artefact when its relationships and overall structure carry meaning that would be lost through immediate atomisation.

Examples include:

- journey views
- service maps
- system models
- thematic models
- complex workshop syntheses

Connect or extract objects selectively. Whole-artefact preservation is one treatment within non-linear ingestion, not the default for all assumptive knowledge.

## Need-shaped inputs

A need-shaped input is material that appears to express a user need, but has not yet been processed into a first-class user need object.

Need-shaped inputs may be real research-derived material. They should not be treated as invalid simply because they are not yet linked to specific evidence or research-study records.

They should also not be copied directly into the user needs folder without a fuller ingestion and reconciliation process.

A useful workflow is:

```text
need-shaped input
→ candidate formulation using user-needs rules
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

## Reconciliation before finalising a slice or capture

Before finalising an ingestion PR, check nearby existing objects and views:

- user needs
- civic needs
- behaviours
- pain points
- insights
- themes
- evidence records
- research studies or source records
- relevant summaries, journey views or analytical models

The PR summary should record reconciliation notes, such as:

```markdown
## Reconciliation notes

- Input form and basis:
- Original material preserved:
- New objects created:
- Existing objects linked:
- Existing objects updated:
- Candidate objects not created because they overlapped:
- Provisional relationships or attributes:
- Objects needing future split, merge or supersession review:
- Severity, scope or lifecycle judgements that remain relative or uncertain:
- Evidence or source links still unresolved:
- Material left in the inbox or source view:
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
- which parts of the formulation are evidenced, inferred or still assumptive

## Backward evidence-linking

Backward evidence-linking is the process of taking partially structured knowledge and connecting it back to source or evidence records after capture.

Use this when:

- a need-shaped input is known to be research-derived but not yet linked to the specific extract
- a synthesis exists before the evidence objects have been created
- a collaborator contributes knowledge from known work but the repository does not yet contain the source trail
- older notes contain useful knowledge but need source/evidence reconstruction
- a generated view or model contains claims that can later be linked to more specific evidence

Backward evidence-linking should make the current state explicit. Use conservative status and review metadata until the provenance is clearer.

Do not silently upgrade confidence, evidence strength or review status just because a backward link has been added.

## Capture and use are separate decisions

A low barrier to responsible capture does not mean every captured item is safe for every use.

Distinguish whether knowledge is safe to:

- capture
- include in a provisional view
- use for research planning
- use for operational or design decisions
- use for benchmarking, policy or other consequential purposes
- treat as established knowledge

Candidate and assumptive knowledge can reveal the shape of a problem space and guide research without being treated as settled or validated.

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

## AI-assisted continuity and authorisation

Repository-aware tools should inspect this guidance, relevant issues and nearby objects before recommending an ingestion treatment.

They should not:

- treat the most recently tested route as the only route
- ask the user to repeatedly restore an already documented principle
- discard useful assumptive knowledge because traceability is incomplete
- force every input through source-first extraction or whole-model preservation
- silently narrow the operating model

Creating or updating an issue, branch or pull request does not authorise merging, closing, deleting or otherwise finalising it. Finalising actions require explicit user instruction.

## What this changes

This model changes the ingestion emphasis from a strictly linear process to a flexible, live knowledge process.

The repository should support:

- getting useful knowledge in
- selecting a treatment based on form, basis and maturity
- marking uncertainty honestly at the right level
- working backwards to evidence where needed
- reconciling new material with existing objects and views
- preserving coherent artefacts where their structure carries meaning
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

1. Identify the input's useful form, basis and maturity.
2. Choose the smallest capture level that preserves meaning and relationships.
3. Preserve original summaries, views or models where their whole structure carries value.
4. Compare candidate objects and relationships with the existing knowledge landscape.
5. Create, link, update, split, merge or defer based on reconciliation.
6. Record unsupported attributes, relationships, provenance and object-boundary questions in the PR.
7. Keep maturity and review status conservative unless explicit human review has happened.
8. Stop at a reviewable PR unless the user explicitly authorises finalisation.
