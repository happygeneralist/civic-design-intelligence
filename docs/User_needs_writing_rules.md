# User needs writing rules

This file gives practical rules for drafting, reviewing and refining user needs in the research repository. Read it with [Needs as evolving knowledge](Needs_semantic_contract.md), which defines the semantic roles and their boundaries.

It is designed for human contributors and LLM-assisted workflows. Examples illustrate distinctions; they are not independently validated need statements or exact answers that every agent must reproduce.

## Core rule

A user need should describe what a person needs to achieve, preserve, recover, avoid or change. Its relevant context must be recoverable, but does not have to be embedded in the sentence.

It should not simply describe a solution, feature, user story, policy requirement, organisational objective or vague knowledge state. Specific professional or task-level needs are legitimate when they describe human progress rather than merely reproducing the existing system's instructions.

The aim is useful, stable and revisable knowledge, not perfect wording. Retain clearly labelled assumptions, competing interpretations and candidate needs. Do not suppress plausible hypotheses merely because direct participant evidence is not yet available, and do not pretend that inference is source evidence.

## One identity and several useful forms

- `id` preserves identity and learning.
- `short_name` is the compact communicative need label for maps and navigation.
- `need` is the current canonical working formulation. Persist it; do not regenerate it for each query.
- Authentic user language remains source evidence, not an invented first-person rendering.
- A user-facing formulation may support recognition and discussion; label it as an interpretation unless quoted.
- A value-oriented view can combine the need with pain, expected value and fulfilment conditions, keeping those propositions distinguishable.
- Structured fields and relationships make the object computable without requiring unnatural language.

Reusable audience views must identify the object and the revisions of the propositions used. A change of audience does not authorise a change of meaning. Use Git references where sufficient rather than inventing mandatory version fields.

## Need, pain, value and fulfilment

A pain point describes an obstruction, burden, harm or risk. Expected value explains why fulfilment matters and for whom. Fulfilment conditions describe what would count as the need being sufficiently met; indicators help assess those conditions. They are not interchangeable.

Do not require all of these in one sentence. Keep them explicitly related in the object body or linked objects. A compact need may include an essential protection or outcome, but should not silently combine several claims into one apparently evidenced proposition. Avoiding harm or undue burden can itself be a legitimate need; do not erase it solely to make the wording shorter.

Check actor, beneficiary and responsibility separately. A person's need does not mean they must perform every action required to meet it. For example, needing support to progress does not establish that a parent should coordinate institutions. Preserve the responsibility question as a tension where unresolved.

## User needs are not solution requirements

Do not write needs that preselect the answer.

Poor:

```text
I need a dashboard.
```

More useful working interpretation:

```text
I need to assess service demand so I can make fair and responsive decisions.
```

The evidence must establish whether this is the right action and value. A dashboard may be one possible response, not the need. Do not reverse this rule by declaring that a legitimate higher-level need is invalid because many different solution classes could contribute to it.

## Use action-oriented language without erasing experience

Prefer language describing the progress or protection required. Useful verbs include `access`, `check`, `choose`, `compare`, `confirm`, `correct`, `decide`, `find`, `maintain`, `prepare`, `provide`, `recover`, `resolve` and `secure`. The right wording depends on meaning, evidence and level, not a verb whitelist.

Be careful with `know`, `understand`, `learn` and `be aware of`. They can hide a more actionable need, but comprehension may itself be necessary for safety, rights, consent or an informed choice.

```text
I need to check whether I am eligible before spending time applying.
I need to understand the consequences of choosing this pathway before committing to it.
```

Do not mechanically replace comprehension or emotional meaning with an administrative action. Changing `know options exist` to `compare options` or `secure an option` changes the proposition, not just its style.

## Use Jobs to Be Done and user needs together

Jobs to Be Done can help examine situations, progress, functional/emotional/social dimensions, pains, desired outcomes and forces around change. It is a method resource, not an authority that overrides this repository's semantics.

