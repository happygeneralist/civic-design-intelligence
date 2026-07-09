# User needs quality: public summary

This document gives a public-safe summary of how to review the quality of user needs in this repository.

It is intended for public contributors and reviewers. It does not publish detailed quality rubrics, scoring methods, ontology/navigation logic, prompt chains or protected user-needs methodology.

Detailed or advanced method material belongs in the private `happygeneralist/design-intelligence-orchestration` repository or the Happygeneralist knowledge repo unless there is an explicit publication decision.

## Purpose

User needs are first-class research objects in this repository. They should be persistent, traceable and supersedable, not casually overwritten or deleted.

A user need should help the repository preserve what a person needs to achieve, preserve, recover or change in context.

Quality review should protect meaning, evidence traceability and solution-agnostic framing without turning every first-pass need into a heavy governance exercise.

## What good enough means

A public user need is good enough to keep as a candidate when:

- it describes a person’s need, not a service mechanism;
- it is solution-agnostic;
- it uses action-oriented wording unless comprehension itself is the evidenced need;
- it is scoped at an appropriate level;
- it preserves relevant emotional, social, civic or experiential meaning;
- its evidence basis and review state are not overstated;
- uncertainty is visible;
- nearby existing needs have been checked before creating a new object.

Good enough does not mean final, validated or complete.

## Minimum review questions

Before promoting or relying on a user need, ask:

1. Is this actually a user need, or is it a policy requirement, service step, feature, page requirement, organisational need or preferred solution?
2. What does the person need to achieve, preserve, recover or change?
3. Is the wording solution-agnostic?
4. Is the verb appropriate for the evidence?
5. Are cognitive verbs such as `know` or `understand` justified by the evidence?
6. Is the need scoped at the right level?
7. Does the wording preserve important emotional, relational, social, civic or experiential meaning?
8. Does the evidence support the wording and level?
9. Would one word change alter the solution direction?
10. Is the evidence basis, confidence and review state honest?

## Public red flags

Review a user need carefully when it:

- starts from a solution, channel, form, dashboard, page, notification or tool;
- uses vague cognitive wording without showing why comprehension itself is the need;
- repeats a policy, statutory or administrative requirement as if it were a person’s need;
- describes what the council, service, team or organisation needs users to do;
- removes emotional, relational, social or civic meaning to make the need sound more task-like;
- combines multiple levels of need into one statement;
- duplicates an existing nearby need with different wording;
- claims validated, reviewed or high-confidence status without evidence of human review.

## Public/private boundary

The public repository may contain:

- writing rules;
- simple quality questions;
- red flags;
- evidence and review-state expectations;
- examples needed for contribution and auditability;
- public-safe explanations of why wording matters.

The private orchestration layer may contain:

- detailed quality rubrics;
- scoring methods;
- prompt chains;
- advanced distortion typologies;
- relationship/navigation logic;
- protected review workflows;
- book/IP-adjacent method material.

## LLM-assisted review

LLMs may help draft, compare or review candidate wording, but LLM output is not evidence and is not human review.

LLM-assisted user needs should remain conservative by default:

```yaml
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
review_status: not_reviewed
```

Do not mark a user need as reviewed, validated or final unless a human reviewer has explicitly completed that review.

## Relationship to other documents

Use this summary alongside:

- `docs/User_needs_writing_rules.md`
- `docs/Needs_hierarchy.md`
- `docs/Lifecycle_states.md`
- `docs/Evidence_standards.md`
- `docs/LLM_safety_model.md`
- `docs/Openness_protection_model.md`

## Current status

This is a public-safe quality summary.

It is intentionally lightweight. It gives enough guidance for public scrutiny, contribution and safe review without exposing the protected method used to operationalise user-needs quality at scale.
