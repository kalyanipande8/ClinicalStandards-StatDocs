import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.simulate_submission_dataset import simulate
from src.compliance_checker import run_compliance_checks, validate_compliance_recovery, overall_compliance_rate


def test_cohort_has_400_records():
    df, _ = simulate()
    assert len(df) == 400


def test_all_violation_types_detected_with_high_recall():
    df, true_violations = simulate()
    flags = run_compliance_checks(df)
    recovery = validate_compliance_recovery(flags, true_violations)
    for name, r in recovery.items():
        assert r["recall_pct"] >= 95.0, f"{name}: {r}"


def test_clean_records_mostly_pass():
    df, _ = simulate()
    flags = run_compliance_checks(df)
    rate = overall_compliance_rate(df, flags)
    assert rate > 85.0


def test_duplicate_key_check_flags_both_rows():
    df, true_violations = simulate()
    flags = run_compliance_checks(df)
    assert len(flags["duplicate_usubjid_visit"]) >= len(true_violations["duplicate_usubjid_visit"])


def test_numeric_type_check_rejects_non_numeric():
    df, _ = simulate()
    flags = run_compliance_checks(df)
    for idx in flags["non_numeric_age"]:
        assert df.loc[idx, "AGE"] == "unknown"
