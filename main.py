import asyncio
from aiogram import Bot, Dispatcher
from services.config import settings
from handlers import inline_images, inline_animations, inline_videos


async def main():
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()
    dp.include_routers(inline_images.router)
    dp.include_routers(inline_animations.router)
    dp.include_routers(inline_videos.router)

    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
