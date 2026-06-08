from typing import Any, Dict, List


Issue = Dict[str, Any]


def normalize_bandit(data: Dict[str, Any]) -> List[Issue]:
    issues: List[Issue] = []
    for item in data.get("results", []):
        issues.append(
            {
                "tool": "bandit",
                "file": item.get("filename"),
                "severity": item.get("issue_severity", "LOW"),
                "message": item.get("issue_text", ""),
            }
        )
    return issues


def normalize_pip_audit(data: Dict[str, Any]) -> List[Issue]:
    issues: List[Issue] = []
    dependencies = data.get("dependencies", [])

    for dep in dependencies:
        for vuln in dep.get("vulns", []):
            issues.append(
                {
                    "tool": "pip-audit",
                    "package": dep.get("name"),
                    "severity": "HIGH",
                    "message": vuln.get("id") or vuln.get("description") or "dependency vulnerability",
                }
            )
    return issues


def normalize_semgrep(data: Dict[str, Any]) -> List[Issue]:
    issues: List[Issue] = []
    for item in data.get("results", []):
        extra = item.get("extra", {})
        issues.append(
            {
                "tool": "semgrep",
                "file": item.get("path"),
                "severity": extra.get("severity", "MEDIUM"),
                "message": extra.get("message", ""),
            }
        )
    return issues
