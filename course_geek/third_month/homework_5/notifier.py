import random
from aiogram import types
from config import scheduler, bot



async def find(message: types.Message):
    word = 'напомни'
    interval = random.randrange(2000, 20000)
    cut_word = message.text.lower().replace('напомни', '')
    if word in message.text.lower():
        scheduler.add_job(notify, 'interval', seconds=interval, args=(message.chat.id, cut_word, ))
        await message.answer('хорошо напомню!')

"""
Creates a random interval for reminder.
"""

async def notify(user_id: int, cut_word):
    await bot.send_message(
        text=cut_word,
        chat_id=user_id
    )

"""
Sends a reminder.
"""