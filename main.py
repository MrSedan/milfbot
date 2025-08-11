import asyncio
from aiogram import Bot, Dispatcher
from services.config import settings
from handlers import inline_images, inline_animations, inline_videos
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command

async def main():
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()
    dp.include_routers(inline_images.router)
    dp.include_routers(inline_animations.router)
    dp.include_routers(inline_videos.router)

    async def get_guide_text():
        username = (await bot.me()).username if hasattr(bot, "me") else "YOURBOT"
        return (
            "*How to use this bot:*\n\n"
            f"Just type in any chat:\n`@{username} pic r34 cat`\n"
            f"Or:\n`@{username} gif danbooru neko`\n\n"
            "*You can use:*\n"
            "`pic`, `gif`, `vid` and `r34`, `danbooru`, `safebooru` as sources\.\n\n"
            "*Example:*\n"
            f"`@{username} pic r34 cat`\n\n"
            "_Note: Danbooru restricts tag searches for users without an upgraded account\. Only one tag per search unless you have a gold danbooru profile\._"
        )

    @dp.message()
    async def guide_message(message):
        if message.text and (message.text == "/start" or message.text.startswith("/start guide")):
            await message.answer(await get_guide_text(), parse_mode=ParseMode.MARKDOWN_V2)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
