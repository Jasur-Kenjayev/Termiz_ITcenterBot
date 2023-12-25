from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram import types
from keyboards.default.keybordmenu import menu
from keyboards.default.location_button import keyboard
from utils.misc.get_distance import choose_shortest
from loader import dp, bot
from data.config import CHANNELS

@dp.message_handler(text= "Orqaga ▶️")
async def enter_orgaga(message: types.Message):
	await message.answer("🏠",reply_markup=menu)

@dp.message_handler(text="📍Lokatsiya")
async def show_menu(message: types.Message):
	video_id = "BAACAgIAAxkBAAIFk2LurhAkY0weTJzl7ONNTqelOu5OAALLHQACL9p5S9ArQjM_hgL2KQQ"
	await message.answer_video(video_id,caption="<b>🤖 Botmizdagi lokatsiya yuborish funksiyasni ishlatish bo'yicha video qo'lanma\n\n🔎 Siz lokatsiya yuborish orqali bizning markazimiz joylashuvi va 👤 Sizda qancha masofada joylashgani haqida ma`lumot olishingiz mumkin\n\n🗺 Lokatsiya yuborish tugmasi orqali lokatsiyangizni yuboring👇\n\n✅ @Termiz_ITcenterBot</b>",reply_markup=keyboard)

@dp.message_handler(content_types='location')
async def get_contact(message: Message):
    username = message.from_user.username
    name = message.from_user.full_name
    id = message.from_user.id
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    closest_shops = choose_shortest(location)
    link = f"https://maps.google.com/maps?q={latitude},{longitude}"
    await bot.send_message(CHANNELS[0],f"<b>🛎New Location📍Information✅\n\n👤Nik 👉 {name}\n✍Lic 👉 @{username}\n🆔ID 👉 {id}\n📍Lokatsiyasi 👉 <a href='{link}'>link</a></b>")
    
    text = "\n\n".join([f"<a href='{url}'>{shop_name}</a>\n 🚘 Masofa: {distance:.1f} KM"
                        for shop_name, distance, url, shop_location in closest_shops])

    await message.answer(f"<b>👤Siz turgan joydan bizning IT-Centergacha bo'lgan masofa👇</b>\n\n"
                         f"{text}", disable_web_page_preview=True, reply_markup=menu)

    for shop_name, distance, url, shop_location in closest_shops:
        await message.answer_location(latitude=shop_location["lat"],
                                      longitude=shop_location["lon"])
                                      
