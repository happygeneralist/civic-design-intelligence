# User needs writing rules

This file gives short, practical rules for drafting, reviewing and refining user needs in the research repository.

It is designed for human contributors and LLM-assisted workflows.

## Core rule

A user need should describe what a person needs to achieve, preserve, recover or change in context.

It should not describe:

- a solution
- a feature
- a user story
- a policy requirement
- an organisational objective
- a vague knowledge state

## User needs are not solution requirements

Do not write needs that preselect the answer.

Poor:

```text
I need a dashboard.
```

Better:

```text
I need timely, trustworthy visibility of service demand so I can make fair and responsive decisions.
```

A dashboard may become a solution requirement later, but it should not be treated as the need.

## Use action-oriented language

Prefer verbs that describe what the user needs to do or achieve.

Useful verbs include:

```text
access
apply
check
choose
compare
confirm
complete
correct
decide
determine
find
maintain
prepare
provide
recover
resolve
submit
track
```

The right verb depends on the level of need.

## Be careful with cognitive verbs

Avoid vague cognitive verbs unless understanding, knowledge or awareness is genuinely the thing the user must achieve.

Use cognitive verbs cautiously:

```text
know
understand
learn
be aware of
```

These often hide a more actionable need.

Poor:

```text
I need to know if I am eligible.
```

Better:

```text
I need to check whether I am eligible.
```

Poor:

```text
I need to understand the form.
```

Better:

```text
I need to complete the form accurately so I can apply for support.
```

Cognitive verbs may be appropriate when comprehension itself is necessary for safety, rights, consent, compliance or informed decision-making.

Appropriate:

```text
I need to understand the consequences of choosing this pathway before I commit to it.
```

Appropriate:

```text
I need to understand my right to appeal so I can challenge a decision safely.
```

## Use Jobs to Be Done and user needs together

Jobs to Be Done and user needs can often be used interchangeably as ways of describing what a person is trying to get done, especially when the focus is the user's goal, progress, context and outcome.

JTBD methods are useful because private-sector practice has developed strong tools for strategy, innovation, segmentation, value proposition design and opportunity framing.

Use JTBD tools to strengthen user needs work, especially to understand:

- the situation that triggers the need
- the progress the person is trying to make
- functional, emotional and social dimensions of the need
- pains, anxieties and barriers
- desired gains and outcomes
- forces that push, pull, block or create anxiety around change

In value proposition design and journey mapping, the `job` can often be replaced with the `user need`, provided the context is handled carefully.

For example:

```text
JTBD job: Check whether I am eligible before applying.
User need: I need to check whether I am eligible before I spend time applying.
```

The important difference is contextual, not mechanical.

In constrained public-service contexts, including SEND, people often cannot choose whether they need the service, cannot freely choose between competing solutions, and may be navigating statutory, institutional or relational constraints. Many JTBD tools assume a market context where the aim is to pull a person towards a product or service. Use that logic carefully.

Do not use JTBD to make the need product-led.

Good use of JTBD:

```text
When planning a post-16 pathway, I need to compare realistic options so I can make a decision that protects future choices.
```

Poor use of JTBD:

```text
When planning a post-16 pathway, I want a personalised dashboard so I can compare options.
```

The dashboard may be a solution, but the need is about comparison, decision-making and protecting future choices.

## Separate user needs from user stories

A user need describes the underlying problem or outcome.

A user story describes a possible delivery expression.

User need:

```text
I need to check whether I am eligible before I spend time applying.
```

User story:

```text
As an applicant, I want to use an eligibility checker so that I can see whether I should apply.
```

Both can be useful, but they are not the same object.

## Separate user needs from policy requirements

Policy and funding requirements may shape the service, but they are not automatically user needs.

Policy requirement:

```text
Applicants must provide two forms of identification.
```

User need:

```text
I need to provide the right evidence without making repeated or unnecessary submissions.
```

## Policy, service and design-history references

Policy documents, service decisions and design histories may reference user needs, but they should not determine the wording of user needs.

A user need should remain grounded in what a person needs to achieve, preserve, recover, decide, access or sustain.

If a policy, service model or operational process responds to a need, capture that response as a related policy, service, solution, decision-history or context object. Do not rewrite the user need to fit the institutional response.

## Scope the need correctly

User needs exist at different levels.

Use `need_level` to avoid collapsing broad needs and detailed needs.

Example:

```text
Experience need: I need to feel that I have a future.
Service need: I need joined-up support to plan a realistic pathway.
Page need: I need to check whether this course is suitable for someone with my support needs.
Interaction need: I need to filter options by support type, location and entry requirements.
```

