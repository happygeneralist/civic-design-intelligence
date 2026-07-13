# Ofsted Essex delay ingestion slice plan

Status: proposed
Related issue: #91
Related workflow issue: #86
Related guardrail issue: #87
Source domain: SEND
Source locality: Essex

## Purpose

Define the next bounded evidence-led ingestion slice from the partially ingested Essex Ofsted/CQC Area SEND inspection source.

This planning note controls the source and interpretation boundary before a candidate evidence table is created. It does not create evidence records or change user needs, civic needs, pain points, behaviours, insights, themes, schemas or relationships.

The slice should help the repository learn through ingestion rather than waiting for a complete operating model.

## Source

### Source title

Area SEND inspection of Essex Local Area Partnership.

### Source type

Public Ofsted and Care Quality Commission area SEND inspection report.

This is institutional inspection evidence and synthesis. It is not direct lived-experience research and should not be treated as validated evidence of a user need on its own.

### Source archive

```text
happygeneralist/civic-design-secondary-research
sources/SRC_001_ofsted_essex_area_send_inspection_jan_2026/
```

Primary archive candidate:

```text
Extract 002 in extracts.md
```

### Primary source location

```text
Page 2
Section: What is it like to be a child or young person with special educational needs and/or disabilities (SEND) in this area?
```

The relevant paragraph states, in summary, that:

- delays in assessment of needs create inconsistent experiences and outcomes;
- EHC plan timeliness is poor;
- some children and young people wait too long for appropriate provision and support from some services;
- many families are dissatisfied because of these delays.

### Limited wider-source context

The candidate evidence review may inspect the page 5 material stating that:

- too few EHC plans are issued within the statutory timeframe;
- the report attributes the main cause of EHC plan delays to challenges recruiting educational psychologists;
- delays create inconsistencies in support.

This context is included only to clarify the EHC-plan delay claim and the source's own causal or consequence assertions. It does not open the whole page 5 problem cluster to ingestion.

## Slice name

```text
Delays in assessment of needs, EHC plans, provision and support
```

The wording deliberately uses `assessment of needs` rather than automatically relabelling the first source claim as `EHC needs assessment delay`.

The candidate evidence review must confirm whether the wider source supports that narrower interpretation. If it does not, preserve the source's broader wording.

## Included claim units

Treat the following as separate candidate claim units unless the source itself clearly binds them:

1. **Assessment delay** — delays in assessment of needs exist in the Essex SEND context.
2. **Assessment consequence synthesis** — the inspection says these delays create inconsistent experiences and outcomes.
3. **EHC plan delay** — EHC plan timeliness is poor.
4. **Statutory-timeframe manifestation** — too few EHC plans are issued within the statutory timeframe.
5. **Provision wait** — some children and young people wait too long for appropriate provision.
6. **Support wait** — some children and young people wait too long for support from some services.
7. **Family dissatisfaction** — the report associates family dissatisfaction with these delays.
8. **Source-attributed contributor** — recruitment challenges affecting educational psychologists are presented by the report as the main cause of EHC plan delays.
9. **Support inconsistency consequence** — the report says delays create inconsistencies in support.

The candidate evidence table may combine provision and support only if the exact source wording does not allow them to be represented faithfully as separate claims.

## Excluded material

Do not include, except for a minimal sentence of limiting context where necessary:

- neurodevelopmental assessment waits;
- unequal access to health services by locality;
- speech and language assessment or therapy access;
- emotional wellbeing and mental health waits;
- EHC plan quality, accuracy or professional input;
- communication while waiting, already handled by the first bounded slice;
- families needing to push hard for support;
- mediation, tribunal, Ombudsman complaints or escalation routes;
- preparation for adulthood;
- alternative provision;
- leadership, governance or strategy recommendations;
- the whole report-level `inconsistent experiences and outcomes` judgement;
- national or cross-locality prevalence, severity or causal claims.

Do not infer that assessment delay, EHC plan delay, provision delay and support delay form one chronological sequence.

## Why this boundary is useful

The source paragraph is small enough to review, but contains several different claims and evidential functions.

It can test whether the repository can:

