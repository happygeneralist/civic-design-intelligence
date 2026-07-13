# Candidate evidence table: Ofsted Essex delay slice

Status: candidate evidence review — needs_review
Related issue: #91
Related workflow issue: #86
Related guardrail issue: #87
Follows proposed plan: `docs/ingestion-slices/ISSUE_091_ofsted_essex_delay_slice_plan.md`
Source domain: SEND
Source locality: Essex

## Scope

This note reviews only the bounded delay slice:

```text
Delays in assessment of needs, EHC plans, provision and support
```

It does not create evidence records or change user needs, civic needs, pain points, behaviours, insights, themes, schemas or relationships.

The purpose is to identify the smallest useful evidence set while preserving the different claims and evidential functions bundled by the inspection report.

## Source

Source title: Area SEND inspection of Essex Local Area Partnership

Source type: Public Ofsted and Care Quality Commission area SEND inspection report

Inspection dates: 19 January 2026 to 23 January 2026

Source archive:

```text
happygeneralist/civic-design-secondary-research
sources/SRC_001_ofsted_essex_area_send_inspection_jan_2026/
```

Primary archive candidate:

```text
Extract 002 in extracts.md
```

## Source-status note

This is institutional inspection evidence and synthesis, not direct lived-experience research.

The report can support local evidence about delay conditions, source-attributed consequences and source-asserted contributors. It must not be treated as direct validation of a user need, national prevalence, national severity or a complete causal chain.

## Nearby-object and evidence search

The planning review inspected:

- `PP_002_parent_carries_pathway_navigation_burden`;
- `UN_015_need_to_coordinate_next_steps`;
- `UN_007_reconcile_pathway_information`;
- deprecated `UN_010_consider_steps_rights_adjustments` as lineage only;
- `BEH_009_chases_pathway_support`;
- the first Ofsted evidence-to-object fit review;
- existing evidence records from the communication-while-waiting slice.

### Existing evidence overlap

`EVID_003_ofsted_essex_communication_support_available` already preserves the page 5 issue-cluster extract that includes:

```text
the timeliness of EHC needs assessments
```

Its title, tags and interpretation were written for the communication slice, but the underlying quoted extract also contains an EHC needs-assessment timeliness claim.

Do not create a duplicate evidence record for the same page 5 statement merely because the new slice is organised around delay.

The candidate review should instead decide whether:

- the existing evidence record can be reused with a clearly bounded relationship;
- a later evidence-maintenance note should clarify that the record contains several claim components;
- the existing record should remain communication-focused while a separate non-duplicative extract is used for delay;
- evidence granularity needs a public guardrail under #87.

No evidence or metadata change is made in this table.

## Candidate evidence table

