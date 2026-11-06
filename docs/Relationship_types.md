# Relationship types

Read with `Needs_semantic_contract.md` and `Needs_hierarchy.md`.

The repository already uses `related_*`, `parent_needs`, `child_needs` and supersession fields. Keep these for navigation and compatibility. A generic link establishes association, not the truth of a specific claim.

## Current operating rule

Where relationship meaning matters, state it in the object body, a review note or a research view. A plain table is sufficient. No new mandatory frontmatter structure, relationship type or validator migration is introduced here.

A useful relationship record identifies source and target, the proposition, relevant context, its basis and limitations, supporting/challenging sources and unresolved questions. Use current object IDs. Identify the revision when a view depends on wording that can change.

## Distinctions to preserve

| Meaning | Interpretation | Not implied |
| --- | --- | --- |
| Constituent / broader need | A meaningful part of, or broader progress encompassing, another need. | Exactly one parent, automatic parent retirement or shared evidence certainty. |
| Contributes to / enables | May help another need, capability or outcome become possible. | Necessary or sufficient causation. |
| Depends on | Fulfilment is proposed to require another condition in a specified context. | A universal dependency without evidence. |
| Supports / contextualises | Evidence supports identified clauses or helps interpret circumstances. | Whole-object direct support. |
| Challenges / limits | Evidence or an argument qualifies an interpretation. | Automatic deletion of the candidate. |
| Obstructs / harms | A pain or condition impedes fulfilment or diminishes value. | That removing it alone fulfils the need. |
| In tension with | Claims, needs, interests or obligations cannot simply be satisfied or interpreted together. | That linguistic refinement resolves the conflict. |
| Contextual manifestation | The need appears in specified circumstances. | A different identity for every locality or a claim of universal prevalence. |
| Normative / legal anchoring | Connection to a specified capability framework, commitment or applicable right/obligation. | Legal compliance, identical interests or an efficiency trade-off. |
| Claimed response | A policy, service or solution says it addresses a need. | Demonstrated fulfilment or realised value. |
| Supersession | A later proposition replaces an earlier interpretation with lineage retained. | That every decomposition or audience view replaces the object. |

These are meanings to test, not an instruction to create a new ontology or enforce these labels mechanically. Earlier candidate labels such as `evidenced_by`, `supports`, `blocked_by`, `challenged_by`, `local_variant_of`, `addressed_by` and `context_for` can be explained using these distinctions.

## Lightweight body example

Use real IDs in actual records; the following is only an explanatory table shape:

| From | Relationship claim | To | Basis/context | Limits or tension |
| --- | --- | --- | --- | --- |
| Need ID | Proposed contribution | Broader need/capability ID or cited framework | Analyst hypothesis informed by specified evidence | Alternative explanation and missing evidence remain visible. |

Do not manufacture links just to complete this table. Unknown relationships may remain open. The examples here are not research evidence.

## Many-to-many, without inherited truth

A need can contribute to several higher-level needs; one capability or right can be relevant to many needs. Parents, children, professionals and institutions may have related but distinct propositions. Not every useful connection is a hierarchy edge.

A path through the graph must not automatically propagate evidence, confidence, validation, legal applicability, priority or fulfilment. Distinguish a structural cycle in a claimed hierarchy from a legitimate feedback relationship or tension. Record the interpretation rather than assuming every link can be traversed as proof.

## Tensions are retained knowledge

Record competing propositions, whose perspectives or interests they represent, source/context, the current working choice if one exists, and what could change it. Differentiate missing evidence from a genuine conflict of needs or obligations. Keep dissent visible after a provisional decision.

The goal is not a perfectly harmonious graph. It is a model that helps people investigate uncertainty and make more accountable judgements.

## Policy, service and rights boundaries

External policy, service, solution and design-history artefacts can reference needs but must not silently determine their canonical wording. A response claim is separate from evidence that the need is met.

Rights and civic obligations are not merely optional preference weights. Identify their normative/legal basis and relevant limits. Do not treat a higher efficiency score as automatic authority to disregard them, or invent a legal conclusion from an abstract capability label.

## Future structured relationships

Formalise machine-readable relationship records only when the pilot demonstrates which fields and distinctions genuinely improve retrieval or decision support. Preserve existing fields and identifiers. Do not require complete relationship metadata to capture useful candidates, and do not let an absent schema justify hiding consequential relationship assumptions in prose.
