# FMC ACP Exporter

## Overview

FMC-ACP-Exporter is a Python-based tool designed to export Cisco Secure Firewall Management Center (FMC) Access Control Policies (ACP) into structured formats for analysis, reporting, and automation.

The tool connects to the FMC API, retrieves Access Control Policies and their rules, and outputs the data in JSON or CSV format.

---

## Features

- Retrieve Access Control Policies (ACP) from FMC
- Export full rule sets for a selected policy
- Support for:
  - JSON output (structured, hierarchical)
  - CSV output (flattened, report-friendly)
- Modular design for easy extension
- Clean separation of API interaction and output formatting

---

## Project Structure

FMC-ACP-Exporter
├── src
│   ├── auth.py        # FMC authentication (token handling)
│   ├── client.py      # FMC API communication
│   ├── config.py      # Configuration (FMC host, credentials)
│   ├── exporter.py    # ACP and rule export logic
│   ├── formatter.py   # JSON and CSV formatting
│   └── main.py        # CLI entry point
│
├── output            # Generated export files (ignored by git)
│   ├── *.json
│   └── *.csv
│
├── .gitignore
└── README.md

---

## Requirements

- Python 3.9 or higher
- Access to FMC (on-prem or virtual)
- FMC API credentials

---

## Configuration

Update your FMC connection details in config.py or via environment variables:

- FMC host or IP
- Username
- Password

---

## Usage

### List Available Policies

python src/main.py --list-policies

---

### Export a Policy

python src/main.py --policy-id <POLICY_ID>

---

### Export with Output Format

python src/main.py --policy-id <POLICY_ID> --json
python src/main.py --policy-id <POLICY_ID> --csv

---

## Example Workflow

1. Run the tool to list available policies
2. Copy the desired Policy ID
3. Export the policy using JSON or CSV

---

## Output

Exports are written to the output directory.

### JSON Output

- Preserves full hierarchy:
  - Policy
  - Rules
  - Conditions (source, destination, applications, etc.)

### CSV Output

- Flattened structure for:
  - Excel analysis
  - Reporting
  - Auditing

---

## Example Fields (CSV)

- policy_name
- rule_name
- action
- source_zones
- destination_zones
- source_networks
- destination_networks
- applications
- ports
- logging
- enabled

---

## Design Principles

- Read-only operations (no changes to FMC)
- Clarity over complexity
- Modular architecture
- Extensible for future enhancements

---

## Future Enhancements

- Rule filtering (by action, zone, application)
- Multi-policy export
- Object resolution (expand network or object groups)
- Simple UI (Streamlit or similar)
- Policy comparison and diffing

---

## Git Ignore Notes

Ensure output files are excluded:

/output/*.json
/output/*.csv
.DS_Store
src/.DS_Store

---

## Disclaimer

This tool uses the FMC API and requires appropriate access permissions.
Ensure credentials are handled securely.

---

## Author

Mike Culp
Cisco Security Consulting Engineer Technical Lead