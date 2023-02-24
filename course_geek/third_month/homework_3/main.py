from aiogram import executor
from config import dp
from admin import proverka, other


if __name__ == "__main__":
    dp.register_message_handler(other, commands=["del"])
    dp.register_message_handler(proverka)
    executor.start_polling(dp)