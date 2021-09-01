from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Найти сопровождение")
        ],
        [
            KeyboardButton(text="Персональный менеджер")
        ]
    ]
)
