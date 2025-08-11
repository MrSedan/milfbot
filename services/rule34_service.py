from aiohttp import ClientSession
from services.config import settings

async def get_post_list(tags="", limit=50, page=0):
    async with ClientSession() as session:
        base_url = (
            f"{settings.rule34_url}"
            f"?page=dapi&s=post&q=index&json=1&limit={limit}&pid={page}"
        )
        if tags:
            url = f"{base_url}&tags={tags} -ai_generated -ai -ai_assisted"
        else:
            url = base_url

        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            return []
