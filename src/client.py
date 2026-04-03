import requests

from auth import FmcAuthenticator
from models import ApiError


class FmcClient:
    def __init__(self, config, credentials):
        self.config = config
        self.credentials = credentials
        self.session = requests.Session()
        self.domain_uuid = None

    def login(self):
        auth = FmcAuthenticator(self.session, self.config, self.credentials)
        self.domain_uuid = auth.login()

    def _url(self, path):
        return f"{self.config.base_url}/api/fmc_config/v1/domain/{self.domain_uuid}{path}"

    def list_access_policies(self):
        return self._get_paginated("/policy/accesspolicies")

    def list_access_rules(self, policy_id):
        return self._get_paginated(f"/policy/accesspolicies/{policy_id}/accessrules")

    def list_prefilter_rules(self, policy_id):
        return self._get_paginated(f"/policy/prefilterpolicies/{policy_id}/prefilterrules")

    def get_access_policy(self, policy_id):
        return self._get(f"/policy/accesspolicies/{policy_id}")

    def get_prefilter_policy(self, policy_id):
        return self._get(f"/policy/prefilterpolicies/{policy_id}")

    def _get(self, path):
        r = self.session.get(self._url(path), verify=self.config.verify_tls)
        if r.status_code >= 400:
            raise ApiError(r.text)
        return r.json()

    def _get_paginated(self, path):
        url = self._url(path)
        items = []
        offset = 0

        while True:
            params = {"offset": offset, "limit": 1000, "expanded": "true"}
            r = self.session.get(url, params=params, verify=self.config.verify_tls)

            if r.status_code >= 400:
                raise ApiError(r.text)

            data = r.json()
            batch = data.get("items", [])

            if not batch:
                break

            items.extend(batch)
            offset += len(batch)

        return items