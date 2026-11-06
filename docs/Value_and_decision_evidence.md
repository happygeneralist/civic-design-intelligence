# Value and decision evidence

This file explains how the repository supports value-based decision-making, not only user-needs analysis. Read with `Needs_semantic_contract.md` and `Relationship_types.md`.

## Purpose

The repository should provide the human intelligence needed to design good services, challenge weak or harmful solution ideas, and answer policy, ministerial, product and service questions with evidence.

It should help teams explain:

- what people need;
- what creates or destroys value, and for whom;
- what trade-offs and tensions are visible;
- which solutions are likely to help;
- which solutions are unsupported, risky or premature;
- what evidence supports or challenges a proposed direction.

The purpose is not to endorse politically preferred solutions. It is to provide an inspectable basis for human judgement about services, policy and public outcomes.

## Value is part of the knowledge model

Value is not the same as user preference, stakeholder enthusiasm, adoption or administrative efficiency.

Value may be created when a policy, service, product, process or intervention helps meet needs, reduce avoidable burden, improve outcomes or protect people's real opportunities and capabilities. Those effects require evidence; an attractive proposition does not demonstrate them.

In public-service contexts, including SEND, value may include reducing harm, improving access, preserving agency, enabling participation, increasing fairness, supporting trust and helping institutions discharge their responsibilities. Benefits to an institution and benefits to affected people must remain distinguishable.

## Need, pain, value and fulfilment are different claims

| Concept | What it says | What it does not establish |
| --- | --- | --- |
| Need | Required progress, protection, recovery or change for a person. | That the person must perform all enabling work. |
| Pain | An obstruction, burden, risk or harm. | That removing it alone meets the need. |
| Expected value | Anticipated benefit, protection or avoided harm, with beneficiaries identified. | An observed result or demonstrated causal effect. |
| Fulfilment conditions | What would count as the need being sufficiently met in a relevant context and period. | Delivery of a particular feature, a universal threshold or a perfect need formulation. |
| Indicator | Observable or reportable information used to assess a condition. | That the proxy fully represents the person's experience. |
| Realised value | A change supported by observations, including distribution and limitations. | That the intervention caused it without an appropriate evidential basis. |

Keep these propositions identifiable even when a practitioner-facing value statement composes them into one narrative. Save the current canonical need and bind derived views to the revisions used; do not reformulate the need for every audience.

Fulfilment conditions may be qualitative, partial, continuing or disputed. Unknown criteria can stay unknown. Do not invent numbers or infer fulfilment from silence, completed referrals or uptake. Participant recognition, quality of a formulation, service performance, human need fulfilment and realised value are separate assessments.

## Human rights, civic obligations and capabilities

Always consider the human experience enabled or harmed by a response. Capabilities concern real opportunities and choices, not merely an available service or an achieved activity. The relevant higher-level connection may change through research; do not assume safety or dignity is always the decisive anchor.

Distinguish empirical evidence, normative commitments and legal applicability. For a legal claim identify the actual source/provision, jurisdiction, relevant people and scope; obtain appropriate review rather than inferring legal compliance from a need or value label.

**Do not automatically offset rights or civic obligations against efficiency using a weighted value score.** Consider applicable obligations and legitimate constraints separately from preference ranking. Preserve disagreements about interpretation and genuine tensions. This does not mean every right is absolute or that every conflict has an automatic answer.

These anchors can be proposed and investigated while candidate needs remain useful. Missing legal or capability mapping is not a reason to invent completeness or block all early exploration.

## Why value needs to be explicit

Teams may be asked to pursue a solution because it sounds attractive, convenient or easy to deliver. A value model helps make the reasoning visible, including the possibility that the preferred solution does not address the need, shifts burden, or damages another person's opportunities.

Show whose needs and outcomes are included, whose may be omitted, what is assumed and which alternative explanations would change the decision. Record a tension rather than removing it through an aggregate score.

## Value objects

Use the existing `value_dimension` template and schema. A value dimension describes what matters in the problem space and can be shared across many needs; it is not a score for a particular solution.

```yaml
type: value_dimension
id: VAL_001
title:
value_statement:
status: assumption
evidence_basis: none
related_needs:
related_pain_points:
related_capabilities:
related_civic_needs:
related_outcomes:
related_evidence:
```

