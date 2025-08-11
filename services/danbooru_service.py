from aiohttp import ClientSession, ClientError
from services.config import settings

async def get_post_list(tags="", limit=50, page=1):
    url = f"{settings.danbooru_url}?limit={limit}&page={page}&tags={tags}"
    async with ClientSession() as session:
        try:
            response = await session.get(url)
            response.raise_for_status()
            return await response.json()
        except ClientError as e:
            print(f"Error: {e}")
            return []