These are connected, but they are not interchangeable.

## Use emotional and social needs carefully

Emotional and social needs are valid in public-service contexts, including SEND.

Examples:

```text
I need to feel safe asking for support without shame or blame.
I need to maintain my role as a capable parent while navigating the system.
```

Do not force these into purely functional task language if doing so removes important meaning.

## Keep wording stable when it affects direction

Small wording changes can substantially change the solution vector.

For example:

```text
I need to know what options exist.
```

points towards information provision.

```text
I need to compare options.
```

points towards comparison and decision support.

```text
I need to understand which options are appropriate for my child.
```

points towards interpretation, guidance and personalisation.

When wording changes meaning, treat it as a material change and update the changelog.

For high-sensitivity needs, add:

```markdown
## Wording rationale

Why this wording was chosen and what alternative wording would imply.
```

## Good user need pattern

A useful pattern is:

```text
I need to [action] [object/context] so that [outcome/value].
```

Example:

```text
I need to check whether I am eligible for support before I spend time applying.
```

But do not force every need into this exact structure. Experience, civic and emotional needs may need different phrasing.

## Short names for mapping and design

Use `short_name` as a compact version of the user need for Obsidian Bases, maps, workshops, post-it notes and design artefacts.

The short name should still read as a need, not as a theme label or topic.

Preferred pattern:

```text
Need to [verb] [object/context]
```

Good examples:

```text
Need to determine sailing area
Need to choose a suitable supplier
Need to choose matching equipment
Need to set up navigational equipment
Need to assess regional travel risk
Need to choose payment model
Need to evaluate the service
```

Short names deliberately strip out some context. This reduces cognitive load when moving needs around in mapping and prioritisation work. The full `need` field remains the canonical, evidence-sensitive formulation.

Leave these out of the short name:

- actor or persona
- `so that` outcome or value
- detailed evidence nuance
- caveats and uncertainty
- organisational or service goals

Include only enough object or context to distinguish nearby needs.

Be especially careful with cognitive verbs. Do not use short names such as `Need to understand options` by default. Prefer a more action-oriented verb such as `compare`, `choose`, `check`, `determine`, `assess`, `prepare`, `provide`, `secure` or `resolve`.

Cognitive short names are acceptable only when comprehension itself is the real need, such as rights, consent, safety, consequences or informed decision-making.

Example:

```yaml
id: UN_012
short_name: Need to plan options early
need: A parent/carer of a young person with SEND needs to begin planning before key education choices become fixed, so they can make realistic decisions with enough time to act.
```

Filename:

```text
UN_012_need_to_plan_options_early.md
```

## Red flags

Review or rewrite needs that include:

- `I need an app...`
- `I need a dashboard...`
- `I need a page...`
- `I need to know...`
- `I need to understand...`
- `I need to comply with...`
- `The service needs...`
- `The council needs users to...`

These may still point to something important, but the wording should be checked.

## LLM rules

When drafting user needs, the LLM should:

- prefer action-oriented wording
- avoid cognitive verbs unless justified
- create short names using `Need to + verb + object/context` where useful for mapping and Bases
- keep needs solution-agnostic
- use JTBD tools where useful for context, progress, pains, gains and strategic opportunity framing
- avoid importing market-led JTBD assumptions uncritically into public-service contexts, including SEND
- distinguish user needs from policy requirements and user stories
- keep policy, service, organisation and locality context outside the canonical wording unless it is intrinsic to the evidenced need
- set `need_level` where possible
- preserve emotional and social meaning where relevant
- mark weak or unlinked needs as assumptions or candidates
- add a wording rationale when wording is sensitive

The LLM should not:

- convert solution ideas into user needs without reframing them
- treat policy requirements as user needs
- rewrite user needs to fit policy, service or design-history artefacts that reference them
- remove emotional, social or civic meaning just to make a need more task-like
- materially reword reviewed or validated needs without a changelog and review trail

## Review checklist

Before promoting a user need, check:

- [ ] Is it solution-agnostic?
- [ ] Is the verb appropriate?
- [ ] Are cognitive verbs justified?
- [ ] Is the need scoped at the right level?
- [ ] Has JTBD language been used appropriately for the context?
- [ ] Is it distinct from a user story, feature or policy requirement?
- [ ] Does the wording preserve the person's perspective rather than an institutional, policy or service framing?
- [ ] Is emotional or social meaning preserved where relevant?
- [ ] Does the evidence support this wording and level?
- [ ] Would one word change alter the solution direction?
- [ ] Is the evidence and review status clear?
