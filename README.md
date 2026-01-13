# Illumio Python 101 — In-Depth Coding Series

## Overview
This project is part of a **Python Coding 101 (In-Depth)** training series.

The goal of the series is to teach how to build a **real, production-style Python script** that:
- uses a virtual environment
- loads configuration from files
- handles authentication securely and compliantly
- calls a real API (Illumio)
- logs execution details
- produces structured output files
- is easy for another engineer to understand and run

This repository represents the **cumulative result of Lessons 4–7**.

---

## What This Script Does
When run, the script:
1. Loads configuration from a YAML file
2. Reads Illumio API credentials from environment variables (Basic Auth)
3. Tests connectivity to the Illumio API
4. Retrieves a small sample of workloads
5. Writes a JSON report to the `out/` directory
6. Writes execution logs to the `logs/` directory
7. Prints a short summary to the console

---

## Requirements
- Python 3.10+ (3.11 recommended)
- Network access to the Illumio PCE
- Valid Illumio API user and API key

---

## Repository Structure
illumio-python101/
├── src/
│ ├── main.py # Script entry point
│ ├── config_loader.py # Loads YAML config
│ ├── illumio_client.py # Illumio API calls
│ ├── reporter.py # Writes output reports
│ └── logger_setup.py # Logging configuration
├── config/
│ ├── settings.example.yaml # Example config (safe to commit)
│ └── settings.yaml # Real config (NOT committed)
├── logs/ # Runtime logs (created automatically)
├── out/ # Output reports (created automatically)
├── requirements.txt
├── .gitignore
├── README.md
└── TRAINING_REPORT.md


---

## Setup Instructions

### 1) Create and Activate a Virtual Environment

#### Windows (PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\activate
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration
Config File
Copy the example config and update values as needed:
```bash
cp config/settings.example.yaml config/settings.yaml
```
Important rules:
settings.yaml contains configuration values only
Secrets must NOT be stored in this file
settings.yaml is excluded via .gitignore

Example settings.yaml
```yaml
base_url: "https://your-pce.example.com:8443"
org_id: 1
verify_ssl: true
timeout_seconds: 30
```

## Authentication
This script uses Illumio API Basic Authentication:
API User → username
API Key → password

Credentials MUST be provided via environment variables.
```powershell
$env:ILLUMIO_API_USER="your_api_user"
$env:ILLUMIO_API_KEY="your_api_key"
```

## Running Script
Default (uses config/settings.yaml)
```bash
python -m src.main
```
Specify a config file explicitly
```bash
python -m src.main config/settings.yaml
```

## Output
Logs:Location: logs/

One log file per execution

Includes timestamps and error details

Safe for troubleshooting (no secrets)

Reports

Location: out/

Format: JSON

File name includes timestamp

Designed to be attached to tickets or further processed

## Troubleshooting
Common Issues

Missing environment variables

Ensure ILLUMIO_API_USER and ILLUMIO_API_KEY are set in the same terminal session

Config file not found

Verify config/settings.yaml exists

SSL errors

In real environments, use an approved CA bundle

Avoid disabling SSL unless explicitly approved

## Training Notes

This repository intentionally uses:

simple functions

clear file separation

readable control flow

minimal abstractions

Advanced patterns (argument parsing, retries, pagination, testing) are introduced in later sessions.
