from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

class Form(StatesGroup):
    name = State()
    address = State()
    day = State()

async def start_form(callback: types.CallbackQuery):
    await callback.answer("Hello! In order to send you the goods, we "
                        "need to get some information. Please enter "
                        "your name.")
    await Form.name.set()

