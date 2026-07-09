# Provisional documentation inventory

Status: provisional inventory
Related issue: #65
Last updated: 2026-07-09

This inventory classifies current documentation so contributors and LLM assistants can understand the repository before any physical folder restructuring.

It does not move, rename, merge, rewrite, deprecate or delete any document.

It is navigation and classification work only.

## Classification fields

| Field | Meaning |
|---|---|
| Logical layer | Provisional layer from `docs/Repository_documentation_architecture_plan.md`. |
| Authority category | Provisional authority role: source of truth, current operating rule, supporting guidance, concept note, roadmap direction, worked example, historical or migration record, reference/background, generated/public-site support, or template/reference. |
| Semantic risk | Risk of future changes to the document: low, medium or high. |
| Current use | Whether the document appears to be current guidance, historical context, exploratory material, generated/public-site support, migration material or template/reference. |
| Human review before authoritative use | Whether a human should review the document before treating it as controlling guidance. |

## Provisional source-of-truth candidates

These documents appear to control important repository decisions unless superseded by a human-reviewed change:

| Document | Controls |
|---|---|
| `GOVERNANCE.md` | Repository governance and review authority. |
| `CONTRIBUTING.md` | Contribution workflow and contributor expectations. |
| `AGENTS.md` | Assistant/Codex start-of-work behaviour. |
| `llm-instructions.md` | LLM operating boundaries. |
| `SCHEMA.md` | Core object schema expectations. |
| `docs/Source_use_policy.md` | Public-source posture and source-use constraints. |
| `docs/Evidence_standards.md` | Evidence handling and evidence-state expectations. |
| `docs/Lifecycle_states.md` | Lifecycle and review-state meanings. |
| `docs/Naming_and_linking_contract.md` | Naming, IDs, filenames and linking rules. |
| `docs/User_needs_writing_rules.md` | Public user-needs wording rules. |
| `docs/User_needs_quality_public_summary.md` | Public-safe user-needs quality review summary. |
| `docs/Repository_validation.md` | Repository validation behaviour and validation expectations. |

This list is provisional. Where documents overlap, human review should decide authority before meaning is changed.

## Inventory

