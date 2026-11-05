# Needs as evolving knowledge: semantic contract

Working operating contract. Related work: CDI #86, #87 and #99; AI Capability Layer #39. This specifies public, inspectable knowledge semantics, not protected prompts or an autonomous extraction system. It changes no existing research object's wording, evidence or review state.

## Purpose and authority

CDI exists to help people develop, reuse and challenge a progressively better account of human experience. Services, journeys, policies and products are possible responses, not the boundaries of human need or the final measure of success.

**Build useful, specific, revisable knowledge; do not wait for perfect needs.** Human and machine interpretations are fallible. Stable objects let us learn from that fallibility. Candidate needs can already support discovery, design exploration and provisional policy comparisons; consequential claims need proportionate evidence and human judgement.

Use this contract with `User_needs_writing_rules.md`, `Needs_hierarchy.md`, `Relationship_types.md` and `Value_and_decision_evidence.md`. It clarifies those documents where older wording implies one strict hierarchy, only a few candidates, mandatory context inside each sentence, or validation before any useful analysis. `SCHEMA.md`, lifecycle rules and privacy controls still govern records. Do not invent new frontmatter types from the explanatory vocabulary below.

## 1. Distinct semantic roles

| Role | Meaning | Important boundary |
| --- | --- | --- |
| User need | A current interpretation of what a person needs to achieve, preserve, recover, avoid or change. | Not necessarily an activity that the person must perform themselves. |
| Actor | The person experiencing the need. | Distinguish the actor, beneficiaries and parties responsible for enabling fulfilment. A professional can have a genuine user need. |
| Context | Circumstances in which the need manifests or changes. | A need can recur across contexts; context is not automatically part of its identity or wording. |
| Pain point | A condition, burden, barrier, harm or risk affecting people or fulfilment. | Avoiding harm can itself be a need. Pain and need are different analytical roles, not mutually exclusive kinds of experience. |
| Expected value | Anticipated benefit, protection, capability or avoided harm, specifying for whom. | An expectation is not an observed outcome or a causal finding. |
| Realised value | Beneficial or harmful change supported by observations, including its distribution and limits. | Observed improvement does not by itself prove that an intervention caused it. |
| Fulfilment conditions | What would count as this need being sufficiently met in a stated context and period. | Not feature-delivery criteria, proof that the formulation is correct, or a compulsory binary completion test. |
| Indicator | Something observable or reportable that may help assess fulfilment or value. | A proxy is not the need; meeting a service target is not necessarily meeting a human need. |
| Evidence | What a source says, reports, observes or measures, with voice and provenance. | Analyst inference, normative commitments and machine output are not participant evidence. |
| Relationship | A proposition connecting objects or claims with a specified meaning. | A related link does not establish direct support, causation, equivalence or fulfilment. |
| Tension | A persistent, inspectable uncertainty or conflict between interpretations, needs, interests, obligations or conditions. | Do not remove it merely by choosing smoother wording. |

These roles need not all be complete for a candidate to be worth keeping. Do not fill missing fields with invented certainty.

## 2. Human experience, rights and capabilities are anchors

Always consider what the work enables or protects in people's lives, not only what improves the current service. Higher-level needs, civic obligations, rights and human capabilities make this question visible during detailed delivery work.

Anchoring is **many-to-many and contestable**. Do not force every need to terminate at safety, dignity or another predetermined label. Record proposed links, reasons, sources, alternatives, disagreements and unknowns. Revising an interpretation of what matters may change the solution set while leaving useful lower-level needs intact.

Distinguish three bases:

- **Empirical:** evidence about people's experiences, circumstances and effects.
- **Normative:** a declared ethical or human-development commitment and the framework being used.
- **Legal:** a cited instrument, provision, jurisdiction, applicability and interpretation requiring appropriate human review.

A capability is not just an available service or a completed activity. Consider people's real opportunities and choice, including whether they can meaningfully decline or pursue different lives. Do not equate uptake with fulfilment.

