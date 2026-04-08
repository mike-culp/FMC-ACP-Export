from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class FmcCredentials:
    username: str
    password: str


@dataclass(slots=True)
class FmcConfig:
    base_url: str
    verify_tls: bool = False
    timeout: int = 15


@dataclass(slots=True)
class ExportOptions:
    output_dir: Path
    export_json: bool
    export_csv: bool


class FmcExporterError(Exception):
    pass


class ConnectivityError(FmcExporterError):
    pass


class AuthenticationError(FmcExporterError):
    pass


class ApiError(FmcExporterError):
    pass