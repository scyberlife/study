from aiogram import Dispatcher, Bot
from os import getenv
from dotenv import load_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage


load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)