# Knowledge evolution implementation roadmap

Public-source reset note: the repository is currently in a public-source-first rebuild. Retained candidate knowledge objects should not be treated as evidence-linked until supported by public, openly licensed or explicitly authorised sources.

This roadmap describes a staged implementation approach for knowledge evolution, user need persistence, pain point recurrence, repository naming guardrails, safe research ingestion, context sensemaking, secondary research ingestion, documentation architecture, openness/protection boundaries and LLM intervention logging.

The aim is to establish enough operating discipline to support high-volume ingestion without creating heavy governance, semantic drift or accidental publication of protected orchestration methods.

## Current position: July 2026

The repository has moved through a substantial normalisation and reset pass.

Completed or substantially complete:

- user need `short_name` convention piloted and applied to early pathway-planning needs
- major filename normalisation across insights, user needs, evidence, research studies and early legacy notes
- validation filename warnings substantially reduced through focused migration PRs
- early user needs cleaned up and renamed using readable ID-prefixed filenames
- Obsidian-oriented naming pattern established: stable ID plus readable slug
- decision-shaped user needs captured as a user need shape rather than a separate Decision object
- LLM-assisted work rules strengthened to preserve evidence, status, review state and naming conventions
- companion public secondary-research repository created: `happygeneralist/civic-design-secondary-research`
- first companion source archive example created for the public-source ingestion workflow
- whole-system wording clarified so SEND is the initial worked domain, not the limit of the repository
- public Ofsted source example clarified as public inspection-report provenance, not proprietary material
- general templates cleaned so they do not apply SEND defaults unintentionally
- issue-first workflow guidance added for non-trivial scoped work
- documentation architecture plan added to reduce docs sprawl and clarify authority before broad file moves

Active or pending before high-volume ingestion:

- review and merge a provisional documentation authority map so contributors and LLM assistants can find source-of-truth guidance quickly
- review and merge a draft openness/protection model so detailed LLM prompts, ingestion routines and orchestration playbooks are not accidentally published
- create a provisional documentation inventory by logical layer, authority category and semantic risk before any folder restructuring
- define the private orchestration component boundary, including the proposed `design-intelligence-orchestration` component
- only then start a small public-source ingestion pass using SEND pathway-planning material
- preserve locality, service-area and organisation context as sensemaking context, not as the primary meaning of user needs
- use public secondary research as traceable source material without turning this repository into a raw document archive
- create matching source records and selected evidence extracts in this repository for companion archive sources when they are used
- tighten validation only after the current object patterns have been used in practice

The repository should now move from normalising structure to finishing the minimum operating layer needed for safe ingestion, then using the structure with real research again.

## Roadmap cursor

Use `docs/Roadmap_cursor.md` as the current operational pointer.

The cursor should answer:

- what phase the repository is in now
- what is next
- what has intentionally been deferred
- what must not be overbuilt yet

Update the cursor after each meaningful roadmap shift, not after every administrative PR.

## Stage 1: Agree the model

Status: substantially complete; keep refining through use.

Core distinctions:

- Git history is the technical audit trail.
- Object change logs are the human-readable knowledge evolution trail.
- LLM intervention logs are the semantic-risk and governance trail.
- Issues define purpose, scope, out of scope and acceptance criteria for non-trivial work.
- Filenames support human and Obsidian use, but frontmatter is the queryable data contract.
- Evidence has an origin, needs have an applicability horizon and patterns emerge over time.
- Public secondary sources are source material; selected extracts become evidence objects.
- The companion secondary-research repository is a source archive, not a competing intelligence repository.
- Documentation architecture helps people and LLM assistants find the right authority; it is not a reason to delay ingestion indefinitely.
- The open knowledge model and protected orchestration layer should remain distinct until the openness/licensing model is clearer.

First-class objects, especially user needs and civic needs, should remain persistent, traceable and supersedable.

Pain points should remain visible when resolved, dormant or at risk of recurring, because they can indicate coverage, regression risk and blocked value delivery.

## Stage 2: Establish minimum viable practice

Status: substantially complete for naming, metadata hygiene and PR practice; active for documentation authority, operating-layer separation and ingestion.

