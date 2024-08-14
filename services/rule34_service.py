from aiohttp import ClientSession
from services.config import settings
import logging

async def get_post_list(tags = ""):
    async with ClientSession() as session:
        base_url = settings.rule34_url
        if tags:
            url = f"{base_url}&tags={tags}"
        else:
            url = base_url
        response = await session.get(url)
        if response.status == 200:
            data = await response.json()
            return data  
        else: 
            logging.error(f"{response.status}")
            return []
