from aiogram import executor
from config import dp
from commands import words_check, ban_user


if __name__ == "__main__":
    dp.register_message_handler(ban_user, commands=["yes"])
    dp.register_message_handler(words_check)
    executor.start_polling(dp)