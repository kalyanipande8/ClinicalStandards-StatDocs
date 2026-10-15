"""Real standards-compliance checker validating a submission dataset
against CDISC-style conventions: controlled terminology, data typing,
and key uniqueness."""
from __future__ import annotations

import pandas as pd

VALID_SEX_CODES = {"M", "F", "U"}


def check_controlled_terminology(df: pd.DataFrame, field: str, valid_codes: set) -> set:
    return set(df.index[~df[field].isin(valid_codes)])


def check_numeric_type(df: pd.DataFrame, field: str) -> set:
    def is_numeric(v):
        try:
            float(v)
            return True
        except (TypeError, ValueError):
            return False
    return set(df.index[~df[field].apply(is_numeric)])


def check_unique_key(df: pd.DataFrame, key_fields: list) -> set:
    dup_mask = df.duplicated(subset=key_fields, keep=False)
    return set(df.index[dup_mask])


def run_compliance_checks(df: pd.DataFrame) -> dict:
    return {
        "invalid_sex_code": check_controlled_terminology(df, "SEX", VALID_SEX_CODES),
        "non_numeric_age": check_numeric_type(df, "AGE"),
        "duplicate_usubjid_visit": check_unique_key(df, ["USUBJID", "VISITNUM"]),
    }


def validate_compliance_recovery(flags: dict, true_violations: dict) -> dict:
    report = {}
    for name, detected in flags.items():
        true_set = set(true_violations.get(name, []))
        tp = len(detected & true_set)
        recall = tp / len(true_set) if true_set else 1.0
        precision = tp / len(detected) if detected else 1.0
        report[name] = {"recall_pct": round(recall * 100, 2), "precision_pct": round(precision * 100, 2),
                         "n_true": len(true_set), "n_detected": len(detected)}
    return report


def overall_compliance_rate(df: pd.DataFrame, flags: dict) -> float:
    any_violation = set()
    for s in flags.values():
        any_violation |= s
    return round(100 * (1 - len(any_violation) / len(df)), 4)