| Document | Logical layer | Authority category | Semantic risk | Current use | Human review before authoritative use | Notes |
|---|---|---|---|---|---|---|
| `README.md` | Start here / orientation | Source of truth | Medium | Current guidance | Yes | Main repository orientation. Changes can affect how the whole repository is understood. |
| `docs/README.md` | Start here / orientation | Supporting guidance | Medium | Current guidance | Yes | Documentation map if maintained; candidate place for future index tables. |
| `CONTRIBUTING.md` | Governance and contribution | Source of truth | Medium | Current guidance | Yes | Controls contribution expectations. |
| `GOVERNANCE.md` | Governance and contribution | Source of truth | High | Current guidance | Yes | Changes may affect authority, review and validation expectations. |
| `CHANGELOG.md` | Governance and contribution | Historical or migration record | Low | Historical context | No | Technical/project change summary; Git remains the technical audit trail. |
| `AGENTS.md` | Codex and LLM operating guidance | Source of truth | High | Current guidance | Yes | Controls assistant behaviour in repository work. |
| `llm-instructions.md` | Codex and LLM operating guidance | Source of truth | High | Current guidance | Yes | Public LLM-facing instruction surface; changes may affect method exposure. |
| `docs/LLM_safety_model.md` | Codex and LLM operating guidance | Source of truth | High | Current guidance | Yes | Controls safe use of LLMs, review and validation boundaries. |
| `docs/LLM_intervention_logging.md` | Codex and LLM operating guidance | Source of truth | High | Current guidance | Yes | Controls when LLM intervention logs are needed. |
| `docs/LLM_research_breakdown_prompts.md` | Codex and LLM operating guidance | Supporting guidance | Medium | Current guidance | Yes | Public-safe summary only; detailed prompt catalogue now belongs privately. |
| `docs/Codex_repository_automation.md` | Codex and LLM operating guidance | Supporting guidance | Medium | Current guidance | Yes | Automation guidance; changes may affect repository operations. |
| `docs/Ingestion_operating_model.md` | Operating model and workflows | Current operating rule | High | Current guidance | Yes | Controls ingestion workflow posture. |
| `docs/Ingestion_slice_workflow.md` | Operating model and workflows | Current operating rule | High | Current guidance | Yes | Active ingestion-slice workflow; currently subject to public/private boundary caution. |
| `docs/Research_breakdown_workflow.md` | Operating model and workflows | Supporting guidance | Medium | Current guidance | Yes | Public-safe summary; detailed workflow now belongs privately. |
| `docs/Non_linear_research_ingestion.md` | Operating model and workflows | Supporting guidance | Medium | Current guidance | Yes | May describe flexible ingestion patterns; check before treating as controlling. |
| `docs/Review_process.md` | Operating model and workflows | Current operating rule | High | Current guidance | Yes | Review process affects object authority and lifecycle state. |
| `docs/Researcher_input_checklist.md` | Operating model and workflows | Supporting guidance | Medium | Current guidance | Yes | Practical checklist; may overlap with ingestion guidance. |
| `docs/Source_use_policy.md` | Ingestion and source/evidence handling | Source of truth | High | Current guidance | Yes | Controls what material can be used and how. |
| `docs/Input_and_evidence_classification.md` | Ingestion and source/evidence handling | Current operating rule | High | Current guidance | Yes | Controls classification between source, input and evidence. |
| `docs/Source_capture_workflow.md` | Ingestion and source/evidence handling | Current operating rule | High | Current guidance | Yes | Controls source capture process; changes may affect evidence provenance. |
| `docs/Evidence_standards.md` | Ingestion and source/evidence handling | Source of truth | High | Current guidance | Yes | Controls evidence expectations and evidence-basis meanings. |
| `docs/Secondary_research_ingestion.md` | Ingestion and source/evidence handling | Current operating rule | High | Current guidance | Yes | Controls public secondary-research ingestion behaviour. |
| `docs/Safe_research_ingestion_MVP.md` | Ingestion and source/evidence handling | Current operating rule | High | Current guidance | Yes | MVP ingestion safety guidance; check against public/private boundary before expansion. |
| `SCHEMA.md` | Object model, schemas, lifecycle and templates | Source of truth | High | Current guidance | Yes | Core object and frontmatter expectations. |
| `docs/Lifecycle_states.md` | Object model, schemas, lifecycle and templates | Source of truth | High | Current guidance | Yes | Controls lifecycle and review-state meaning. |
| `docs/Repository_validation.md` | Object model, schemas, lifecycle and templates | Source of truth | Medium | Current guidance | Yes | Validation behaviour and expected repository checks. |
| `docs/Templates_and_maturity.md` | Object model, schemas, lifecycle and templates | Supporting guidance | Medium | Current guidance | Yes | Template maturity and optionality guidance. |
| `Templates/` | Object model, schemas, lifecycle and templates | Template/reference | High | Template/reference | Yes | Template changes can affect object creation and metadata meaning. |
| `docs/User_needs_writing_rules.md` | User-needs and research-object guidance | Source of truth | High | Current guidance | Yes | Public user-needs wording rules. |
| `docs/User_needs_quality_public_summary.md` | User-needs and research-object guidance | Source of truth | High | Current guidance | Yes | Public-safe user-needs quality summary. |
| `docs/User_need_quality_tests.md` | User-needs and research-object guidance | Supporting guidance | High | Current or legacy guidance | Yes | Potentially method-bearing; review before expanding or treating as final rubric. |
| `docs/Needs_hierarchy.md` | User-needs and research-object guidance | Source of truth candidate | High | Current guidance | Yes | Controls need levels and hierarchy. |
| `docs/Need_patterns.md` | User-needs and research-object guidance | Concept note | Medium | Exploratory/current concept | Yes | Candidate pattern guidance; avoid treating as fixed schema unless reviewed. |
| `docs/Decision_shaped_user_needs.md` | User-needs and research-object guidance | Supporting guidance | High | Current guidance | Yes | Affects how decision-shaped needs are modelled. |
| `docs/Solution_vector_sensitivity.md` | User-needs and research-object guidance | Concept note | High | Current or exploratory guidance | Yes | Method-bearing concept; keep public-safe. |
| `docs/Personas_and_journeys.md` | User-needs and research-object guidance | Supporting guidance | Medium | Current guidance | Yes | Controls restraint around static personas and journeys. |
| `docs/Value_and_decision_evidence.md` | Strategy, roadmap and value model | Supporting guidance | Medium | Current guidance | Yes | Connects evidence to value and decisions. |
| `docs/Roadmap_cursor.md` | Strategy, roadmap and value model | Roadmap direction | Medium | Current guidance | Yes | Current operational pointer; should be updated after meaningful roadmap shifts. |
| `docs/Knowledge_evolution_implementation_roadmap.md` | Strategy, roadmap and value model | Roadmap direction | Medium | Current guidance | Yes | Longer roadmap and sequencing context. |
| `docs/Knowledge_evolution_strategy.md` | Strategy, roadmap and value model | Concept note | High | Current strategic context | Yes | Strategic/theory-adjacent; do not rewrite casually. |
| `docs/Civic_design_intelligence_system.md` | Theory and conceptual foundations | Concept note | High | Conceptual foundation | Yes | Explains the wider system concept; high semantic risk. |
| `docs/Theory_of_change_MVP.md` | Theory and conceptual foundations | Concept note | High | Conceptual foundation | Yes | Theory of change; changes can affect interpretation of the repository. |
| `docs/Bridging_civic_design_intelligence_and_civic_ai.md` | Theory and conceptual foundations | Concept note | High | Exploratory/conceptual | Yes | High-level conceptual bridge; review before treating as operating rule. |
| `docs/Openness_protection_model.md` | Theory and conceptual foundations | Source of truth candidate | High | Current guidance | Yes | Controls public/private boundary posture. |
| `docs/Obsidian_workflow.md` | Obsidian, views and navigation | Supporting guidance | Low | Current guidance | No | Practical vault-use guidance. |
| `docs/index.html` | Obsidian, views and navigation | Generated/public-site support | Low | Generated/public-site support | No | Generated or presentation surface; do not treat as source guidance. |
| `docs/roadmap.html` | Obsidian, views and navigation | Generated/public-site support | Low | Generated/public-site support | No | Generated or presentation surface; source should be Markdown roadmap docs. |
| `docs/stats.json` | Obsidian, views and navigation | Generated/public-site support | Low | Generated/public-site support | No | Generated stats output. |
| `docs/assets/` | Obsidian, views and navigation | Generated/public-site support | Low | Generated/public-site support | No | Static assets for public/generated views. |
| `docs/ID_and_link_migration.md` | Archive, migration and historical records | Historical or migration record | Low | Migration material | No | Preserve as context; do not treat as current naming authority if superseded. |
| `docs/Governance_legal_basis.md` | Archive, migration and historical records | Reference/background | Medium | Historical or legal-context material | Yes | Review before treating as current governance. |
| `migration/` | Archive, migration and historical records | Historical or migration record | Low | Migration material | No | Migration plans and audits; not current operating rules by default. |
| `docs/drafts/` | Inbox or unclassified material | Reference/background | Medium | Draft/unclassified | Yes | Treat as non-authoritative unless promoted through review. |

