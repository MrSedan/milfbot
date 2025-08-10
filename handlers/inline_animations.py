from aiogram import Router, F
from aiogram.types import InlineQuery, InlineQueryResultGif
from aiogram.enums.parse_mode import ParseMode
import sys
from services import rule34_service, danbooru_service

sys.path.append("..")
router = Router()

@router.inline_query(F.query.contains("gif"))
async def show_user_gifs(inline_query: InlineQuery):
    try:
        service = inline_query.query.split(" ")[1]
        tags = inline_query.query.split(f"gif {service}", 1)[-1].strip()
        result = []
        if service == "r34":
            response_data = await rule34_service.get_post_list(tags)
            if response_data:
                for item in response_data:
                    file_url = item.get("file_url")
                    if file_url and file_url.endswith(".gif"):
                        result.append(InlineQueryResultGif(
                            id=str(item.get("hash")),
                            gif_url=file_url,
                            thumbnail_url=item.get("preview_url"),
                            parse_mode=ParseMode.MARKDOWN_V2,
                            caption=f"[Source](https://rule34.xxx/index.php?page=post&s=view&id={item.get('id')})"
                        ))
        elif service == "danbooru":
            response_data = await danbooru_service.get_post_list(tags)
            if response_data:
                for item in response_data:
                    file_url = item.get("file_url")
                    if file_url and file_url.endswith(".gif"):
                        result.append(InlineQueryResultGif(
                            id=str(item.get("md5")),
                            gif_url=file_url,
                            thumbnail_url=item.get("preview_file_url"),
                            parse_mode=ParseMode.MARKDOWN_V2,
                            caption=f"[Source](https://danbooru.donmai.us/posts/{item.get('id')})"
                        ))
    except Exception:
        print("An error occurred while processing the inline query.")

    await inline_query.answer(result, is_personal=True)