Minimum viable practice:

1. Use issues for non-trivial scoped work.
2. Use PR summaries for administrative migration batches.
3. Add lightweight object change logs only where meaning changes.
4. Use LLM intervention logs only for material semantic risk.
5. Treat resolved or dormant pain points as useful service intelligence, not waste.
6. Use the naming and linking contract when creating, renaming or linking structured notes.
7. Preserve Obsidian usability through readable filenames, aliases where needed and resolvable wikilinks.
8. Treat frontmatter as the future API/database ingestion contract.
9. Capture lived experience first, then map service, organisation and locality context around it.
10. Keep structured source records, evidence extracts and derived knowledge objects in this repository.
11. Keep raw or lightly processed public secondary research in `happygeneralist/civic-design-secondary-research` where useful.
12. Use companion `evidence-map.md` files to link public source folders back to structured source, evidence and analysis objects in this repository.
13. Keep detailed LLM prompts, ingestion routines and orchestration playbooks out of the public repository unless there is an explicit publication decision.
14. Keep private orchestration material in a separate private component, not in hidden folders inside the public repository.

## Stage 3: Stabilise naming, linking and documentation authority

Status: naming guardrails merged; documentation authority mapping and inventory still active.

The repository should avoid repeated migrations by making correctness a creation-time habit.

Minimum viable guardrails:

- structured notes must use stable frontmatter IDs
- filenames must begin with the frontmatter ID
- readable filename slugs should support Obsidian search and graph use
- user need slugs should derive from `short_name`, not the full canonical `need`
- aliases should preserve old ID-only links during and after migrations
- LLM-assisted work must check naming rules before creating new files
- contributors and LLM assistants should use the documentation map to find the right source-of-truth guidance
- contributors and LLM assistants should use the documentation inventory to distinguish current guidance, historical records, exploratory material and high-risk semantic documents

Useful next actions:

1. Merge or replace the provisional documentation authority map.
2. Complete issue #65 by creating a provisional documentation inventory by logical layer, authority category and semantic risk.
3. Use the inventory to decide whether section index pages or folders are needed.
4. Consider folder moves only after navigation/index and inventory work has been tested.

Do not create another broad filename or documentation-folder migration unless validation, Obsidian use or ingestion work reveals a concrete problem.

## Stage 4: Define the private orchestration component

Status: open.

Issue #66 should define the private orchestration component boundary before detailed prompts or operating playbooks are used for high-volume ingestion.

Working component name:

```text
design-intelligence-orchestration
```

This component should be reusable beyond the current SEND and public-service context. It may support user needs, civic needs, organisational needs, evidence structuring and design-intelligence workflows across public, civic and private-sector settings.

The public repository should contain:

- open civic/design intelligence knowledge objects
- public documentation
- safe principles and method summaries
- schemas and templates intended for public use
- source records, selected evidence extracts and reviewed/captured analysis objects

The private orchestration component may contain:

- full LLM system instructions
- ingestion prompts
- transformation prompts
- evidence decomposition routines
- object reconciliation prompts
- evaluation rubrics
- assistant orchestration patterns
- batch-processing methods
- private operational playbooks
- workflow checklists for high-volume ingestion

Do not assume anything is protected if it is committed to the public repository, even in a hidden folder or ignored path.

## Stage 5: Resume safe research ingestion

Status: next recommended phase after the minimum documentation-authority, documentation-inventory and private-orchestration boundary work is complete or deliberately deferred.

Use `docs/Safe_research_ingestion_MVP.md`, `docs/Ingestion_slice_workflow.md`, `docs/Input_and_evidence_classification.md`, `docs/Source_capture_workflow.md`, `docs/Secondary_research_ingestion.md`, `docs/User_needs_writing_rules.md`, `docs/Source_use_policy.md` and `docs/Evidence_standards.md` as the immediate public operating guide.

Start with one bounded public or explicitly authorised SEND pathway-planning source and create only the strongest useful objects first:

- source records
- selected evidence extracts
- behaviours
- pain points
- user needs
- civic needs, where relevant
- insights
- themes