## Candidate overlaps needing later review

These are not problems to solve in this PR. They are candidates for later issue-scoped reconciliation if they block ingestion or create drift.

| Area | Candidate documents | Risk | Notes |
|---|---|---|---|
| Ingestion workflow | `docs/Ingestion_operating_model.md`, `docs/Ingestion_slice_workflow.md`, `docs/Safe_research_ingestion_MVP.md`, `docs/Non_linear_research_ingestion.md`, `docs/Research_breakdown_workflow.md` | High | Establish which file controls ingestion sequencing before expanding guidance. |
| Source and evidence handling | `docs/Source_use_policy.md`, `docs/Source_capture_workflow.md`, `docs/Input_and_evidence_classification.md`, `docs/Evidence_standards.md`, `docs/Secondary_research_ingestion.md` | High | Preserve distinction between source capture, evidence extraction and interpretation. |
| User-needs quality | `docs/User_needs_writing_rules.md`, `docs/User_needs_quality_public_summary.md`, `docs/User_need_quality_tests.md`, `docs/Needs_hierarchy.md`, `docs/Solution_vector_sensitivity.md` | High | Keep public guidance useful while detailed method remains private by default. |
| Documentation authority | `docs/Repository_documentation_architecture_plan.md`, `docs/README.md`, `docs/Roadmap_cursor.md`, this inventory | Medium | Decide whether future navigation belongs in `docs/README.md`, section index pages or both. |
| Strategy and theory | `docs/Knowledge_evolution_strategy.md`, `docs/Knowledge_evolution_implementation_roadmap.md`, `docs/Civic_design_intelligence_system.md`, `docs/Theory_of_change_MVP.md` | High | Do not merge or rewrite without explicit semantic-review scope. |

## Candidate next steps

After human review of this inventory, choose one of:

1. Add or improve section index pages without moving files.
2. Update `docs/README.md` with a source-of-truth/navigation table.
3. Reconcile one narrow overlapping guidance area, such as ingestion workflow authority.
4. Run one bounded public-source ingestion slice and test whether this inventory is sufficient.
5. Defer physical folder moves until real use shows that navigation remains a blocker.

## Out-of-scope reminders

This inventory does not:

- move files;
- create folders;
- merge overlapping documents;
- rewrite theory or operating guidance;
- resolve conflicting guidance;
- edit research objects;
- edit templates, schemas or validation logic;
- change review status, lifecycle state, evidence strength or confidence.
