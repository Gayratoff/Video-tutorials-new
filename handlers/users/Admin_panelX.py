from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import BotBlocked
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ContentType
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from states.txtpost import Xabar
from states.photopost import Rasm_Xabar,inlen
from keyboards.default.admin import tasdiq,xabar_panel
from loader import dp, bot, base
from utils.db_api.SQLDB import *

@dp.message_handler(text="RASM Xabar 📝",chat_id="1625900856")
async def bot_echo(message: types.Message):
    await message.answer(text="RASM JONATING")
    await inlen.Photo_Xabar.set()

@dp.message_handler(state=inlen.Photo_Xabar, content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message, state: FSMContext):
    rasm = message.photo[0].file_id

    await state.update_data({"rasm": rasm})
    await message.answer(text="RASMGA SARLAVHA KIRITNG")
    await inlen.Xabar_Matni.set()

@dp.message_handler(state=inlen.Xabar_Matni)
async def bot_echo(message: types.message,state:FSMContext):
    matn= message.text
    await state.update_data({"matn": matn})
    await message.answer(text="INLINE TUGMA UCHUN EKRNAGA CHIQADIGON YOZUVNI KIRITING\n\nMasalan: Kanalga Kirish")
    await inlen.in_tugma.set()

@dp.message_handler(state=inlen.in_tugma)
async def bot_echo(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({"text": text})
    await message.answer(text="SSILKA KIRITNG\n\nMasalan: <i>https://t.me/MistrUz</i> ")
    await inlen.ssilka.set()

@dp.message_handler(state=inlen.ssilka)
async def bot_echo(message: types.Message, state: FSMContext):
    silka = message.text
    user_id = message.from_user.id
    await state.update_data({"silka": silka})

    malumot= await state.get_data()

    rasm=malumot.get("rasm")
    matn = malumot.get("matn")
    text = malumot.get("text")
    silka = malumot.get("silka")

    ekranga_chiqarish =  f"<b>{matn}</b>"

    inline_tugma = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=text, url=silka)]])
    await bot.send_photo(chat_id="1625900856",photo=rasm, caption=ekranga_chiqarish,reply_markup=inline_tugma)
    try:
        await message.answer("Reklama postingiz to'g'ri bo'lsa Tasdiqlashni bosin aks holda Bekor qilish",reply_markup=tasdiq)
    except Exception:
        pass
    await inlen.Xabarni_Tasdiqlash.set()


@dp.message_handler(state=inlen.Xabarni_Tasdiqlash,text="✅ Tasdiqlash",chat_id="1625900856")
async def bot_echo(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    malumot = await state.get_data()

    rasm=malumot.get("rasm")
    matn = malumot.get("matn")
    text = malumot.get("text")
    silka = malumot.get("silka")

    users = bot_stat()
    all_users = 0
    blocked_users = 0
    for x in users:
        try:
            await bot.send_chat_action(chat_id=x[0],action='typing')
            all_users += 1
        except BotBlocked:
            blocked_users += 1
    await bot.send_message(chat_id=user_id, text=f"<b>{all_users} ta foidalanuvchilarga reklama yuborildi ✅\n\n{blocked_users} ta odam botni bloklagan</b>", reply_markup=xabar_panel)
    await state.finish()

    userlar= base.select_all_foidalanuvchilar()
    for user in userlar:
        user_id =user[3]
        ekranga_chiqarish = f"<b>{matn}</b>"
        inline_tugma = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=text, url=silka)]])
        try:
            await bot.send_photo(chat_id=user_id, photo=rasm, caption=ekranga_chiqarish, reply_markup=inline_tugma)
        except Exception:
            pass

@dp.message_handler(state=inlen.Xabarni_Tasdiqlash,text="❌ Bekor qilish")
async def bot_echo(message: types.Message, state: FSMContext):
    txt = message.text
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text="Bekor qilindi ❌",reply_markup=xabar_panel)
    await state.finish()


# mail_bt =InlineKeyboardButton(text="11-15 Dars",callback_data="3dars3")
#
# inline_tugma = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="1-5 Dars",callback_data="1dars1")]])
@dp.message_handler(text="TEXT Xabar 📝",chat_id="1625900856")
async def bot_echo(message: types.Message):
    await message.answer(text="<b>👤 Foydalanuvchilarga xabar yuborish Matin kiriting.\n\nIltimos xabar faqat TEXT formatda bo'lsin</b>")
    await Xabar.Xabar_Matni.set()

