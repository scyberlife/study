from aiogram.dispatcher import FSMContext
from config import dp, bot, storage
from aiogram import types, Bot
from aiogram.dispatcher.filters.state import StatesGroup, State


class Ban_user(StatesGroup):
    user_id = State()


async def admin_if(message: types.Message):
    admins_mention = ""
    admins = await bot.get_chat_administrators(chat_id=message.chat.id)
    for admin in admins:
        if admins_mention == admin:
            return True
        else:
            return False


async def proverka(message: types.Message):
    words = ['fool', 'fool1']
    admins_mention = ""
    admins = await bot.get_chat_administrators(chat_id=message.chat.id)
    for admin in admins:
        admins_mention += f"@{admin.user.username}, "
    for word in words:
        if word == message.text:
            await Ban_user.user_id.set()
            await bot.send_message(chat_id=message.chat.id,
                                   text=f"{admins_mention} забанить ли данного человека @{message.from_user.username}")

            break


async def other(message: types.Message, state: FSMContext):
    a = message
    if await admin_if(a) == False:
        await ban_user(bot, message.chat.id, message.from_user.id, FSMContext)


async def ban_user(bot: Bot, chat_id: int, user_id: int, state: FSMContext):
    message_obj = await state.get_data()
    print(f"{message_obj}")
    try:
        await bot.ban_chat_member(chat_id=chat_id, user_id=user_id)
        await bot.send_message(chat_id=chat_id, text=f"Пользователь с ID {user_id} забанен.")
    except Exception as e:
        await bot.send_message(chat_id=chat_id,
                               text=f"Не удалось забанить пользователя с ID {user_id}. Ошибка: {e}")  # your code goes here