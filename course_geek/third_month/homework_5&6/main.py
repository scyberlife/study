import logging
from aiogram import executor
from config import dp, scheduler
from commands import products
from pprint import pprint as pp
from parsing import scrape_cars
from db.base import (
    db_init,
    delete_tables,
    create_tables,
    populate_products,
    get_products,
)
from db.cars import (
    db_ini,
    create_tab,
    done_cars,
    get_cars,
)

from notifier import find
from notifier import (
    Form,
    process_hour,
    process_name,
    process_minutes
)


async def startup(_):
    db_init()
    delete_tables()
    create_tables()
    populate_products()
    get_products()
    db_ini()
    create_tab()
    done_cars()
    get_cars(cars)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    cars = scrape_cars()
    get_cars(cars)
    pp(cars)
    dp.register_message_handler(products, commands=["products"])
    dp.register_message_handler(process_name, state=Form.name)
    dp.register_message_handler(process_hour, state=Form.hour)
    dp.register_message_handler(process_minutes, state=Form.minutes)
    dp.register_message_handler(find)
    scheduler.start()
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=startup)