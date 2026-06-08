import json
import subprocess
from typing import Any, Dict


def run_bandit() -> Dict[str, Any]:
    try:
        result = subprocess.run(
            ["bandit", "-r", ".", "-f", "json"],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return {"error": "bandit not installed"}

    if result.returncode != 0 and not result.stdout:
        return {"error": "bandit failed", "details": result.stderr.strip()}

    if not result.stdout.strip():
        return {"results": []}

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return {"error": "bandit output could not be parsed as JSON"}
