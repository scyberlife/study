from aiogram import executor
from config import dp
from comands.start import start
from comands.start1 import start1
from comands.onas import onas
from aiogram.dispatcher.filters import Text
from comands.iphone import address
from comands.iphone import otvet

if __name__ == "__main__":
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(start, Text("назад"))
    dp.register_message_handler(start1, Text("Просмотр товаров"))
    dp.register_message_handler(onas, Text("О нас"))
    dp.register_message_handler(address, Text("Iphone"))
    dp.callback_query_handler(otvet, Text("5s"))
    # dp.register_callback_query_handler(address, Text(equals="Iphone"))


    executor.start_polling(dp)