**Do not automatically trade rights or civic obligations against administrative efficiency in a weighted value score.** Separate applicable obligations, relevant limits and contested interpretations from preference optimisation. This does not assert that every right is absolute or that every conflict has an obvious answer. Do not invent a legal obligation from a general value label. A candidate with an unresolved rights/capability link remains useful; consequential reliance should expose that unresolved basis.

External orientation, not substitutes for source-specific analysis: [UNDP human development](https://hdr.undp.org/about/human-development) emphasises people's opportunities and choices; [Universal Declaration of Human Rights](https://www.un.org/en/about-us/universal-declaration-of-human-rights) supplies a normative reference. Neither alone determines a particular service's legal compliance or a particular need's correct higher-level relationship.

## 3. Breadth, granularity and learning

There is no preferred small number of needs per source and no architectural reason to stop at hundreds or thousands. Bound work by authorised sources, questions, reviewable batches and actual execution capacity, **not by a quota of acceptable needs**.

Distinguish source statements from need hypotheses developed using them. One inspection report can prompt many actor-specific and multilevel hypotheses; that does not turn them into directly observed needs or prove prevalence. Label each inferential step. A large candidate landscape is valuable only if its provenance, relationships and uncertainty remain navigable.

Discovery must inspect different actors, levels, contexts, positive cases, omissions and tensions. Check nearby objects, but do not suppress genuinely distinct hypotheses just because a broader need already exists. Retain possible overlap for comparison when identity is unresolved. Do not inflate counts with synonymous sentences or fabricate specificity to meet a target.

### Decompose, ladder and vary context separately

- **Decompose:** expose independently meaningful constituent progress/protection needs. A constituent can be met while another remains unmet, or may require a different evidential assessment. Retain a useful broad parent as well as its children. Decomposition does not automatically deprecate the parent.
- **Ladder:** investigate what a need contributes to or protects at a broader level. One need may have multiple higher-level connections. A contribution is not necessarily containment or a sufficient cause.
- **Explore context:** examine whether the same need recurs with different barriers, urgency or fulfilment conditions, or whether the underlying progress actually changes.

Conjunctions and different possible solutions are diagnostic clues, not automatic splitting rules. Administrative steps can suggest underlying needs, but copying steps from the current solution is not need decomposition. Conversely, a meaningful task-level need is not invalid merely because it is specific. Preserve a composite or relational need when splitting would erase meaning.

Use existing `parent_needs`, `child_needs`, `related_capabilities`, `related_rights`, `related_civic_needs` and `related_*` links. Explain relationship meaning in the body where generic fields are insufficient. No forced single tree, no automatic inheritance of evidence, rights, confidence or fulfilment along a path.

## 4. One identity, a current formulation, several useful forms

| Form | Function | Preservation rule |
| --- | --- | --- |
| Stable ID | Identity, links and learning over time. | Retain unless an explicit split/merge/supersession requires new objects. |
| `short_name` | Mapping, navigation, visual comparison and conversation. | A compact need label, not the entire canonical sentence or a new object. |
| Canonical `need` | Current shared working interpretation. | Persist it. Never regenerate or overwrite it on each view or query. |
| Authentic language | Evidence of what people actually said or expressed. | Preserve source wording, context and provenance. No simulated quotations. |
| User-facing formulation | Discussion, recognition, challenge and idea generation. | Label it as an interpretation unless it is an actual quotation. |
| Value-oriented view | Needs/pain/value/fulfilment comparison for prioritisation or policy work. | Compose named propositions without silently adding causation, consensus or certainty. |
| Computable representation | Queries, graphs, comparisons and relationships. | Structured claims must remain accountable to the current formulation and evidence. Formal-looking language is not more computable merely because it is less natural. |

Bind reusable views to the need ID and the actual revisions of the formulation and other propositions they use. A Git commit/blob reference can supply version identity; do not add an incompatible mandatory version field. Store a useful current view or cache it where needed. Regenerate deliberately after a relevant change, label an older view stale, and make material semantic differences reviewable. A change of audience is not permission to change the need.

Do not reproduce the full canonical sentence on every map: the short label is an intentional affordance. Expanding it should recover the current interpretation, basis and relationships. Record ambiguity in the underlying object, not only in one presentation.

## 5. Context without context-heavy sentences

Keep source context and evidence scope explicit. Keep the canonical formulation reusable where the progress/protection is the same across situations. Put a contextual qualifier in the statement only when removing it materially changes what need is meant.

For each relevant manifestation, record circumstances, affected actors, evidence, pain, value and fulfilment limits as available. Do not claim universal applicability from a reusable label. Different context may change urgency, criteria or relationships without creating a different need; where meaning changes, propose a linked variant or a distinct object and explain why.

Do not make location, a current policy or a particular service the definition of an enduring need merely because that is where the first evidence was found.

## 6. Fulfilment, value and assessment

Keep **knowledge-object quality**, **need fulfilment**, **rights/capability compatibility**, and **realised value** distinct. An excellent need formulation can describe an unmet need. A completed service transaction can coexist with unmet needs or harms.

Document provisional fulfilment conditions with context, whose perspective is represented, indicators and what remains unknown. Conditions may be qualitative, partial, continuing or contested. Do not invent numeric thresholds, guarantee emotional recognition or infer fulfilment from lack of complaints. No compulsory 'end state' for continuing safety, affiliation or agency.

Expected value can motivate a hypothesis without being demonstrated. Removing a barrier does not necessarily meet the need; meeting one need does not necessarily remove every pain or satisfy other actors' needs. Preserve distributional effects and contradictory evidence.

An illustrative SEND distinction is between planned actions being completed, a child receiving appropriate support, a parent retaining agency/caring capacity, and institutions carrying their responsibilities. These are related claims, not one interchangeable success measure. It is an example to test, not a rewrite or validation of UN_015.

## 7. Record relationships and tensions as learnable propositions

For an important relationship, retain its source and target, what is claimed, context, basis, qualification and counterevidence. Use an ordinary body table or review note until a tested schema is justified. Evidence can support a clause, qualify a relation or challenge a proposed abstraction without supporting the entire object.

For a consequential tension record: the competing propositions, whose interests/interpretations they represent, relevant contexts and evidence, current working choice if any, and what could change it. Distinguish uncertainty about what is true from a real conflict between legitimate needs or obligations. Do not force resolution before capture, and do not erase disagreement after a provisional decision.

Civic and capability anchors are also relationships to study. An officer's professional need and a detained person's safety or agency need may be connected through an institutional obligation; that is not automatically a parent-child relationship or a statement that staff efficiency proves safety.

## 8. Honest gates without perfection gates

Protect privacy, source identity, non-fabrication, stable IDs, authorised writes and truthful review status. Flag semantic uncertainty and contradictions for investigation. A weak candidate can be retained; a falsely attributed quote or fabricated review cannot be disguised as useful uncertainty.

Automated checks may verify structure and version binding, not objective truth or legal compliance. Model critique is not human review. Keep hard integrity failures distinct from advisory semantic findings and proportionate review of consequential use. Do not silently certify a candidate because two models agree.

Evaluate **breadth and omission** as well as false claims: actors or needs missed, over-refusal, premature merging, useful decomposition, persistent tensions, context handling, source fidelity and human attention cost. A small number of fluent statements is not proof of a good needs landscape. A large number alone is not proof either.

## 9. Lightweight implementation and ownership

Use existing fields and optional body sections first. Do not require every candidate to have a complete value/rights map, all audience forms, an explicit tension or finished criteria. Capture missing material honestly and deepen the parts that a real use depends on.

CDI owns these definitions, objects and review states. The private secondary-research repository owns permitted original documents. AI Capability Layer owns reusable skills, reviewer interfaces, adapters and evaluation tooling; Design Intelligence Orchestration owns protected methods. Public participation is a separate authorised contribution route, not publication of private source material.

The next test is the existing #99 pilot, following the bounded source/review calibration in AI Capability Layer #39. Those controls should help the work proceed, not require exhaustive historical source review or another general agent platform.
