import json
import os

from src.simulate_submission_dataset import simulate
from src.compliance_checker import run_compliance_checks, validate_compliance_recovery, overall_compliance_rate


def main():
    df, true_violations = simulate()
    flags = run_compliance_checks(df)
    recovery = validate_compliance_recovery(flags, true_violations)
    compliance_rate = overall_compliance_rate(df, flags)

    summary = {"n_records": len(df), "violation_recovery": recovery,
               "overall_compliance_rate_pct": compliance_rate}

    os.makedirs("results", exist_ok=True)
    with open("results/summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
