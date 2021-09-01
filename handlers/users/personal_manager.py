from aiogram import types
from states.start_order import Order_state
from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.notify_admins import notify_admin
from loader import bot
from loader import dp

from utils.mongo.clients_class import Client
from utils.mongo.order_class import Order
from keyboards.default.main_kb import main_menu_kb
from keyboards.default.choice_kb import gender_kb, age_kb, body_kb, confirmation_kb
from utils.notify_admins import notify_admin


@dp.message_handler(Text(equals="Персональный менеджер"), state="*")
async def call_manager(message: types.Message):
    data_ = await Client(message.from_user.id).get_info()
    if data_.get("priority"):
        await notify_admin(dp, message.from_user, "Запрашивает персонального менеджера")
        await message.answer("Ваш персональный менеджер скоро с вами свяжется")
    else:
        await message.answer("У вас не оплачен премиальный аккаунт,хотели бы его приобрести? (тут будет приобритене аккаунта)")
