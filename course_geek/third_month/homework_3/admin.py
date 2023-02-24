from config import dp, bot
from aiogram import types, Bot


async def admin_if(message: types.Message):
    message_author = message.from_user.id
    admins = await bot.get_chat_administrators(chat_id=message.chat.id)
    for admin in admins:
        if message_author == admin["user"]["id"]:
            return True
    return False

"""
Function checks if the user is an administrator.
"""

async def proverka(message: types.Message):
    words = ['fool', 'fool1']
    admins_mention = ""
    if message.chat.type != 'private':
        admins = await bot.get_chat_administrators(chat_id=message.chat.id)
        for admin in admins:
            admins_mention += f"@{admin.user.username}, "
        for word in words:
            if word == message.text.lower():
                await message.reply(text=f"{admins_mention} Should this person be banned?"
                                         f"@{message.from_user.username} id:/ {message.from_user.id}")
                break

"""
The function contacts the chat administrators if 
there are any words from the list.
"""

async def ban_user(message: types.Message):
    admin_author = await admin_if(message)
    user_id = int(message.reply_to_message["text"].split('/')[1])
    if admin_author:
        try:
            await bot.ban_chat_member(chat_id=message.chat.id,
                                      user_id=user_id)
            await message.answer(f"Пользователь с ID {user_id} забанен.")
        except Exception as e:
            await message.answer(f"Не удалось забанить пользователя с ID {user_id}. Ошибка: {e}")

"""
The function bans the user.
"""