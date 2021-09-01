from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

gender_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Мужской"),
            KeyboardButton(text="Женский")
        ],
        [
            KeyboardButton(text="Персональный менеджер")
        ]
    ]
)

age_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="18-25"),
            KeyboardButton(text="25-35"),
            KeyboardButton(text="35-45"),
            KeyboardButton(text="45+"),
        ],
        [
            KeyboardButton(text="Персональный менеджер")
        ]
    ]
)

body_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Стройное"),
            KeyboardButton(text="Нормальное"),
            KeyboardButton(text="Chubby"),
        ],
        [
            KeyboardButton(text="Персональный менеджер")

        ]
    ]
)

confirmation_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ДА"),
            KeyboardButton(text="НЕТ"),
        ],
        [
            KeyboardButton(text="Персональный менеджер")
        ]
    ]
)
