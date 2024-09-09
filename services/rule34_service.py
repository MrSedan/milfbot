from aiohttp import ClientSession
from services.config import settings

async def get_post_list(tags=""):
    async with ClientSession() as session:
        base_url = f"{settings.rule34_url}?page=dapi&s=post&q=index&json=1&limit=50"
        if tags:
            url = f"{base_url}&tags={tags}"
        else:
            url = base_url
        response = await session.get(url)
        if response.status == 200:
            data = await response.json()
            return data
        else:
            return []
