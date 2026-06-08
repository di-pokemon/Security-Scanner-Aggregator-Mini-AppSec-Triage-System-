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

        self.assertEqual(len(issues), 3)
        summary = calculate_severity(issues)
        self.assertEqual(summary["CRITICAL"], 0)
        self.assertEqual(summary["HIGH"], 2)
        self.assertEqual(summary["MEDIUM"], 1)

    def test_false_positive_filter(self):
        issues = [
            {"message": "Issue in test file", "severity": "LOW"},
            {"message": "Example code issue", "severity": "LOW"},
            {"message": "Real issue", "severity": "HIGH", "file": "src/main.py"},
        ]
        filtered = filter_false_positives(issues)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]["message"], "Real issue")


if __name__ == "__main__":
    unittest.main()
