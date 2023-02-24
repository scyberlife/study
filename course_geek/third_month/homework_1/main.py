from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from os import getenv
import random

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        f"Hello {message.from_user.full_name}"
    )


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.answer(
        f"""

        /start - greets by name
        /help - displays list of commands
        /myinfo - sends user their data (id, first_name, username)
        /picture - sends a random picture

        """
    )


@dp.message_handler(commands=["myinfo"])
async def myinfo(message: types.Message):
    await message.answer(
        f"ID         {message.from_user.id}\n"
        f"FIRST_NAME {message.from_user.first_name}\n"
        f"USER_NAME  {message.from_user.username}\n"
    )


@dp.message_handler(commands=["picture"])
async def picture(message: types.Message):
    all = ["images/1.webp", "images/2.webp", "images/3.webp"]
    photo = open(random.choice(all), "rb")
    await message.answer_photo(
        photo
    )


@dp.message_handler()
async def all(message: types.Message):
    c = len(message.text.split(" "))
    if c > 3:
        await message.answer(
            f"{message.text.upper()}"
        )
    else:
        pass


executor.start_polling(dp)

