# Candidate evidence table: Ofsted Essex communication while waiting slice

Status: candidate evidence table
Related issue: #79
Related execution-model issue: #80
Follows slice plan: `docs/ingestion-slices/ISSUE_079_first_ofsted_send_ingestion_slice_plan.md`
Source domain: SEND pathway planning
Source locality: Essex

## Scope

This note analyses only the agreed bounded slice:

```text
Communication with families while waiting for assessments or services.
```

It does not create evidence objects, user needs, civic needs, pain points, insights, themes or service-context objects.

It selects candidate extracts that may later be converted into structured evidence or used to support, qualify or challenge existing CDI objects after reconciliation.

## Source

Source title: Area SEND inspection of Essex Local Area Partnership

Source type: Public Ofsted and Care Quality Commission area SEND inspection report

Inspection dates: 19 January 2026 to 23 January 2026

Source archive repository reference:

```text
happygeneralist/civic-design-secondary-research
sources/SRC_001_ofsted_essex_area_send_inspection_jan_2026
```

Working source used for this table:

```text
Essex_Area_SEND_Full_inspection_Jan26.pdf
```

## Source-status note

This is a public inspection report. It is secondary/system evidence, not direct user research.

Inspection findings may support candidate evidence, pain points, civic needs, insights or source notes. They must not be treated as validated user needs on their own.

## Nearby-object search summary

A light nearby-object search was carried out before proposing object recommendations.

Searches used:

- `communication families waiting assessment support SEND user need pain point`
- `families communication SEND assessments services wait`
- `local offer SEND available support families know services`

The search returned documentation rather than existing research objects. No obvious existing user need, pain point or insight object was identified from this light search.

This is not a full repository reconciliation. Before creating objects, a fuller nearby-object check should inspect relevant folders, especially:

- `002_Evidence/`
- `003_User_needs/`
- `005_Pain_point/`
- `006_Insights/`
- `007_Themes/`
- any SEND pathway-planning source or service-context notes.

## Candidate evidence extracts

