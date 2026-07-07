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
- PR #64 merged and established the current operating-layer readiness framing before high-volume ingestion resumes
- issue #66 now has a boundary proposal tying together the prompt/orchestration audit in #68, the specialised user-needs methodology audit in #69 and the public-safe user-needs surface proposal in #70

Active or pending before high-volume ingestion:

- complete issue #65 by creating a provisional documentation inventory by logical layer, authority category and semantic risk before any folder restructuring
- use the #66 boundary proposal to guide the public/private split between `civic-design-intelligence` and `design-intelligence-orchestration`
- replace or tighten high-risk public prompt and workflow surfaces with public-safe summaries
- create public-safe user-needs writing and quality summaries so the public repo remains intelligible without exposing protected methodology
- create or use private holding structures in `design-intelligence-orchestration` for protected ontology/navigation logic and advanced user-needs methodology
- use issue #71 to preserve or triage deferred roadmap detail from the stale backup without re-expanding protected detail in public
- only then start a small public-source ingestion pass using SEND pathway-planning material, and only where any private method stays private and public outputs remain evidence-linked and reviewable
- preserve locality, service-area and organisation context as sensemaking context, not as the primary meaning of user needs
- use public secondary research as traceable source material without turning this repository into a raw document archive
- create matching source records and selected evidence extracts in this repository for companion archive sources when they are used
- tighten validation only after the current object patterns have been used in practice

The repository should now move from normalising structure to finishing the minimum public/private boundary implementation needed for safe ingestion, then using the structure with real research again.

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
- The public knowledge model and protected orchestration layer should remain distinct unless there is an explicit publication decision.

First-class objects, especially user needs and civic needs, should remain persistent, traceable and supersedable.

Pain points should remain visible when resolved, dormant or at risk of recurring, because they can indicate coverage, regression risk and blocked value delivery.

## Stage 2: Establish minimum viable practice

Status: substantially complete for naming, metadata hygiene and PR practice; active for public/private boundary implementation and ingestion readiness.

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
13. Keep detailed LLM prompts, ingestion routines, ontology/navigation logic, advanced methodology and orchestration playbooks out of the public repository unless there is an explicit publication decision.
14. Keep private orchestration material in `happygeneralist/design-intelligence-orchestration`, not in hidden folders inside the public repository.
15. Keep public governance, source-use policy, object definitions, evidence/review/status meaning and contribution safety public enough for scrutiny and reuse.

## Stage 3: Stabilise naming, linking and documentation authority

Status: naming guardrails and documentation authority are in place enough for the current reset; documentation inventory remains active.

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

1. Complete issue #65 by creating a provisional documentation inventory by logical layer, authority category and semantic risk.
2. Use the inventory to decide whether section index pages or folders are needed.
3. Consider folder moves only after navigation/index and inventory work has been tested.
4. Use issue #71 to preserve useful deferred roadmap detail without restoring stale sequencing or protected method detail.

Do not create another broad filename or documentation-folder migration unless validation, Obsidian use or ingestion work reveals a concrete problem.

## Stage 4: Apply the public/private boundary

Status: boundary proposal posted; implementation planning active.

Issue #66 now provides the umbrella boundary proposal for the operating relationship between this public repository and `happygeneralist/design-intelligence-orchestration`. It draws on:

- #68 for prompt and orchestration exposure risk
- #69 for specialised user-needs methodology exposure risk
- #70 for the public-safe user-needs methodology surface

The private repository already exists. Its related issues cover the protected user-needs ontology boundary and the protected home for advanced user-needs methodology.

The public repository should contain:

- open civic/design intelligence knowledge objects
- public documentation needed for intelligibility, auditability, contribution and reuse
- public governance, source-use policy, object definitions and safety rules
- evidence, review, lifecycle and status meanings
- schemas and templates intended for public use
- source records, selected evidence extracts and reviewed/captured analysis objects
- public-safe summaries of higher-risk concepts where the public needs to know that the concept exists

The private orchestration repository should contain protected material used to operate, scale, navigate or improve the method beyond ordinary public contribution guidance.

Do not assume anything is protected if it is committed to the public repository, even in a hidden folder or ignored path.

## Stage 5: Public-safe summary work before ingestion

Status: next implementation step before any ingestion that depends on protected method.

The next public implementation work should be practical and small:

1. Create public-safe summaries for high-risk prompt and workflow files identified through #68 and #70.
2. Create public-safe user-needs writing and quality summaries from the #69 and #70 boundary work.
3. Keep the minimum public surface needed for object scrutiny, contribution and reuse.
4. Avoid expanding detailed user-needs methodology, quality tests, relationship/navigation logic, prompt catalogues or orchestration routines in public.
5. Leave advanced private method, ontology/navigation work and book/IP-adjacent method development to `design-intelligence-orchestration` or later human/IP review.

The public repo should not become too thin to audit. It should still explain what objects are, how evidence and review states work, what contributors must not overclaim, and how public outputs can be challenged or reused.

