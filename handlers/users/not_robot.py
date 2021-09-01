from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.notify_admins import notify_admin
from loader import bot
from loader import dp

from utils.mongo.clients_class import Client
from keyboards.default.main_kb import main_menu_kb



@dp.message_handler(Text(equals="Я не робот"), state= "*")
async def not_robot(message: types.Message):
    info_ = await Client(message.from_user.id).get_info()
    if info_ is not None and info_['status'] == 'started':
        await message.answer("Вы прошли первичную верификацию. Я передаю ваш контакт менеджеру."
                             "Он свяжется с вами и расскажет как работает бот.", reply_markup=main_menu_kb)
        await Client(message.from_user.id).update_field("status", "registered")

        await notify_admin(dp, message.from_user, "Прошел регистрацию. Нужно с ним связаться")