| ID | Source location | Exact extract or faithful paraphrase | Claim type | Actor scope and context | What it directly supports | What it does not support | Nearby-object fit | Recommendation | Confidence and uncertainty | Operating question exposed |
|---|---|---|---|---|---|---|---|---|---|---|
| CEE-DL-001 | Page 2, opening paragraph under `What is it like...` | `Delays in the assessment of needs create inconsistent experiences and outcomes for children and young people with SEND in Essex.` | Inspection synthesis; source-asserted consequence | Children and young people with SEND; Essex; assessment of needs | The inspection identifies assessment delay in Essex and asserts a relationship with inconsistent experiences and outcomes. | It does not specify which assessment route, quantify delay, isolate the affected group, provide direct lived-experience evidence or establish a national pattern. It does not prove that every inconsistency is caused by delay. | No direct fit with `PP_002`, `UN_015`, `UN_007` or `BEH_009`. Possible evidence for a future narrow delay condition or insight. | **Create selected evidence.** Preserve `assessment of needs` rather than silently narrowing it to EHC needs assessment. Do not link to an interpreted object yet. | Medium. The source claim is explicit, but broad and synthesised. The scope and causal strength are not explained. | #87: how should one evidence record distinguish existence of delay from the source's asserted consequence? |
| CEE-DL-002 | Page 2, same paragraph | `The timeliness of education, health and care (EHC) plans is poor.` | Inspection finding; local manifestation | Children and young people whose support involves EHC plans; Essex; statutory planning context | The inspection directly judges EHC plan timeliness to be poor in Essex. | It does not provide a denominator, duration, distribution, cause, direct user experience, individual consequence or national comparison. | No direct existing object fit. It may later support a mechanism-specific pain manifestation, but not a user need framed as receiving an EHC plan on time. | **Create selected evidence.** Keep the EHC plan mechanism explicit in evidence context. Defer pain-point or civic-need creation. | Medium-high for local existence; low for prevalence, severity and consequence. | No new issue. This is a straightforward mechanism-specific evidence item. |
| CEE-DL-003 | Page 2, same paragraph | `Some children and young people wait too long to receive appropriate provision and support from some services.` | Inspection finding; source-bundled condition | Some children and young people with SEND; Essex; unspecified services and provision | Some children and young people wait too long for appropriate provision and support from some services. | It does not identify which services, distinguish provision from support, quantify `some`, describe duration, show what is unavailable during the wait or establish a single pathway sequence. | No direct fit with `PP_002`; delay may create burden but is not navigation burden itself. Potential basis for a new narrow pain point only after evidence review. | **Create one selected evidence record preserving the bundle. Do not split it into separate provision and support records from this sentence alone.** | Medium. The finding is direct but deliberately non-specific. | #87: planned analytical categories must not force one source sentence into false atomisation. |
| CEE-DL-004 | Page 2, same paragraph | `Many families are dissatisfied because of these delays.` | Source-asserted consequence and causal attribution | Families of children and young people with SEND; Essex; antecedent delay cluster in the paragraph | The inspection attributes family dissatisfaction to the delays described immediately before it. | It does not show which delay contributes most, provide direct family accounts, quantify `many`, establish the mechanism of dissatisfaction or support a broader claim about family burden. | Does not directly support `PP_002`, because dissatisfaction is not evidence of navigation burden. No user-need fit. | **Create selected evidence as a bounded source-attributed consequence.** Keep the antecedent as the paragraph's delay cluster rather than assigning the consequence to one delay type. | Medium. The causal wording is explicit in the report, but the underlying evidence and contribution of each delay are not visible. | #87: evidence links may need to preserve a consequence attached to a cluster without implying that every component has equal causal support. |
| CEE-DL-005 | Page 5, first improvement finding | Faithful paraphrase: the report identifies EHC needs-assessment timeliness as one of several long-term issues underlying much family dissatisfaction. | Inspection synthesis; issue-cluster context | Families; children and young people with SEND; Essex; EHC needs assessment alongside excluded neurodevelopmental and communication issues | EHC needs-assessment timeliness is explicitly identified elsewhere in the report as a long-term issue connected to family dissatisfaction. | It does not prove that page 2's broader `assessment of needs` phrase refers only to EHC needs assessments. It does not isolate EHC assessment timeliness from the other issues in the cluster. | The exact source statement already exists in `EVID_003`. No new object fit follows automatically. | **Reuse or reference existing `EVID_003`; do not create duplicate evidence.** Consider a later evidence-maintenance decision only if the communication-focused interpretation prevents safe reuse. | High that the source names EHC needs-assessment timeliness; medium-low for isolated consequence because the statement is bundled. | #87: how should a multi-claim evidence record be reused across slices without duplicating evidence or implying whole-record support? |
| CEE-DL-006 | Page 5, EHC plan timeliness finding | `Too few EHC plans are issued within the statutory timeframe.` | Inspection finding; statutory-timeframe manifestation | Children and young people whose support involves EHC plans; Essex; statutory planning mechanism | The inspection identifies underperformance against the statutory timeframe as a concrete manifestation of poor EHC plan timeliness. | It does not provide the proportion, trend, duration beyond the timeframe, affected subgroups, lived consequence or national comparison. | No direct current object fit. It can qualify CEE-DL-002 and may later support a narrow mechanism manifestation. | **Create selected evidence.** Keep separate from CEE-DL-002 because this is a more concrete statutory manifestation, while avoiding duplicate object links. | Medium-high for existence; low for scale and consequence. | #86: later object review should test whether high-level and concrete manifestations need separate evidence records or one grouped source note. |
| CEE-DL-007 | Page 5, same finding | `The main cause of delays has been challenges with the recruitment of educational psychologists.` | Source-asserted causal contributor; operational context | Essex partnership; educational psychologists; EHC plan process | The report asserts that educational-psychologist recruitment challenges have been the main cause of the EHC plan delays discussed in this paragraph. | It does not expose the causal analysis, rule out other contributors, establish future persistence or support a general claim that workforce shortages cause all assessment or support delays. | This is mechanism and operational context, not a user need, pain point or civic need by itself. | **Defer as a separate evidence record for now.** Preserve it in source context for CEE-DL-006. Create separately only if later causal or operational analysis requires traceable treatment. | Medium. The attribution is explicit but not independently tested in the report text. | `design-intelligence-orchestration#10` is not yet needed; ordinary source-attribution notes are sufficient. |
| CEE-DL-008 | Page 5, same finding | `The delays create inconsistencies in the support for children and young people.` | Source-asserted consequence | Children and young people with SEND; Essex; EHC plan-delay paragraph | The report asserts that the EHC plan delays described in the paragraph create inconsistencies in support. | It does not specify the form of inconsistency, identify affected services, quantify prevalence, describe user experience or establish that every support inconsistency arises from EHC plan delay. | No direct fit with `PP_002`. Potential future insight or narrow pain manifestation, but the source does not yet reveal the underlying lived-experience condition. | **Create selected evidence.** Keep the consequence bounded to the EHC plan-delay paragraph. Defer insight and pain-point creation. | Medium. The source assertion is clear, but its mechanism and manifestation are not detailed. | #87: evidence-to-object links must preserve source-bounded causal scope. |

