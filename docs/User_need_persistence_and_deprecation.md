# User need persistence and deprecation strategy

User needs are first-class research objects in this repository.

They are not simple labels, tickets or content requirements. They represent an interpretation of evidence about what people need to achieve, avoid, access, understand, decide or sustain. Because of that, their evolution matters.

This document defines how user needs should persist, evolve, be superseded and be deprecated. It also clarifies how related objects such as pain points should remain visible when they are resolved, dormant or at risk of recurring.

## Core principle

User needs should be persistent, traceable and supersedable.

They should not be casually deleted because the team's understanding changes. If a user need is wrong, incomplete, too broad or later addressed, the repository should preserve that history so future work can understand what changed and why.

Use these words carefully:

- Persistent: the object remains part of the research record.
- Traceable: the evidence and reasoning behind the object can be followed.
- Supersedable: a better or more mature framing can replace it without erasing the earlier framing.
- Deprecated: the object is no longer recommended for active use, but remains part of the historical record.

Avoid describing user needs as strictly immutable. They can and should evolve. The important rule is that meaningful evolution should not be silent.

## Why persistence matters

Small changes to a user need can imply large changes in possible solutions.

For example:

```text
I need information about available options.
```

is not equivalent to:

```text
I need help identifying which options match my child's needs and aspirations.
```

The first framing may imply content, search or navigation. The second may imply interpretation, brokerage, relational support, confidence-building, planning tools or professional judgement.

When wording changes in this way, the change should be visible.

## Separate lifecycle, maturity, review and evidence

Do not force one status field to do all the work.

In future schema work, distinguish between:

```yaml
lifecycle_state: active | superseded | deprecated | resolved | dormant
maturity_state: captured | reviewed | validated
review_status: not_reviewed | needs_review | reviewed | rejected
evidence_basis: none | indicative | traceable | substantiated | validated
```

This matters because an object can be mature but no longer active.

For example, a user need may once have been validated, then later superseded by a better-framed need. That should not erase the fact that the earlier framing was valid at the time.

If the repository keeps a single `status` field for now, treat it as pragmatic current-state metadata and recognise that it may later split into lifecycle and maturity fields.

## Recommended lifecycle states

Recommended future lifecycle states:

```yaml
lifecycle_state: active
lifecycle_state: superseded
lifecycle_state: deprecated
lifecycle_state: resolved
lifecycle_state: dormant
```

Meanings:

- `active`: still recommended for current analysis or design work
- `superseded`: replaced by one or more better-framed objects
- `deprecated`: retained for history but no longer recommended for active use
- `resolved`: addressed in the current service or product context
- `dormant`: not currently observed or blocking, but may recur if conditions change

## Recommended maturity states

Recommended future maturity states:

```yaml
maturity_state: captured
maturity_state: reviewed
maturity_state: validated
```

Meanings:

- `captured`: recorded as a candidate or working interpretation
- `reviewed`: reviewed by a human and accepted as useful
- `validated`: strongly supported by evidence and review

LLMs should not set `maturity_state: validated` or `evidence_basis: validated`. Validation requires human review.

## Superseding user needs

When a user need is replaced by a better framing, keep the original note and link the relationship.

Example:

```yaml
lifecycle_state: superseded
superseded_by:
  - "[[UN_014]]"
supersedes:
```

The new need can include:

```yaml
supersedes:
  - "[[UN_003]]"
superseded_by:
```

The old need should explain why it was superseded:

```markdown
## Change log

- 2026-06-20: Superseded by UN_014 after evidence showed that the problem was not simply access to information but interpretive support for comparing options.
```

## Deprecating user needs

A user need should be deprecated when it is no longer recommended for active use but remains relevant as historical or contextual knowledge.

Deprecation may happen when:

- a need was based on weak or misleading assumptions
- the framing is no longer appropriate
- the need has been replaced by stronger evidence or a better segmentation
- the need is no longer active for a specific population or phase

Deprecation is not deletion. It should mean: do not use this framing for current analysis unless there is a reason.

Example:

```yaml
lifecycle_state: deprecated
deprecation_reason: Replaced by more specific pathway-planning needs after evidence review.
```

The body should preserve the rationale:

