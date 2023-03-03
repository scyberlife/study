from aiogram import types, bot
from db.base import get_products


async def products(message: types.Message):
    products = get_products()
    for product in products:
        text = f"{product[1]}"
        await message.answer_photo(await send_product_info(product[3]), caption=text,
                                   reply_markup=await key_by(product[0], product[2]))

"""
Displays the characteristics of each item of goods taken from the database.
"""

async def key_by(id: int, price: int):
    kb = types.InlineKeyboardMarkup(

)
    kb.add(types.InlineKeyboardButton(text=f"buy - {price}$",
                                      callback_data=f"{id}")
)
    reply_markup = kb
    return reply_markup

"""
create keyboard
"""

async def send_product_info(photo_path: str):
    photo = open(photo_path, 'rb')
    return photo

"""
Opens a photo.
"""
