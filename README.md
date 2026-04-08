# FMC-ACP-Exporter

## Overview

FMC-ACP-Exporter is a Python-based CLI tool for interactively exporting Cisco Secure Firewall Management Center (FMC) Access Control Policies (ACP) and their associated rule sets.

The tool:
- Prompts for FMC connection details at runtime
- Authenticates securely using FMC API token-based auth
- Allows interactive selection of Access Control Policies
- Exports ACP rules and linked prefilter rules
- Supports JSON and CSV output formats

---

## Key Features

- Interactive CLI workflow (no hardcoded config required)
- Secure credential handling (password not echoed)
- Automatic FMC connectivity validation
- Full ACP rule export
- Linked prefilter policy export (if present)
- JSON and CSV output support
- Modular design for future extensibility

---

## Project Structure

FMC-ACP-Exporter/
- src/
  - main.py          # Entry point / CLI workflow
  - client.py        # FMC API client
  - auth.py          # Authentication handling
  - models.py        # Data models and exceptions
  - prompts.py       # User interaction (input prompts)
  - utils.py         # Helpers (connectivity, parsing, file handling)
  - exporters.py     # JSON/CSV export logic
- output/            # Exported files (ignored by git)
- README.md

---

## Requirements

- Python 3.9+
- Network access to FMC (HTTPS / TCP 443)
- Valid FMC username and password
- FMC API enabled

---

## Installation

Clone the repository:

    git clone <your-repo-url>
    cd FMC-ACP-Exporter

(Optional) Create virtual environment:

    python -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows

Install dependencies:

    pip install requests

---

## Usage

Run the tool:

    python src/main.py [OPTIONS]

---

## Available Options

- --json  
  Export output in JSON format

- --csv  
  Export output in CSV format

- --output-dir <dir>  
  Specify output directory (default: ./output)

If no format is specified, JSON is used by default.

---

## Interactive Workflow

1. Run the script
2. Enter FMC IP address or hostname
3. Enter FMC username
4. Enter FMC password (hidden input)
5. Tool validates connectivity to FMC
6. Tool authenticates and retrieves Access Control Policies
7. A numbered list of policies is displayed
8. Select a policy by number
9. Tool exports:
   - ACP rules
   - Linked prefilter rules (if present)
10. Files are written to the output directory

---

## Example Run

    python src/main.py --json

Prompt sequence:

    FMC IP/Hostname: fmc.company.com
    Username: admin
    Password:

Then:

    1. Global_ACP
    2. Datacenter_ACP
    3. Edge_ACP
    Select:

---

## Output Files

Generated in the output directory:

### JSON

- <policy_name>_acp.json
- <policy_name>_prefilter.json (if applicable)

Structure:

    {
      "rules": [...]
    }

---

### CSV

- <policy_name>_acp.csv
- <policy_name>_prefilter.csv (if applicable)

- Flattened rule structure
- Suitable for Excel or reporting

---

## Security Notes

- Password input is handled securely using hidden terminal input
- Credentials are not stored on disk
- Authentication tokens are managed in-memory only

---

## Connectivity Behavior

- Tool validates FMC reachability before authentication
- Uses TCP socket connection to verify host/port (default 443)
- Fails fast if FMC is unreachable

---

## Design Notes

- Clean separation of concerns:
  - CLI workflow (main.py)
  - User interaction (prompts.py)
  - API communication (client.py)
  - Authentication (auth.py)
  - Export formatting (exporters.py)
- Designed for easy extension to:
  - NAT policy export
  - Object resolution
  - Rule filtering
  - Streamlit UI

---

## Git Ignore Recommendations

Ensure output files are ignored:

    /output/*.json
    /output/*.csv

---

## Quick Test Checklist

    python src/main.py -h
    python src/main.py --json
    python src/main.py --csv
    python src/main.py --json --csv
    python src/main.py --output-dir ./exports

---

## Known Limitations

- Exports rule data only (not full policy metadata structure)
- No non-interactive mode (policy ID via CLI not yet supported)
- Limited error messaging for connectivity/auth failures

---

## Future Enhancements

- Non-interactive CLI mode (policy ID flag)
- Streamlit UI
- Policy metadata export
- Object resolution (networks, ports, URLs)
- Rule filtering (action, zones, applications)
- Multi-policy export

---

## Summary

FMC-ACP-Exporter provides a simple, secure, and extensible way to extract Access Control Policy rule data from FMC, enabling analysis, reporting, and automation workflows.