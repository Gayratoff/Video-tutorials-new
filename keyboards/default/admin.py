from aiogram import types
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from loader import dp
from . Menu import Menu_button



@dp.message_handler(text="🔙   Orqaga")
async def bot_start(message: types.Message):
    await message.answer(f"<b>🔙 Orqaga</b>" , reply_markup=admin_panel)

@dp.message_handler(commands="panel",chat_id="1625900856")
async def bot_start(message: types.Message):
    await message.answer("<b>✅ panel ishladi! @MistrUz</b>",reply_markup=admin_panel)

@dp.message_handler(commands="panel")
async def bot_start(message: types.Message):
    await message.answer("<b>Bu bo'lim faqat @MistrUz uchun</b>",reply_markup=Menu_button)


admin_panel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👤 Foydalanuvchilarga xabar yuborish")

        ],
        [
            KeyboardButton(text="👤 Foydalanuvchiga xabar yuborish")
        ],
        [
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="👤 Foydalanuvchilarga xabar yuborish",chat_id="1625900856")
async def bot_start(message: types.Message):
    await message.answer(f"<b>👤 Foydalanuvchilarga xabar yuborish uchun post turini tanlang...</b>" , reply_markup=xabar_panel)

xabar_panel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="TEXT Xabar 📝"),
            KeyboardButton(text="RASM Xabar 📝")

        ],
        [
            KeyboardButton(text="VIDEO Xabar 📝")
        ],
        [
            KeyboardButton(text="🔙   Orqaga")
        ]
    ],
    resize_keyboard=True
)

tasdiq = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Tasdiqlash"),
            KeyboardButton(text="❌ Bekor qilish")
        ]
    ],
    resize_keyboard=True
)