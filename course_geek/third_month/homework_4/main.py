from aiogram import executor
from config import dp
import logging
from user_info_fsm import (
    Form,
    start_form,
    process_age,
    process_name,
    process_address,
    process_day
)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    dp.register_message_handler(start_form, commands=["start"])
    dp.register_message_handler(process_name, state=Form.name)
    dp.register_message_handler(process_age, state=Form.age)
    dp.register_message_handler(process_address, state=Form.address)
    dp.register_message_handler(process_day, state=Form.day)

    executor.start_polling(dp)