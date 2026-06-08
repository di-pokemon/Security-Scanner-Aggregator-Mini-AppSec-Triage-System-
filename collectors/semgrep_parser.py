import json
import subprocess
from typing import Any, Dict


def run_semgrep() -> Dict[str, Any]:
    try:
        result = subprocess.run(
            ["semgrep", "scan", "--json"],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return {"error": "semgrep not installed"}

    if result.returncode not in (0, 1):
        return {"error": "semgrep failed", "details": result.stderr.strip()}

    if not result.stdout.strip():
        return {"results": []}

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return {"error": "semgrep output could not be parsed as JSON"}
