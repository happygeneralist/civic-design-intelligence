# Model-led ingestion operational correction

## Status

`operational correction — needs_review`

Related issues: #86 and #87  
Related PR: #88  
Related guidance:

- `docs/Non_linear_research_ingestion.md`
- `docs/Templates_and_maturity.md`
- `docs/Safe_research_ingestion_MVP.md`

## Purpose

Correct the follow-up sequencing proposed in the Essex evidence-to-object fit review and make an existing repository commitment operationally explicit.

The repository already allows useful partial knowledge, assumptive objects, research summaries, workshop outputs and analytical syntheses to enter before full source-to-evidence traceability exists.

The first Ofsted test used an evidence-led route because that route suited an inspection report. It must not become the default route for every input.

This note does not introduce a new conceptual model. It applies the existing non-linear ingestion model to coherent assumptive journey and service analyses.

## Correction to the Essex review

The Essex review says the preferred next contrast is direct lived-experience research.

That would be a useful later source, but it should not be treated as the prerequisite for the next step.

The better next operational test is the existing public-information journey analysis described by the repository owner. That analysis already combines:

- publicly available comments about lived experience;
- healthcare-professional or practitioner knowledge;
- analysis of the existing institutional and service system;
- analyst synthesis;
- assumptive journey phases or contexts.

The analysis should enter as a coherent provisional model. It should not first be dismantled and rebuilt from atomic evidence records.

Direct lived-experience research can then strengthen, challenge, split, reframe or disconfirm parts of that model.

## Two supported ingestion lanes

### Evidence-led ingestion

Use when a bounded source is the primary input and traceable extraction is the most useful starting point.

```text
source
-> source context
-> selected evidence
-> bounded interpretation
-> object reconciliation
-> candidate object changes
```

Examples include:

- inspection reports;
- research reports;
- Ombudsman decisions;
- datasets;
- policy or statutory material;
- individual research sessions with usable source records.

### Model-led ingestion

Use when a coherent analytical model, journey hypothesis, expert synthesis or partially structured body of knowledge already exists.

```text
existing model
-> preserve the whole artefact
-> document its mixed input basis
-> identify assumptions, evidence and inference
-> reconcile with existing repository objects
-> selectively structure useful components
-> expose gaps, tensions and contradictions
-> strengthen or revise progressively
```

Examples include:

- assumptive journey analyses;
- service or pathway models;
- workshop syntheses;
- practitioner-informed maps;
- public-information analyses;
- legacy research syntheses;
- models created before the repository existed.

Neither lane is inherently more legitimate. They begin from different input states and must preserve different risks.

## Preserve the whole model

A model-led ingestion pass must preserve the original analytical artefact before selective extraction or restructuring.

The original model provides value because it shows:

- the proposed whole shape;
- relationships among phases, contexts, needs, pain, mechanisms and outcomes;
- assumptions that may not be visible in isolated objects;
- gaps and contradictions;
- where institutional logic may have shaped the analysis;
- where later evidence changes the model.

The model should remain inspectable even if individual components are later revised or superseded.

Do not reduce a coherent model to disconnected objects and then discard the view that made the relationships visible.

## Minimum model record

The first pass should capture enough information to understand and use the model without pretending it is established knowledge.

Record:

- model title and purpose;
- author or contributors;
- date or period created;
- domain and scope;
- intended decisions or uses;
- source and input types;
- what is directly evidenced;
- what is practitioner-informed;
- what is analyst synthesis;
- what is assumed;
- whether phases are service-defined, lived-experience-informed or mixed;
- known limitations;
- review status;
- links to any later extracted or related objects.

This can begin as a working note or model record. It does not require a new first-class object type or schema before the test.

## Selective structuring, not wholesale atomisation

The model-led pass should identify which parts are useful to structure now.

Possible outcomes include:

- link an existing user need or pain point;
- create a conservative candidate object;
- identify a journey-pattern hypothesis;
- preserve a mechanism or service-context observation;
- record a contradiction;
- identify an evidence gap;
- leave material within the whole model until its boundary is clearer.

Not every phase, statement or relationship needs to become an object.

The aim is to increase useful coverage while preserving the model's coherence.

## Maturity and respect for different knowledge states

Ground-up, directly evidenced objects do not replace provisional models. Provisional models do not gain evidential authority merely by being comprehensive.

The repository should preserve the distinction between:

- a coherent assumptive model;
- a candidate object;
- an evidence-linked object;
- a human-reviewed interpretation;
- a validated or substantiated finding where that status is justified.

A provisional whole can be extremely useful for inspection, planning and research prioritisation even when many of its components remain assumptions.

The appropriate safeguard is visible maturity and provenance, not exclusion.

## Journey treatment

Assumptive journey phases may enter as a working design scaffold.

They should be marked as provisional and should not be treated as one universal linear path.

The model-led review should identify:

- service-defined phases;
- recurring lived-experience contexts;
- events and triggers;
- transitions;
- waits;
- loops and repeated attempts;
- parallel activities;
- changes in responsibility;
- escalation and recovery;
- emotional, agency and burden shifts;
- areas where phase boundaries are weak or contradictory.

Later evidence may confirm, merge, split, reorder or remove phases without invalidating the value of the original model as a historical analytical artefact.

## Operational responsibility for AI-assisted ingestion

Repository-aware agents must manage continuity across accepted guidance, issues and prior decisions.

Before recommending an ingestion route, an agent should inspect at least:

- `docs/Non_linear_research_ingestion.md`;
- `docs/Templates_and_maturity.md`;
- `docs/Safe_research_ingestion_MVP.md`;
- the relevant open ingestion and ontology issues;
- nearby existing models and objects.

An agent must not:

- infer that the most recently tested ingestion route is the only route;
- require the repository owner to repeatedly restate accepted non-linear-ingestion principles;
- discard or atomise a coherent existing model merely because its evidence chain is incomplete;
- silently narrow the repository operating model during a cautious source-ingestion test;
- treat direct lived-experience research as the only legitimate starting point;
- make an assumptive model look validated because it is coherent or comprehensive.

When an agent detects tension between current activity and existing repository commitments, it should:

1. state the tension;
2. check the authoritative guidance;
3. preserve the existing model and decisions;
4. propose the smallest correction;
5. record that correction in the relevant issue or PR;
6. avoid transferring the burden of continuity back to the user.

## Next operational test

Use the existing public-information assumptive journey analysis as the next non-linear ingestion test.

The test should:

1. preserve the source analysis as a coherent working model;
2. document its mixed input basis;
3. identify which phases are assumed, publicly evidenced, practitioner-informed or system-derived;
4. compare the model with existing CDI needs, pain points, behaviours and evidence;
5. identify useful candidate objects or links without requiring complete atomisation;
6. expose evidence gaps and contradictions;
7. show how the model can guide future research;
8. keep all new or changed interpretations at conservative maturity states;
9. leave direct lived-experience research as a strengthening and challenge route, not an entry gate.

## Acceptance conditions for the test

The model-led test is successful when:

- the original analytical model remains intact and findable;
- its assumptions and mixed evidence basis are visible;
- the repository gains useful shape rather than only isolated evidence records;
- extracted objects remain traceable to the model and any underlying sources;
- no unsupported status or confidence upgrade occurs;
- journey phases remain usable but explicitly provisional;
- the output identifies where further evidence would have the highest value;
- future agents can repeat the route without requiring the user to reconstruct this decision.

## What this note does not change

- No research object is created or modified.
- No evidence link is added.
- No object is reviewed or validated.
- No new ontology or schema field is introduced.
- No fixed journey hierarchy is adopted.
- The partial-fit findings about the Essex evidence and `PP_002` remain unchanged.
- Direct lived-experience research remains valuable; it is no longer framed as the required next entry route.