## Stage 6: Resume safe research ingestion

Status: blocked where ingestion depends on protected method; otherwise next recommended phase after the minimum boundary work is complete or deliberately deferred.

Ingestion remains blocked for any workflow that depends on:

- advanced user-needs methodology
- prompt catalogues
- orchestration routines
- relationship/navigation logic
- quality rubrics
- private ontology

Once the relevant boundary work is complete, start with one bounded public or explicitly authorised SEND pathway-planning source and create only the strongest useful objects first:

- source records
- selected evidence extracts
- behaviours
- pain points
- user needs
- civic needs, where relevant
- insights
- themes

The goal is to test whether the repository now supports useful research breakdown without creating naming debt, overclaiming confidence, flattening meaning, leaking private method or forcing immature material into the wrong schema.

Recommended next ingestion pass, once unblocked:

1. Select one bounded public or explicitly authorised source.
2. Use only public-safe guidance in the public repo.
3. Keep any protected method support private.
4. Create or confirm the source record before extracting evidence where the input is a public secondary source.
5. Capture selected evidence notes only where the material is useful and traceable.
6. Extract candidate needs, behaviours and pain points with conservative metadata.
7. Link each object back to evidence where possible.
8. Use `short_name` and filename conventions at creation time.
9. Preserve service, organisation and locality context where it appears in evidence, but do not encode it into canonical need wording unless it is intrinsic.
10. If the source exists in `civic-design-secondary-research`, record the source archive reference and update the companion evidence map.
11. Record meaning changes in object change logs only where meaning changes.
12. Use the PR summary for administrative cleanup and public-safe disclosure of LLM/private-method assistance.
13. Leave uncertain or loose material in `000_Inbox/`.

## Stage 7: Model context, locality and pattern sensemaking

Status: direction captured; defer schema until examples exist and the public/private boundary is stable.

The repository should support sensemaking over time.

A need may first be captured from local or service-specific evidence, but later be recognised as a wider pattern when similar evidence appears in other places, services or institutional contexts.

The first observed context should be preserved as evidence provenance. It should not permanently define the scope of the need unless the need is inherently place-specific or service-specific.

Near-term working rule:

```text
Capture lived-experience needs directly. Capture service areas, organisations and localities as context or mappings.
```

Do not build a full locality, service-area or organisation taxonomy until research examples show the minimum useful structure and the related boundary decisions are settled.

## Stage 8: Ingest public secondary research cautiously

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
-> raw or lightly processed public source material
-> source-level documentation
-> candidate extracts
-> evidence maps back to structured objects

civic-design-intelligence
-> source records, selected evidence extracts and structured knowledge objects
```

A secondary source should not directly become a user need.

Recommended chain:

```text
Ofsted report or secondary source
-> source record
-> selected evidence extracts
-> candidate needs, pain points, behaviours, civic needs and insights
-> cross-source patterns
```

Secondary evidence should be interpreted conservatively. An inspection finding, literature review or policy report may support a need or pain point, but it should not automatically validate one.

## Stage 9: Openness, licensing and protection

Status: public principle in place; protection-by-default applies to method-bearing material until later decisions are clearer.

The repository should remain open enough to support civic reuse, scrutiny and adoption. However, the project also needs an intentional boundary between:

- open civic knowledge layer
- controlled implementation layer
- protected orchestration layer

High-level safety guidance and public documentation can remain open where it helps users understand the repository without publishing the full operating method.

This should not block ingestion indefinitely. It should shape what is committed publicly during ingestion, where protected operating material is kept, and how public outputs are reviewed before commit.

## Stage 10: Update templates lightly

Status: general template SEND-default cleanup complete; future changes should follow ingestion evidence and boundary decisions.

After one or two ingestion passes, check whether templates need optional fields or prompts for:

```yaml
source_type:
evidence_type:
reported_voice:
source_archive_ref:
source_location:
```

Do not add complex event structures to every template yet.

Only require fields that are useful now. Optional fields should remain optional until the repository has more examples and the public/private boundary is stable.

## Current sequencing

Near-term sequence:

1. Complete issue #65: provisional documentation inventory before folder restructuring.
2. Use issue #66 as the public/private boundary proposal for implementation planning.
3. Create public-safe summaries for high-risk prompt and workflow files.
4. Create public-safe user-needs writing and quality summaries.
5. Establish the private holding structure in `design-intelligence-orchestration` for protected ontology/navigation logic and advanced user-needs methodology.
6. Use issue #71 to preserve deferred roadmap detail from the stale backup without reintroducing stale sequencing or protected method detail.
7. Decide whether section index pages or folders are needed before ingestion.
8. Resume ingestion with one bounded public or explicitly authorised source only when the relevant method can remain private and the public outputs remain intelligible, auditable and reusable.

The immediate priority is not a perfect repository structure. It is safe enough documentation authority, safe enough public/private separation and safe enough traceable ingestion.
