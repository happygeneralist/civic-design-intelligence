# Input and evidence classification

This document helps contributors decide what kind of material they are working with and how it should move through the ingestion workflow.

It should be read alongside:

- `docs/Non_linear_research_ingestion.md`
- `docs/Ingestion_operating_model.md`
- `docs/Ingestion_slice_workflow.md`
- `docs/Safe_research_ingestion_MVP.md`
- `docs/User_needs_writing_rules.md`

## Purpose

Different kinds of material need different ingestion routes.

A quote, a transcript, a workshop note, a need-shaped summary, an inspection report and a collaborator observation can all be useful. They should not all be treated as the same kind of evidence.

The aim is to:

- get useful knowledge into the repository
- preserve what kind of material it came from
- avoid overclaiming evidence strength
- avoid copying partially structured material directly into canonical objects
- support backward evidence-linking where needed
- make review and provenance gaps visible

## Core distinction

```text
Input type is not the same as evidence strength, maturity or object quality.
```

For example:

- a quote may be direct lived-experience evidence but still need interpretation
- a need-shaped input may be research-derived but not yet linked to a specific evidence object
- a public report may be authoritative but still be secondary evidence
- a collaborator observation may be valuable but need provenance and role context
- an LLM-generated candidate may be well structured but not evidence-strong

Classify the entry state first. Then decide how to ingest, reconcile and review it.

## Entry states

### Raw source

A raw source is an original or near-original material item.

Examples:

- interview transcript
- workshop recording or notes
- survey export
- public report
- inspection report
- policy document
- service data export
- meeting notes

Default route:

```text
raw source
→ source or research-study record
→ selected evidence extracts
→ candidate objects
→ reconciliation
```

Use raw sources when the repository needs a clear provenance trail.

Do not import large raw document corpora directly into the structured intelligence repository unless there is a clear reason. Public raw or lightly processed source material should usually live in `civic-design-secondary-research`.

### Evidence extract

An evidence extract is a selected piece of material from a source that is useful for analysis.

Examples:

- anonymised quote
- transcript excerpt
- report paragraph
- survey free-text response
- observed behaviour note
- selected inspection finding

Default route:

```text
evidence extract
→ evidence object
→ candidate objects
→ reconciliation
```

Evidence extracts are useful when they can support or challenge user needs, civic needs, behaviours, pain points or insights.

Preserve enough source context to make the extract reviewable.

### Need-shaped input

A need-shaped input appears to express a user need, but has not yet been processed into a first-class user need object.

Examples:

- research-derived need summary
- workshop sticky note phrased as a need
- collaborator-proposed need
- LLM-generated draft need
- legacy note that looks like a need

Default route:

```text
need-shaped input
→ ingestion slice
→ candidate user needs and related objects
→ check against existing user needs
→ evidence/source linking where possible
→ create, link, update, defer or leave in inbox
```

Need-shaped inputs may be real and research-derived. They should not be dismissed as invalid because they are not yet fully evidence-linked.

They also should not be copied directly into canonical user need objects without reconciliation.

Check `docs/User_needs_writing_rules.md` before creating or changing any user need.

### Behaviour-shaped input

A behaviour-shaped input describes something a person, group or institution does, but has not yet been processed into a behaviour object.

Examples:

- parents repeatedly chasing for updates
- young people avoiding conversations about future options
- practitioners informally translating system language
- schools escalating late because support routes are unclear

Default route:

```text
behaviour-shaped input
→ candidate behaviour
→ check actor, trigger, context and frequency
→ link to needs, pain points and evidence
→ reconcile with existing behaviours
```

Check whether the material is really a behaviour, or whether it is a pain point, need, coping strategy, workaround or institutional process.

### Pain-point-shaped input

A pain-point-shaped input describes friction, harm, burden, risk, failure or blocked value.

Examples:

- families have to repeat information
- young people feel blamed for needing support
- deadlines are missed because responsibilities are unclear
- support depends on who a family happens to meet

Default route:

```text
pain-point-shaped input
→ candidate pain point
→ check affected actors, condition, impact and recurrence risk
→ link to evidence, needs and behaviours
→ reconcile with existing pain points
```

Do not overclaim severity. Severity is often relative and may require comparison with nearby pain points.

Resolved, dormant or recurring pain points may still be useful service intelligence.

### Civic-need-shaped input

A civic-need-shaped input points to an institutional obligation, public value, equity concern, rights issue, accountability gap or system duty.

Examples:

- people need access to statutory support without unequal navigation burden
- decisions need to be explainable and challengeable
- support should not depend on informal advocacy capacity
- public institutions need to prevent avoidable exclusion from future pathways

Default route:

```text
civic-need-shaped input
→ candidate civic need
→ check evidence basis and institutional obligation
→ link to user needs, pain points and public outcomes
→ human review before treating as stable
```

Civic needs should not be created casually from weak signals. They may emerge from patterns across user needs, evidence, pain points and statutory or public-value context.

### Insight-shaped input

An insight-shaped input explains a pattern, mechanism or meaning across evidence.

Examples:

- families interpret silence as abandonment because the pathway lacks visible progress signals
- planning burden increases when options are technically available but not practically comparable
- young people disengage when pathway conversations feel like decisions about them rather than with them

Default route:

```text
insight-shaped input
→ candidate insight
→ check supporting evidence and related objects
→ link to needs, behaviours, pain points and themes
→ mark review status conservatively
```

Insights need evidence and interpretation. Do not treat a single plausible statement as a validated insight without review.

### Theme-shaped input

A theme-shaped input groups related material without necessarily making a claim.

Examples:

- navigation burden
- trust and accountability
- post-16 planning uncertainty
- parent advocacy labour
- young person voice and agency

Default route:

```text
theme-shaped input
→ candidate theme or tag-like grouping
→ check whether it is organising material rather than asserting a finding
→ link to relevant objects
```

Themes are useful for organising, but they can become too vague. Do not use a theme where a more precise need, behaviour, pain point or insight is required.

### Collaborator observation

A collaborator observation comes from a practitioner, partner, third-sector organisation, parent forum, researcher or other informed contributor.

Examples:

- a practitioner reports recurring confusion about post-16 options
- a third-sector worker identifies a common gap in local support
- a parent group highlights repeated communication failures
- a professional notes that families rely on informal networks to navigate provision

Default route:

```text
collaborator observation
→ contribution or source note
→ provenance and role context
→ candidate evidence or object interpretation
→ reconciliation
→ review
```

Preserve who the observation represents, where it came from and whether it is direct experience, professional interpretation, synthesis or hearsay.

Do not treat collaborator observations as automatically representative.

### Public secondary source

A public secondary source is a published report, inspection, strategy, guidance, evaluation, literature review or dataset.

Examples:

- Ofsted area SEND inspection report
- local authority strategy
- government guidance
- parliamentary report
- research publication
- charity report

Default route:

```text
public secondary source
→ archive or reference source material
→ source record
→ selected evidence extracts
→ candidate objects
→ reconciliation
```

A secondary source should not directly become a user need.

Use conservative interpretation. A report finding may support a need or pain point, but it should not automatically validate one.

## Evidence voice

Where possible, identify whose voice or perspective the material represents.

Common categories:

- direct lived experience
- reported lived experience
- parent/carer perspective
- young person perspective
- practitioner perspective
- institutional perspective
- inspector or evaluator perspective
- third-sector perspective
- researcher synthesis
- policy or statutory framing
- operational data
- LLM-assisted synthesis

Evidence voice helps reviewers understand what can and cannot be claimed from the material.

## Evidence relationship to objects

Evidence may relate to objects in different ways.

Useful relationship types to observe, even if they are not formal schema fields yet:

- supports
- illustrates
- contextualises
- limits
- challenges
- contradicts
- broadens
- localises
- indicates recurrence
- indicates severity

Do not assume every evidence link means strong support.

For example, a quote may illustrate a pain point without proving that it is widespread. A report may contextualise a need without directly evidencing the lived experience wording.

## Default handling by input type

| Input type | Create source record? | Create evidence extract? | Create object directly? | Main risk |
|---|---:|---:|---:|---|
| Raw primary source | Usually | Selectively | No | privacy, over-extraction |
| Evidence quote/extract | If source exists or is needed | Yes | Candidate only | over-interpreting a small extract |
| Need-shaped input | Maybe later | Where possible | No, reconcile first | copying summaries into canonical needs |
| Behaviour-shaped input | Maybe | Where possible | Candidate only | confusing behaviour with pain or need |
| Pain-point-shaped input | Maybe | Where possible | Candidate only | overclaiming severity |
| Civic-need-shaped input | Usually useful | Where possible | Human review first | overclaiming institutional obligation |
| Insight-shaped input | Usually useful | Needed | Candidate only | treating synthesis as validated finding |
| Theme-shaped input | Not always | Not always | Maybe as theme | vague buckets replacing precise objects |
| Collaborator observation | Yes or contribution note | Maybe | Candidate only | representativeness and provenance |
| Public secondary source | Yes | Selectively | No | treating report findings as validated needs |

## Classification questions

Before ingesting material, ask:

1. What kind of input is this?
2. Whose voice or perspective does it represent?
3. Is it direct evidence, reported evidence, synthesis, interpretation or operational context?
4. What object types might it imply?
5. What existing objects might already cover this space?
6. What evidence or provenance is missing?
7. What should stay in the inbox?
8. What should not be created yet?
9. What needs human review?
10. What would be dangerous to overclaim?

## Maturity and traceability

Classifying input does not decide maturity.

Maturity depends on evidence basis, review state, confidence, stability, provenance and reconciliation with existing objects.

Use conservative metadata unless the object has been explicitly reviewed.

Do not mark objects as reviewed or validated simply because they came from a structured source, public report or plausible synthesis.

## Backward evidence-linking

Some material will enter before the source trail is complete.

Use backward evidence-linking when:

- a need-shaped summary is known to be research-derived but not linked to a specific extract
- a collaborator provides a synthesis before the underlying source material is available
- an older note contains useful knowledge but no source record
- a candidate object exists before its evidence basis is fully reconstructed

Backward evidence-linking should improve traceability without pretending the object is more mature than it is.

## Relationship to ingestion slices

Every ingestion slice should begin by classifying the input material.

The classification should appear in the reconciliation brief:

```markdown
## Input classification

Input type:
Evidence voice:
Source/provenance state:
Likely object types:
Main overclaiming risks:
```

Use this classification to choose the ingestion route and review questions.

## Guardrails

Do not:

- treat every input as direct evidence
- treat every source as equally strong
- treat synthesis as validation
- create user needs directly from public reports
- copy need-shaped input directly into canonical user needs
- collapse emotional, social or relational meaning into functional task language
- overclaim severity from one extract
- hide provenance gaps
- mark review or validation complete without human review

## Done criteria

Input classification is good enough when:

- the entry state is clear
- evidence voice is clear enough for review
- the likely object types are identified
- the main overclaiming risks are visible
- the ingestion route is chosen intentionally
- provenance gaps are explicit
- the material can move into an ingestion slice without pretending to be more mature than it is
