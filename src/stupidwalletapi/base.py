import httpx


class BaseAPI:
    def __init__(self, token: str, base_url: str):
        self.TOKEN = token
        self.BASE_URL = base_url
        self._headers = {
            'accept': 'application/json',
            'api-key': self.TOKEN,
        }

    async def _make_request(self, method, url, params=None) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.request(method, self.BASE_URL + url, params=params, headers=self._headers)
            got = await response.json()
            print(response.status, got)
            return got
