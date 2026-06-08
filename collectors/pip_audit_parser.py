import json
import subprocess
from typing import Any, Dict


def run_pip_audit() -> Dict[str, Any]:
    try:
        result = subprocess.run(
            ["pip-audit", "-f", "json"],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return {"error": "pip-audit not installed"}

    if result.returncode != 0 and not result.stdout:
        return {"error": "pip-audit failed", "details": result.stderr.strip()}

    try:
        parsed = json.loads(result.stdout or "[]")
    except json.JSONDecodeError:
        return {"error": "pip-audit failed"}

    if isinstance(parsed, list):
        return {"dependencies": parsed}
    if isinstance(parsed, dict):
        return parsed
    return {"dependencies": []}
