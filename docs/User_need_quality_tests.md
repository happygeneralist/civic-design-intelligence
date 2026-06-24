# User need quality tests

This document defines practical quality tests for creating and reviewing user needs.

It should be read alongside:

- `docs/User_needs_writing_rules.md`
- `docs/Input_and_evidence_classification.md`
- `docs/Ingestion_slice_workflow.md`
- `docs/Repository_validation.md`

## Purpose

The repository needs to allow early, weak and draft user needs without letting lazy or bundled needs become accepted structure.

These tests help contributors decide whether a user need is well scoped, action-oriented and useful for public-service design intelligence.

They are not a replacement for human judgement. They are a review aid and a basis for lightweight automated warnings.

## Core test

```text
A good user need should point to a coherent problem-space job that could be addressed by many possible solution options.
```

This has two parts:

1. If a need can only be solved by one specific solution, it is probably too narrow or solution-shaped.
2. If a need points to several unrelated solution classes, it is probably too broad or bundled.

The aim is not to write needs at the exact size of a product feature. The aim is to write needs that are coherent enough to support analysis, prioritisation, value mapping and later solution exploration.

## Test 1: Multiple solution options

Ask:

```text
Could this need be met in several materially different ways?
```

A need is too narrow if it preselects one solution.

Poor:

```text
A parent/carer needs a checklist of pathway steps.
```

Better:

```text
A parent/carer needs to plan the next pathway steps, so they can keep decisions and support moving at the right time.
```

The better version could be supported through guidance, a planning conversation, a checklist, a local offer flow, a caseworker, a school meeting, a digital planning tool or other service interventions.

## Test 2: Coherent solution vector

Ask:

```text
Would one coherent class of support, service, content, interaction or operational capability address this need?
```

A need is too broad if it combines things that would be solved differently.

Poor:

```text
A parent/carer needs to check pathway steps, rights and adjustments, so they can act with confidence.
```

This bundles different jobs:

- planning pathway steps
- checking rights and entitlements
- describing or communicating adjustments

Each may need different evidence, service responses, content, operational roles or decision support.

Better:

```text
A parent/carer needs to plan the next pathway steps, so they can keep decisions and support moving at the right time.
```

```text
A parent/carer needs to check which rights and entitlements may apply, so they can ask for, secure or challenge support appropriately.
```

```text
A parent/carer needs to describe the young person's support needs and adjustments clearly, so education and support settings can understand what needs to be in place.
```

## Test 3: Bundling test

Ask:

```text
Does the need contain several objects joined by `and`, commas or a broad list?
```

A list is not always wrong. Some linked objects belong together.

Potentially acceptable:

```text
A young person needs to compare travel time, course requirements and available support, so they can choose a realistic option.
```

Here the listed items are comparison criteria for one job: choosing a realistic option.

Likely bundled:

```text
A parent/carer needs to check steps, rights and adjustments, so they can act with confidence.
```

Here the listed items point to different jobs and solution vectors.

## Test 4: Jobs-to-be-Done progress test

Ask:

```text
Is this one progress arc, or several jobs mashed together?
```

JTBD framing can help separate the situation, progress and desired outcome.

For example, this is too bundled:

```text
When planning a pathway, I want to understand steps, rights and adjustments, so I can feel confident.
```

It contains multiple jobs:

```text
When a pathway decision is approaching, I want to work out what needs to happen next, so I can keep planning moving.
```

```text
When support decisions are being made, I want to check which rights and entitlements apply, so I can ask for or challenge support appropriately.
```

```text
When my child moves into a new setting or pathway, I want to communicate their support needs clearly, so they do not have to start again or go unsupported.
```

## Test 5: Container solution test

Ask:

```text
Would the same proposed solution only work because it is a container for many different needs?
```

Examples of container solutions:

- guide
- toolkit
- dashboard
- local offer page
- checklist pack
- portal
- pathway planner

A container can respond to multiple needs, but it does not prove that those needs are one need.

If the only reason a need feels coherent is that one page, guide or service could contain all of it, split the need.

## Test 6: Confidence outcome test

Ask:

```text
Is confidence the need, or is confidence the outcome of meeting a more specific need?
```

Confidence is often a valid outcome or value dimension. It is not always the user need.

Poor:

```text
A parent/carer needs to know they have considered everything, so they can feel confident.
```

Better:

```text
A parent/carer needs to confirm which pathway actions are still unresolved, so they can act with confidence rather than constant doubt.
```

Better, if rights are the real object:

```text
A parent/carer needs to check which rights and entitlements may apply, so they can ask for, secure or challenge support appropriately.
```

## Test 7: Cognitive verb test

Ask:

```text
Is `know`, `understand` or `be aware of` genuinely the thing the person must achieve?
```

Cognitive verbs often hide a more actionable need.

Prefer verbs such as:

```text
check
confirm
compare
choose
decide
plan
prepare
provide
communicate
secure
challenge
resolve
track
```

Cognitive verbs may still be appropriate where comprehension itself is necessary for:

- rights
- consent
- safety
- legal consequences
- informed decision-making
- challenge or appeal

Even then, check whether `check`, `confirm`, `decide` or `challenge` is more precise.

## Test 8: Level test

Ask:

```text
Is this need at one level, or is it mixing experience, journey, task, content and interaction needs?
```

A higher-level need may sit above several more specific needs.

Example parent need:

```text
A parent/carer needs guidance through pathway planning, so they can make timely decisions without having to discover every step, right and support route alone.
```

Possible child needs:

- need to plan next pathway steps
- need to check rights and entitlements
- need to describe support needs and adjustments
- need to compare realistic options
- need to coordinate next steps without carrying the navigation burden alone

Do not collapse the child needs into the parent need if they have different solution vectors.

## Test 9: Evidence-fit test

Ask:

```text
Does the evidence support this exact wording and level?
```

A need may be plausible but still too broad for the available evidence.

If the evidence only supports one part of a bundled need, split the need or narrow it.

If the evidence is weak, keep conservative metadata and make uncertainty visible.

## Test 10: Noise test

Ask:

```text
Would this need attract too many unrelated evidence links, behaviours, pain points or solution ideas?
```

If yes, it is probably too broad or bundled.

A noisy need becomes hard to use for:

- evidence review
- journey mapping
- opportunity framing
- service design
- prioritisation
- public accountability

## Automated warning candidates

The validator should start with warnings, not errors.

Good first automated warnings:

- user need uses cognitive verbs such as `need to know` or `need to understand`
- user need includes likely container-solution words such as `dashboard`, `portal`, `toolkit`, `checklist`, `guide` or `page`
- user need includes broad bundled lists such as `steps, rights and adjustments`
- user need has several `and` joins in the main need statement
- short name uses cognitive verbs by default

These warnings should prompt review. They should not automatically prove the need is wrong.

## Review outcome options

When a need fails one or more tests, choose one of these actions:

- rewrite the need without changing meaning
- split the need into several needs
- create a higher-level parent need and child needs
- mark the need as needing review
- leave the material in the inbox
- supersede the need if it has already shaped the object landscape

If wording changes the solution vector or interpretation, record the change in the object changelog.
