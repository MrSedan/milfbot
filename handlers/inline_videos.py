from aiogram import Router, F
from aiogram.types import InlineQuery, InlineQueryResultVideo
from aiogram.enums.parse_mode import ParseMode
import sys
from services import rule34_service, danbooru_service

sys.path.append("..")
router = Router()

@router.inline_query(F.query.contains("vid"))
async def show_user_videos(inline_query: InlineQuery):
    result = []
    try:
        service = inline_query.query.split(" ")[1]
        tags = inline_query.query.split(f"vid {service}", 1)[-1].strip()
        if service == "r34":
            response_data = await rule34_service.get_post_list(tags)
            if response_data:
                for item in response_data:
                    file_url = item.get("file_url")
                    if file_url and file_url.endswith(".mp4"):
                        result.append(InlineQueryResultVideo(
                            id=str(item.get("hash")),
                            video_url=file_url,
                            mime_type="video/mp4",
                            thumbnail_url=item.get("preview_url"),
                            title="Rule34 Video",
                            parse_mode=ParseMode.MARKDOWN_V2,
                            caption=f"[Source](https://rule34.xxx/index.php?page=post&s=view&id={item.get('id')})",
                            video_width=item.get("width"),
                            video_height=item.get("height"),
                            video_duration=item.get("duration"),
                            description=tags
                        ))
        elif service == "danbooru":
            response_data = await danbooru_service.get_post_list(tags)
            if response_data:
                for item in response_data:
                    file_url = item.get("file_url")
                    if file_url and file_url.endswith(".mp4"):
                        result.append(InlineQueryResultVideo(
                            id=str(item.get("md5")),
                            video_url=file_url,
                            mime_type="video/mp4",
                            thumbnail_url=item.get("preview_file_url"),
                            title="Danbooru Video",
                            parse_mode=ParseMode.MARKDOWN_V2,
                            caption=f"[Source](https://danbooru.donmai.us/posts/{item.get('id')})",
                            video_width=item.get("image_width"),
                            video_height=item.get("image_height"),
                            video_duration=item.get("duration"),
                            description=tags
                        ))
    except Exception:
        pass

    await inline_query.answer(result, is_personal=True)