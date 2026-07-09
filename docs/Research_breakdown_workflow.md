# Research breakdown workflow: public summary

This document gives a public-safe summary of how research material may be broken down into candidate problem-space objects in this repository.

It intentionally does not publish detailed ingestion routines, LLM prompt sequences, object reconciliation workflows, review rubrics, scoring methods or protected orchestration methods.

Detailed operating material belongs in the private `happygeneralist/design-intelligence-orchestration` repository unless there is an explicit publication decision.

## Purpose

The repository needs a safe way to make emerging research material visible without pretending that every candidate object is fully evidenced, reviewed or validated.

A public-safe breakdown process should support:

- traceability from structured objects back to source material;
- clear separation between evidence and interpretation;
- conservative metadata;
- visible uncertainty;
- problem-space focus;
- later deepening when a candidate object will affect design, policy, prioritisation or stakeholder communication.

## Public workflow shape

A safe public workflow follows this broad shape:

```text
capture source material
-> identify candidate problem-space objects
-> preserve traceability and uncertainty
-> structure only what is useful enough to keep
-> deepen only when consequences increase
```

This is a public governance shape, not a reusable private operating workflow.

## Candidate objects

Research breakdown may identify candidate:

- evidence items;
- user needs;
- civic needs;
- behaviours;
- pain points;
- insights;
- themes;
- opportunities;
- value dimensions.

These candidate objects should not be treated as final, reviewed or validated simply because they have been structured.

## Inbox and source handling

Loose or immature material should remain in the inbox or another staging area until it is clear how it should be used.

Do not force material into structured schemas just because it exists.

Do not add raw transcripts, recordings, identifiable participant data or unredacted case details.

Where structured objects are created, preserve a trace back to the source note, study or evidence context where possible.

## Conservative metadata

LLM-assisted or first-pass candidate objects should use conservative metadata.

They should normally remain marked as candidate, assumption, not reviewed or needs review until a human reviewer has assessed the evidence, wording and interpretation.

Do not use:

```yaml
evidence_basis: validated
```

unless a human reviewer has explicitly completed validation.

Do not mark an LLM-generated object as human reviewed.

## User-needs caution

User needs require particular care.

A candidate user need should describe what a person needs to achieve, preserve, recover or change in context. It should not be a service mechanism, content requirement, policy requirement, backlog item, organisational need, page requirement, form requirement or preferred solution.

LLM-generated user needs are candidate formulations only. They should not be treated as stable until reviewed for:

- wording;
- scope and level;
- evidence basis;
- solution-agnostic framing;
- civic, emotional, social and experience meaning where relevant;
- risk that wording changes would alter solution direction.

## Evidence handling

Evidence should remain close to its source.

LLMs may help identify possible evidence items, but they do not create evidence.

If an object is supported only by source-level interpretation rather than direct evidence links, that limitation should be visible.

## Deepening rule

Deepen a candidate object only when the consequences of using it increase.

Examples include use in:

- page or content design;
- service design;
- policy challenge;
- prioritisation;
- stakeholder-facing synthesis;
- value assessment;
- technical or data requirements;
- review or validation.

Deepening may include checking evidence links, wording, related objects, contradictory evidence and review notes.

## Problem-space focus

This repository is focused on problem-space understanding.

It should not turn first-pass breakdown work into solution tracking.

Opportunities and value dimensions may create future connection points for solution-mapping work, but solution options should not be treated as research findings.

## Public/private boundary

The public repository may contain:

- high-level workflow principles;
- safety rules;
- conservative metadata expectations;
- object definitions;
- evidence and review-state meanings;
- enough explanation for contributors to understand and challenge public objects.

The private orchestration layer may contain:

- detailed ingestion routines;
- LLM prompt sequences;
- batch processing workflows;
- object reconciliation methods;
- review checklists;
- quality rubrics;
- protected user-needs methodology;
- ontology or navigation logic.

## Related documents

- `docs/LLM_research_breakdown_prompts.md`
- `docs/LLM_safety_model.md`
- `docs/LLM_intervention_logging.md`
- `docs/User_needs_writing_rules.md`
- `docs/Openness_protection_model.md`
- `docs/Source_use_policy.md`
- `docs/Evidence_standards.md`

## Current status

This file is a public-safe replacement for an earlier detailed workflow.

The replacement keeps the repository intelligible and auditable while avoiding publication of repeatable orchestration detail that should remain private by default.
