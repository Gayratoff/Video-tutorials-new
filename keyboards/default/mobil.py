from aiogram import types
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from loader import dp
Mobil=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Flutter 0 dan PRO gacha πΊπΏ")
        ],
        [
            KeyboardButton(text="Kotlin dasturlash tili πΊπΏ")
        ],
        [
            KeyboardButton(text="π Orqaga"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)
@dp.message_handler(text="π orqaga")
async def bot_start(message:types.Message):
    await message.answer(f"<b>Mobil Dasturlash πΊπΏ</b>", reply_markup=Mobil)
@dp.message_handler(text="orqagaπ")
async def bot_start(message:types.Message):
    await message.answer(f"<b>Mobil Dasturlash πΊπΏ</b>", reply_markup=Flutre)

@dp.message_handler(text="Flutter 0 dan PRO gacha πΊπΏ")
async def bot_start(message:types.Message):
    await message.answer(f"<b>Mobil Dasturlash πΊπΏ</b>", reply_markup=Flutre)

Flutre= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="#1 Modul"), KeyboardButton(text="#2 Modul")],
        [
            KeyboardButton(text="π orqaga"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)
@dp.message_handler(text="#1 Modul")
async def bot_start(message:types.Message):
    await message.answer(f"<b>Mobil Dasturlash πΊπΏ</b>", reply_markup=modul)
modul= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Dars 1-6"), KeyboardButton(text="Dars 7-12")],
        [KeyboardButton(text="Dars 13-18"), KeyboardButton(text="Dars 19-24")],
        [KeyboardButton(text="Dars 25-32"), KeyboardButton(text="orqagaπ")],
    ],
    resize_keyboard=True
)

@dp.message_handler(text="#2 Modul")
async def bot_start(message:types.Message):
    await message.answer(f"<b>Web Dasturlash πΊπΏ</b>", reply_markup=modul1)
modul1= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Dars 33-39"), KeyboardButton(text="Dars 40-45")],
        [KeyboardButton(text="Dars 46-50"), KeyboardButton(text="orqagaπ")],
    ],
    resize_keyboard=True
)

@dp.message_handler(text="Kotlin dasturlash tili πΊπΏ")
async def bot_start(message:types.Message):
    await message.answer(f"<b>Kotlin dasturlash tili πΊπΏ</b>", reply_markup=kotlin)
kotlin= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Dars 1-8"),KeyboardButton(text="Dars 9-16")],
        [KeyboardButton(text="π orqaga")]
    ],
    resize_keyboard=True
)