import os
from dotenv import load_dotenv

from Nordigen import NordigenTelegramBot

load_dotenv(".env.local")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_API_KEY")
NORDIGEN_TOKEN = os.getenv("NORDIGEN_TOKEN")
NORDIGEEN_ACCOUNT_ID = os.getenv("NORDIGEEN_ACCOUNT_ID")

bot = NordigenTelegramBot(TELEGRAM_TOKEN, NORDIGEN_TOKEN, NORDIGEEN_ACCOUNT_ID)
bot.start_bot()