import random
from aiogram import types
from config import scheduler, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class Form(StatesGroup):
    name = State()
    hour = State()
    minutes = State()



async def start_form(message: types.Message):
    await message.reply("")
    await Form.hour.set()


async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await message.reply("Enter your hour.")
        await Form.hour.set()


async def process_hour(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['hour'] = message.text
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        keyboard.add(KeyboardButton("1"), KeyboardButton("2"))
        keyboard.add(KeyboardButton("3"), KeyboardButton("4"))
        keyboard.add(KeyboardButton("5"), KeyboardButton("6"), KeyboardButton("7"),
                     KeyboardButton("8"), KeyboardButton("9"), KeyboardButton("10"),
                     KeyboardButton("11"), KeyboardButton("12"))
        await message.reply("minutes",
                            reply_markup=keyboard)
        await Form.minutes.set()


async def process_minutes(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['minutes'] = message.text
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        keyboard.add(KeyboardButton("10"), KeyboardButton("20"))
        keyboard.add(KeyboardButton("30"), KeyboardButton("40"))
        keyboard.add(KeyboardButton("50"), KeyboardButton("60"))
        await message.reply("minutes",
                            reply_markup=keyboard)
        await find()
        await stae.finish()



async def find(message: types.Message):
    word = 'напомни'
    interval = random.randrange(2000, 20000)
    cut_word = message.text.lower().replace('напомни', '')
    if word in message.text.lower():
        await process_name(cut_word)
        scheduler.add_job(notify, 'cron', day_of_week='mon', hour=9, args=(message.chat.id, cut_word, ))
        await message.answer('хорошо напомню!')

"""
Creates a random interval for reminder.
"""

async def notify(user_id: int, cut_word):
    await bot.send_message(
        text=cut_word,
        chat_id=user_id
    )

"""
Sends a reminder.
"""