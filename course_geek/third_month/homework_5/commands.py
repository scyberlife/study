from aiogram import types, bot
from db.base import get_products


async def products(message: types.Message):
    products = get_products()
    for product in products:
        text = f"ID: {product[0]}\nName: {product[1]}\nPrice: {product[2]}$"
        await message.answer_photo(await send_product_info(product[3]), caption=text)

"""
Displays the characteristics of each item of goods taken from the database.
"""

async def send_product_info(photo_path: str):
    photo = open(photo_path, 'rb')
    return photo

"""
Opens a photo.
"""
