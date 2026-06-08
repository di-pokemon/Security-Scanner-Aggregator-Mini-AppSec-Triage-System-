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

    if result.returncode not in (0, 1) and not result.stdout:
        return {"error": "semgrep failed", "details": result.stderr.strip()}

    try:
        return json.loads(result.stdout or "{}")
    except json.JSONDecodeError:
        return {"error": "semgrep failed"}
