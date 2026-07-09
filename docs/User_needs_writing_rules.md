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

## Umbrella and reusable needs

Umbrella needs are useful when they reveal a stable pattern across narrower needs, evidence extracts or service contexts. They should help organise the object landscape without becoming so broad that they stop guiding design, policy or service decisions.

Do not make a need local-only just because the first evidence instance comes from a local report. Locality usually belongs on the source, evidence, severity note, service context or implementation condition. Create a local variant only where place materially changes the meaning of the need.

Poor umbrella need:

```text
Families need communication.
```

Better reusable need:

```text
Families need to maintain enough communication with the right people to coordinate support, resolve questions and respond to changing needs while they wait for SEND assessments or services.
```

The better version is still reusable, but it names the actor, action, pathway moment and value at stake.

When using local evidence for a reusable need:

- keep the user need wording at the highest useful level;
- link local evidence as a source-specific support, challenge or qualification;
- do not claim national prevalence, severity or consistency unless comparative evidence supports it;
- connect narrower needs to umbrella needs where this helps pattern analysis;
- avoid merging needs where the action, context or value at stake is materially different.

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
