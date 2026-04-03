import json
import requests

from models import AuthenticationError


class FmcAuthenticator:
    def __init__(self, session, config, credentials):
        self.session = session
        self.config = config
        self.credentials = credentials

    def login(self) -> str:
        url = f"{self.config.base_url}/api/fmc_platform/v1/auth/generatetoken"

        response = self.session.post(
            url,
            auth=(self.credentials.username, self.credentials.password),
            verify=self.config.verify_tls,
        )

        if response.status_code >= 400:
            raise AuthenticationError("Authentication failed")

        token = response.headers.get("X-auth-access-token")
        domains = response.headers.get("DOMAINS")

        if not token:
            raise AuthenticationError("No token returned")

        self.session.headers.update({
            "X-auth-access-token": token,
            "Content-Type": "application/json",
        })

        if domains:
            parsed = json.loads(domains)
            return parsed[0]["uuid"]

        raise AuthenticationError("No domain found")