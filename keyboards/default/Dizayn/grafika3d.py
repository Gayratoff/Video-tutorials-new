from aiogram import types
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from loader import dp

Grafika = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="3Ds Max πΊπΏ"),
            KeyboardButton(text="Blender asoslari πΊπΏ")
        ],
        [
            KeyboardButton(text="ZBrush πΊπΏ"),
            KeyboardButton(text="AutoCAD πΊπΏ")
        ],

        [
            KeyboardButton(text="Maya - boshlang'ich kurs πΊπΏ")
        ],
        [
            KeyboardButton(text="π Ortga"),
            KeyboardButton(text="π Asosiy Menyu")
        ]

    ],
    resize_keyboard=True
)
@dp.message_handler(text="π   Ortga")
async def bot_start(message: types.Message):
    await message.answer(f"<b>π Ortga qaytdingiz</b>" , reply_markup=d3g)

@dp.message_handler(text="Ortga  π")
async def bot_start(message: types.Message):
    await message.answer(f"<b>π Ortga qaytdingiz</b>" , reply_markup=Grafika)

@dp.message_handler(text="3Ds Max πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>3Ds Max πΊπΏ</b>" , reply_markup=d3g)
d3g = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="3Ds Max 0 dan"),KeyboardButton(text="Modeling")],
        [
            KeyboardButton(text="Ortga  π"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="3Ds Max 0 dan")
async def bot_start(message: types.Message):
    await message.answer(f"<b>3Ds Max 0 dan</b>" , reply_markup=d3s)

d3s = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Dars 1"),
            KeyboardButton(text="Dars 2"),
            KeyboardButton(text="Dars 3")
        ],
        [
            KeyboardButton(text="Dars 4"),
            KeyboardButton(text="Dars 5"),
            KeyboardButton(text="Dars 6")
        ],
        [
            KeyboardButton(text="Dars 7"),
            KeyboardButton(text="Dars 8"),
            KeyboardButton(text="Dars 9")
        ],
        [
            KeyboardButton(text="Dars 10"),
            KeyboardButton(text="Dars 11")
        ],
        [
            KeyboardButton(text="Dars 12"),
            KeyboardButton(text="Dars 13"),
            KeyboardButton(text="Dars 14")
        ],
        [
            KeyboardButton(text="Dars 15"),
            KeyboardButton(text="Dars 16"),
            KeyboardButton(text="Dars 17")
        ],
        [
            KeyboardButton(text="Dars 18"),
            KeyboardButton(text="Dars 19"),
            KeyboardButton(text="Dars 20")
        ],
        [
            KeyboardButton(text="Dars 21"),
            KeyboardButton(text="Dars 22"),
            KeyboardButton(text="Dars 23")
        ],
        [
            KeyboardButton(text="Dars 24"),
            KeyboardButton(text="Dars 25"),
            KeyboardButton(text="Dars 26")
        ],
        [
            KeyboardButton(text="Dars 27"),
            KeyboardButton(text="Dars 28"),
            KeyboardButton(text="Dars 29"),
        ],
        [
            KeyboardButton(text="Dars 30"),
            KeyboardButton(text="Dars 31"),
            KeyboardButton(text="Dars 32")
        ],
        [
            KeyboardButton(text="Dars 33"),
            KeyboardButton(text="Dars 34"),
            KeyboardButton(text="Dars 35")
        ],
        [
            KeyboardButton(text="Dars 36"),
            KeyboardButton(text="Dars 37"),
            KeyboardButton(text="Dars 38"),
        ],
        [
            KeyboardButton(text="Dars 39"),
            KeyboardButton(text="Dars 40"),
            KeyboardButton(text="Dars 41")
        ],
        [
            KeyboardButton(text="Dars 42"),
            KeyboardButton(text="Dars 43"),
            KeyboardButton(text="Dars 44")
        ],
        [
            KeyboardButton(text="Dars 45"),
            KeyboardButton(text="Dars 46"),
            KeyboardButton(text="Dars 47"),
        ],
        [
            KeyboardButton(text="Dars 48"),
            KeyboardButton(text="Dars 49"),
            KeyboardButton(text="Dars 50")
        ],
        [
            KeyboardButton(text="Dars 51"),
            KeyboardButton(text="Dars 52")
        ],
        [
            KeyboardButton(text="π   Ortga"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)


@dp.message_handler(text="Blender asoslari πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Blender asoslari πΊπΏ</b>" , reply_markup=Blendr)
Blendr = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="DARS 1-3"),KeyboardButton(text="DARS 4-6")],
        [
            KeyboardButton(text="Ortga  π"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="Maya - boshlang'ich kurs πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Maya - boshlang'ich kurs πΊπΏ</b>" , reply_markup=maya)
maya = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="DARS 1-4"),KeyboardButton(text="DARS 5-7")],
        [
            KeyboardButton(text="Ortga  π"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="ZBrush πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>ZBrush πΊπΏ</b>" , reply_markup=zbrush)
zbrush = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="DARS  1-5"),KeyboardButton(text="DARS 6-9")],
        [
            KeyboardButton(text="Ortga  π"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="AutoCAD πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>ZBrush πΊπΏ</b>" , reply_markup=Autocad)
Autocad = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="DARS 1-6"),KeyboardButton(text="DARS 7-11")],
        [
            KeyboardButton(text="Ortga  π"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)