```markdown
## Deprecation note

This user need is no longer recommended for active use because later evidence showed that it combined several distinct needs. It remains historically important because it shows an earlier stage of the team's understanding.
```

## Resolved and dormant pain points

Pain points need slightly different handling from user needs.

A user need is an interpretation of what someone needs to achieve, access, decide or sustain. A pain point is an experienced friction, harm, barrier, burden or failure point.

A solved pain point should not necessarily be deprecated. It may become resolved or dormant.

This matters because a pain point can return if service conditions change. For example, information fragmentation may be resolved by a new service model, then recur later if ownership changes, content becomes outdated or access routes fragment again.

Recommended fields for pain points:

```yaml
lifecycle_state: active | resolved | dormant | deprecated
resolution_state: unresolved | partially_addressed | addressed_currently | no_longer_observed
recurrence_risk: low | medium | high
recurrence_conditions:
  - service ownership changes
  - information becomes outdated
  - support pathway changes
```

Example:

```yaml
lifecycle_state: dormant
resolution_state: addressed_currently
recurrence_risk: high
recurrence_conditions:
  - university support information becomes outdated
  - responsibility for maintaining content changes
  - families report renewed difficulty comparing support options
```

This enables dashboards and analysis to show not only where pain exists now, but where pain may return.

## Blocking value delivery

Pain points should be connected to value delivery.

A future reporting layer should be able to identify:

- unresolved pain points
- pain points blocking validated user needs
- pain points that reduce access to value
- resolved pain points that could recur
- areas where a service appears to meet a need but leaves a related pain unresolved

This makes the repository useful for product and service decisions, not just research storage.

## Merging user needs

When two or more user needs are merged, keep the original notes and mark them as superseded.

Example:

```yaml
lifecycle_state: superseded
superseded_by:
  - "[[UN_021]]"
```

The new need should record:

```yaml
supersedes:
  - "[[UN_007]]"
  - "[[UN_008]]"
```

The change log should explain the reasoning:

```markdown
## Change log

- 2026-06-20: Merged with UN_008 because review showed both needs described the same underlying decision-support need from different evidence fragments.
```

## Splitting user needs

When a need is too broad, split it rather than overwriting it.

Original need:

```yaml
lifecycle_state: superseded
superseded_by:
  - "[[UN_022]]"
  - "[[UN_023]]"
```

Change log:

```markdown
## Change log

- 2026-06-20: Split into UN_022 and UN_023 after evidence showed separate needs around emotional readiness and information overload.
```

## Lightweight user need change log

Every mature or first-class user need should eventually include a lightweight change log.

Recommended format:

```markdown
## Change log

- 2026-06-08: Created from migrated pathway-planning material. Status: captured.
- 2026-06-14: Linked to EVID_001 and BEH_001. Evidence basis remains indicative.
- 2026-06-20: Refined wording to clarify that the need is interpretive decision support, not generic signposting. Change level: material.
```

Do not write a long narrative for every small edit. The change log should capture meaningful stages in the maturity of the object.

## Frontmatter fields for persistence

Recommended future fields for user needs:

```yaml
lifecycle_state: active
maturity_state: captured
review_status: not_reviewed
evidence_basis: indicative
last_meaningful_change:
supersedes:
superseded_by:
deprecation_reason:
```

Only use `supersedes`, `superseded_by` and `deprecation_reason` when relevant.

Avoid adding `version` until there is a clear rule for when it increments. If versioning is introduced later, increment only for material or major meaning changes, not administrative edits.

## What not to do

Avoid:

- silently overwriting meaningful user need wording
- deleting superseded or deprecated needs without a strong reason
- upgrading evidence basis because wording sounds plausible
- letting LLM-polished wording replace evidence-derived language without review
- treating solved needs or pain points as if they never existed
- using `deprecated` when `resolved` or `dormant` would be more accurate

## Strategic value

Persistent user needs and pain points allow the repository to support deeper analysis:

- which needs have matured over time
- which needs were reframed by evidence
- which needs have been addressed but may recur
- which pain points are blocking value delivery
- which pain points are resolved, dormant or unresolved
- which needs are still weak or assumption-led
- which needs underpin product, service or policy decisions

The history of the object is part of the knowledge.