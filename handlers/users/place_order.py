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
from utils.form_order_string import form_order_string


@dp.message_handler(Command("start_order"), state="*")
@dp.message_handler(Text(equals="Найти сопровождение"), state="*")
async def start_find_mate(message: types.Message):
    info_ = await Client(message.from_user.id).get_info()
    print(info_)
    if info_.get('status') == 'registered':
        # start_state
        await Order_state.Chose_Gender.set()
        await message.answer("Выберите пол партнера: ",reply_markup=gender_kb)


@dp.message_handler(state=Order_state.Chose_Gender)
async def get_body_shape(message: types.Message, state: FSMContext):
    answer_ = message.text
    await state.update_data(gender=answer_)
    await Order_state.next()
    await message.answer("Предпочитаемый возраст:\n", reply_markup=age_kb)


@dp.message_handler(state=Order_state.Chose_Age)
async def get_age(message: types.Message, state: FSMContext):
    answer_ = message.text
    await state.update_data(age=answer_)
    await Order_state.next()
    await message.answer("Выберите телосложение:\n", reply_markup=body_kb)

    @dp.message_handler(state=Order_state.Chose_Body_Type)
    async def get_body(message: types.Message, state: FSMContext):
        answer_ = message.text
        await state.update_data(body=answer_)
        await Order_state.next()
        await message.answer("Бюджет на вечер", reply_markup=main_menu_kb)

    @dp.message_handler(state=Order_state.Budget)
    async def get_body(message: types.Message, state: FSMContext):
        answer_ = message.text
        await state.update_data(budget=answer_)
        await Order_state.next()
        await message.answer("Напишите дату и время встречи", reply_markup=main_menu_kb)


    @dp.message_handler(state=Order_state.Date_Time)
    async def get_body(message: types.Message, state: FSMContext):
        answer_ = message.text
        await state.update_data(date_time=answer_)
        await Order_state.next()
        await message.answer("Напишите адрес встречи", reply_markup=main_menu_kb)

    @dp.message_handler(state=Order_state.Location)
    async def get_body(message: types.Message, state: FSMContext):
        answer_ = message.text
        await state.update_data(address=answer_)
        await Order_state.next()
        await message.answer("Напишите пожелания при подборе", reply_markup=main_menu_kb)

    @dp.message_handler(state=Order_state.Chose_preferences)
    async def get_body(message: types.Message, state: FSMContext):
        answer_ = message.text
        await state.update_data(preferences=answer_)
        await Order_state.next()
        await message.answer("Напишите номер или телеграм логин,"
                             "который мы можем показать вашему "
                             "сопровождению")


    @dp.message_handler(state=Order_state.Contact_info)
    async def get_prefs(message: types.Message, state: FSMContext):
        answer_ = message.text
        await state.update_data(contact=answer_)
        await Order_state.next()
        data_ = await state.get_data()
        string_ = await form_order_string(data_)
        await bot.send_message(message.from_user.id, string_)
        await message.answer("Подтверждаете свой выбор?", reply_markup=confirmation_kb)

    @dp.message_handler(state=Order_state.User_Confirmation)
    async def get_prefs(message: types.Message, state: FSMContext):
        answer_ = message.text
        await state.update_data(confirmation=answer_)
        if message.text == "ДА":
            data_ = await state.get_data()
            # store order in db
            order_ = Order(message.from_user.id)
            await order_.add_order(data_)
            # notify admin
            await message.answer("Ваша заяка на модерации. Скоро мы ее опубликуем", reply_markup=main_menu_kb)
            await notify_admin(dp, str(data_), "запрос создан подтвердите")
            await state.finish()
        else:
            await state.finish()
            await message.answer("Пожалуйста создайте заявку заново /start_order")
