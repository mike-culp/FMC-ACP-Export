# FMC-ACP-Exporter

## Overview

FMC-ACP-Exporter is a Python-based tool designed to interact with Cisco Secure Firewall Management Center (FMC) APIs to export Access Control Policy (ACP) data in structured formats.

The tool supports:
- Listing available Access Control Policies
- Exporting policy rule data
- Outputting results in JSON or CSV format
- Modular architecture for future expansion

---

## Project Structure

FMC-ACP-Exporter/
- src/
  - main.py          (Entry point / CLI interface)
  - client.py        (FMC API communication)
  - auth.py          (Authentication handling)
  - config.py        (Configuration - FMC host, credentials, etc.)
  - models.py        (Data structures)
  - services/        (Business logic - policies, rules, etc.)
  - formatters/      (Output formatting - JSON, CSV)
- output/            (Generated output files - ignored by git)
- .gitignore
- README.md

---

## Requirements

- Python 3.9+
- Access to FMC API
- FMC credentials (username/password or token-based depending on implementation)

---

## Configuration

Update your FMC connection details in:

src/config.py

Example:

FMC_HOST = "https://your-fmc-host"
USERNAME = "your_username"
PASSWORD = "your_password"

---

## Usage

General syntax:

python src/main.py [OPTIONS]

---

## Available Options

- --list-policies       List all Access Control Policies
- --policy-id <id>      Export a specific Access Control Policy
- --json                Output results in JSON format
- --csv                 Output results in CSV format
- --output-dir <dir>    Specify output directory (default: ./output)

---

## Examples

1. List Available Policies

python src/main.py --list-policies

Example output:

Available Access Control Policies:
1. DA_Policy (00000000-0000-0ed3-0000-064424585866)
2. DA_policy_copy (00000000-0000-0ed3-0000-167504089256)
3. dflt (00000000-0000-0ed3-0000-042950195890)

---

2. Export Policy as JSON

python src/main.py --policy-id 00000000-0000-0ed3-0000-064424585866 --json

Output file:

output/policy_<id>.json

---

3. Export Policy as CSV

python src/main.py --policy-id 00000000-0000-0ed3-0000-064424585866 --csv

Output file:

output/policy_<id>.csv

---

4. Export to Custom Directory

python src/main.py --policy-id 00000000-0000-0ed3-0000-064424585866 --json --output-dir ./exports

---

## Output Formats

JSON:
- Full structured representation of policy rules
- Ideal for automation and further processing

CSV:
- Flattened rule data
- Ideal for Excel analysis or reporting

---

## Design Notes

- CLI is modular and designed for extensibility
- Separation of concerns:
  - CLI parsing (main.py)
  - API interaction (client.py)
  - Business logic (services/)
  - Output formatting (formatters/)
- Easily extendable to:
  - NAT policies
  - Object exports
  - Rule filtering
  - UI (Streamlit)

---

## Future Enhancements

- Streamlit UI for interactive usage
- Filtering (rule name, action, zones, etc.)
- Multi-policy export
- Object resolution (networks, ports, URLs)
- Delta comparison between policies

---

## Git Notes

Ensure output files are ignored:

/output/*.json
/output/*.csv

---

## Quick Test Checklist

python src/main.py -h
python src/main.py --list-policies
python src/main.py --policy-id <id> --json
python src/main.py --policy-id <id> --csv

---

## Summary

This tool provides a clean, extensible foundation for interacting with FMC Access Control Policies programmatically, enabling both operational visibility and automation workflows.