- split a source-bundled statement without distorting it;
- distinguish an observed condition from inspection synthesis;
- preserve a statutory mechanism as context without turning it into an enduring need;
- distinguish local existence from prevalence and severity;
- record source-asserted causation separately from analyst inference;
- decide whether one broad delay pain point would preserve or flatten meaning;
- avoid creating a user need merely because a statutory process is late.

## Nearby-object reconciliation completed for planning

The planning review inspected the most relevant existing objects identified by the first Ofsted fit review.

### `PP_002`: parent carries pathway navigation burden

The existing evidence-to-object review concluded that the first communication evidence set supports only parts of this broad pain point.

The new delay slice may provide contextual evidence about conditions that increase burden, but delay is not automatically the same condition as navigation burden. Do not link new evidence to `PP_002` without claim-level reasoning.

### `UN_015`: coordinate pathway next steps

This need remains an unsupported candidate. Delay evidence may make the need plausible, but the inspection source does not directly establish that the central user action is coordinating next steps or carrying planning work.

Do not add an evidence link by default.

### `UN_007`: reconcile pathway information

Delay is not evidence that people must reconcile conflicting or partial information. No direct fit is currently apparent.

### `UN_010`: deprecated bundled pathway-planning need

Use only as lineage and a warning against bundling process, rights, information and confidence into one need. Do not restore or link it.

### `BEH_009`: chases pathway support

The included delay material does not directly establish chasing or recontact behaviour. The `push hard` material that may support this behaviour is explicitly outside the slice.

### Other pain points, insights and civic needs

The repository currently has no obvious delay-specific pain point or insight and no established civic-need object that should receive these claims directly.

The candidate evidence review must repeat a lightweight nearby search before recommending creation. Absence of an obvious object does not itself justify a new one.

## Questions for the candidate evidence review

### Claim separation

- Does the report support assessment, plan, provision and support delay as distinguishable conditions?
- Is `assessment of needs` specifically an EHC needs assessment claim, or broader inspection wording?
- Are provision and support two useful claim units, or one source-bundled finding?

### Evidence strength and meaning

- Which statements are direct inspection findings?
- Which are inspection synthesis?
- Which are source-attributed consequences, associations or causes?
- Does the source establish existence only, or provide meaningful evidence about severity or prevalence?
- What is limited by terms such as `some`, `many`, `too few` and `poor` where no denominator is given?

### Object fit

- Does any claim directly, partially or contextually support `PP_002`?
- Is a new delay pain point necessary, or would it wrongly collapse distinct conditions?
- Is there enough evidence for an action-oriented user need about what a child, young person or family needs to achieve while formal processes remain incomplete?
- Does the evidence only expose a research question about maintaining access to suitable support during institutional delay?
- Does the material point towards a civic condition around timeliness, continuity, protection from avoidable harm or equitable access without yet supporting a mature civic need?

### Mechanism context

- Which parts belong specifically to the EHC statutory mechanism?
- What more durable human or civic condition may be visible through that mechanism?
- How can the mechanism remain inspectable without defining the canonical need or pain point?

## Expected evidence types

Candidate entries may be classified as:

- inspection finding;
- inspection synthesis;
- local manifestation;
- statutory-mechanism context;
- source-attributed consequence;
- source-attributed association;
- source-asserted causal contributor;
- contextual or limiting evidence.

These classifications are review descriptions, not a new schema or controlled vocabulary.

## Candidate object treatments

For each candidate evidence item, consider:

- create a selected evidence record;
- link to an existing object directly, partially or contextually;
- update an existing object only after material fit review;
- challenge or qualify an existing object;
- propose a new narrow pain point;
- propose an action-oriented user need for later testing;
- record a candidate insight with inference clearly separated;
- record a civic-condition question for later theory work;
- keep as evidence only;
- defer.

Not every source sentence needs a knowledge object.

## User-need safeguard

Do not formulate a user need as:

- receiving an EHC plan on time;
- completing an EHC needs assessment;
- meeting a statutory timeframe;
- accessing a named administrative process;
- making the local authority comply.

These are mechanisms, entitlements or service conditions.

