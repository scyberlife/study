from aiogram import executor
from config import dp, scheduler
from commands import products
from db.base import (
    db_init,
    delete_tables,
    create_tables,
    populate_products,
    get_products,
)
from notifier import find


async def startup(_):
    db_init()
    delete_tables()
    create_tables()
    populate_products()
    get_products()

if __name__ == '__main__':
    dp.register_message_handler(products, commands=['products'])
    dp.register_message_handler(find)
    scheduler.start()
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=startup)