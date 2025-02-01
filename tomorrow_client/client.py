from typing import Any, Dict, Optional, Type, TypeVar

import httpx
from pydantic import BaseModel

from .exceptions import TomorrowAPIError
from .models import ApiResponse, ForecastResponse, TimeStep, Units

T = TypeVar("T", bound=BaseModel)


class TomorrowClient:
    """Client for the Tomorrow.io API."""

    def __init__(self, api_key: str, base_url: str = "https://api.tomorrow.io/v4", timeout: int = 10):
        """Initialize the Tomorrow.io API client.

        Args:
            api_key: Your Tomorrow.io API key
            base_url: API base URL (default: https://api.tomorrow.io/v4)
            timeout: Request timeout in seconds (default: 10)
        """
        self.api_key = api_key
        self.client = httpx.AsyncClient(
            base_url=base_url.rstrip("/"),
            timeout=timeout,
            headers={"accept": "application/json", "accept-encoding": "gzip"},
        )

    async def __aenter__(self) -> "TomorrowClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.client.aclose()

    async def get_forecast(
        self, location: str, timesteps: TimeStep, units: Units = Units.IMPERIAL, timeout: Optional[int] = None
    ) -> ApiResponse[ForecastResponse]:
        """Get weather forecast for a location.

        Args:
            location: Location name or "latitude,longitude"
            timesteps: Forecast interval (MINUTELY, HOURLY, or DAILY)
            units: Unit system (METRIC or IMPERIAL)
            timeout: Optional request timeout override

        Returns:
            ApiResponse containing correlation_id and ForecastResponse data.

        Raises:
            TomorrowAPIError: If an error occurs during the request.
        """
        params = {"location": location, "timesteps": timesteps.value, "units": units.value}

        return await self._request(
            method="GET", endpoint="weather/forecast", response_model=ForecastResponse, params=params, timeout=timeout
        )

    async def _request(
        self,
        method: str,
        endpoint: str,
        response_model: Type[T],
        params: Optional[Dict[str, Any]] = None,
        payload: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> ApiResponse[T]:
        """Make HTTP request to the API.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            response_model: Pydantic model class for response
            params: Query parameters
            payload: JSON request body
            timeout: Optional request timeout override

        Returns:
            ApiResponse containing response data, rate limit information, and correlation ID.

        Raises:
            TomorrowAPIError: If an error occurs during the request.
        """
        params = params or {}
        params["apikey"] = self.api_key

        response = await self.client.request(
            method=method, url=endpoint.lstrip("/"), params=params, json=payload, timeout=timeout
        )

        if response.status_code < 200 or response.status_code >= 300:
            self._handle_response_errors(response)

        return ApiResponse(
            correlation_id=response.headers.get("X-Correlation-ID", ""),
            data=response_model.model_validate(response.json()),
        )

    def _handle_response_errors(self, response: httpx.Response) -> None:
        """Handle error responses from the API."""
        error_data = response.json()
        raise TomorrowAPIError(
            code=error_data.get("code", response.status_code),
            message=error_data.get("message", "Unknown error"),
            type=error_data.get("type", "Unknown"),
        )