A candidate user need is appropriate only if the evidence supports what a person needs to achieve, preserve, recover or change in context. The candidate table should defer formulation where the inspection voice does not reveal the underlying action clearly enough.

## Civic-need safeguard

Do not convert the inspection judgement or statutory duty directly into a civic need.

The source may help expose questions about:

- protection from avoidable harm during delay;
- continuity of suitable support;
- equitable access to assessment, planning and provision;
- accountability where public processes remain incomplete;
- reducing dependence on family persistence or capacity.

These remain questions until the normative basis, affected people, public obligation, outcome at risk and mechanism relationship are sufficiently developed.

## Public/private method boundary

The public plan and candidate evidence table may include:

- source locations;
- faithful extracts or paraphrases;
- claim boundaries;
- nearby-object checks;
- public-safe interpretation rationale;
- uncertainty;
- create, link, update, challenge or defer recommendations;
- concrete questions exposed for #86 or #87.

Do not include:

- protected prompts or prompt chains;
- detailed scoring or diagnostic rubrics;
- ontology-navigation logic;
- reusable private orchestration routines;
- tool-specific protected runbooks;
- private scratch reasoning not needed to inspect the public decision.

Open work in `design-intelligence-orchestration#10` only if the slice exposes a concrete judgement that cannot be handled through existing public reasoning and human review.

## Candidate evidence table requirements

For each candidate item, record:

- candidate ID;
- precise source location;
- exact extract or faithful paraphrase;
- claim type;
- actor scope;
- locality and service context;
- what the item directly supports;
- what it does not support;
- possible nearby object;
- create, link, update, challenge or defer recommendation;
- confidence and uncertainty;
- whether a public modelling issue or protected-rubric question was exposed.

The table should contain no more than 5 to 8 useful candidate entries.

## Stop or shrink conditions

Stop or narrow the slice if:

- more than 8 candidate evidence entries are needed;
- the work starts importing the whole report delay landscape;
- `assessment of needs` cannot be interpreted without pulling in unrelated assessment pathways;
- provision and support cannot be separated without rewriting the source;
- the analysis starts treating all four delay claims as one causal sequence;
- a proposed object requires the excluded escalation, communication, health-equity or plan-quality evidence to make sense;
- a candidate user need remains mechanism-defined;
- a new pain point is being proposed before the nearby-object check is complete;
- severity, prevalence or causation would need to be inferred beyond the source;
- public rationale would require publication of protected method.

Fallback boundary:

```text
Assessment-of-needs delay and EHC-plan timeliness only.
```

If the fallback is used, retain the provision-and-support sentence as one deferred source-bundled candidate rather than forcing a split.

## Acceptance criteria

- [ ] The candidate review stays within the included claim units.
- [ ] Assessment, plan, provision and support delay are not automatically collapsed.
- [ ] The meaning of `assessment of needs` is checked rather than silently narrowed.
- [ ] Direct findings, synthesis, associations, consequences and source-asserted causes remain distinguishable.
- [ ] Existing objects are checked before creation or linking.
- [ ] Mechanism context remains visible without defining enduring user or civic needs.
- [ ] No national prevalence, severity or causal claim is made.
- [ ] No object is marked reviewed or validated.
- [ ] The candidate evidence table precedes structured evidence and object changes.
- [ ] Any workflow finding is routed to #86, #87, orchestration #10 or the source archive according to type.

## Expected PR sequence

1. This slice-plan PR.
2. A candidate-evidence-table PR with no knowledge-object changes.
3. A selected-evidence PR, including the companion evidence-map update.
4. A separate optional object-maintenance PR only where direct fit is sufficiently strong.
5. A separate optional guidance correction only where the worked example exposes a concrete repeated or unsafe ambiguity.

## What this plan does not do

This plan does not:

- ingest the whole Ofsted report;
- create evidence records;
- create or change user needs, civic needs, pain points, behaviours or insights;
- create a new delay taxonomy or hierarchy;
- change the schema, templates or validators;
- treat the EHC mechanism as the enduring need;
- mark anything reviewed or validated;
- expose protected orchestration method;
- authorise merge, closure or any other finalising action.