The example is a partial explanatory shape, not a complete record. Actual records must use the current template and honest review metadata.

One possible value dimension is reducing work that does not help people achieve what matters. That is a proposition to examine: not all effort is waste, and efficiency must not displace agency, participation or legitimate protections.

## Solution options and assessments

Solutions are possible responses to needs and must stay separate from needs and value dimensions. Policy, service, technical, content, partnership and institutional responses may all be relevant.

`solution_option` / `SOL_` and a dedicated assessment schema are conceptual possibilities, not instructions to create unsupported canonical object types. Use an authorised proposal or research view until the relevant schema is explicitly adopted. Do not disguise a proposed solution as a `user_need` merely because a solution schema is absent.

## Evidence basis

Use the current values:

```yaml
evidence_basis: none | indicative | traceable | substantiated | validated
```

They describe the defensibility of the particular proposition, not absolute truth. Traceability establishes that a source can be followed, not that every clause or relationship is supported. Stronger states require the relevant evidence and review; automated agreement does not provide human validation.

## Challenging proposed responses

Ask which need the response claims to address, how that need is currently grounded, what broader experience/capability/obligation it connects to, and what benefits or harms might result for different people. Include supporting and challenging evidence, enabling assumptions, operational feasibility, alternative approaches and unresolved tensions.

Do not require every candidate to be mature before an exploratory comparison. Increase scrutiny when the consequences of relying on a claim increase.

## Recommendation language

For a scoped assessment, clearly distinguish an option that is worth exploring, one that needs evidence, one that is not yet feasible, and one that has sufficient support for a specified decision. A recommendation is contextual and human-accountable, not a permanent property of a need.

Earlier suggested labels such as `weak_candidate`, `promising`, `recommended`, `needs_more_evidence` and `not_yet` can aid discussion; they are not new mandatory frontmatter or automatic approval states.

## Value scoring

A score can be a useful summary of a declared judgement but must not hide its assumptions, coverage, uncertainties or distributional effects. Keep the criteria, rationale and supporting claims accessible.

No single weighted score should silently trade away rights or collapse human, institutional and civic effects. A high score cannot fill missing evidence, establish legal permission or certify need fulfilment. Keep consequential constraints and unresolved tensions visible alongside rankings.

## Evidence against a solution is valuable

Retain challenging evidence, counterexamples, risks and harms as well as supporting evidence. State what assumptions would have to hold and what could change the recommendation. Do not discard dissent because a preferred intervention has already been funded or implemented.

## Exploratory value from candidate needs

Candidates can already support research planning, idea generation and provisional policy/service coverage comparisons. Keep the following distinct:

- **Need proposition:** the current formulation, actor, evidence/assumptions and applicability.
- **Policy intent or obligation:** what a current source actually commits to, with date, scope and basis checked.
- **Provision or capability:** what is available and under which conditions, not necessarily what people receive.
- **Experienced outcome:** what direct or mediated evidence establishes in people's circumstances.
- **Gap hypothesis:** an apparent mismatch, missing coverage or uncertainty to investigate, not a compliance finding.

Show positive cases and alternatives. A source-inspired candidate may expose a useful question even when the wording or higher-level connection remains contested. Knowledge role and maturity are independent: a reusable need is not certified merely because it appears in a gold-layer view.

See [SEND pilot #99](https://github.com/happygeneralist/civic-design-intelligence/issues/99). Reusable review tooling belongs in AI Capability Layer; this file defines public-safe semantics, not a scoring engine or protected method.

## Relationship to user needs

Connect needs, evidence, human experience, civic responsibilities, capabilities, rights, value and possible responses as a network of explicit propositions. There is no compulsory one-to-one chain and no automatic inheritance of truth or fulfilment.

A reviewed need can still be wrong or unmet. An assumption can already aid exploration. The learning value lies in keeping current meaning, basis, alternatives and consequences inspectable as the model evolves.

## Practical rule

Make value visible, traceable and contestable. Show what is expected, what was observed, whose perspective is represented and what remains uncertain. Do not confuse service completion with human fulfilment, or a preference score with authority to disregard an obligation.
