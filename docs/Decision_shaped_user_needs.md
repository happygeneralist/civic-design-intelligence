# Decision-shaped user needs

This note defines a lightweight convention for user needs that involve consequential choices.

Decision-shaped needs remain user needs. They are not governance decisions, design-history decisions, policy decisions or institutional decision records.

Use this convention when the evidence shows that a person needs to decide, choose, compare, commit, consent, escalate, prioritise or plan a route through uncertainty.

## Core rule

Keep the need active, direct and evidence-led.

Use wording such as:

```text
Need to decide which post-school route to take
Need to choose whether to request additional support
Need to decide whether to challenge a decision
Need to choose who to involve in planning support
Need to compare realistic routes before committing to one
```

Do not soften a decision-shaped need into a vague information need unless the evidence shows the need is only informational.

For example, do not rewrite:

```text
Need to decide which post-school route to take
```

as:

```text
Need to understand post-school options
```

unless comprehension itself is the evidenced need. In many cases the deeper need is not merely to receive information, but to make a consequential choice with enough support, confidence, time and clarity.

## Frontmatter convention

Use `need_shape` as an optional field on `user_need` notes.

```yaml
need_shape:
  - decision_support
```

This field highlights the shape of the need. It does not replace the `need`, `short_name`, `need_level`, evidence links or review fields.

During the MVP, `decision_support` is the only formally introduced `need_shape` value. Other values should not be standardised until they are needed across multiple real objects. Keep concepts such as planning, comparison or escalation in the need wording, tags or interpretation notes unless and until they become reviewed `need_shape` values.

## Example

```yaml
type: user_need
id: UN_XXX
short_name: Need to decide which post-school route to take
actor: Young person with SEND
journey_stage: Pathway_planning
need: A young person with SEND needs to decide which post-school route to take, so they can move towards a realistic next step that fits their aspirations, support needs and circumstances.
need_level: journey
need_shape:
  - decision_support
status: draft
analysis_state: candidate
review_status: needs_review
```

## When to use `decision_support`

Use `decision_support` when the user need involves one or more of the following:

- deciding between routes, options, actions or next steps
- comparing realistic choices and their consequences
- committing to a pathway where later reversal may be difficult
- deciding whether to challenge, escalate, appeal or request support
- choosing who to involve in planning or advocacy
- making a choice while eligibility, evidence, capacity or timing is uncertain
- protecting future options through an early or time-sensitive decision

## When not to use it

Do not use `decision_support` for:

- governance decisions about the repository
- design decisions about products, prototypes or content
- institutional policy decisions
- service ownership or delivery decisions
- generic information needs where no consequential choice is evidenced
- every point in a journey where the service branches

Those may be documented through design history, PR summaries, governance material, service rules or generated journey views. They should not be turned into user needs unless they describe what a person needs to achieve, preserve, recover or change in context.

## Relationship to generated journeys

Needs marked with `decision_support` can help generated journey views identify choice moments.

A generated journey may use these needs to show where a person has to compare routes, weigh consequences, involve others, act before a deadline or make a pathway-shaping choice.

The user need remains the source object. The journey view is a generated or synthesised view over evidence, needs, behaviours, pain points and service context.

## LLM handling

When an LLM drafts or updates decision-shaped needs, it should:

- preserve direct action-oriented wording
- prefer `decide`, `choose`, `compare`, `commit`, `challenge`, `escalate`, `prioritise` or `plan` where supported by evidence
- avoid rewriting decision needs as `understand` needs unless comprehension is the evidenced need
- add `need_shape: decision_support` only where the evidence or existing interpretation supports it
- keep the item at its current evidence, confidence and review status
- record a changelog entry when adding or removing the marker changes how the need should be interpreted or retrieved

The LLM should not create a standalone Decision object for this pattern during the current MVP.
