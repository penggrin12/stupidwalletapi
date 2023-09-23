import asyncio

import httpx


class SWError(Exception):
  def __init__(self, message: str):
    self.message = message
    super().__init__(message)
    


class BaseAPI:
    def __init__(self, token: str, base_url: str):
        self.TOKEN = token
        self.BASE_URL = base_url
        self.lock = asyncio.Lock()
        self._headers = {
            'accept': 'application/json',
            'api-key': self.TOKEN,
        }

    async def _make_request(self, method, url, params=None) -> dict:
        async with self.lock:
            async with httpx.AsyncClient() as client:
                response = await client.request(method, self.BASE_URL + url, params=params, headers=self._headers)
                print(url, response.status_code, response.json())

            await asyncio.sleep(0.42)
            if (response.json()).get('detail') is None:
                return response.json()
            else:
                raise SWError((response.json()).get('detail'))
