from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class Form(StatesGroup):
    name = State()
    age = State()
    address = State()
    day = State()


async def start_form(message: types.Message):
    await message.reply("Hello! In order to send you the goods, we "
                        "need to get some information. Please enter "
                        "your name.")
    await Form.name.set()

"""
The function greets and saves the name.
"""

async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await message.reply("Enter your age.")
        await Form.age.set()

"""
The function saves the age
"""

async def process_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
        await message.reply("Enter your address.")
        await Form.address.set()

"""
The function saves the address.
"""

async def process_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        keyboard.add(KeyboardButton("Monday"), KeyboardButton("Tuesday"))
        keyboard.add(KeyboardButton("Wednesday"), KeyboardButton("Thursday"))
        keyboard.add(KeyboardButton("Friday"), KeyboardButton("Saturday"), KeyboardButton("Sunday"))
        await message.reply("Enter the day of the week that is convenient for you to receive the goods.",
                            reply_markup=keyboard)
        await Form.day.set()

"""
The function saves the day and outputs buttons.
"""

async def process_day(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['day'] = message.text
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        if message.text not in days:
            await message.answer("Invalid day of the week selected.")
        else:
            await state.finish()
            await message.answer("Your data has been accepted. Please wait for a call from the manager.")

"""
The function checks the days and finishes.
"""
