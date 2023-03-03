import asyncio
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import scheduler, bot


class Form(StatesGroup):
    name = State()
    hour = State()
    minutes = State()


async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await message.reply("Введите час.")
        await Form.hour.set()


async def process_hour(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['hour'] = message.text
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        keyboard.add(*(str(i) for i in range(1, 13)))
        await message.reply("Введите минуты.", reply_markup=keyboard)
        await Form.minutes.set()


async def process_minutes(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['minutes'] = message.text
        chat_id = message.chat.id
        name = data['name']
        hour = data['hour']
        minutes = data['minutes']
        await add(name, hour, minutes, chat_id)
        await message.reply('Отлично! Я напомню вам об этом в указанное время.')
        await state.finish()


async def find(message: types.Message, state: FSMContext):
    word = 'напомни'
    chat_id = message.chat.id
    cut_word = message.text.lower().replace('напомни', '').strip()
    if word in message.text.lower():
        async with state.proxy() as data:
            await Form.name.set()
        await process_name(message, state)


def notify(chat_id: int, name: str):
    asyncio.create_task(bot.send_message(chat_id=chat_id, text=name))


async def add(name: str, hour: int, minutes: int, chat_id: int):
    scheduler.add_job(notify, 'cron', day_of_week='*', hour=hour, args=(chat_id, name, ))
