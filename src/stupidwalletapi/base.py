import aiohttp


class BaseAPI:
    def __init__(self, token: str, base_url: str):
        self.TOKEN = token
        self.BASE_URL = base_url

    async def _make_request(self, method, url, params) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.request(method, self.BASE_URL + url, params=params, headers={"api-key": self.TOKEN}) as response:
                responsed = await response.json()
                print(response.status, responsed)
                return responsed
