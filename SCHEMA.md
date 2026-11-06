# Repository schema

This file defines the common structure for notes in the research repository.

The schema is intended to make the repository queryable, reviewable and safe to use with LLM-assisted workflows.

Use `docs/Lifecycle_states.md` for valid combinations of `status`, `analysis_state` and `review_status`. Use `docs/Needs_semantic_contract.md` for the distinction between object identity, formulations, contexts, evidence, value and fulfilment. The contract adds no mandatory fields.

## General rules

Every structured note should have YAML frontmatter.

Every note should have:

```yaml
type:
id:
status:
analysis_state:
evidence_strength:
confidence:
creation_mode:
llm_generated:
human_reviewed:
review_status:
change_level:
tags:
```

Use lower case values for controlled fields unless the ID convention requires capitals.

## Core model

The repository distinguishes between evidence and analysis.

Evidence is captured as close to the source as possible.

Analysis objects are interpreted research objects created from evidence, researcher judgement and synthesis. They include user needs, civic needs, behaviours, pain points, insights, themes, journeys and opportunities.

Persona and segment models are deferred during the current MVP. The `persona` type remains reserved for future development, but canonical persona objects should not be created until the modelling approach is documented.

The repository should support fast creation and incremental refinement of analysis objects without losing rigour.

```text
fast creation, slow validation
```

LLMs may create, decompose, merge, refactor, link and incrementally update analysis objects within task authorisation, provided the work remains status-controlled, evidence-linked where possible, and material changes are recorded. Candidates can already support appropriately qualified exploration; validation is not a prerequisite for all use or a claim of perfect truth.

## Controlled values

### `status`

```yaml
status: captured | draft | assumption | reviewed | validated | deprecated
```

- `captured`: evidence or information has been recorded but not synthesised.
- `draft`: synthesis has been drafted but not reviewed.
- `assumption`: plausible but not directly supported by sufficient evidence.
- `reviewed`: checked by a human reviewer, but not necessarily validated.
- `validated`: supported by evidence and approved for a stated scope of use as a reliable finding, still open to challenge.
- `deprecated`: superseded, withdrawn or no longer recommended for use.

### `analysis_state`

```yaml
analysis_state: captured | placeholder | candidate | drafted | evidence_linked | reviewed | validated | deprecated
```

- `captured`: source material or evidence has been captured.
- `placeholder`: an item holds a possible pattern or object, not yet fully formulated.
- `candidate`: useful provisional knowledge needing further analysis, evidence or refinement.
- `drafted`: formulated into a usable draft.
- `evidence_linked`: has at least one explicit evidence link, whose scope must still be assessed.
- `reviewed`: a human has reviewed the item.
- `validated`: reviewed and sufficiently supported for the stated use.
- `deprecated`: superseded, rejected or withdrawn.

`analysis_state` describes development of the analysis. `status` describes the current claim status. Neither implies that a human need has been fulfilled in practice.

### `evidence_basis`

```yaml
evidence_basis: none | indicative | traceable | substantiated | validated
```

Use the current evidence/lifecycle guidance. A traceable source is not automatically direct support for every clause or relationship. Do not label a basis validated without explicit human review.

### `evidence_strength`

```yaml
evidence_strength: none | weak | moderate | strong
```

- `none`: no supporting evidence is linked.
- `weak`: limited, indirect or single-source evidence.
- `moderate`: multiple relevant evidence items, but with limitations.
- `strong`: multiple credible evidence items across relevant sources or methods.

These are existing pragmatic categories, not a numerical evidence score or automatic source-count formula.

### `confidence`

```yaml
confidence: low | medium | high
```

Confidence is the researcher's current judgement about reliability, not a substitute for evidence strength.

### `creation_mode`

```yaml
creation_mode: manual | llm_assisted | imported | migrated
```

- `manual`: created directly by a human contributor.
- `llm_assisted`: created or materially shaped with LLM support.
- `imported`: brought in from another source or system.
- `migrated`: created or updated as part of repository restructuring.

### `review_status`

```yaml
review_status: not_reviewed | needs_review | reviewed | rejected
```

Reviewed/validated declarations require consistent `human_reviewed` and review metadata. Structural validation can check declared consistency, not prove that the review actually took place.

### `change_level`