| ID | Source location | Exact or near-exact extract | Why it matters | Evidence type | Possible object type supported | Confidence and uncertainty | Create, link, update or defer recommendation |
|---|---|---|---|---|---|---|---|
| CEE-CW-001 | Page 2, section `What is it like to be a child or young person with special educational needs and/or disabilities (SEND) in this area?` | `However, the frequency and quality of communication from the partnership is inconsistent.` | This is the clearest high-level finding that communication itself is a system condition affecting children, young people and families. It supports the slice boundary and may support a pain point or theme about inconsistent communication. | Inspection finding / secondary interpretation | Pain point; theme; source note; possible service context | Medium. The statement is direct and relevant, but broad. It does not specify which communication channels, pathway moments or actors are most affected. | Create selected evidence later. Do not create a user need from this extract alone. Consider linking to a broader communication pain point or theme after nearby-object reconciliation. |
| CEE-CW-002 | Page 2, same section | `Children and young people with SEND are sometimes not aware of what support is available, particularly from health and social care.` | This identifies a specific consequence of communication and orientation failure: available support is not visible or accessible enough to some children and young people. It may point to a need to find, access or be guided towards relevant support. | Inspection finding / secondary interpretation | Evidence; pain point; possible user need; possible civic need; service context | Medium. Strong relevance, but the source does not provide direct first-person evidence. The wording uses awareness, so any user need should avoid simply restating `need to know` unless comprehension/awareness is genuinely the supported need. | Create selected evidence later. Candidate object should probably be a pain point or service-context note first. A user need may be proposed only after checking nearby needs. |
| CEE-CW-003 | Page 2, same section | `Often, they and their families need more help to understand what community activities are available to them.` | This links communication gaps to families' ability to make use of community activities. It may support an access-oriented or orientation need, but should be handled carefully because the wording is service-facing and uses `understand`. | Inspection finding / secondary interpretation | Evidence; pain point; possible user need; service context | Medium-low. It is relevant but narrower than the core waiting-communication slice because it focuses on community activities rather than assessments or services. | Defer or include as contextual evidence only unless the slice is expanded to include available-support orientation. Do not create a standalone object from this in the first pass. |
| CEE-CW-004 | Page 5, section `What does the area partnership need to do better?` | `Some long-term issues underlie much of the dissatisfaction of families. These are the timeliness of EHC needs assessments, the waits for neurodevelopmental assessments and communication to families and professionals about the support available for children and young people with SEND.` | This connects communication about available support to family dissatisfaction and places it alongside two major waiting-time issues. It supports a system-level issue cluster: delay plus insufficient orientation/communication. | Inspection finding / secondary interpretation | Evidence; pain point; insight; theme; civic need | Medium. It is highly relevant but bundles multiple issues. It should not be used to collapse assessment timeliness and communication into one object without further analysis. | Create selected evidence later. Use as issue-cluster evidence. Candidate insight may be that communication gaps compound the harm of waiting, but that should remain `needs_review`. |
| CEE-CW-005 | Page 5, same section | `Many families are dissatisfied with the delays, such as for EHC needs assessments.` | This gives context that delays are experienced as a family-dissatisfaction issue. It does not itself evidence communication failure, but it helps explain why communication while waiting matters. | Contextual evidence / inspection finding | Evidence; service context; contextual support for pain point | Medium. Useful context, but not enough on its own for the communication slice. | Include only as contextual evidence if needed. Do not create a separate object from this slice. |
| CEE-CW-006 | Page 5, same section | `High numbers of families end up in mediation, tribunals or making complaints to the ombudsman.` | This suggests escalation burden and potential failure to resolve issues earlier in the pathway. In this slice, it matters only insofar as it sits next to insufficient communication and unresolved questions/anxieties. | Inspection finding / contextual evidence | Pain point; insight; civic need; evidence | Medium-low for this slice. It is important but risks pulling the slice into dispute, accountability and statutory-process evidence. | Defer for a later escalation/dispute slice unless needed as limited context for CEE-CW-007. |
| CEE-CW-007 | Page 5, same section | `Some families find that they can only gain support when they push hard for it.` | This is a strong burden/power signal. It may indicate that families must become persistent advocates to access support. It is connected to the communication and support-access cluster but broader than communication alone. | Inspection finding / secondary interpretation | Pain point; behaviour; insight; possible civic need | Medium. Strong wording, but it does not specify whether `push hard` relates to communication, assessment access, provision, dispute or all of these. | Defer as a candidate for a later burden/escalation slice, or include as contextual evidence only. Do not create an object from this communication slice alone. |
| CEE-CW-008 | Page 5, same section | `Communication between services and individual families about plans and support is often insufficient to resolve families’ questions and anxieties.` | This is the strongest extract for the agreed slice. It directly links communication quality with unresolved questions and anxieties while families navigate plans and support. It preserves functional and emotional meaning. | Inspection finding / secondary interpretation | Evidence; pain point; possible user need; possible civic need; insight | High for this slice. It is direct, specific and relevant. It remains inspection evidence, not direct user research. | Create selected evidence later. This is the best candidate to support a reusable pain point and possibly an umbrella user need after nearby-object reconciliation. |
| CEE-CW-009 | Page 6 to 7, `Areas for improvement` | `Leaders across the partnership should improve their approach to communication with children and young people and parents.` | This is an improvement recommendation. It confirms that communication is a recognised system improvement area. | Improvement recommendation | Source note; civic need; service context; opportunity later | Medium. It is a recommendation to leaders, not a user need or pain point. | Create as evidence only if useful. Do not convert directly into a user need. May later support a civic need or opportunity after problem objects are stable. |
| CEE-CW-010 | Page 6 to 7, `Areas for improvement` | `develop consistent approaches to ensure that children and young people with SEND and their families, and professionals, know what needs-led support and services are available` | This recommendation identifies consistency of approach and available-support orientation as a system responsibility. It may support a civic need, but the wording is institutional and solution-adjacent. | Improvement recommendation | Civic need; service context; source note; opportunity later | Medium. Relevant but framed as what leaders should do. A derived object must not simply restate the mechanism. | Create as evidence only or source note. Candidate civic need possible after reconciliation: the system needs to make needs-led support findable and actionable across actors. |
| CEE-CW-011 | Page 6 to 7, `Areas for improvement` | `improve communication with individual families while they wait for assessments or services.` | This is the clearest recommendation for the bounded slice. It names individual families, waiting, assessments and services. It supports the slice as a distinct pathway moment. | Improvement recommendation | Evidence; pain point; service context; civic need; possible opportunity later | High for this slice. It is direct and tightly scoped. It is an improvement recommendation, not direct user research. | Create selected evidence later. Strong candidate to support a pain point and civic need. A user need may be proposed only after checking nearby needs and preserving the difference between communication need and service mechanism. |

