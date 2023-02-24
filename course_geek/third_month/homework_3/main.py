from aiogram import executor
from config import dp
from admin import proverka, ban_user


if __name__ == "__main__":
    dp.register_message_handler(ban_user, commands=["yes"])
    dp.register_message_handler(proverka)
    executor.start_polling(dp)