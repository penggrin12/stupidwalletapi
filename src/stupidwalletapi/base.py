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
        async with httpx.AsyncClient() as session:
            async with await session.request(method, self.BASE_URL + url, params=params, headers=self._headers) as response:
                responsed = await response.json()
                print(response.status, responsed)
                return responsed
