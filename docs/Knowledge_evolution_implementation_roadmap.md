# Knowledge evolution implementation roadmap

This roadmap describes a staged implementation approach for knowledge evolution, user need persistence and LLM intervention logging.

The aim is to establish useful governance without slowing down the current research migration work.

## Stage 1: Agree the model

Review and agree the core distinctions:

- Git history is the technical audit trail.
- Object change logs are the human-readable knowledge evolution trail.
- LLM intervention logs are the semantic-risk and governance trail.

Agree that first-class objects, especially user needs, should be persistent, traceable and supersedable.

## Stage 2: Update templates lightly

Start with user needs only.

Update the user need template to include:

```markdown
## Change log

- YYYY-MM-DD: Created/captured. Source: [study/evidence/insight]. Status: captured.
```

Do not add complex event structures to every template yet.

Recommended frontmatter additions for user needs:

```yaml
version: 1
last_meaningful_change:
supersedes:
superseded_by:
deprecation_reason:
```

Only require fields that are useful now. Optional fields should remain optional until the repository has more examples.

## Stage 3: Add LLM operating rules

Before any LLM-assisted edit to first-class objects, require the LLM to state:

```text
Planned change type:
Expected semantic risk:
LLM intervention log required: yes/no
```

After the edit, require:

```text
Meaning changed: yes/no/possibly
Evidence relationships changed: yes/no
Review status changed: yes/no
LLM intervention log created: yes/no
```

This does not require tooling immediately. It can begin as a working convention in chats and PR descriptions.

## Stage 4: Create the change-events folder

Create:

```text
011_Change_events/
  README.md
  LLM/
  Objects/
  Reviews/
```

At first, use this only for:

- material LLM-assisted changes
- user need split, merge, supersede or deprecation
- evidence-basis changes
- review or validation decisions

Do not log administrative changes here.

## Stage 5: Add validator checks cautiously

Only add validator rules once the pattern has been tested manually.

Possible future checks:

- if `status: superseded`, require `superseded_by`
- if `status: deprecated`, require `deprecation_reason`
- if `semantic_change_review: needs_review`, require `review_status: needs_review`
- if `last_change_actor: llm_assisted` and `change_level: material`, require a linked change event

Avoid strict validation too early. The goal is to support research governance, not block useful work with premature schema constraints.

## Stage 6: Query and reporting layer

Once examples exist, build queries or scripts to report:

- user needs by maturity
- superseded and deprecated needs
- LLM-assisted material changes awaiting review
- objects with evidence basis changes
- solved or dormant pain points that may recur
- needs that underpin product or service decisions

This is where the strategy becomes a source of product and service intelligence.

## Recommended first implementation PR

A practical first implementation PR could include:

1. `011_Change_events/README.md`
2. `011_Change_events/LLM/.gitkeep`
3. `011_Change_events/Objects/.gitkeep`
4. `011_Change_events/Reviews/.gitkeep`
5. Updates to `Templates/User_need_template.md`
6. A short note in `docs/Repository_validation.md` explaining that change-event validation is future work

## What not to do yet

Do not immediately:

- create detailed change logs for every existing object
- require LLM event logs for every administrative migration
- force every template to include complex history structures
- build a central ledger before there are real examples
- make the validator enforce rules before the team understands the workflow

## Success criteria

This system is working when:

- user needs can evolve without losing their lineage
- deprecated or solved pain points remain historically visible
- LLM-assisted semantic changes are reviewable
- Git is not duplicated inside notes
- future analysis can distinguish mature knowledge from unreviewed synthesis
- the process is light enough that people actually use it