from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.contrib.fsm_storage.memory import MemoryStorage



load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())
scheduler = AsyncIOScheduler()