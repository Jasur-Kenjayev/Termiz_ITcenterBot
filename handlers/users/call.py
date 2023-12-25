from loader import dp
from aiogram import types

@dp.message_handler(text="📞 Bog'lanish")
async def alloqaa(message:
	types.Message):
		text = "<b>✅ Quyidagi raqamlar orqali biz bilan bog'laning👇\n\n1⃣ Telefon: +998998880000\n2⃣ Telefon: +998900000000\n\n📡 Telegram kanal - @Termiz_ITCenter\n📸 Instagram - <a href='https://instagram.com/termiz_itcenter?igshid=YmMyMTA2M2Y='>@Termiz_ITCenter</a>\n\n✅ @Termiz_ITcenterBot</b>"
		photo_id = "AgACAgIAAxkBAAIG3mLvGvwAAcnrrD-eL4OOa-PZKqhwZgACpMAxG4E2eUvNPNjX8DlcRAEAAwIAA3kAAykE"
		await message.answer_photo(photo_id,caption=text)