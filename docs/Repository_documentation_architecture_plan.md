# Repository documentation architecture plan

This is a planning document. It proposes a lightweight documentation architecture for the repository before any file moves, rewrites or consolidation work.

It does not move, rename, delete, deprecate or rewrite existing documents.

## 1. Purpose and success criteria

Documentation architecture is an operational control, not tidiness for its own sake.

The repository now contains governance rules, contribution guidance, ingestion workflows, object guidance, theory, strategy, roadmap direction, Obsidian support, generated views and historical migration material. As the repository grows, mixed documentation can create drift: older concept notes may be treated as current rules, worked-domain examples may be mistaken for system-wide assumptions, and Codex or other LLMs may follow exploratory material as if it were authoritative.

This plan should make the repository safer and easier to use by:

- reducing documentation drift
- supporting rigorous ingestion from source material to reviewed knowledge
- improving findability for contributors, reviewers and Codex
- clarifying which documents are authoritative for different decisions
- preserving separation between evidence, interpretation, operating rules, theory, strategy, roadmap direction and history
- making future service-area expansion safer beyond the initial SEND worked domain
- making Codex and LLM-assisted work more reliable
- keeping the repository lightweight, Markdown-first and Obsidian-friendly

Success looks like contributors and LLM assistants being able to answer:

- where to start
- which document controls a decision
- which guidance is current practice, concept note, roadmap direction, reference material or historical record
- how to follow the ingestion path from source to evidence to candidate objects to reconciliation and review
- which future documentation changes are low, medium or high semantic risk

## 2. Proposed documentation layers

These are logical layers, not immediate folder moves. A later execution PR may choose to implement some of them as section index pages, folder structure or navigation tables. The first consolidation pass should not assume that every logical layer needs a physical folder.

| Layer | Purpose | Initial examples |
|---|---|---|
| Start here / orientation | Help readers understand the repository and choose the next document | `README.md`, `docs/README.md` |
| Governance and contribution | Define roles, review authority, contribution handling and change expectations | `GOVERNANCE.md`, `CONTRIBUTING.md` |
| Codex and LLM operating guidance | Define safe assistant behaviour and LLM boundaries | `AGENTS.md`, `llm-instructions.md`, `docs/LLM_safety_model.md`, `docs/Codex_repository_automation.md` |
| Operating model and workflows | Explain how repository work should proceed in practice | `docs/Ingestion_operating_model.md`, `docs/Ingestion_slice_workflow.md`, `docs/Research_breakdown_workflow.md` |
| Ingestion and source/evidence handling | Control source classification, source capture, evidence extraction and public-source posture | `docs/Source_use_policy.md`, `docs/Source_capture_workflow.md`, `docs/Input_and_evidence_classification.md`, `docs/Evidence_standards.md`, `docs/Secondary_research_ingestion.md`, `docs/Safe_research_ingestion_MVP.md` |
| Object model, schemas, lifecycle and templates | Define object structure, metadata, lifecycle states, validation and template expectations | `SCHEMA.md`, `docs/Lifecycle_states.md`, `docs/Repository_validation.md`, `docs/Templates_and_maturity.md`, `Templates/` |
| User-needs and research-object guidance | Guide creation and review of user needs, civic needs and related analysis objects | `docs/User_needs_writing_rules.md`, `docs/Needs_hierarchy.md`, `docs/User_need_quality_tests.md`, `docs/Decision_shaped_user_needs.md`, `docs/Personas_and_journeys.md` |
| Strategy, roadmap and value model | Explain current direction, future sequencing, knowledge evolution and decision value | `docs/Roadmap_cursor.md`, `docs/Knowledge_evolution_implementation_roadmap.md`, `docs/Knowledge_evolution_strategy.md`, `docs/Value_and_decision_evidence.md` |
| Theory and conceptual foundations | Explain why the system exists and the concepts behind it | `docs/Civic_design_intelligence_system.md`, `docs/Theory_of_change_MVP.md`, `docs/Bridging_civic_design_intelligence_and_civic_ai.md` |
| Obsidian, views and navigation | Support vault use, generated pages, Bases and public navigation | `docs/Obsidian_workflow.md`, `docs/index.html`, `docs/roadmap.html`, `docs/stats.json`, `docs/assets/` |
| Archive, migration and historical records | Preserve migration context and historical decisions without treating them as current instruction | `migration/`, `docs/ID_and_link_migration.md`, `docs/Governance_legal_basis.md` where historical or legal-context use is intended |
| Inbox or unclassified material | Hold drafts, loose material or unclear documents until classified | `docs/drafts/`, future unclassified notes |

## 3. Document authority model

Future documentation maps should classify documents by authority. This prevents drift by helping contributors and Codex distinguish current instruction from background, examples, history or future direction.

Suggested authority categories:

| Category | Meaning |
|---|---|
| Source of truth | Controls a specific decision area unless a human reviewer explicitly supersedes it |
| Current operating rule | Describes how contributors or Codex should work now |
| Supporting guidance | Helps apply a rule but does not override the source of truth |
| Concept note | Explores an idea, model or future direction; not automatically current practice |
| Roadmap direction | Describes intended sequencing or deferred work |
| Worked example | Shows how guidance applies in a bounded domain, currently often SEND pathway planning |
| Historical or migration record | Preserves previous state, migration decisions or audit history |
| Reference/background | Useful context that should not be treated as instruction by default |

Initial source-of-truth candidates should be explicit. For example:

