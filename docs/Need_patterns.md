# Need patterns

This note defines an emerging convention for reusable need patterns and context-specific expressions of those patterns.

It is a concept note for safe ingestion and later schema discussion. Do not treat it as a required schema or object type yet.

## Purpose

Some user needs recur across services, domains, organisations and localities.

For example:

```text
Need to compare realistic options
```

This may appear in SEND pathway planning, housing, health, social care, immigration, benefits, justice, education and employment support.

However, the reusable pattern is not enough on its own. It needs contextual expression before it can support design, service or policy work.

The repository should be able to preserve both:

- the reusable need pattern
- the context-specific expression of that pattern

## Core distinction

A need pattern is a reusable shape of need that may recur across contexts.

A need expression is a situated user need grounded in a specific actor, context, evidence base and consequence.

Example:

| Level | Example | Purpose |
|---|---|---|
| Need pattern | Need to compare realistic options | Reusable cross-service learning |
| Domain expression | A young person with SEND needs to compare realistic post-school routes | Domain-specific meaning |
| Segment expression | A young person with high decision agency needs to compare routes with light parental support | Segment-specific design intelligence |
| Service expression | Need to compare local college, training and supported employment routes | Service-context application |
| Content or interaction expression | Need to filter options by support, location and entry requirements | Delivery-level implication |

These levels should not be collapsed.

## Why this matters

Need patterns can help the repository transfer learning across services without pretending every context is the same.

They can support:

- reusable design principles
- cross-service pattern recognition
- future civic knowledge graph queries
- generated journey or service views
- comparison of how the same underlying need appears in different places
- identification of where one broad problem has different behavioural or capability expressions

## Working rule

During the current MVP, use existing `parent_needs` and `child_needs` where a wider or narrower relationship is clear.

Do not create a new need-pattern object type until real examples show it is needed.

If a possible need pattern appears during ingestion, capture it in review notes, the object body or the PR summary.

## Possible future structure

A future implementation may introduce a dedicated object type such as:

```yaml
type: need_pattern
id: NP_001
short_name: Need to compare realistic options
pattern_statement: People need to compare realistic options so they can choose a route, action or support arrangement that fits their circumstances and consequences.
related_user_needs:
  - "[[UN_013]]"
related_civic_needs:
related_pain_points:
related_design_principles:
status: draft
analysis_state: candidate
review_status: needs_review
```

A context-specific user need might then include:

```yaml
expression_of:
  - "[[NP_001]]"
```

This is not required during the current MVP.

## Guardrails

Do not make need patterns so abstract that they lose practical meaning.

Do not use need patterns to erase actor, context, capability, behaviour, evidence or power differences.

Do not treat a need pattern as validated across contexts just because it appears in one setting.

A pattern becomes stronger only when multiple evidence-linked expressions support it.

## Relationship to design principles

Need patterns may later support reusable design principles.

Example:

```text
Need pattern: Need to compare realistic options
Design principle: Help people compare options by consequence, suitability and feasibility, not just by availability.
```

The design principle should link back to the need pattern and to specific evidence-linked need expressions.

## LLM handling

When an LLM identifies a possible need pattern, it should:

- keep the context-specific user need intact
- avoid replacing situated need wording with generic pattern wording
- mark the pattern as candidate or assumption unless reviewed
- preserve evidence links at the expression level
- avoid claiming cross-context validity without multiple sources