## Strongest candidate extracts for first object pass

If the next step creates structured evidence objects, prioritise only these extracts first:

1. CEE-CW-008: insufficient communication about plans and support does not resolve questions and anxieties.
2. CEE-CW-011: improve communication with individual families while they wait for assessments or services.
3. CEE-CW-001: frequency and quality of communication from the partnership is inconsistent.
4. CEE-CW-004: communication about support available is one of the long-term issues underlying family dissatisfaction.
5. CEE-CW-002 or CEE-CW-010: support availability is not consistently visible to children, young people, families and professionals.

This keeps the evidence set within the planned 5 to 8 extract stop/shrink criterion.

## Candidate object recommendations

These are recommendations only. They are not created by this PR.

### Candidate pain point

Possible reusable pain point:

```text
Families waiting for SEND assessments or services do not receive enough consistent communication about plans, support and available help to resolve questions, reduce anxiety or stay oriented.
```

Recommended status if created later: `draft` or `needs_review`, with Essex evidence as a local evidence instance.

Reasoning:

- best supported by CEE-CW-001, CEE-CW-004, CEE-CW-008 and CEE-CW-011;
- preserves waiting, communication, plans/support, questions and anxiety;
- does not claim national prevalence;
- should be checked against existing pain points before creation.

### Candidate user need

Possible reusable user need, subject to nearby-object reconciliation:

```text
Families need to maintain enough communication with the right people to coordinate support, resolve questions and respond to changing needs while they wait for SEND assessments or services.
```

Recommended status if created later: conservative candidate, `needs_review`, not validated.

Reasoning:

- action-oriented: `maintain`, `coordinate`, `resolve`, `respond`;
- avoids a vague `need to know` formulation;
- keeps the need general enough to support future cross-locality comparison;
- should not be created until nearby existing needs have been checked more fully.

Uncertainty:

- the report is inspection evidence, not direct family research;
- the extract supports the need indirectly through inspection findings and recommendations;
- direct user research would strengthen the wording and emotional/relational framing.

### Candidate civic need

Possible civic need, subject to reconciliation:

```text
The SEND system needs to provide reliable communication and orientation for families while they wait, so that delay does not leave plans, support routes, questions and anxieties unmanaged.
```

Recommended status if created later: candidate / `needs_review`.

Reasoning:

- reflects an institutional obligation rather than an individual task;
- supported by improvement recommendations on pages 6 to 7;
- connects communication to fairness, access and burden during long or uncertain pathways.

Uncertainty:

- needs checking against existing civic needs;
- should avoid becoming an operational requirement such as `create a communication process`.

### Candidate insight

Possible insight:

```text
Waiting-time harm is compounded when families do not receive enough communication to resolve questions, manage anxiety or understand what support is available.
```

Recommended status if created later: `draft` / `needs_review`.

Reasoning:

- synthesises CEE-CW-004, CEE-CW-008 and CEE-CW-011;
- useful for design and policy sensemaking;
- should remain provisional because it is derived from inspection findings rather than direct research.

## Evidence-only or deferred material

The following extracts should probably not create objects in this first pass:

- CEE-CW-003: community activities orientation may belong in a wider support-visibility slice;
- CEE-CW-005: family dissatisfaction with delay is useful context but not communication-specific enough;
- CEE-CW-006: mediation, tribunals and Ombudsman complaints are better handled in a later escalation/dispute slice;
- CEE-CW-007: `push hard for support` is a strong burden signal but should probably be analysed in a later burden/escalation slice.

## Public/private boundary check

This table includes:

- selected public source extracts;
- source locations;
- public-safe rationale;
- uncertainty;
- candidate object recommendations;
- conservative status suggestions;
- local-evidence/general-object reasoning.

It does not include:

- protected prompt chains;
- hidden rubrics;
- scoring;
- private orchestration workflow;
- ontology/navigation inference logic;
- private scratch reasoning.

## Validation status

Nothing in this table is reviewed or validated.

No object should be marked reviewed or validated on the basis of this table.

The next step should be a small object-creation PR only if the candidate evidence set and object recommendations are accepted.
