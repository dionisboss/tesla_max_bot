from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from aiogram.dispatcher.filters import Text
from loader import bot
from utils.misc import rate_limit
from utils.notify_admins import need_assitance


@rate_limit(5, 'help')
@dp.message_handler(Text(equals="Нужна помощь"),state="*")
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await need_assitance(dp, message.from_user)
    await message.answer("Пожалуйста обратитесь к @dionisboss")
