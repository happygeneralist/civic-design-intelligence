# Knowledge evolution implementation roadmap

This roadmap describes a staged implementation approach for knowledge evolution, user need persistence, pain point recurrence, repository naming guardrails, safe research ingestion, context sensemaking and LLM intervention logging.

The aim is to establish useful governance without slowing down the current research migration work.

## Current position: June 2026

The repository has moved through a substantial normalisation pass.

Completed or substantially complete:

- user need `short_name` convention piloted and applied to early pathway-planning needs
- major filename normalisation across insights, user needs, evidence, research studies and early legacy notes
- validation filename warnings substantially reduced through focused migration PRs
- early user needs `UN_001` to `UN_004` cleaned up and renamed using readable ID-prefixed filenames
- Obsidian-oriented naming pattern established: stable ID plus readable slug
- decision-shaped user needs captured as a user need shape rather than a separate Decision object
- LLM-assisted work rules strengthened to preserve evidence, status, review state and naming conventions

Active or pending:

- use the naming contract for all future structured objects
- start a small safe-ingestion pass using SEND pathway-planning research
- preserve locality, service-area and organisation context as sensemaking context, not as the primary meaning of user needs
- tighten validation only after the current object patterns have been used in practice

The repository should now move from normalising existing structure to using the structure with real research.

## Roadmap cursor

Use `docs/Roadmap_cursor.md` as the current operational pointer.

The cursor should answer:

- what phase the repository is in now
- what is next
- what has intentionally been deferred
- what must not be overbuilt yet

Update the cursor after each meaningful roadmap shift, not after every administrative PR.

## Stage 1: Agree the model

Status: mostly complete.

Review and agree the core distinctions:

- Git history is the technical audit trail.
- Object change logs are the human-readable knowledge evolution trail.
- LLM intervention logs are the semantic-risk and governance trail.
- Filenames support human and Obsidian use, but frontmatter is the queryable data contract.
- Evidence has an origin, needs have an applicability horizon and patterns emerge over time.

Agree that first-class objects, especially user needs, should be persistent, traceable and supersedable.

Agree that pain points should remain visible when resolved, dormant or at risk of recurring, because they can indicate coverage, regression risk and blocked value delivery.

## Stage 2: Establish minimum viable practice

Status: substantially complete for naming, metadata hygiene and PR practice; still active for ingestion.

Start with lightweight working rules before changing the schema.

Minimum viable practice:

1. Use PR summaries for administrative migration batches.
2. Add lightweight object change logs only where meaning changes.
3. Start with user needs as the first-class object requiring change-log discipline.
4. Do not create change events for metadata cleanup.
5. Use LLM intervention logs only for material semantic risk.
6. Treat resolved or dormant pain points as useful service intelligence, not waste.
7. Use the naming and linking contract when creating, renaming or linking structured notes.
8. Preserve Obsidian usability through readable filenames, aliases where needed and resolvable wikilinks.
9. Treat frontmatter as the future API/database ingestion contract.
10. Capture lived experience first, then map service, organisation and locality context around it.

## Stage 3: Stabilise naming and linking guardrails

Status: current guardrails merged; procedural adoption ongoing.

The repository should avoid repeated filename migrations by making naming correctness a creation-time habit.

Minimum viable guardrails:

- structured notes must use stable frontmatter IDs
- filenames must begin with the frontmatter ID
- readable filename slugs should support Obsidian search and graph use
- user need slugs should derive from `short_name`, not the full canonical `need`
- aliases should preserve old ID-only links during and after migrations
- LLM-assisted work must check naming rules before creating new files

Useful next actions:

1. Add a short pointer to the naming contract from `docs/Obsidian_workflow.md`.
2. Add a short pointer from `docs/Repository_validation.md` explaining which naming rules are already checked and which remain procedural.
3. Consider a later validator rule for user needs where the slug diverges from `short_name`, but only after more examples exist.

Do not create another broad filename migration unless validation or Obsidian use reveals a concrete problem.

## Stage 4: Start safe research ingestion

Status: next recommended phase.

Use `docs/Safe_research_ingestion_MVP.md` as the immediate operating guide.

