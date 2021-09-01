import logging

from aiogram import Dispatcher

from data.config import admins



async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "Бот Запущен и готов к работе")

        except Exception as err:
            logging.exception(err)

async def need_assitance(dp:Dispatcher, user_data):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, f"Пользователю {user_data.full_name} {user_data.username} нужна помощь")

        except Exception as err:
            logging.exception(err)


async def notify_admin(dp: Dispatcher, user_info:str, text:str):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, f"{text} {user_info}")

        except Exception as err:
            logging.exception(err)
