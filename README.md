# Tomorrow Client

A Python client for the Tomorrow.io API.

## Endpoints

- [x] Get Forecast

## Example

```python
import asyncio

from tomorrow_client import TomorrowClient
from tomorrow_client.models import TimeStep, Units

async def main():
    client = TomorrowClient(api_key="")
    try:
        response = await client.get_forecast(
            location="new york", timesteps=TimeStep.HOURLY, units=Units.IMPERIAL
        )
        print(response)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
```
