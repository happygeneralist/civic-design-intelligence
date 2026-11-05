"""Deterministic regression checks; these do not certify semantic correctness."""
from __future__ import annotations
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import validate_repository as v


class NeedContractTests(unittest.TestCase):
    def note(self, **changes):
        fm = {
            "type": "user_need", "id": "UN_001", "short_name": "Need to secure support",
            "need": "A person needs to secure appropriate support.", "need_level": "service",
            "status": "assumption", "analysis_state": "candidate", "evidence_basis": "none",
            "evidence_strength": "none", "confidence": "low", "creation_mode": "llm_assisted",
            "llm_generated": "true", "human_reviewed": "false", "review_status": "needs_review", "tags": [],
        }
        fm.update(changes)
        return v.Note(v.ROOT / "003_User_needs" / (fm["id"] + "_need_to_secure_support.md"), fm, "", True)

    def test_ids_through_ten_thousand(self):
        for n in range(1, 10001):
            self.assertIsNotNone(v.ID_PATTERN.fullmatch(f"UN_{n:03d}"))

    def test_large_id_passes_full_id_check(self):
        n = self.note(id="UN_10000")
        self.assertEqual(v.check_id(n, {"UN_10000": [n.path]}, False, False), [])

    def test_bad_id_shapes_remain_invalid(self):
        for value in ("UN_1", "UN_01", "un_001", "UN_-001", "UN_1O00", "UN_1000_more", "UN_001\n"):
            self.assertIsNone(v.ID_PATTERN.fullmatch(value))

    def test_duplicate_ids_still_fail(self):
        n = self.note(id="UN_10000")
        found = v.check_id(n, {"UN_10000": [n.path, n.path.parent / "other.md"]}, False, False)
        self.assertTrue(any(f.severity == "error" and "duplicate" in f.message for f in found))

    def test_type_prefix_still_checked(self):
        n = self.note(id="CN_10000")
        self.assertTrue(any(f.severity == "error" for f in v.check_id(n, {}, False, False)))

    def test_assumption_without_evidence_or_context_sentence_is_allowed(self):
        n = self.note()
        found = v.check_required_fields(n, False, False) + v.check_lifecycle_rules(n, False, False)
        self.assertEqual(found, [])

    def test_direct_fit_without_basis_is_advisory_not_rejection(self):
        n = self.note(evidence_scope_fit="direct")
        found = v.check_user_need_quality(n, False, False)
        self.assertTrue(any("evidence_scope_fit" in f.message for f in found))
        self.assertTrue(all(f.severity == "warning" for f in found))

    def test_partial_fit_not_treated_as_full_support(self):
        n = self.note(evidence_scope_fit="partial", evidence_basis="traceable", evidence_strength="weak")
        self.assertEqual(v.check_user_need_quality(n, False, False), [])

    def test_template_fit_options_not_research_claim(self):
        n = self.note(evidence_scope_fit="direct")
        n.path = v.ROOT / "Templates" / "User_need_template.md"
        self.assertFalse(any("evidence_scope_fit" in f.message for f in v.check_user_need_quality(n, True, False)))

    def test_reviewed_flag_cannot_contradict_human_review(self):
        for changes in ({"status": "reviewed"}, {"analysis_state": "reviewed"}, {"review_status": "reviewed"},
                        {"analysis_state": "validated", "evidence_basis": "traceable"}):
            n = self.note(**changes)
            self.assertTrue(any(f.severity == "error" for f in v.check_lifecycle_rules(n, False, False)))

    def test_consistent_recorded_human_review_passes(self):
        # This checks declared consistency, not whether review really occurred.
        n = self.note(status="reviewed", analysis_state="reviewed", human_reviewed="true", review_status="reviewed")
        self.assertEqual(v.check_lifecycle_rules(n, False, False), [])

    def test_review_state_requires_review_status(self):
        n = self.note(status="reviewed", human_reviewed="true")
        self.assertTrue(any("review_status" in f.message for f in v.check_lifecycle_rules(n, False, False)))

    def test_cognitive_wording_is_warning_not_automatic_rejection(self):
        n = self.note(need="A person needs to understand the consequences before consenting.")
        found = v.check_user_need_quality(n, False, False)
        self.assertTrue(found)
        self.assertTrue(all(f.severity == "warning" for f in found))

    def test_multiple_parent_links_resolve_without_one_parent_rule(self):
        n = self.note(parent_needs=["[[UN_1000]]", "[[UN_1001]]"])
        targets = {x: n.path for x in ("UN_1000", "UN_1001")}
        self.assertEqual(v.check_relationship_links(n, targets, False, False), [])

    def test_missing_evidence_link_is_still_reported(self):
        n = self.note(related_evidence=["[[EVID_10000]]"])
        self.assertTrue(v.check_relationship_links(n, {}, False, False))

    def test_canonical_text_not_mutated_by_checks(self):
        n = self.note(evidence_scope_fit="direct")
        before = dict(n.frontmatter)
        v.check_user_need_quality(n, False, False)
        v.check_lifecycle_rules(n, False, False)
        self.assertEqual(n.frontmatter, before)


if __name__ == "__main__":
    unittest.main()
