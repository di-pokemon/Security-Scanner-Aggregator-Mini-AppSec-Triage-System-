# Security Scanner Aggregator

## Overview
A security triage system that aggregates outputs from multiple security scanners and normalizes vulnerability data for analysis and reporting.

## Features
- Bandit scan integration
- pip-audit dependency scanning integration
- Semgrep static analysis integration
- Unified vulnerability normalization
- Severity classification engine
- False positive filtering logic
- Security dashboard API

## Project Structure
```
collectors/
engine/
dashboard/
reports/
app.py
requirements.txt
```

## Run
```bash
pip install -r requirements.txt
python app.py
```

## Dashboard
```bash
python dashboard/app.py
```

Open `http://127.0.0.1:5001/report` to see the unified report.
