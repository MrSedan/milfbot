from aiogram import Router, F
from aiogram.types import InlineQuery, InlineQueryResultPhoto
import sys
from services import rule34_service

sys.path.append("..")
router = Router()


@router.inline_query(F.query.contains("r34"))  
async def show_user_links(inline_query: InlineQuery):
    tags = inline_query.query.split("r34 ", 1)[-1].strip()
    response_data = await rule34_service.get_post_list(tags)
    results = []
    if response_data:
        for item in response_data:
            file_url = item.get("file_url")
            if file_url:
                results.append(InlineQueryResultPhoto(
                    id=str(item.get("hash")),
                    photo_url=file_url,
                    thumbnail_url=item.get("preview_url")
                ))

    else: results = []
    await inline_query.answer(results, is_personal=True)