```yaml
change_level: none | minor | material | major
```

- `none`: no meaningful change recorded.
- `minor`: spelling, formatting, metadata tidy-up or link correction.
- `material`: changes interpretation, wording, evidence links, confidence, status or evidence strength.
- `major`: substantially reframes, splits, merges, replaces or deprecates an item, changes validated content or affects published outputs.

### `need_level`

```yaml
need_level: capability | civic | experience | service | journey | task | page | interaction | content
```

Use the level to describe scope and aid navigation, not to impose a single universal hierarchy.

- `capability`: a human-development concern involving real opportunities, agency, affiliation or control.
- `civic`: institutional obligation, such as dignified access or redressability; keep `type: civic_need` distinct.
- `experience`: what the person needs to experience, preserve or recover.
- `service`: progress or protection across a service relationship.
- `journey`: a particular stage or transition.
- `task`: meaningful activity or comprehension in a bounded task.
- `page`: what a bounded content context must help the person accomplish or comprehend.
- `interaction`: immediate progress or protection an interaction must enable.
- `content`: what a content item or explanation must help the person accomplish or comprehend.

`solution_requirement` appeared in older examples but is not an allowed user-need level in the existing validator/templates. Keep solution requirements as separately identified response proposals, not as needs. This correction reconciles the documentation with the existing allowed values; it does not migrate research records.

### `evidence_scope_fit`

```yaml
evidence_scope_fit: direct | partial | contextual | weak
```

- `direct`: evidence directly supports this level and wording.
- `partial`: supports part, but not the full formulation.
- `contextual`: helps explain context rather than establishing the need.
- `weak`: relevant but too indirect to rely on without more work.

This optional field should not claim direct fit when `evidence_basis` is none. Leave it unclaimed or record uncertainty in the body until assessed; preserve existing inconsistencies as review findings rather than inventing evidence.

### Boolean fields

```yaml
llm_generated: true | false
human_reviewed: true | false
anonymisation_checked: true | false
```

## ID conventions

Use stable IDs with uppercase prefixes and at least three numeric digits. Three digits are minimum padding, not a cap: `UN_999`, `UN_1000` and `UN_10000` are valid. Do not renumber, repad or recycle existing IDs. Check uniqueness across the type namespace and concurrent work before allocation.

```text
RS_001     research study
EVID_001   evidence item
UN_001     user need
CN_001     civic need
BEH_001    behaviour
PP_001     pain point
INS_001    insight
TH_001     theme
PER_001    persona (reserved)
JNY_001    journey
OPP_001    opportunity
REV_001    review note
CLM_001    claim
VAL_001    value dimension
```

See `docs/Naming_and_linking_contract.md` for readable filenames and links.

## Common fields for analysis objects

Use these across relevant types:

```yaml
type:
id:
actor:
journey_stage:
status:
analysis_state:
evidence_basis:
evidence_strength:
confidence:
creation_mode:
llm_generated:
human_reviewed:
review_status:
change_level:
supersedes:
superseded_by:
related_evidence:
related_needs:
related_behaviours:
related_pain_points:
related_insights:
related_themes:
tags:
```

The current validator has a smaller required subset; use the appropriate template rather than treating every explanatory field as newly mandatory.

## Needs relationships and representations

```yaml
need_level:
parent_needs:
child_needs:
related_capabilities:
related_civic_needs:
related_rights:
related_outcomes:
evidence_scope_fit:
wording_sensitivity: low | medium | high
```

Do not force every link to be complete. Multiple parents and other higher-level links are allowed. Do not infer causation, legal applicability or evidence strength from a graph path. Generic related fields are navigational; explain important relation claims, contexts and tensions in the body.

The stable ID, canonical `need`, `short_name`, authentic language and role-specific presentations have different functions. The canonical formulation persists until deliberately revised; saved views refer to the revisions used. Context need not be part of the sentence when the underlying need recurs unchanged.

Optional body sections may capture contextual manifestations, expected/realised value, fulfilment conditions, indicators, tensions and rights/capability anchors. No new mandatory frontmatter fields are introduced for these.

## Object types

The following are explanatory shapes; use the actual templates for complete records and select values rather than copying option lists.

### Research study

