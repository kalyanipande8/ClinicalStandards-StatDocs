# Clinical Data Standards Guide

**Document type:** Standards guide
**Status:** Final

## Scope

Defines the CDISC-SDTM-style conventions this submission dataset must
conform to, implemented and checked by `src/compliance_checker.py`.

## Variable conventions

| Variable | Rule |
|---|---|
| `USUBJID` | Unique subject identifier; combined with `VISITNUM` must be unique |
| `SEX` | Controlled terminology: one of {M, F, U} |
| `AGE` | Numeric |
| `VISITNUM` | Numeric visit sequence number |
| `AVAL` | Numeric analysis value |

## Controlled terminology

`SEX` uses the standard CDISC SEX codelist: `M` (Male), `F` (Female),
`U` (Unknown). Any other value is a non-conformant code and must be
flagged, not silently accepted.

## Key integrity

Each `(USUBJID, VISITNUM)` pair must be unique within the dataset. A
duplicate indicates either a data-entry error or an unresolved
protocol deviation and must be flagged for site query.
