import json
from pathlib import Path

from flask import Flask, jsonify

app = Flask(__name__)

REPORT_PATH = Path(__file__).resolve().parents[1] / "reports" / "unified_report.json"


@app.route("/report")
def report():
    try:
        with REPORT_PATH.open(encoding="utf-8") as report_file:
            return jsonify(json.load(report_file))
    except FileNotFoundError:
        return jsonify({"error": "report not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "report is invalid"}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False)
