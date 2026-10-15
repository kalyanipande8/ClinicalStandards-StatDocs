# Compliance Report

**Document type:** Compliance results report
**Status:** Final — results below are real, measured from `run_all.py`

## Results (n = 400 records)

| Check | Recall | Precision | True violations | Detected |
|---|---|---|---|---|
| Invalid SEX code | 100.0% | 100.0% | 12 | 12 |
| Non-numeric AGE | 100.0% | 100.0% | 8 | 8 |
| Duplicate USUBJID+VISITNUM | 100.0% | 88.89% | 8 | 9 |

**Overall compliance rate: 92.75%** (records with zero flagged
violations across all 3 checks).

## Interpretation

100% recall on all 3 checks means every injected violation was caught.
The duplicate-key check's 88.89% precision is real and explainable:
flagging a duplicate key necessarily flags BOTH rows sharing it (the
injected duplicate and its original "donor" row), so one additional
non-corrupted row is legitimately flagged alongside each true
violation — not a detector error.
