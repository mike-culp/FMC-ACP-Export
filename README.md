# FMC-ACP-Exporter

## Overview

FMC-ACP-Exporter is a lightweight Python CLI tool for exporting Cisco Secure Firewall Management Center (FMC) Access Control Policies (ACP) and associated Pre-Filter policies.

The tool is designed for:
- Engineers needing quick visibility into policy rules
- Data extraction for analysis or reporting
- Automation workflows and integrations

---

## Features

- Interactive CLI workflow
- Secure credential handling (no plaintext storage)
- Lists available Access Control Policies
- Exports:
  - Access Control Policy rules
  - Linked Pre-Filter Policy rules (if present)
- Output formats:
  - JSON (structured, automation-friendly)
  - CSV (flattened, Excel-friendly)
- Configurable TLS verification (secure vs lab environments)
- Modular architecture for easy extension

---

## Project Structure

FMC-ACP-Exporter/
- src/
  - main.py        # CLI entry point
  - client.py      # FMC API interactions
  - auth.py        # Authentication handling
  - prompts.py     # User input prompts
  - exporters.py   # JSON / CSV export logic
  - models.py      # Data models and exceptions
  - utils.py       # Helper utilities
- output/          # Exported files (gitignored)
- README.md

---

## Requirements

- Python 3.9+
- Network access to FMC
- FMC credentials with API access

---

## Installation

git clone https://github.com/mike-culp/FMC-ACP-Export.git  
cd FMC-ACP-Export  

(Optional) Create virtual environment:

python -m venv venv  
source venv/bin/activate  

Install dependencies:

pip install requests  

---

## Usage

Run the tool:

python src/main.py  

Optional flags:

--json              Output JSON (default if no format specified)  
--csv               Output CSV  
--output-dir <dir>  Output directory (default: ./output)  

---

## Workflow

1. Enter FMC IP or hostname  
2. Enter username and password (secure prompt)  
3. Choose TLS verification mode:  
   - y → Verify certificate (secure)  
   - N / Enter → Skip verification (lab/self-signed)  
4. Tool connects to FMC and retrieves policies  
5. Select desired Access Control Policy  
6. Tool exports:  
   - ACP rules  
   - Linked Pre-Filter rules (if configured)  
7. Files are written to the output directory  

---

## Example

python src/main.py --json --output-dir exports  

Example interaction:

FMC IP/Hostname: 198.51.100.58  
Username: admin  
Password:  
Verify TLS certificate? [y/N]: n  

WARNING: TLS verification is disabled. Certificate validation will be skipped.  

Available Access Control Policies:  
1. Prod_Policy  
2. Dev_Policy  

Select: 1  

Output:

exports/Prod_Policy_acp.json  
exports/Prod_Policy_prefilter.json  

---

## TLS Behavior

The tool supports both secure and lab environments:

- Default: TLS verification disabled  
  - Suppresses certificate warnings  
  - Suitable for self-signed FMC deployments  

- Secure mode:  
  - Enable certificate validation  
  - Recommended for production environments  

---

## Output Formats

JSON  
- Full structured rule data  
- Ideal for automation and downstream processing  

CSV  
- Flattened rule fields  
- Ideal for Excel or reporting  

---

## Design Notes

- Uses requests.Session for connection reuse  
- Pagination handled automatically  
- Clean separation of concerns:
  - Input handling  
  - API interaction  
  - Data export  

---

## Future Enhancements

- Non-interactive mode (CLI flags for automation)  
- --insecure / --verify-tls flags  
- Streamlit UI  
- Policy filtering (zones, actions, objects)  
- Object resolution (networks, ports, URLs)  
- Multi-policy export  

---

## Git Notes

Ensure output files are ignored:

/output/*.json  
/output/*.csv  

---

## Disclaimer

This tool is provided as-is for operational and automation use.  
Ensure appropriate access controls and credential handling when using in production environments.

---

## Summary

FMC-ACP-Exporter provides a simple, extensible way to extract and analyze FMC Access Control Policies, bridging the gap between GUI visibility and programmatic access.