## Candidate-set decision

The proposed selected set is:

1. CEE-DL-001 — assessment-of-needs delay and source-asserted inconsistency.
2. CEE-DL-002 — poor EHC plan timeliness.
3. CEE-DL-003 — bundled wait for appropriate provision and support.
4. CEE-DL-004 — family dissatisfaction attributed to the delay cluster.
5. CEE-DL-006 — too few EHC plans within the statutory timeframe.
6. CEE-DL-008 — source-asserted inconsistency in support caused by EHC plan delays.

Treat CEE-DL-005 through the existing `EVID_003` record rather than duplicating the source statement.

Defer CEE-DL-007 as separate structured evidence unless a later causal or operational analysis needs it. Preserve the source attribution as context for CEE-DL-006.

This produces six new evidence candidates, one existing-evidence reuse question and one deferred causal-context item.

## Claim-boundary conclusions

### Assessment delay is not yet safely identical to EHC needs-assessment delay

Page 2 uses the broader phrase `assessment of needs`.

Page 5 separately identifies EHC needs-assessment timeliness as a long-term issue. This makes an EHC interpretation plausible, but does not prove that the page 2 claim is exclusively about that mechanism.

Create the page 2 evidence using the source's broader wording. Reuse `EVID_003` where the explicit EHC needs-assessment claim is needed.

### Provision and support should remain bundled in the selected evidence

The page 2 sentence does not tell us whether `provision` and `support` are distinct categories, overlapping descriptions or one combined phrase.

Splitting the sentence into two records would imply a distinction the source does not evidence. Preserve one evidence item and defer any object-level separation until another source or more specific report material supports it.

### Delay conditions should not become one pain point by default

The source contains at least three different types of condition:

- assessment-of-needs delay;
- EHC plan timeliness failure;
- waiting for appropriate provision and support.

It also contains two different source-attributed consequences:

- inconsistent experiences and outcomes;
- dissatisfaction and inconsistent support.

