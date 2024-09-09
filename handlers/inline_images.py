from aiogram import Router, F
from aiogram.types import InlineQuery, InlineQueryResultPhoto
import sys
from services import rule34_service, danbooru_service

sys.path.append("..")
router = Router()


@router.inline_query(F.query.contains("pic"))
async def show_user_links(inline_query: InlineQuery):

    service = inline_query.query.split(" ")[1]
    tags = inline_query.query.split(f"pic {service}", 1)[-1].strip()
    result = []
    if service == "r34":
        response_data = await rule34_service.get_post_list(tags)
        if response_data:
            for item in response_data:
                file_url = item.get("file_url")
                if file_url:
                    result.append(InlineQueryResultPhoto(
                        id=str(item.get("hash")),
                        photo_url=file_url,
                        thumbnail_url=item.get("preview_url")
                    ))
                else:
                    result = []
    elif service == "danbooru":
            response_data = await danbooru_service.get_post_list(tags)
            if response_data:
                for item in response_data:
                    file_url = item.get("file_url")
                    if file_url:
                        result.append(InlineQueryResultPhoto(
                            id=str(item.get("md5")),
                            photo_url=file_url,
                            thumbnail_url=item.get("preview_file_url"),
                            caption = f"Source: https://danbooru.donmai.us/posts/{item.get('id')}"
                        ))
            else:
                result = []

    await inline_query.answer(result, is_personal=True)
