from aiogram import executor
from config import dp
from admin import proverka, delete


if __name__ == "__main__":
    dp.register_message_handler(delete, commands=["да"])
    dp.register_message_handler(proverka)
    executor.start_polling(dp)