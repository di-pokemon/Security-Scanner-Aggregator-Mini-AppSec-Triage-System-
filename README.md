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
## Architecture
<img width="1376" height="768" alt="Security Scanner Aggregator" src="https://github.com/user-attachments/assets/92176864-c824-4a87-9312-0d58bd2459cc" />

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