The goal is to test whether the repository now supports useful research breakdown without creating naming debt, overclaiming confidence, flattening meaning or forcing immature material into the wrong schema.

Recommended next ingestion pass:

1. Select one bounded public or explicitly authorised source.
2. Classify input type, evidence voice and overclaiming risk.
3. Create or confirm the source record before extracting evidence where the input is a public secondary source.
4. Capture selected evidence notes only where the material is useful and traceable.
5. Extract candidate needs, behaviours and pain points with conservative metadata.
6. Link each object back to evidence where possible.
7. Use `short_name` and filename conventions at creation time.
8. Preserve service, organisation and locality context where it appears in evidence, but do not encode it into canonical need wording unless it is intrinsic.
9. If the source exists in `civic-design-secondary-research`, record the source archive reference and update the companion evidence map.
10. Record meaning changes in object change logs only where meaning changes.
11. Use the PR summary for administrative cleanup.
12. Leave uncertain or loose material in `000_Inbox/`.

## Stage 6: Model context, locality and pattern sensemaking

Status: direction captured; defer schema until examples exist.

The repository should support sensemaking over time.

A need may first be captured from local or service-specific evidence, but later be recognised as a wider pattern when similar evidence appears in other places, services or institutional contexts.

The first observed context should be preserved as evidence provenance. It should not permanently define the scope of the need unless the need is inherently place-specific or service-specific.

Near-term working rule:

```text
Capture lived-experience needs directly. Capture service areas, organisations and localities as context or mappings.
```

Do not build a full locality, service-area or organisation taxonomy until research examples show the minimum useful structure.

## Stage 7: Ingest public secondary research cautiously

Status: direction captured; first companion archive source exists.

The companion source archive is:

```text
happygeneralist/civic-design-secondary-research
```

The first source example is:

```text
SRC_001_ofsted_essex_area_send_inspection_jan_2026
```

This is a public Ofsted inspection-report example, not proprietary council, employer or unpublished research material.

The recommended split is:

```text
civic-design-secondary-research
→ raw or lightly processed public source material
→ source-level documentation
→ candidate extracts
→ evidence maps back to structured objects

civic-design-intelligence
→ source records, selected evidence extracts and structured knowledge objects
```

A secondary source should not directly become a user need.

Recommended chain:

```text
Ofsted report or secondary source
→ source record
→ selected evidence extracts
→ candidate needs, pain points, behaviours, civic needs and insights
→ cross-source patterns
```

Secondary evidence should be interpreted conservatively. An inspection finding, literature review or policy report may support a need or pain point, but it should not automatically validate one.

## Stage 8: Openness, licensing and protection

Status: draft position open for review.

The repository should remain open enough to support civic reuse, scrutiny and adoption. However, the project also needs an intentional boundary between:

- open civic knowledge layer
- controlled implementation layer
- protected orchestration layer

Until this model is agreed, avoid committing detailed LLM ingestion prompts, full system instructions, orchestration playbooks, evaluation rubrics or automation recipes to the public repository.

High-level safety guidance and public documentation can remain open where it helps users understand the repository without publishing the full operating method.

This should not block ingestion indefinitely. It should shape what is committed publicly during ingestion and where protected operating material is kept.

## Stage 9: Update templates lightly

Status: general template SEND-default cleanup complete; future changes should follow ingestion evidence.

After one or two ingestion passes, check whether templates need optional fields or prompts for:

```yaml
source_type:
evidence_type:
reported_voice:
source_archive_ref:
source_location:
```

Do not add complex event structures to every template yet.

Only require fields that are useful now. Optional fields should remain optional until the repository has more examples.

## Current sequencing

Near-term sequence:

1. Merge or replace the provisional documentation authority map.
2. Merge or replace the draft openness/protection model.
3. Complete issue #65: provisional documentation inventory before folder restructuring.
4. Complete issue #66: define the private orchestration component boundary.
5. Decide whether section index pages or folders are needed before ingestion.
6. Resume ingestion with one bounded public or explicitly authorised source.

The immediate priority is not a perfect repository structure. It is safe enough documentation authority, safe enough operating-layer separation and safe enough traceable ingestion.
