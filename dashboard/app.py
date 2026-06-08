import json
from pathlib import Path

from flask import Flask, jsonify

app = Flask(__name__)

REPORT_PATH = Path(__file__).resolve().parents[1] / "reports" / "unified_report.json"


@app.route("/report")
def report():
    with REPORT_PATH.open(encoding="utf-8") as report_file:
        return jsonify(json.load(report_file))


if __name__ == "__main__":
    app.run(port=5001)
