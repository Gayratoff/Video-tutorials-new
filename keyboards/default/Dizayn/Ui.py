from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

UX = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Figma πΊπΏ"),
        ],
        [
            KeyboardButton(text="π Ortga"),
            KeyboardButton(text="π Asosiy Menyu")
        ]

    ],
    resize_keyboard=True
)