- repository governance and validation authority: `GOVERNANCE.md`
- contributor workflow: `CONTRIBUTING.md`
- Codex start-of-work behaviour: `AGENTS.md`
- LLM safety and operating boundaries: `llm-instructions.md`
- public-source posture: `docs/Source_use_policy.md`
- evidence standards: `docs/Evidence_standards.md`
- lifecycle meanings: `docs/Lifecycle_states.md`
- naming and linking: `docs/Naming_and_linking_contract.md`
- user-need wording: `docs/User_needs_writing_rules.md`
- validation behaviour: `docs/Repository_validation.md`

Where documents overlap, a later PR should identify the source of truth before wording is reconciled. Codex may list the overlap, but a human reviewer should decide authority when meaning could change.

## 4. Evidence and ingestion separation

The documentation architecture should preserve the distinction between:

- source material: the external or internal material being considered
- source records: repository records that identify and describe sources
- evidence extracts: selected quotes, observations, data points or document extracts
- candidate research objects: draft needs, behaviours, pain points, insights, themes, journeys, opportunities or value dimensions
- reviewed or validated knowledge objects: objects that have passed the relevant human review threshold
- synthesis/views: summaries, maps, dashboards, public pages or Obsidian views that present knowledge
- decision-support material: value dimensions, option assessments, design histories or other material used to support decisions

The intended ingestion path is:

```text
input/source
-> classification
-> source capture
-> evidence extraction
-> candidate objects
-> reconciliation
-> review
-> synthesis/view
```

The IA should make this path easy to follow without collapsing the steps. Source capture guidance should not become evidence interpretation. Evidence extracts should not become validated claims by proximity. Synthesis and views should reference stable objects rather than silently becoming the source of truth.

## 5. Semantic-risk model

Documentation changes should be planned by semantic risk.

Low-risk changes:

- creating index pages
- adding navigation tables
- adding source-of-truth tables without changing the underlying documents
- classifying documents provisionally
- moving files without content changes where links can be updated safely
- correcting obvious stale references
- fixing broken links where the intended target is unambiguous

Medium-risk changes:

- clarifying wording
- reconciling overlapping guidance
- changing examples
- changing current-workflow descriptions
- changing document summaries in ways that may affect how readers use them
- moving documents where the new location implies a different authority level

High-risk changes:

- merging documents
- rewriting theory
- changing user-needs rules
- changing ingestion rules
- changing evidence interpretation
- changing object lifecycle or validation meaning
- converting concept notes into current operating rules
- moving historical material into active guidance
- deleting or deprecating documents

High-risk changes need explicit issue scope and human semantic review before implementation.

## 6. Codex-safe work

Codex can safely help with mechanical and provisional work when scope is clear:

- inventory documentation files
- classify documents provisionally
- create index pages
- create source-of-truth tables for human review
- propose moves without performing them
- update relative links after approved moves
- detect overlapping guidance
- list candidate duplicates
- identify stale references
- run repository validation
- prepare small PRs for reviewed low-risk batches

Codex should not independently decide semantic authority where guidance conflicts.

Human semantic review is needed for:

- merging theory documents
- changing source-of-truth rules
- rewriting user-needs guidance
- changing ingestion or evidence-handling rules
- deciding which document is authoritative where guidance conflicts
- moving historical material into active guidance
- deleting, archiving or deprecating documents
- deciding whether SEND worked-example guidance should become system-wide guidance
- changing lifecycle, validation, evidence strength or confidence meaning

Codex should treat historical, migration and exploratory documents as context unless an issue or human reviewer explicitly says they are current instruction.

## 7. Proposed first execution PR

The smallest useful next PR should be low risk.

Recommended first execution PR:

- improve `docs/README.md` as the documentation map
- add a source-of-truth table
- classify existing docs by logical layer and authority category
- mark classifications as provisional where human review is still needed
- do not move files
- do not rewrite source documents
- do not resolve contradictions

This would give contributors and Codex a safer navigation surface before any folder restructuring.

Alternative low-risk first PRs:

- create section index pages without moving documents
- add an "authority" column to the documentation map
- add a "read this first" path for ingestion, source capture, user needs and LLM-assisted work

Broad file moves should not be the first execution step unless a human reviewer decides the navigation problem is severe enough to justify that risk.

## 8. Migration principles

Future documentation consolidation should follow these principles:

- move first, rewrite later
- do not delete anything in the first consolidation pass
- do not merge documents with distinct concepts
- do not rewrite theory while moving files
- do not convert concept notes into operating rules without review
- preserve Git history as the technical audit trail
- use issues for scoped work
- use PR summaries for administrative moves
- use object changelogs only where research-object meaning changes
- use LLM intervention logs only for material semantic changes
- preserve British English
- preserve Obsidian usability
- keep folder depth shallow unless there is a clear navigation benefit
- update links and indexes in the same PR as any approved move
- keep SEND as a worked-domain example unless guidance is intentionally system-wide

## 9. Open questions

Questions for human review before any file moves:

- Should the IA become physical folders, mostly index/navigation pages, or a hybrid?
- Which documents are source of truth versus supporting guidance?
- Which documents are historical but still useful?
- Which guidance overlaps should be reconciled later?
- Which concept notes should remain exploratory?
- Which roadmap documents are current direction versus historical sequencing?
- How deep can folders become before Obsidian usability suffers?
- Should generated public pages and Obsidian support files stay under `docs/` or be separated later?
- Should migration records remain outside `docs/` or be mirrored in a documentation map?
- What is the right convention for worked-domain examples as the system expands beyond SEND?
- Which documents should Codex treat as current instruction by default?