```yaml
type: research_study
id: RS_001
title:
research_lead:
date_range:
method:
participants:
setting:
status: captured | reviewed | validated | deprecated
analysis_state: captured | reviewed | validated | deprecated
creation_mode: manual | llm_assisted | imported | migrated
related_evidence:
related_insights:
tags:
```

A research study describes an activity or source collection, not raw identifiable data. A source catalogue entry is not automatically a fully analysed study.

### Evidence

```yaml
type: evidence
id: EVID_001
source_study: "[[RS_001]]"
evidence_kind: quote | observation | survey_result | statistic | document_extract | desk_research | professional_judgement
actor:
context:
journey_stage:
date_collected:
method:
sensitivity: low | medium | high
anonymisation_checked: true | false
confidence: low | medium | high
status: captured | reviewed | deprecated
analysis_state: captured | reviewed | deprecated
creation_mode: manual | llm_assisted | imported | migrated
related_needs:
related_behaviours:
related_pain_points:
related_insights:
tags:
```

Preserve source meaning and voice. Participant quotations must not be silently rewritten. Classify mediated accounts, inspection conclusions, assumptions and direct experience appropriately.

### User need

```yaml
type: user_need
id: UN_001
short_name:
actor:
journey_stage:
need:
need_level: capability | civic | experience | service | journey | task | page | interaction | content
parent_needs:
child_needs:
related_capabilities:
related_civic_needs:
related_rights:
related_outcomes:
evidence_scope_fit: direct | partial | contextual | weak
wording_sensitivity: low | medium | high
status: draft | assumption | reviewed | validated | deprecated
analysis_state: placeholder | candidate | drafted | evidence_linked | reviewed | validated | deprecated
evidence_basis: none | indicative | traceable | substantiated | validated
evidence_strength: none | weak | moderate | strong
confidence: low | medium | high
creation_mode: manual | llm_assisted | imported | migrated
related_evidence:
related_behaviours:
related_pain_points:
related_insights:
importance: low | medium | high
llm_generated: true | false
human_reviewed: true | false
review_status: not_reviewed | needs_review | reviewed | rejected
change_level: none | minor | material | major
supersedes:
superseded_by:
tags:
```

A need describes what a person needs to achieve, preserve, recover, avoid or change. It does not automatically assign all enabling work to that person. Use `short_name` for mapping and the canonical `need` for the current shared interpretation. Do not collapse experience, journey and detailed needs or force every context into their wording.

### Civic need

Use `Templates/Civic_need_template.md`, prefix `CN_` and `type: civic_need`. The content field is `civic_need`, not `need`. Civic needs express what institutions or systems must uphold; they are not interchangeable with a person's need. Distinguish normative commitments from claims of applicable legal obligations.

### Behaviour

```yaml
type: behaviour
id: BEH_001
actor:
journey_stage:
behaviour:
status: draft | assumption | reviewed | validated | deprecated
analysis_state: placeholder | candidate | drafted | evidence_linked | reviewed | validated | deprecated
evidence_strength: none | weak | moderate | strong
confidence: low | medium | high
creation_mode: manual | llm_assisted | imported | migrated
related_evidence:
related_needs:
related_pain_points:
related_insights:
llm_generated: true | false
human_reviewed: true | false
review_status: not_reviewed | needs_review | reviewed | rejected
change_level: none | minor | material | major
supersedes:
superseded_by:
tags:
```

Describe what a person does, avoids, repeats, compensates for or attempts. Distinguish observed from inferred behaviour.

### Pain point

```yaml
type: pain_point
id: PP_001
actor:
journey_stage:
pain_point:
status: draft | assumption | reviewed | validated | deprecated
analysis_state: placeholder | candidate | drafted | evidence_linked | reviewed | validated | deprecated
evidence_strength: none | weak | moderate | strong
confidence: low | medium | high
creation_mode: manual | llm_assisted | imported | migrated
related_evidence:
related_needs:
related_behaviours:
related_insights:
llm_generated: true | false
human_reviewed: true | false
review_status: not_reviewed | needs_review | reviewed | rejected
change_level: none | minor | material | major
supersedes:
superseded_by:
tags:
```

Describe a barrier, burden, risk, harm, friction or structural problem. Resolution of a pain is not necessarily fulfilment of every linked need. Preserve resolved, dormant or recurring conditions through the applicable lifecycle guidance rather than treating them as irrelevant history.

