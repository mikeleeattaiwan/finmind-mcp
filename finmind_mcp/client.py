"""Small FinMind API v4 client used by MCP tools."""

from __future__ import annotations

import os
from typing import Any

import requests


class FinMindClient:
    """Client for FinMind v4 API.

    FinMind accepts bearer-token authentication. A token is optional for public data,
    but using FINMIND_TOKEN increases the official request quota.
    """

    def __init__(
        self,
        token: str | None = None,
        base_url: str = "https://api.finmindtrade.com/api/v4",
        timeout: float = 30.0,
    ) -> None:
        self.token = token if token is not None else os.getenv("FINMIND_TOKEN", "")
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    @property
    def headers(self) -> dict[str, str]:
        headers = {"Accept": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def data(
        self,
        dataset: str,
        data_id: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        **extra_params: Any,
    ) -> dict[str, Any]:
        """Query FinMind /data endpoint."""
        params: dict[str, Any] = {"dataset": dataset}
        if data_id:
            params["data_id"] = data_id
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        params.update({k: v for k, v in extra_params.items() if v not in (None, "")})
        return self._get("/data", params=params)

    def datalist(
        self,
        dataset: str,
        data_id: str | None = None,
        **extra_params: Any,
    ) -> dict[str, Any]:
        """Query FinMind /datalist endpoint."""
        params: dict[str, Any] = {"dataset": dataset}
        if data_id:
            params["data_id"] = data_id
        params.update({k: v for k, v in extra_params.items() if v not in (None, "")})
        return self._get("/datalist", params=params)

    def _get(self, path: str, params: dict[str, Any]) -> dict[str, Any]:
        url = f"{self.base_url}{path}"
        response = requests.get(url, params=params, headers=self.headers, timeout=self.timeout)
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, dict):
            raise ValueError(f"Unexpected FinMind response type: {type(payload)!r}")
        return payload
