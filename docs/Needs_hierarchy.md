# Needs hierarchy and many-to-many relationships

Read with `Needs_semantic_contract.md`, `User_needs_writing_rules.md` and `Relationship_types.md`.

Services are not the source or boundary of many needs. They are one possible institutional response to what matters in people's lives. A need may be useful before every evidence link or higher-level relationship is established.

## Levels are a navigational aid

The familiar levels remain available:

```text
capability / life
civic
experience
service
journey
task / page
interaction / content
```

This list is **not a compulsory one-directional chain or a single tree**. A need can have multiple parents or children and can contribute to multiple capabilities or rights. A civic obligation, a right and a human experience need are not interchangeable objects. A solution requirement is a related response, not an additional user-need level.

Use the existing `need_level` values:

```yaml
need_level: capability | civic | experience | service | journey | task | page | interaction | content
```

The `civic` label does not remove the distinction between `type: user_need` and `type: civic_need`. Do not force every note to fill every level.

## What the levels help us ask

| Level | Question | Illustrative direction, not a validated need |
| --- | --- | --- |
| Capability/life | What must a person have a real opportunity to be or do? | Exercise practical reason, participate, maintain affiliation or control aspects of one's life. |
| Civic | What must institutions uphold or enable? | Dignified access, accountability, equitable support, rights or redress. |
| Experience | What does the person need to experience, preserve or recover? | Feel safe asking for help; maintain agency; retain a sense of future possibilities. |
| Service | What progress/protection matters across a service relationship? | Obtain support that fits the person's needs and aspirations. |
| Journey | What matters in a particular phase or transition? | Compare realistic options before a decision; recover from an unsuccessful route. |
| Task/page | What meaningful activity or comprehension is required? | Assess whether an option is suitable; establish what evidence is relevant. |
| Interaction/content | What immediate progress must the interaction enable? | Retain progress when interrupted; distinguish relevant options. |

A filter, checklist, save button or named channel may be a solution requirement. The existence of a detailed level does not turn a specific interface into the underlying need. Equally, being operational or professional does not disqualify a genuine need.

## Three different operations

### Decompose

Identify meaningful constituent needs that can be fulfilled, investigated or challenged separately. Preserve a useful broad parent and expose children. Do not retire the parent merely because its constituents are now visible. Do not split on grammar alone or reproduce every current process step as a need.

### Ladder

Investigate why fulfilling a need matters and what it contributes to or protects. A need may contribute to participation, safety, affiliation and agency through different relationships. Those links can be uncertain or contested; they are not automatically containment or causal proof.

### Explore context

Identify recurring manifestations and variations. Context may change urgency, pain, value or fulfilment conditions without changing the core need. Create a distinct variant when meaning materially differs, not just because the source locality differs.

## Existing fields

Continue using:

```yaml
need_level:
parent_needs:
child_needs:
related_capabilities:
related_civic_needs:
related_rights:
related_outcomes:
```

Empty links can honestly remain empty. Do not invent parents, rights or evidence to complete a chain. Preserve current IDs and use ordinary body notes for relationship meaning until a tested structured convention is justified.

`parent_needs` and `child_needs` should identify a meaningful broader/constituent relationship. Where the relationship is contribution, dependency, contextual association or an obligation, explain that and use the appropriate related field instead of disguising it as a parent.

## No automatic inheritance

Evidence for a detailed claim does not prove every higher-level need. A general right does not establish that a particular service mechanism is legally required. Meeting one child need does not automatically meet its parent or another actor's need.

For example, information about eligibility may support a task-level need directly and only help explain a broader support-access need. Distinguish that scope. Use the existing optional fit values where justified:

```yaml
evidence_scope_fit: direct | partial | contextual | weak
```

A recorded fit is a reviewable judgement. Do not mark `direct` while claiming no evidential basis. Generic related links do not carry all these meanings by themselves.

## Needs, capabilities and rights

Always consider the broader human experience affected. Record whether a proposed anchor is empirical, normative or legal, and its rationale and source. Unknown or challenged links are part of the learning model, not reasons to withhold all candidate knowledge.

Do not force every need into safety, dignity or a predetermined list. If evidence changes which higher-level connection matters, preserve that learning and reconsider its implications for possible responses. Rights and civic obligations must not be automatically traded against efficiency through a common preference score.

## Wording sensitivity and stable views

Small wording changes can alter the possible response. Use `wording_sensitivity` and a concise wording rationale where useful. Distinguish finding information, comparing options, securing support and retaining agency rather than treating them as stylistic synonyms.

Keep the canonical formulation stable until a deliberate revision. Use the short need label for maps, with expansion into the fuller interpretation, evidence, contexts, tensions and value. Different presentations must remain linked to their underlying object and revision.

## Garden model: visibility and tending

A need may remain useful even when it has not been edited recently. Do not deprecate it for age alone. Prioritise visibility, connection, useful granularity, evidence awareness and deeper review when an actual use depends on it.

Candidates, evidence-linked objects and reviewed objects can all contribute at different levels of certainty. The repository may grow to thousands of needs; meaningful views and relationships should manage human attention rather than imposing a small object count.

Keep this lightweight. The pilot should test whether the distinctions help real analysis, not require a completed ontology before continuing.
