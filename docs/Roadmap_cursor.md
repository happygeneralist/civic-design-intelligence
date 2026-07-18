# Roadmap cursor

Last updated: 2026-07-13

This cursor records the current operational focus for the repository.

It is intentionally shorter than the full roadmap. Use it to decide what to do next, what to avoid overbuilding and when the roadmap has moved to a new phase.

Where the sequencing in `docs/Knowledge_evolution_implementation_roadmap.md` conflicts with this cursor, use this cursor as the current operating position.

## Current phase

The repository is now in:

```text
learning through bounded ingestion
```

The minimum public/private boundary exists at MVP level. The documentation authority map and provisional inventory exist. One bounded evidence-led Ofsted Essex ingestion route has been planned, run and reviewed.

The repository should not return to a pre-ingestion readiness phase while every governance, ontology, documentation or orchestration question is resolved.

The current operating loop is:

```text
bounded ingestion
-> inspect what becomes difficult, ambiguous or unsafe
-> capture the issue
-> make the smallest necessary operating correction
-> continue with the next bounded slice
```

Slow, bounded ingestion is the primary way to discover the real requirements for safer and faster ingestion.

## Current repository position

Completed or sufficiently established for continued bounded ingestion:

- whole-system framing, with SEND pathway planning as the initial worked domain rather than the limit of the repository;
- public-source and evidence-handling guidance;
- issue-first practice for non-trivial work;
- documentation authority guidance and a provisional documentation inventory;
- an MVP public/private boundary between this repository and `happygeneralist/design-intelligence-orchestration`;
- public-safe summaries for higher-risk prompt, workflow and user-needs quality material;
- a companion public secondary-research source archive;
- the first bounded Ofsted Essex communication-while-waiting slice;
- one source record, five evidence records and a cautious link to an existing pain point;
- an evidence-to-object fit review that identified partial rather than wholesale support;
- public non-linear ingestion guidance that supports evidence-led, object-led and model-led entry routes.

The first Ofsted source remains partially ingested. The completed first slice is a worked example, not a universal sequence and not evidence that the operating model is finished.

## Active focus

The current focus is:

```text
Continue slow, reviewable ingestion and evolve the operating guidance from repeated examples.
```

This means:

- treat issue #86 as the active workflow-learning umbrella;
- use issue #87 for public evidence-context-object and non-linear journey guardrails exposed through real ingestion;
- keep `design-intelligence-orchestration#10` available for concrete protected judgement or review-rubric needs, without making it an ingestion prerequisite;
- keep `design-intelligence-orchestration#8` ready as a lightweight private roadmap/boundary task, but do not treat it as an ingestion blocker;
- keep issue #89 as a separate model-led journey-view test rather than allowing it to displace the next evidence-led slice;
- update public guidance only where an ingestion example exposes a repeated, material or unsafe ambiguity;
- continue using small issues and PRs so source selection, evidence interpretation and semantic changes remain reviewable.

## Immediate next actions

1. Put issue #86 into active work on the portfolio Project.
2. Keep issue #87 ready as supporting work generated through ingestion.
3. Run issue #91 as the next bounded Ofsted Essex slice, focused on delays in assessment, EHC plans, provision and support.
4. Create a slice plan that separates the source's bundled claims and defines stop or shrink conditions.
5. Create a candidate evidence table before creating or changing knowledge objects.
6. Create selected evidence records and update the secondary-research evidence map only after the candidate set has been reviewed.
7. Make object changes only where nearby-object reconciliation shows a sufficiently direct fit.
8. Route any concrete workflow or modelling difficulty to the existing umbrella issue that owns it, then continue ingestion.

## Boundary for the next evidence-led slice

The next slice should use Extract 002 from:

```text
happygeneralist/civic-design-secondary-research
sources/SRC_001_ofsted_essex_area_send_inspection_jan_2026/extracts.md
```

Working slice:

```text
Delays in EHC needs assessments, EHC plans, provision and support
```

The work must distinguish rather than automatically combine:

- delays in assessment of needs;
- poor EHC plan timeliness;
- waits for appropriate provision;
- waits for support from some services;
- inconsistent experiences and outcomes as inspection synthesis;
- family dissatisfaction as a source-attributed consequence or association.