One broad `SEND delays` pain point would be easy to create but would flatten mechanism, affected actor, consequence and possible remedy differences.

Do not create a pain point in the evidence PR.

### The existing broad navigation-burden pain point is not the default destination

Delay can increase family work or uncertainty, but the selected statements do not directly evidence:

- navigation work;
- repeated chasing;
- coordination burden;
- unclear routes;
- family responsibility for keeping activity moving.

Do not link the proposed evidence records to `PP_002` without a later material fit review.

## User-need assessment

The source does not directly support a stable action-oriented user need.

A possible research hypothesis is that children, young people and families need to maintain access to appropriate support and continue responding to needs while formal assessment and planning remain incomplete.

That formulation is not ready for creation because the inspection does not show:

- whose action is central;
- what people are trying to achieve during the wait;
- whether the enduring need is continuity, access, agency, protection, adaptation or something else;
- how children and young people's own actions differ from family or institutional responsibilities.

Recommendation: **defer user-need creation** and use the evidence to shape later research or comparison.

Do not formulate a need as receiving an EHC plan or assessment within a statutory timeframe. Those are mechanisms and public obligations, not the underlying user action.

## Civic-condition assessment

The evidence points towards a possible civic condition:

```text
Public assessment and planning delays should not leave children and young people without timely, appropriate and sufficiently consistent support.
```

This is a question for civic-needs development, not a mature civic-need object.

The current source can support:

- local institutional relevance;
- the existence of delay and support inconsistency;
- the inspection's attribution of consequences.

It does not settle:

- the normative basis;
- the enduring capability or protection;
- the distribution of institutional responsibility;
- the relationship between timeliness, continuity, equity and prevention of harm;
- the scope beyond Essex and the current EHC mechanism.

Recommendation: **defer civic-need creation**. Route deeper theory questions to `happygeneralist/Happygeneralist#11` only when a concrete formulation task is ready.

## Candidate insight assessment

A possible later insight is:

```text
Delay at different institutional points can produce different forms of inconsistency, so assessment, planning and access-to-support delays should not be treated as one interchangeable waiting-time problem.
```

This is analyst synthesis across the selected report statements. It is potentially useful, but it should not become an insight object from one local inspection source without comparison or direct lived-experience evidence.

Recommendation: **defer insight creation**.

## Evidence-record recommendations

A later selected-evidence PR should:

- create six evidence records from CEE-DL-001, 002, 003, 004, 006 and 008;
- keep each record at `captured` / `needs_review` or current equivalent;
- avoid related user need, civic need, behaviour, pain point or insight links unless separately justified;
- preserve the Essex locality and inspection-report basis;
- distinguish inspection synthesis from direct finding and source-asserted consequence;
- reference `EVID_003` rather than duplicating the page 5 long-term issue-cluster extract;
- keep CEE-DL-007 as source context unless separate traceability becomes necessary;
- update the companion `evidence-map.md` only when the new CDI evidence records exist.

## Public modelling findings for #87

This candidate review exposes two concrete guardrail questions:

1. **Source-bundled evidence should not be atomised to match planned analytical categories.** The `provision and support` sentence should remain one evidence unit until another source supports a meaningful split.
2. **A multi-claim evidence record may need reuse across bounded slices.** `EVID_003` already contains an EHC needs-assessment timeliness claim inside a communication-focused record. The repository needs a lightweight way to reuse the supported claim without duplicating the evidence or implying that every part of the record supports every linked object.

These questions belong under #87. They do not yet justify schema or relationship-type changes.

## Protected-method finding

No new protected rubric task is required from this review.

The distinctions were manageable through public source attribution, nearby-object checks and explicit uncertainty. Keep `design-intelligence-orchestration#10` in backlog unless later object selection exposes a judgement that cannot be handled this way.

## Validation status

Nothing in this table is human reviewed or validated.

No knowledge object, evidence strength, confidence, maturity or lifecycle state has changed.

The expected next step is a separate selected-evidence PR only after this candidate set is accepted or revised.
