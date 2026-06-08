from typing import Any, Dict, Iterable, Mapping


def calculate_severity(issues: Iterable[Mapping[str, Any]]) -> Dict[str, int]:
    summary = {
        "CRITICAL": 0,
        "HIGH": 0,
        "MEDIUM": 0,
        "LOW": 0,
    }

    for issue in issues:
        level = str(issue.get("severity", "LOW")).upper()
        if level in summary:
            summary[level] += 1

    return summary