A job map can help discover constituent needs. Do not automatically treat every job step, current workflow action or desired performance metric as a separate user need. Preserve genuine independently meaningful components and retain a useful higher-level need.

Public-service contexts may constrain choice and impose statutory, institutional or relational conditions. Do not assume a market in which a person is free to choose competing products or simply leave the service. Services are one possible response alongside policy, community, infrastructure and institutional change.

Illustrative:

```text
Need: compare realistic options and protect future choices.
Possible contextual expression: when planning a post-16 pathway.
Possible solution: a personalised comparison tool, guidance, brokerage or another response.
```

The context can be stored separately when it does not define a distinct need.

## Separate user needs from user stories and policy requirements

A user need expresses underlying progress or protection. A delivery story describes a possible implementation. A policy requirement describes an obligation or service condition. They can be linked without being treated as the same object.

```text
Need: check eligibility before spending time applying.
Delivery story: use an eligibility checker.
Policy condition: provide particular identification evidence.
Possible related need: establish identity without unnecessary repeated disclosure.
```

The related need is an interpretation to test, not something automatically proved by the policy condition.

Policy, service and design-history references must not determine need wording. Record the response or obligation separately. Do not redefine the need to match what an institution currently provides.

## Context and scope

A need may recur across several contexts. Record context, evidence scope, applicability and limitations; put a qualifier in the canonical statement when it is necessary to distinguish meaning, not merely because it appeared in the first source.

Use `need_level` as a navigational description, not a compulsory single ladder. Experience, service, journey and task needs can coexist. A broad need can have multiple constituent needs and multiple higher-level connections. Rights, capabilities, civic obligations and causal contributions are not automatically parents.

Do not make a need local-only because the first evidence comes from a local report. Equally, reusable wording is not evidence of universal applicability or national prevalence. Keep manifestations, severity and fulfilment assessments contextual.

Create a new or related variant when actor, required progress, essential protection or scope materially changes. Do not create a duplicate solely because the locality or wording differs.

## Decomposition and umbrella needs

When a broad need contains independently meaningful needs, expose those parts as linked candidates. Ask whether parts can be fulfilled, challenged or studied separately. Preserve meaningful relational wholes and do not split merely on conjunctions.

An umbrella can organise a reusable pattern without replacing its narrower needs. Retain it where useful; decomposition is not automatic supersession. Conversely, do not collapse all communication or support propositions into an unhelpfully broad label.

Check nearby objects before creating new ones. Link or reuse when meaning is already covered; preserve unresolved overlap as an explicit comparison rather than forcing a premature merger. No fixed number of needs per source, actor or level is required.

## Human experience, capabilities and rights

For detailed work, ask what broader human experience, capability, right or civic obligation may be enabled, protected or harmed. Make these relationships visible and challengeable rather than assume every need leads to safety or dignity.

Differentiate empirical findings, normative commitments and legal applicability. A service efficiency score must not automatically offset a rights concern. Unknown anchoring does not block candidate capture; record the gap and investigate it when the intended use requires it.

## Emotional and social needs

Emotional, relational, social and identity needs are valid. For example:

```text
I need to feel safe asking for support without shame or blame.
I need to maintain my role as a capable parent while navigating the system.
```

Do not strip the protective or relational meaning to fit a functional formula. Participant recognition, disagreement and qualification are valuable contextual feedback, not automatic universal validation or an emotional-intensity target.

## Meaning changes and tensions

Keep a current formulation and a short rationale. Material changes to actor, agency, progress, scope, evidence, value, fulfilment or relationships require a visible proposal and appropriate change record. Refining wording need not create a new identity; a genuinely different proposition may require related or successor objects.

Record competing interpretations and what would help resolve them. Do not repeatedly rewrite a sentence to hide a real disagreement between actors or an unresolved question about institutional responsibility.

Use existing evidence, lifecycle and review fields conservatively. Unknown value, missing direct evidence or incomplete fulfilment conditions can remain unknown. Specificity should support learning, not manufacture apparent certainty.
