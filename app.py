import json
from pathlib import Path
from typing import Any, Dict, List

from collectors.bandit_parser import run_bandit
from collectors.pip_audit_parser import run_pip_audit
from collectors.semgrep_parser import run_semgrep
from engine.false_positive_filter import filter_false_positives
from engine.normalizer import normalize_bandit, normalize_pip_audit, normalize_semgrep
from engine.severity_engine import calculate_severity

REPORT_PATH = Path("reports/unified_report.json")


def run_pipeline() -> Dict[str, Any]:
    bandit_data = run_bandit()
    pip_audit_data = run_pip_audit()
    semgrep_data = run_semgrep()

    all_issues: List[Dict[str, Any]] = []
    all_issues.extend(normalize_bandit(bandit_data))
    all_issues.extend(normalize_pip_audit(pip_audit_data))
    all_issues.extend(normalize_semgrep(semgrep_data))

    filtered_issues = filter_false_positives(all_issues)
    summary = calculate_severity(filtered_issues)

    report = {
        "summary": summary,
        "total_vulnerabilities": len(filtered_issues),
        "false_positives_filtered": len(all_issues) - len(filtered_issues),
        "issues": filtered_issues,
    }

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=4), encoding="utf-8")

    print("Report generated:", report)
    return report


if __name__ == "__main__":
    run_pipeline()
