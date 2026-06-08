import unittest

from engine.false_positive_filter import filter_false_positives
from engine.normalizer import normalize_bandit, normalize_pip_audit, normalize_semgrep
from engine.severity_engine import calculate_severity


class EngineTests(unittest.TestCase):
    def test_normalize_collectors_and_severity(self):
        bandit_data = {
            "results": [
                {
                    "filename": "app.py",
                    "issue_severity": "HIGH",
                    "issue_text": "Use of insecure function",
                }
            ]
        }
        pip_data = {
            "dependencies": [
                {
                    "name": "requests",
                    "vulns": [{"id": "PYSEC-123"}],
                }
            ]
        }
        semgrep_data = {
            "results": [
                {
                    "path": "src/module.py",
                    "extra": {"severity": "MEDIUM", "message": "Potential injection"},
                }
            ]
        }

        issues = []
        issues.extend(normalize_bandit(bandit_data))
        issues.extend(normalize_pip_audit(pip_data))
        issues.extend(normalize_semgrep(semgrep_data))

        self.assertEqual(3, len(issues))
        summary = calculate_severity(issues)
        self.assertEqual(0, summary["CRITICAL"])
        self.assertEqual(2, summary["HIGH"])
        self.assertEqual(1, summary["MEDIUM"])

    def test_false_positive_filter(self):
        issues = [
            {"message": "Issue in test file", "severity": "LOW"},
            {"message": "Example code issue", "severity": "LOW"},
            {"message": "Real issue", "severity": "HIGH", "file": "src/main.py"},
        ]
        filtered = filter_false_positives(issues)
        self.assertEqual(1, len(filtered))
        self.assertEqual("Real issue", filtered[0]["message"])


if __name__ == "__main__":
    unittest.main()
