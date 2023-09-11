import asyncio

import httpx


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
        print("getting lock")
        async with self.lock:
            print("got lock")
            async with httpx.AsyncClient() as client:
                print("got client")
                response = await client.request(method, self.BASE_URL + url, params=params, headers=self._headers)
                print("got response")
                print(response.status_code, response.json())

            print("ok, sleep")
            await asyncio.sleep(0.42)
            print("sleep done, returning")
            return response.json()
