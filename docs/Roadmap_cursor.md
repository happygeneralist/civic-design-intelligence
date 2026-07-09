# Roadmap cursor

Last updated: 2026-07-09

This cursor records the current operational focus for the repository.

It is intentionally shorter than the full roadmap. Use it to decide what to do next, what to avoid overbuilding, and when the roadmap has moved to a new phase.

## Current phase

The repository is in an ingestion-readiness reset before high-volume research ingestion resumes.

The aim is not to keep refining the repository indefinitely. The aim is to finish the minimum operating scaffolding needed so that a larger volume of public or explicitly authorised material can be ingested without avoidable documentation drift, unclear source-of-truth guidance, or accidental publication of protected orchestration methods.

Recent work has completed or substantially advanced:

- whole-system wording so the repository is framed as a reusable design intelligence system, with SEND pathway planning as the initial worked domain
- public-source clarification for the Ofsted Essex source example
- removal of SEND defaults from general templates
- issue-first workflow guidance for non-trivial work
- a documentation architecture plan for reducing docs sprawl and clarifying authority
- an openness and protection model for distinguishing open civic knowledge from protected LLM orchestration
- PR #64, which created the current operating-layer readiness framing before high-volume ingestion resumes
- issue #66, which now has a boundary proposal tying together the prompt/orchestration audit in #68, the user-needs methodology audit in #69 and the public-safe surface proposal in #70
- PR #73, which replaced the public LLM research breakdown prompt catalogue with a public-safe summary
- PR #74, which replaced the public research breakdown workflow with a public-safe summary
- PR #76, which added a public-safe user-needs quality summary
- private orchestration PR #5, which moved the detailed research breakdown prompt catalogue into `design-intelligence-orchestration` as protected draft material
- private orchestration PR #6, which moved the detailed research breakdown workflow into `design-intelligence-orchestration` as protected draft material
- private orchestration PR #7, which created a protected holding structure for advanced user-needs quality method material

The prompt, workflow and user-needs quality boundary pairs are now in place at MVP level. The public repository has summaries needed for auditability and contribution, while detailed method-bearing material has protected homes in `design-intelligence-orchestration`.

## Active focus

The next focus is:

```text
Finish documentation inventory and deferred-roadmap triage, then select one bounded public-source ingestion slice for SEND pathway planning.
```

This means:

- use the merged documentation authority and openness/protection work as the current baseline
- treat issue #66 as the umbrella boundary decision between this public repository and `happygeneralist/design-intelligence-orchestration`
- keep basic public governance, source-use policy, object definitions, evidence/review/status meaning and contribution safety public
- treat high-risk public prompt, general research-breakdown workflow and user-needs quality surfaces as addressed at MVP level unless later audit finds more exposure
- keep detailed user-needs methodology, quality tests, relationship/navigation logic, prompt catalogues and orchestration routines private unless explicitly published
- complete issue #65 by creating a provisional documentation inventory before any folder restructuring
- preserve deferred roadmap detail through issue #71 rather than re-expanding stale or protected material in this public roadmap
- avoid broad governance work beyond the minimum needed to make ingestion safe
- resume ingestion only with one bounded public or explicitly authorised source, and only where public outputs remain auditable

## Immediate next actions

1. Complete issue #65: create a provisional documentation inventory before folder restructuring.
2. Use issue #71 to preserve or triage deferred roadmap detail from the stale backup, without reintroducing protected method into the public roadmap.
3. Select one bounded public or explicitly authorised source for the next ingestion slice.
4. Run the ingestion slice conservatively, using public-safe guidance in CDI and keeping any protected method support private.
5. Update this cursor after the ingestion slice has tested whether the current boundary and documentation authority are sufficient in practice.

## Documentation and operating-layer readiness

Before the next ingestion slice, the repository should have:

- a usable documentation authority map
- a provisional inventory of current docs by logical layer, authority category and semantic risk
- a clear rule that folders or file moves are a separate future PR, not part of the authority-map work
- a clear public/private boundary for LLM orchestration material and advanced user-needs methodology
- an agreed private location for detailed prompts, protected methodology, relationship/navigation logic and orchestration routines
- public summaries that keep the repository intelligible, auditable and reusable without exposing the protected operating method

This does not require a perfect long-term IA. It requires enough clarity to prevent the next ingestion work from making the public repository messier or exposing material that should remain protected.

## Current ingestion emphasis once readiness is complete

During the next ingestion slice, test whether the repository can connect public-source material, evidence extracts, user needs, behaviours, pain points, civic needs and insights into a coherent problem-space graph.

Pay particular attention to:

- source-to-evidence-to-object traceability
- backward evidence-linking where useful knowledge already exists but provenance needs rebuilding
- not treating inspection findings, report findings or synthesis as validated user needs
- using conservative status, confidence and maturity metadata
- checking candidate objects against neighbouring existing objects before creating new ones
- preserving emotional, relational, social, civic and experiential meaning where evidence supports it
- distinguishing service, organisation and locality context from canonical need wording
- noting relationship types that might later need more precision, without changing the schema now
- noting whether locally observed needs may later become wider cross-service or cross-locality patterns
- using the documentation authority map and inventory rather than searching through every documentation file manually
- keeping any private method used to support the work out of the public commit and PR description

