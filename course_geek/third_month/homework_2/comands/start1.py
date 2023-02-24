from aiogram import types


kb = types.ReplyKeyboardMarkup(
    resize_keyboard=True
)
kb.add(
    types.KeyboardButton(text="Iphone")
)
kb.add(
    types.KeyboardButton(text="назад")
)
async def start1(message: types.Message):
    await message.answer("Товары:", reply_markup=kb)