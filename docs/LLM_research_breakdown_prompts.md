# LLM research breakdown prompts

This file provides reusable prompts for breaking down research material into candidate problem-space objects.

Use these prompts with the repository schema, templates and writing rules.

## General rules for all prompts

The LLM must:

- keep evidence and interpretation separate
- avoid treating LLM output as evidence
- avoid validating anything
- never use `evidence_basis: validated` unless a human reviewer has explicitly completed validation
- mark unsupported items as assumptions or candidates
- use `creation_mode: llm_assisted`
- use `llm_generated: true`
- use `human_reviewed: false`
- use `review_status: not_reviewed` or `needs_review`
- preserve uncertainty
- avoid solution-led framing
- follow `docs/User_needs_writing_rules.md` when drafting user needs
- follow `docs/Decision_shaped_user_needs.md` when a user need involves choosing, deciding, comparing, committing, escalating or planning under uncertainty

## Minimum viable first pass

For most first-pass research breakdown work, use only:

1. Prompt 1: first-pass breakdown
2. Prompt 2: extract candidate user needs
3. Prompt 8: create structured notes, but only for selected objects worth keeping

Use the other prompts when you need more depth, review or decision-readiness.

## Prompt 1: first-pass breakdown

```text
Review the following anonymised research material and produce a first-pass problem-space breakdown.

Extract candidate:

- evidence items
- user needs
- behaviours
- pain points
- insights
- themes
- opportunities
- value dimensions

Do not validate anything.

For each item, include:

- suggested type
- draft title or formulation
- actor, if known
- journey stage, if known
- need_level, if it is a user need
- need_shape, if it is a user need with a clearly evidenced shape such as decision_support
- evidence_basis: none, indicative, or traceable
- status
- analysis_state
- confidence
- review_status
- related evidence, source note or source study references, if available
- uncertainty or caveats

Use these defaults unless there is a clear reason not to:

status: assumption
analysis_state: candidate
evidence_basis: indicative
confidence: low
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
review_status: not_reviewed

Keep evidence and interpretation separate.
Do not create solution options.
Do not use evidence_basis: validated.
```

## Prompt 2: extract candidate user needs

```text
Extract candidate user needs from this anonymised research material.

Follow the repository's user-needs writing rules:

- use action-oriented wording
- avoid cognitive verbs such as know, understand, learn or be aware of unless comprehension itself is the goal
- keep needs solution-agnostic
- use Jobs to Be Done tools where useful for context, progress, pains, gains and strategic opportunity framing
- avoid importing market-led JTBD assumptions uncritically into public service or SEND contexts
- set need_level where possible
- do not collapse experience, service, journey, page and interaction needs
- preserve emotional, social, civic and experience meaning where relevant
- use `need_shape: decision_support` where the evidence shows that the person needs to decide, choose, compare, commit, escalate or plan under uncertainty
- keep decision-shaped needs direct and active; do not rewrite them as `understand` needs unless comprehension itself is the evidenced need

Treat LLM-generated user needs as candidate formulations, not final wording.

For each candidate need, include:

- need statement
- actor
- journey_stage
- need_level
- need_shape, where supported by evidence or existing interpretation
- parent_needs or likely parent level, if inferable
- evidence_basis: none, indicative, or traceable
- evidence_scope_fit
- wording_sensitivity
- confidence
- status
- analysis_state
- related evidence, source note or source study references, if available
- wording rationale, if wording is sensitive
- uncertainty

Do not validate anything.
Do not use evidence_basis: validated.
Mark weak or unlinked needs as assumptions or candidates.
```

## Prompt 3: extract behaviours

```text
Extract candidate behaviours from this anonymised research material.

A behaviour should describe something a person does, avoids, repeats, compensates for or attempts in context.

For each behaviour, include:

- behaviour statement
- actor
- journey_stage
- triggers or conditions
- related needs, pain points or insights if visible
- evidence_basis: none, indicative, or traceable
- confidence
- status
- analysis_state
- related evidence, source note or source study references, if available
- uncertainty

Keep behaviours separate from pain points, needs and solutions.
Do not validate anything.
Do not use evidence_basis: validated.
```

## Prompt 4: extract pain points

```text
Extract candidate pain points from this anonymised research material.

A pain point should describe a barrier, burden, failure, friction, emotional cost or structural problem experienced by an actor.

For each pain point, include:

- pain point statement
- actor
- journey_stage
- likely cause or condition, if visible
- impact or burden
- related needs, behaviours or insights if visible
- evidence_basis: none, indicative, or traceable
- confidence
- status
- analysis_state
- related evidence, source note or source study references, if available
- uncertainty

Keep pain points separate from user needs and solutions.
Do not validate anything.
Do not use evidence_basis: validated.
```

## Prompt 5: draft insights from evidence

```text
Draft candidate insights from the following evidence and analysis notes.

An insight should explain a pattern, not merely repeat evidence.

For each insight, include:

- title
- core claim
- supporting evidence
- contextual evidence
- contradictory or limiting evidence, if visible
- interpretation
- why it matters
- related user needs
- related behaviours
- related pain points
- related themes
- evidence_basis: none, indicative, traceable, or substantiated
- confidence
- status
- analysis_state
- uncertainty

Do not validate anything.
Do not use evidence_basis: validated.
Do not turn implications into solution options.
```

## Prompt 6: propose need hierarchy

```text
Review the following candidate user needs and propose a lightweight needs hierarchy.

Use these levels:

- capability
- civic
- experience
- service
- journey
- task
- page
