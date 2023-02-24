from config import dp, bot
from aiogram import types, Bot
from pprint import pprint


async def admin_if(message: types.Message):
    message_author = message.from_user.id
    admins = await bot.get_chat_administrators(chat_id=message.chat.id)
    for admin in admins:
        if message_author == admin["user"]["id"]:
            return True
    return False


async def proverka(message: types.Message):
    words = ['fool', 'fool1']
    admins_mention = ""
    if message.chat.type != 'private':

        admins = await bot.get_chat_administrators(chat_id=message.chat.id)
        for admin in admins:
            admins_mention += f"@{admin.user.username}, "
        for word in words:
            if word == message.text:
                await message.reply(text=f"{admins_mention} забанить ли данного человека @{message.from_user.username}/"
                                         f"{message.from_user.id}")
                break

async def other(message: types.Message):
    pprint(message.reply_to_message["text"])
    admin_author = await admin_if(message)
    if admin_author:
        await ban_user(message.chat.id, int(message.reply_to_message["text"].split('/')[1]))

async def ban_user(chat_id: int, user_id: int):
    try:
        await bot.ban_chat_member(chat_id=chat_id, user_id=user_id)
        await bot.send_message(chat_id=chat_id, text=f"Пользователь с ID {user_id} забанен.")
    except Exception as e:
        await bot.send_message(chat_id=chat_id,
                               text=f"Не удалось забанить пользователя с ID {user_id}. Ошибка: {e}")