Start with a small SEND pathway-planning research sample and create only the strongest useful objects first:

- evidence
- behaviours
- pain points
- user needs
- civic needs, where relevant
- insights
- themes

The goal is to test whether the repository now supports useful research breakdown without creating naming debt, overclaiming confidence or forcing immature material into the wrong schema.

Recommended first ingestion pass:

1. Select one bounded research source or extract.
2. Capture evidence notes only where the material is useful and anonymised.
3. Extract candidate needs, behaviours and pain points with conservative metadata.
4. Link each object back to evidence where possible.
5. Use `short_name` and filename conventions at creation time.
6. Preserve service, organisation and locality context where it appears in evidence, but do not encode it into canonical need wording unless it is intrinsic.
7. Record meaning changes in object change logs only where meaning changes.
8. Use the PR summary for administrative cleanup.
9. Leave uncertain or loose material in `000_Inbox/`.

## Stage 5: Model context, locality and pattern sensemaking

Status: direction captured; defer schema until examples exist.

The repository should support sensemaking over time.

A need may first be captured from local or service-specific evidence, but later be recognised as a wider pattern when similar evidence appears in other places, services or institutional contexts.

The first observed context should be preserved as evidence provenance. It should not permanently define the scope of the need unless the need is inherently place-specific or service-specific.

Use `docs/Context_and_pattern_sensemaking.md` as the current concept note.

Near-term working rule:

```text
Capture lived-experience needs directly. Capture service areas, organisations and localities as context or mappings.
```

Possible future dimensions include:

```yaml
evidence_location:
locality_contexts:
service_contexts:
organisation_contexts:
applicability_scope:
pattern_status:
```

Do not add these as required fields yet.

During the first ingestion pass, simply observe where the distinction matters:

- where evidence came from
- whether the need appears local, service-specific or potentially reusable
- whether similar needs may recur across service areas
- whether a local finding may indicate a wider public-service pattern
- whether a need is genuinely place-specific

This layer should help the repository answer:

- Which needs started as local but recur across places?
- Which needs appear across multiple service areas?
- Which local findings may indicate national design or policy issues?
- Which national assumptions are contradicted by local evidence?
- Which operational areas share the same lived-experience need?

Do not build a full locality, service-area or organisation taxonomy until research examples show the minimum useful structure.

## Stage 6: Update templates lightly

Status: do after one or two ingestion passes.

Start with user needs only.

Update the user need template to include:

```markdown
## Change log

- YYYY-MM-DD: Created/captured. Source: [study/evidence/insight]. Status: captured.
```

Also check whether templates should include a creation-time naming checklist or a link to `docs/Naming_and_linking_contract.md`.

Do not add complex event structures to every template yet.

Possible optional frontmatter additions for user needs:

```yaml
lifecycle_state: active
maturity_state: captured
last_meaningful_change:
supersedes:
superseded_by:
deprecation_reason:
```

Only require fields that are useful now. Optional fields should remain optional until the repository has more examples.

Avoid adding `version` until there is a clear rule for when it increments. If versioning is introduced later, increment only for material or major meaning changes, not administrative edits.

## Stage 7: Add LLM operating rules

Status: partly complete; continue through practice.

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

Add the rule that LLMs must not mark objects as validated or reviewed unless a human has explicitly completed that review.

Also require LLMs to follow the naming and linking contract before creating or renaming structured notes.

## Stage 8: Create the change-events folder

Status: defer until ingestion creates real examples.

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
- pain point resolution, dormancy or recurrence-risk changes
- evidence-basis changes
- review or validation decisions

Do not log administrative changes here.

Treat the folder as optional and experimental until real examples show what needs to be validated.

## Stage 9: Add pain point recurrence fields cautiously

Status: defer until more pain point examples exist.

Once examples exist, update the pain point template with optional fields such as:

```yaml
lifecycle_state: active | resolved | dormant | deprecated
resolution_state: unresolved | partially_addressed | addressed_currently | no_longer_observed
recurrence_risk: low | medium | high
recurrence_conditions:
```

Do not require these immediately for all existing pain points.

