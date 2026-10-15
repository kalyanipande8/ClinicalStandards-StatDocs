# Standards Compliance Checklist

**Document type:** Compliance checklist
**Status:** Final

| # | Check | Implementation | Pass criterion |
|---|---|---|---|
| 1 | SEX uses controlled terminology | `check_controlled_terminology` | Value in {M, F, U} |
| 2 | AGE is numeric | `check_numeric_type` | Castable to float |
| 3 | (USUBJID, VISITNUM) is a unique key | `check_unique_key` | No duplicated pairs |

Each check is run against the full dataset by `run_compliance_checks`
in `src/compliance_checker.py`, and the real measured recall/precision
of each check against known injected violations is reported in
`compliance_report.md`.
