import logging
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
from notifier import (
    Form,
    start_form,
    process_hour,
    process_name,
)


async def startup(_):
    db_init()
    delete_tables()
    create_tables()
    populate_products()
    get_products()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    dp.register_message_handler(products, commands=['products'])
    dp.register_message_handler(find)
    scheduler.start()
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=startup)