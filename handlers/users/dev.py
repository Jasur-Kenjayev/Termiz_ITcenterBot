from aiogram import types
from loader import dp, bot
from aiogram.dispatcher.filters import Command

@dp.message_handler(Command("developer"))
async def bot_dev(message: types.Message):
    text = ("<b>👨‍💻 Dasturchi haqida malumot 📇\n\n👤 Dasturchi: Jasur Kenjayev\n💬 Telegram: @Python_Koders\n☎️ Telefon: +998333009888\n📡 Kanalmiz: @Python_Koderuz\n\n✅ @Termiz_ITcenterBot</b>")
    photo_id = "AgACAgIAAxkBAAOsYuvvoUzgdrjAXthqkndhmQMF1WcAAgi_MRvMA2BLeWPO0tvDoPoBAAMCAAN4AAMpBA"
    await message.answer_photo(photo_id,caption=text)