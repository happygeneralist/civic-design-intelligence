# LLM-assisted research breakdown: public summary

This document gives a public-safe summary of how LLMs may assist research breakdown in this repository.

It intentionally does not publish detailed prompt catalogues, prompt chains, ingestion routines, object reconciliation prompts, review rubrics, scoring methods or protected orchestration workflows.

Detailed operating material belongs in the private `happygeneralist/design-intelligence-orchestration` repository unless there is an explicit publication decision.

## Purpose

LLMs may support the maintenance of this repository by helping to structure, summarise and prepare candidate problem-space material for human review.

LLMs must not be treated as evidence, reviewers or validators.

Any LLM-assisted output must remain conservative, traceable and reviewable.

## Public principles

When LLMs are used to assist research breakdown, they must:

- keep evidence and interpretation separate;
- avoid treating LLM output as evidence;
- avoid validating any research object;
- preserve uncertainty, caveats and evidence limits;
- mark unsupported items as assumptions or candidates;
- use conservative review and evidence states;
- avoid solution-led framing;
- preserve the meaning of user needs, civic needs, behaviours, pain points and insights;
- avoid rewriting research material in ways that change interpretation without review;
- avoid creating public-service user needs from service mechanisms, policy requirements, administrative steps, content requirements or organisational needs;
- leave loose or immature material in the inbox rather than forcing it into a structured schema.

## Conservative metadata expectations

LLM-assisted outputs should normally use conservative defaults such as:

```yaml
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
review_status: not_reviewed
analysis_state: candidate
confidence: low
```

Evidence basis, status and review state must not be upgraded unless supported by source material and human review.

An LLM must never set `evidence_basis: validated` or mark an object as reviewed or validated unless a human reviewer has explicitly completed that review.

## Public workflow shape

A public-safe LLM-assisted workflow may include:

1. identifying candidate evidence, user needs, civic needs, behaviours, pain points, insights or themes;
2. separating evidence from interpretation;
3. recording uncertainty and missing evidence;
4. preparing draft objects only where the material is strong enough to keep;
5. leaving weak, ambiguous or immature material in the inbox;
6. flagging anything that needs human review before it affects design, policy, prioritisation or stakeholder communication.

This public shape explains the repository safety model. It is not a reusable operating prompt.

## User-needs caution

User needs require particular care.

A candidate user need should describe what a person needs to achieve, preserve, recover or change in context. It should be solution-agnostic, action-oriented and evidence-linked where possible.

LLM-assisted drafting must not convert the following into user needs:

- service mechanisms;
- preferred solutions;
- content requirements;
- policy requirements;
- administrative steps;
- organisational needs;
- backlog items;
- page, form or channel requirements.

Where comprehension, awareness or judgement is itself the evidenced need, cognitive wording may be appropriate. Otherwise, vague formulations such as `know` or `understand` should be treated cautiously.

## Public/private boundary

The public repository may contain:

- principles for safe LLM assistance;
- review and evidence-state rules;
- object definitions;
- contribution safety guidance;
- enough summary to make public objects intelligible and auditable.

The private orchestration layer may contain:

- detailed prompts;
- prompt chains;
- ingestion routines;
- decomposition and reconciliation workflows;
- quality rubrics;
- ontology or navigation logic;
- private review checklists;
- protected operating methods.

## Related documents

- `docs/LLM_safety_model.md`
- `docs/LLM_intervention_logging.md`
- `docs/User_needs_writing_rules.md`
- `docs/Openness_protection_model.md`
- `docs/Source_use_policy.md`
- `docs/Evidence_standards.md`

## Current status

This file is a public-safe replacement for an earlier public prompt catalogue.

The replacement preserves the safety and governance principles needed for public auditability while removing detailed reusable prompt text from the public repository.