@dp.message_handler(state=Xabar.Xabar_Matni)
async def bot_echo(message: types.Message, state: FSMContext):
    txt = message.text
    user_id = message.from_user.id
    await state.update_data({"text": txt})

    malumot= await state.get_data()

    xabri = malumot.get("text")

    ekranga_chiqarish =  f"💬<b>Murojat :</b> {xabri}\n"

    await bot.send_message(chat_id="1625900856",text=ekranga_chiqarish,reply_markup=tasdiq)
    await Xabar.Xabarni_Tasdiqlash.set()


@dp.message_handler(state=Xabar.Xabarni_Tasdiqlash,text="✅ Tasdiqlash",chat_id="1625900856")
async def bot_echo(message: types.Message, state: FSMContext):
    txt = message.text
    user_id = message.from_user.id
    malumot = await state.get_data()

    xabri = malumot.get("text")
    users = bot_stat()
    all_users = 0
    blocked_users = 0
    for x in users:
        try:
            await bot.send_chat_action(chat_id=x[0],action='typing')
            all_users += 1
        except BotBlocked:
            blocked_users += 1
    await bot.send_message(chat_id=user_id, text=f"<b>{all_users} ta foidalanuvchilarga reklama yuborildi ✅\n\n{blocked_users} ta odam botni bloklagan</b>", reply_markup=xabar_panel)
    await state.finish()

    userlar= base.select_all_foidalanuvchilar()
    for user in userlar:
        user_id =user[3]
        ekranga_chiqarish = f"<b>{xabri}</b>"
        try:
            await bot.send_message(chat_id=user_id,text=ekranga_chiqarish)
        except Exception:
            pass



@dp.message_handler(state=Xabar.Xabarni_Tasdiqlash,text="❌ Bekor qilish")
async def bot_echo(message: types.Message, state: FSMContext):
    txt = message.text
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text="Bekor qilindi ❌",reply_markup=xabar_panel)
    await state.finish()
#
# @dp.message_handler(text="RASM Xabar 📝")
# async def bot_echo(message: types.Message):
#     await message.answer(text="Photo jonating")
#     await Rasm_Xabar.Photo_Xabar.set()
#
# @dp.message_handler(state=Rasm_Xabar.Photo_Xabar, content_types=ContentType.PHOTO)
# async def bot_echo(message: types.Message, state: FSMContext):
#     rasm = message.photo[0].file_id
#
#     await state.update_data({"rasm": rasm})
#     await message.answer(text="TEXT kiriting")
#     await Rasm_Xabar.Xabar_Matni.set()
#
# @dp.message_handler(state=Rasm_Xabar.Xabar_Matni)
# async def bot_echo(message: types.message,state:FSMContext):
#     matn= message.text
#     await state.update_data({"matn": matn})
#     user_id = message.from_user.id
#
#     malumot= await state.get_data()
#
#     rasm=malumot.get("rasm")
#     matn = malumot.get("matn")
#
#     ekranga_chiqarish =  f"<b>{matn}</b>"
#
#     await bot.send_photo(chat_id="1625900856",photo=rasm, caption=ekranga_chiqarish,reply_markup=tasdiq)
#     await Rasm_Xabar.Xabarni_Tasdiqlash.set()
#
# @dp.message_handler(state=Rasm_Xabar.Xabarni_Tasdiqlash,text="✅ Tasdiqlash",chat_id="1625900856")
# async def bot_echo(message: types.Message, state: FSMContext):
#     user_id = message.from_user.id
#     malumot = await state.get_data()
#
#     rasm=malumot.get("rasm")
#     matn = malumot.get("matn")
#     users = bot_stat()
#     all_users = 0
#     blocked_users = 0
#     for x in users:
#         try:
#             await bot.send_chat_action(chat_id=x[0],action='typing')
#             all_users += 1
#         except BotBlocked:
#             blocked_users += 1
#     await bot.send_message(chat_id=user_id, text=f"<b>{all_users} ta foidalanuvchilarga reklama yuborildi ✅\n\n{blocked_users} ta odam botni bloklagan</b>", reply_markup=xabar_panel)
#     await state.finish()
#
#     userlar= base.select_all_foidalanuvchilar()
#     for user in userlar:
#         user_id =user[3]
#         ekranga_chiqarish = f"<b>{matn}</b>"
#         try:
#             await bot.send_photo(chat_id=user_id, photo=rasm, caption=ekranga_chiqarish, reply_markup=xabar_panel)
#         except Exception:
#             pass
#
# @dp.message_handler(state=Rasm_Xabar.Xabarni_Tasdiqlash,text="❌ Bekor qilish")
# async def bot_echo(message: types.Message, state: FSMContext):
#     txt = message.text
#     user_id = message.from_user.id
#     await bot.send_message(chat_id=user_id,text="Bekor qilindi ❌",reply_markup=xabar_panel)
#     await state.finish()