Do not assume these claims form one pain point, one user need or one causal chain.

Keep neurodevelopmental waits, health-access inequality, EHC plan quality, communication while waiting, escalation and preparation for adulthood outside this slice unless a small amount of context is necessary to interpret the included claims.

## Operating guidance during ingestion

For each bounded slice:

- inspect the selected source material and wider source context needed to interpret it accurately;
- inspect nearby user needs, civic needs, pain points, behaviours, insights and views before proposing a new object;
- create a candidate evidence table before structured evidence or semantic object changes;
- identify what each item supports and does not support;
- distinguish existence, manifestation, consequence, severity, prevalence, association and causation;
- preserve service, policy, statutory and administrative mechanisms as context rather than defining enduring needs through them;
- keep local evidence local while allowing it to support a reusable object cautiously;
- use conservative states such as `captured`, `candidate`, `draft` and `needs_review`;
- do not mark anything human reviewed or validated without explicit human instruction;
- preserve whole artefacts where their relationships carry meaning, but do not force every input through whole-model preservation;
- keep public outputs independently inspectable without publishing detailed private orchestration method.

## Public and private operating boundary

The public repository should continue to contain:

- open civic and design intelligence knowledge objects;
- public source, evidence, status, review and contribution guidance;
- public-safe reasoning needed to inspect source boundaries, evidence claims and object decisions;
- source records, selected evidence records and conservative analysis objects;
- reduced public guidance where repeated examples justify it.

The private orchestration repository should continue to contain protected material such as:

- detailed prompts and prompt chains;
- scoring or diagnostic rubrics;
- ontology and navigation logic;
- reusable orchestration routines;
- tool-specific runbooks and model preferences;
- protected review methods that are not required to inspect public outputs.

Unfinished private method does not block a bounded public ingestion slice unless that slice genuinely depends on the missing protected capability.

## Guardrails for the next PRs

For the next few PRs:

- keep PRs small and reviewable;
- do not combine roadmap correction, candidate evidence, structured evidence and semantic object changes in one PR;
- do not expand the schema, relationship vocabulary or validator rules from one example;
- do not create a new object where an existing object is a direct enough fit;
- do not link evidence to an object as though it supports the whole object when it supports only one aspect;
- do not turn inspection findings or recommendations directly into validated user or civic needs;
- do not make national prevalence, severity or causal claims from one local inspection source;
- do not publish detailed protected orchestration method;
- do not import large raw research corpora into this repository;
- do not merge, close, delete, supersede or otherwise finalise work without explicit instruction.

## Things that remain deferred

These are important, but not prerequisites for the next bounded slices:

- high-volume or automatic ingestion;
- automated semantic decisions;
- broad schema expansion;
- enforced typed relationships;
- a full mechanism ontology;
- a full locality, service-area or organisation taxonomy;
- strict validator enforcement across all objects;
- physical documentation folder restructuring without a concrete navigation need;
- full documentation consolidation;
- automated cross-repository synchronisation;
- API or database implementation;
- canonical personas or fixed journey maps;
- a dedicated need-pattern object type;
- a formal causal or theory-of-change layer;
- final licensing or commercial-model decisions beyond the current protection guardrail.

## Decision rule

When deciding what to do next, prefer work that answers:

- What did the latest bounded ingestion example make difficult, ambiguous or unsafe?
- Is the problem local to this source or repeated enough to require operating guidance?
- Can the problem be handled through a note or small correction before adding schema or tooling?
- Can the next slice continue safely without resolving the wider theory question now?
- Does the proposed change preserve meaning, provenance, uncertainty and human control?
- Does it keep the public output auditable while protected method remains private?

If a proposed change does not help the next bounded slice, correct a demonstrated ingestion problem or protect repository integrity, defer it.

## Next review point

Review this cursor after issue #91 has produced:

1. an agreed slice plan;
2. a candidate evidence table;
3. selected evidence records or an explicit decision to defer them;
4. a record of any workflow, modelling or protected-method difficulty exposed by the slice.

At that point, decide whether the next step should be:

- another bounded slice from the same Ofsted source;
- a contrasting source;
- the model-led journey-view test in #89;
- a small object-maintenance PR;
- a narrow public-guidance correction;
- a concrete protected-rubric task in `design-intelligence-orchestration#10`.
