# Roadmap cursor

Last updated: 2026-07-05

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
- a draft openness and protection model for distinguishing open civic knowledge from protected LLM orchestration

The system should not jump straight from these planning documents into high-volume ingestion. The documentation and operating boundary work is not finished yet.

## Active focus

The next focus is:

```text
Finish the minimum documentation-authority, documentation-inventory and private-orchestration boundary work, then resume small public-source ingestion slices for SEND pathway planning.
```

This means:

- finish the documentation authority map so contributors and LLM assistants know which documents to start from
- create a provisional documentation inventory before any folder restructuring
- define the private orchestration component boundary so detailed LLM prompts, ingestion routines and orchestration playbooks are not accidentally published
- finish or replace the draft openness/protection position
- avoid physical folder restructuring until the inventory shows it is needed
- avoid broad governance work beyond the minimum needed to make ingestion safe
- resume ingestion only after the operating layer is clear enough to prevent avoidable drift

## Immediate next actions

1. Review and merge PR #61 if the provisional documentation authority table is acceptable.
2. Review and merge PR #63 if the draft openness/protection model is acceptable.
3. Complete issue #65: create a provisional documentation inventory before folder restructuring.
4. Complete issue #66: define the private orchestration component boundary, including the proposed `design-intelligence-orchestration` component.
5. Update this cursor if those steps change the immediate operating sequence.
6. Only then select one bounded public or explicitly authorised source for the next ingestion slice.

## Documentation and operating-layer readiness

Before the next ingestion slice, the repository should have:

- a documentation authority map
- a provisional inventory of current docs by logical layer, authority category and semantic risk
- a clear rule that folders or file moves are a separate future PR, not part of the authority-map PR
- a clear public/private boundary for LLM orchestration material
- an agreed location outside the public repo for detailed prompts, operating playbooks and orchestration routines

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

Near-term source inputs should remain public or explicitly authorised, for example public Ofsted/CQC Area SEND inspection reports, public Local Government and Social Care Ombudsman decisions, public SEND statutory guidance, public Local Offer pages, public council scrutiny or cabinet papers, public consultation outputs, public charity reports, public parliamentary reports and explicitly published reusable user research.

## Operating documents for the next work

Start with the documentation map once PR #61 is merged. Until then, use these documents directly:

- `docs/Repository_documentation_architecture_plan.md`
- `docs/Safe_research_ingestion_MVP.md`
- `docs/Ingestion_slice_workflow.md`
- `docs/Input_and_evidence_classification.md`
- `docs/Source_capture_workflow.md`
- `docs/Secondary_research_ingestion.md`
- `docs/User_needs_writing_rules.md`
- `docs/Source_use_policy.md`
- `docs/Evidence_standards.md`
- `docs/Openness_protection_model.md` once PR #63 is merged

## Guardrails for the next PRs

For the next few PRs:

- keep PRs small and reviewable
- use issues for non-trivial work
- do not add detailed LLM ingestion prompts, system instructions, orchestration playbooks or automation recipes to the public repository while issue #62 remains open
- do not create a private/public split inside the public repository and assume it protects sensitive material
- do not create folders or move documentation files until issue #65 has created a provisional inventory and a human has reviewed the need for moves
- do not treat PR #61 as completing the whole documentation IA; it is an authority/navigation step only
- do not treat PR #63 as completing the private operating layer; issue #66 still needs to define the separate component boundary
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

## Decision rule

When deciding what to do next, prefer work that helps answer:

- Can contributors and LLM assistants find the right source-of-truth guidance without reading every documentation file?
- Can the repository identify which documentation is current guidance, historical material, exploratory material or source-of-truth guidance?
- Can the public repository stay open while detailed orchestration methods remain protected until intentionally published?
- Can we prevent private prompts, orchestration routines and operating playbooks from being committed publicly by accident?
- Can we ingest real public or explicitly authorised material without semantic drift once the operating layer is clear?
- Can we preserve evidence, uncertainty and review state while moving faster?

If a proposed change does not support documentation authority, documentation inventory, openness/protection boundaries or safe future ingestion, defer it.

## Next review point

Review this cursor after:

1. PR #61 has either merged or been replaced by an equivalent documentation authority map
2. PR #63 has either merged or been replaced by an equivalent openness/protection boundary
3. issue #65 has produced a provisional documentation inventory or been deliberately deferred
4. issue #66 has defined the private orchestration component boundary or been deliberately deferred

At that point, decide whether the next step should be:

- one bounded public-source ingestion slice
- section index pages only
- a small physical folder experiment
- guidance reconciliation for one narrow area
- source/evidence template adjustments
- safe source-capture automation
