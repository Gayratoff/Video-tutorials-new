from aiogram import types

from loader import dp,bot

@dp.message_handler(text="Samar Badriddinov πΊπΏ")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    await message.answer(f"<b>Bu bolimda 5ta darslik mavjudππ»ππ»ππ»</b>")
    video_manzili ="https://t.me/Mobil_dasturchilar/296"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Kirish\n\nπ @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/297"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Machine Learning: yuz belgisini aniqlash\n\nπ @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/298"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Machine Learning: qo'l pozasini aniqlash\n\nπ @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/299"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Machine Learning: pozani aniqlash\n\nπ @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/300"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Machine Learning: tana segmentatsiyasi\n\nπ @ITSchoolUz_RoBot")