from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from loader import bot
from loader import dp



from loader import dp

from keyboards.default.start_kb import start_kb
from keyboards.default.main_kb import main_menu_kb
from data.config import admins
from utils.notify_admins import notify_admin
from utils.mongo.clients_class import Client


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    # put user in db
    if await Client(message.from_user.id).get_info() is None:
        await Client(message.from_user.id).add_user(dict(message.from_user), message.text)
        await message.answer(f'Приветствую вас! Я умный помошник Альфредо. \n'
                             f'Я помогу Вам подобрать сопровождение на вечер. '
                             f'Если вы не робот пожалуйста нажмите на кнопку ниже', reply_markup=start_kb)
    else:
        await message.answer("C возвращением!", reply_markup=main_menu_kb)



