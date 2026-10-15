# Clinical Data Standards & Statistical Documentation

CDISC-SDTM-style standards-compliance checker for a simulated clinical
submission dataset, with 3 authored standards/compliance documents.

> Developed a data-standards compliance checker for a 400-record
> clinical submission dataset; measured 100% recall across all 3
> conformance checks (controlled terminology, data typing, key
> uniqueness) with 92.75% overall record-level compliance. Authored 3
> clinical standards documents.

## What's real vs. synthetic — read this first

**Real:** `src/compliance_checker.py` implements 3 genuine CDISC-style
conformance checks: controlled-terminology validation, numeric-type
validation, and uniqueness-key validation. Because the simulation
tracks exactly which records were corrupted and how, independently of
the checker, the recall/precision numbers in `docs/compliance_report.md`
are real, measured results.

**Synthetic:** there is no real CDISC submission dataset in this
environment. `src/simulate_submission_dataset.py` generates 400
records with 3 types of injected standards violations.

## Documents authored (resume's "3+ statistical/standards documents")

1. `docs/data_standards_guide.md` — variable and controlled-terminology conventions
2. `docs/compliance_checklist.md` — the 3 conformance checks and pass criteria
3. `docs/compliance_report.md` — real measured compliance results

## Results (real, from `run_all.py`)

```
400 records
Invalid SEX code:                  100.0% recall, 100.0% precision (12 true)
Non-numeric AGE:                   100.0% recall, 100.0% precision (8 true)
Duplicate USUBJID+VISITNUM:        100.0% recall,  88.89% precision (8 true)
Overall record-level compliance:   92.75%
```

`tests/test_pipeline.py` (5 tests, all passing) checks cohort size,
>=95% recall for every check, overall compliance >85%, duplicate-key
check flags both rows of each pair, and non-numeric detection is
field-accurate.

## Usage

```bash
pip install -r requirements.txt
python3 run_all.py
python3 -m pytest tests/ -v
```

## Project structure

```
src/
  simulate_submission_dataset.py
  compliance_checker.py
docs/
  data_standards_guide.md
  compliance_checklist.md
  compliance_report.md
run_all.py
tests/test_pipeline.py
```

## Tech stack

Python 3.11, pandas, numpy, pytest. (The resume's tool list names SAS;
this is a Python implementation of the same CDISC-compliance-checking
methodology.)

## Limitations

- No real CDISC submission dataset or define.xml is used.
- Checks cover 3 common conformance classes; a production define.xml
  validator (e.g. Pinnacle 21) checks hundreds of rules.
