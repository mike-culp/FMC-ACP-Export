import json
import socket
from pathlib import Path
from urllib.parse import urlparse

from models import ConnectivityError


def normalize_base_url(user_input: str) -> str:
    value = user_input.strip()
    if not value:
        raise ValueError("FMC hostname/IP cannot be empty.")

    if not value.startswith(("http://", "https://")):
        value = f"https://{value}"

    parsed = urlparse(value)
    if not parsed.hostname:
        raise ValueError("Invalid FMC hostname/IP.")

    return f"{parsed.scheme}://{parsed.netloc}"


def sanitize_filename(value: str) -> str:
    cleaned = "".join(ch if ch.isalnum() or ch in {"-", "_", "."} else "_" for ch in value.strip())
    return cleaned or "unnamed"


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def check_connectivity(base_url: str, timeout: int) -> None:
    parsed = urlparse(base_url)
    host = parsed.hostname
    port = parsed.port or 443

    try:
        with socket.create_connection((host, port), timeout=timeout):
            return
    except OSError as exc:
        raise ConnectivityError(f"Cannot reach FMC at {host}:{port}") from exc


def write_json_file(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def extract_linked_prefilter_id(policy: dict) -> str | None:
    setting = policy.get("prefilterPolicySetting")
    if isinstance(setting, dict):
        return setting.get("id")
    return None