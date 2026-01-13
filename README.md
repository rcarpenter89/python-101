# Illumio Python 101 — In-Depth Coding Series (Lessons 4–7)

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
│ ├── init.py # Allows: python -m src.main
│ ├── main.py # Script entry point (orchestrator)
│ ├── config_loader.py # Loads YAML config
│ ├── illumio_client.py # Illumio API calls (requests.Session)
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
