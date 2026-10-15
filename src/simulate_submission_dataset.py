"""Simulate a CDISC-SDTM-style submission dataset with real injected
standards-compliance violations (non-conformant variable names, wrong
data types, missing controlled-terminology codes) -- the ground truth
a standards-compliance checker must independently detect."""
from __future__ import annotations

import numpy as np
import pandas as pd

N_RECORDS = 400
SEED = 317

# CDISC-style controlled terminology for SEX
VALID_SEX_CODES = {"M", "F", "U"}


def simulate(n: int = N_RECORDS, seed: int = SEED):
    rng = np.random.default_rng(seed)

    df = pd.DataFrame({
        "USUBJID": [f"STUDY01-{i:04d}" for i in range(n)],
        "SEX": rng.choice(["M", "F"], n),
        "AGE": rng.integers(18, 90, n),
        "VISITNUM": rng.integers(1, 10, n),
        "AVAL": np.round(rng.normal(50, 12, n), 2),
    })

    true_violations = {"invalid_sex_code": [], "non_numeric_age": [], "duplicate_usubjid_visit": []}

    # invalid controlled-terminology SEX code (3%)
    idx = rng.choice(df.index, size=int(n * 0.03), replace=False)
    df.loc[idx, "SEX"] = rng.choice(["X", "O", "?"], len(idx))
    true_violations["invalid_sex_code"] = list(idx)

    # AGE stored as non-numeric string (2%)
    idx = rng.choice(df.index, size=int(n * 0.02), replace=False)
    df["AGE"] = df["AGE"].astype(object)
    df.loc[idx, "AGE"] = "unknown"
    true_violations["non_numeric_age"] = list(idx)

    # duplicate USUBJID+VISITNUM key (2%)
    idx = rng.choice(df.index, size=int(n * 0.02), replace=False)
    for i in idx:
        donor = 0 if i != 0 else 1
        df.loc[i, "USUBJID"] = df.loc[donor, "USUBJID"]
        df.loc[i, "VISITNUM"] = df.loc[donor, "VISITNUM"]
    true_violations["duplicate_usubjid_visit"] = list(idx)

    return df, true_violations


if __name__ == "__main__":
    df, v = simulate()
    print(df.shape, {k: len(x) for k, x in v.items()})