Use them first where they support product/service analysis, such as identifying unresolved pain, value blockers or recurrence risk.

## Stage 10: Add validator checks cautiously

Status: future work.

Only add validator rules once the pattern has been tested manually.

Possible future checks:

- if `lifecycle_state: superseded`, require `superseded_by`
- if `lifecycle_state: deprecated`, require `deprecation_reason`
- if `lifecycle_state: dormant`, allow but do not require `recurrence_risk`
- if `semantic_change_review: needs_review`, require `review_status: needs_review`
- if `last_change_actor: llm_assisted` and `change_level: material`, require either a PR-level LLM note or a linked change event
- if a structured filename does not start with its frontmatter `id`, warn or fail depending on validation mode
- if a user need has `short_name`, check that the readable filename slug broadly follows it
- if aliases are removed, check that old links no longer depend on them
- if `applicability_scope` or `pattern_status` are introduced later, check they do not overclaim evidence maturity

Avoid strict validation too early. The goal is to support research governance, not block useful work with premature schema constraints.

## Stage 11: Query and reporting layer

Status: future work after ingestion.

Once examples exist, build queries or scripts to report:

- user needs by maturity
- superseded and deprecated needs
- LLM-assisted material changes awaiting review
- objects with evidence basis changes
- unresolved pain points
- dormant pain points that may recur
- pain points blocking value delivery
- needs that underpin product or service decisions
- validated needs not yet covered by interventions or service responses
- objects with missing `short_name` where one is required for mapping
- objects with unresolved links or missing aliases after rename
- needs first observed locally that later recur across places
- needs that appear across multiple service areas
- local evidence that may indicate national design or policy issues

This is where the strategy becomes a source of product and service intelligence.

## Stage 12: Prepare for future data/API layer

Status: future architecture work; do not build yet.

Before building an API or database layer, define a lightweight export contract:

- which folders are canonical object collections
- which frontmatter fields are required for each object type
- which fields are controlled values
- how links resolve from wikilinks, IDs and aliases
- how lifecycle, review state and evidence maturity are represented
- how context mappings are represented without making them canonical meaning
- how supersession and deprecation are represented
- how generated views should distinguish evidence from synthesis

The repository should remain useful as Markdown and Obsidian first. A database or API should be an additional layer over the same knowledge objects, not a competing source of truth.

## Recommended next implementation PRs

Recommended immediate PRs after the current naming guardrail work:

1. Start one bounded safe-ingestion PR using a SEND pathway-planning research extract.
2. During ingestion, test whether locality, service and organisation context can be captured as lightweight mappings without distorting need wording.
3. After that ingestion PR, review which template changes are actually needed.
4. Only then consider whether any context fields or validator checks should be introduced.

Avoid adding strict validator rules until after the first ingestion pass tests the conventions.

## What not to do yet

Do not immediately:

- create detailed change logs for every existing object
- require LLM event logs for every administrative migration
- force every template to include complex history structures
- build a central ledger before there are real examples
- make the validator enforce rules before the team understands the workflow
- add versioning before there is a clear version-increment rule
- treat resolved pain points as if they should be deleted
- start an API/database layer before the frontmatter contract is stable enough
- do another broad filename migration without a concrete validation or Obsidian problem
- create a full locality, service-area or organisation taxonomy before the repository has worked examples
- treat the first observed local context as the permanent boundary of a need

## Success criteria

This system is working when:

- user needs can evolve without losing their lineage
- deprecated, resolved or dormant pain points remain historically visible
- LLM-assisted semantic changes are reviewable
- Git is not duplicated inside notes
- future analysis can distinguish mature knowledge from unreviewed synthesis
- dashboards can show unresolved pain, recurrence risk and blocked value delivery
- Obsidian links, aliases, Bases and readable filenames support day-to-day use
- frontmatter can support future data/API ingestion without scraping meaning from filenames
- LLM-assisted work can create new notes without introducing naming or link debt
- local evidence can contribute to wider pattern recognition without losing provenance
- reusable lived-experience needs can be mapped to multiple service, organisation and locality contexts
- the process is light enough that people actually use it
