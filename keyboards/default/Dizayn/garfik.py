from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

Grf = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Adobe Photoshop (Asror Iskandarov) πΊπΏ"),
        ],
        [
            KeyboardButton(text="Adobe Illustrator (Madina Mavlonova) πΊπΏ"),

        ],
        [
            KeyboardButton(text="Adobe Illustrator πΊπΏ"),
            KeyboardButton(text="Mockup dizayn kursi πΊπΏ")
        ],
        [
            KeyboardButton(text="π Ortga"),
            KeyboardButton(text="π Asosiy Menyu")
        ]

    ],
    resize_keyboard=True
)