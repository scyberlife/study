from aiogram import types

kb = types.ReplyKeyboardMarkup(
        resize_keyboard=True
)
kb.add(
    types.KeyboardButton(text="Просмотр товаров")
)
kb.add(
    types.KeyboardButton(text="О нас")
)
async def start(message: types.Message):
    await message.answer("Что вас интересует?", reply_markup=kb)