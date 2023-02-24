from aiogram import types


kb = types.InlineKeyboardMarkup()
kb.add(
    types.InlineKeyboardButton(text="Iphone 5s", callback_data="5s")
)
kb.add(
    types.InlineKeyboardButton(text="Iphone 6s", callback_data="6s")
)
kb.add(
    types.InlineKeyboardButton(text="Iphone 7", callback_data="7")
)

async def address(message: types.Message):
    await message.reply("Iphones", reply_markup=kb)


async def otvet(call: types.CallbackQuery):
    await call.message.answer(text="Отсуствует")