### Insight

```yaml
type: insight
id: INS_001
title:
actor:
journey_stage:
status: draft | assumption | reviewed | validated | deprecated
analysis_state: placeholder | candidate | drafted | evidence_linked | reviewed | validated | deprecated
evidence_strength: none | weak | moderate | strong
confidence: low | medium | high
creation_mode: manual | llm_assisted | imported | migrated
related_evidence:
related_needs:
related_behaviours:
related_pain_points:
related_themes:
claims:
llm_generated: true | false
human_reviewed: true | false
review_status: not_reviewed | needs_review | reviewed | rejected
change_level: none | minor | material | major
supersedes:
superseded_by:
tags:
```

An insight interprets why something may be happening and why it matters. Keep evidence, inference, alternatives and limitations distinct.

### Theme

```yaml
type: theme
id: TH_001
title:
status: draft | assumption | reviewed | validated | deprecated
analysis_state: placeholder | candidate | drafted | evidence_linked | reviewed | validated | deprecated
evidence_strength: none | weak | moderate | strong
confidence: low | medium | high
creation_mode: manual | llm_assisted | imported | migrated
related_evidence:
related_needs:
related_behaviours:
related_pain_points:
related_insights:
llm_generated: true | false
human_reviewed: true | false
review_status: not_reviewed | needs_review | reviewed | rejected
change_level: none | minor | material | major
supersedes:
superseded_by:
tags:
```

A theme groups related material without validating everything within it.

### Opportunity

```yaml
type: opportunity
id: OPP_001
title:
actor:
journey_stage:
opportunity:
status: draft | assumption | reviewed | validated | deprecated
analysis_state: placeholder | candidate | drafted | evidence_linked | reviewed | validated | deprecated
evidence_strength: none | weak | moderate | strong
confidence: low | medium | high
creation_mode: manual | llm_assisted | imported | migrated
related_evidence:
related_needs:
related_behaviours:
related_pain_points:
related_insights:
llm_generated: true | false
human_reviewed: true | false
review_status: not_reviewed | needs_review | reviewed | rejected
change_level: none | minor | material | major
supersedes:
superseded_by:
tags:
```

An opportunity suggests an area to investigate, not a decision or commitment.

### Value dimension

Use `Templates/Value_dimension_template.md`, prefix `VAL_` and `type: value_dimension`. It records what matters when examining value, not a particular solution's score. Expected value, realised value and rights/capability compatibility require distinct reasoning.

### Review note

```yaml
type: review_note
id: REV_001
reviewed_item:
reviewer:
review_date:
review_outcome: approved | changes_requested | rejected | deferred
status:
analysis_state:
evidence_strength:
confidence:
change_level:
tags:
```

Use the complete template and common fields. State what the reviewer actually assessed; wording review does not certify fulfilment or every relationship.

## Entry-level changelog

Use `docs/Object_change_logs.md` and `docs/LLM_intervention_logging.md` proportionately. Record material changes to meaning, evidence, metadata, splitting, merger, supersession or review outcomes. Git and PR summaries provide the administrative edit history.

```markdown
## Changelog

- YYYY-MM-DD: Created as an LLM-assisted assumption. Analysis state: candidate. Evidence basis and strength: none. Review status: not_reviewed.
```

## Fast-moving, non-linear knowledge development

Objects can enter as partial knowledge and be linked backwards to evidence. Placeholder, candidate, drafted, evidence-linked and reviewed states are useful distinctions, not a mandatory conversion funnel. Not every useful object needs validation; none should be treated as perfect or universally applicable.

A need may remain valuable without recent editing. Make it visible, connected, scoped and evidence-aware. Deepen it when research or practical use requires it.

## Decomposition, merging and supersession

Expose meaningful constituent needs while retaining a useful parent. Use `parent_needs` and `child_needs` for that relationship. A contextual manifestation or audience view does not automatically require a new identity.

When an interpretation is actually replaced, split into successor objects or merged, preserve the original and explicitly record lineage:

```yaml
supersedes:
  - "[[UN_004]]"
superseded_by:
  - "[[UN_014]]"
change_level: major
```

The example shows available relationship fields, not an instruction to use both directions on every edit. Explain what changed and why, without promoting research status automatically.