Near-term source inputs should remain public or explicitly authorised, for example public Ofsted/CQC Area SEND inspection reports, public Local Government and Social Care Ombudsman decisions, public SEND statutory guidance, public Local Offer pages, public council scrutiny or cabinet papers, public consultation outputs, public charity reports, public parliamentary reports and explicitly published reusable user research.

## Operating documents for the next work

Start with the current documentation authority guidance and these public-safe source-of-truth documents:

- `docs/Repository_documentation_architecture_plan.md`
- `docs/Source_use_policy.md`
- `docs/Evidence_standards.md`
- `docs/Openness_protection_model.md`
- `docs/LLM_research_breakdown_prompts.md`
- `docs/Research_breakdown_workflow.md`
- `docs/User_needs_writing_rules.md`
- `docs/User_needs_quality_public_summary.md`
- `docs/Safe_research_ingestion_MVP.md` only to the extent it remains public-safe under #70
- `docs/Ingestion_slice_workflow.md` only to the extent it remains public-safe under #70
- `docs/Input_and_evidence_classification.md` only to the extent it remains public-safe under #70
- `docs/Source_capture_workflow.md` only to the extent it remains public-safe under #70
- `docs/Secondary_research_ingestion.md` only to the extent it remains public-safe under #70

## Guardrails for the next PRs

For the next few PRs:

- keep PRs small and reviewable
- use issues for non-trivial work
- do not start ingestion until the relevant public/private boundary work is complete enough for the method being used
- do not add detailed LLM ingestion prompts, system instructions, prompt catalogues, orchestration routines, evaluation rubrics, ontology/navigation logic or protected methodology to the public repository
- do not expand high-risk public files while #66, #70 or the related private-repository boundary issues are unresolved
- do not create a private/public split inside the public repository and assume it protects sensitive material
- do not create folders or move documentation files until issue #65 has created a provisional inventory and a human has reviewed the need for moves
- do not treat public summary work as a reason to make the public repository too thin to audit or reuse
- do not do another broad filename migration unless validation or Obsidian use reveals a concrete problem
- do not add strict validator checks before the ingestion workflow has been tested on more examples
- do not build an API/database layer yet
- do not build automated cross-repository sync yet
- do not import large public reports or raw document corpora into this repository
- do not treat source capture as evidence interpretation
- do not treat source archive references as proof of validity
- do not treat synthesis as validation
- do not enforce typed relationships before real examples justify the minimum useful vocabulary
- do not create canonical personas or fixed journey maps before the underlying evidence, needs, behaviours, pain points and contexts are mature enough to support them

## Things that can wait

These are important, but not next:

- physical documentation folder restructuring
- full documentation consolidation or merging overlapping guidance
- strict validator enforcement for all naming and link rules
- full change-event folder and logging system
- pain point recurrence fields across all pain points
- generated journeys or prototypes
- opportunity pipeline
- persona or segment modelling
- API/database implementation
- cross-government taxonomy expansion
- full locality, service-area or organisation taxonomy
- full source ontology for public secondary research
- automated ingestion of secondary research corpora
- automated cross-repository source or roadmap sync
- enforced typed-relationship schema
- dedicated need-pattern object type
- formal causal or theory-of-change layer
- final licensing or commercial model decisions beyond the current draft openness/protection guardrail
- book/IP positioning beyond protection-by-default for method-bearing material

## Decision rule

When deciding what to do next, prefer work that helps answer:

- Can contributors and LLM assistants find the right source-of-truth guidance without reading every documentation file?
- Can the repository identify which documentation is current guidance, historical material, exploratory material or source-of-truth guidance?
- Can the public repository stay open while detailed orchestration methods remain protected until intentionally published?
- Can we prevent private prompts, orchestration routines, ontology/navigation logic and operating playbooks from being committed publicly by accident?
- Can we ingest real public or explicitly authorised material without semantic drift once the operating layer is clear?
- Can we preserve evidence, uncertainty and review state while moving faster?
- Can the public repository remain intelligible, auditable and reusable while protected methods live elsewhere?

If a proposed change does not support documentation authority, documentation inventory, openness/protection boundaries or safe future ingestion, defer it.

## Next review point

Review this cursor after:

1. issue #65 has produced a provisional documentation inventory or been deliberately deferred
2. issue #71 has preserved or triaged deferred roadmap detail from the stale backup
3. the next bounded ingestion slice has been selected
4. one bounded ingestion slice has tested the current public/private boundary in practice

At that point, decide whether the next step should be:

- another bounded public-source ingestion slice
- section index pages only
- a small physical folder experiment
- guidance reconciliation for one narrow area
- source/evidence template adjustments
- safe source-capture automation
