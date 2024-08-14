import os

class Settings():
    rule34_url: str = os.environ.get("RULE34_URL")
    bot_token: str = os.environ.get("BOT_TOKEN")

settings = Settings()