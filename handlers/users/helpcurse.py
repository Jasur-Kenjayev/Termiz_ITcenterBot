import logging
from aiogram.types import Message, CallbackQuery
from keyboards.inline.helpk import categoryMenu
from loader import dp


@dp.message_handler(text="📚 Kurslarimiz")
async def select_category(message: Message):
	await message.answer(f"<b>🖥 Kurslarimiz haqida ma`lumot oling!!!</b>", reply_markup=categoryMenu)

@dp.callback_query_handler(text_contains="web")
async def web_dzayn(call: CallbackQuery):
    await call.message.answer("<b>Veb-dizayn Nima?\n\nWorld Wide Web (WWW) kompyuter tarmog'ining paydo bo'lishi bilan bog'liq, unda reklama maqsadida veb-saytlar yaratish maqsad qilingan (1980 yillarning oxiri - 90-yillarning boshlari). Veb-dizaynerning vazifasi - bu Internetning o'ziga xos xususiyatlarini hisobga olgan holda loyiha uchun uslublar dizaynini ishlab chiqish. Ya'ni, shunchaki zamonaviy ko'rinishga ega bo'lish uchun loyihani loyihalashdan tashqari, u tarmoqning standart talablariga javob berishi kerak: grafik elementlar (logotiplar, plakatlar, chizmalar va boshqalar) optimallashtirilgan bo'lishi kerak, rang va shriftni tanlashda siz zamon talabini hisobga olishingiz kerak. foydalanuvchi qog'ozda emas, balki monitorda loyihaning grafik timsolini ko'radi. Veb-dizayner veb-saytning qanday ko'rinishi va qanday qabul qilinishi uchun javobgardir. U logotiplar, plakatlar va grafikaning boshqa elementlari bilan tanishadi, saytdagi navigatsiya orqali o'ylaydi, matnni qayerga joylashtirishni aniqlaydi. Dizayner nafaqat qiziqarli sayt yaratishi, balki uni yuklash vaqtini ham hisobga olishi kerak. Bunday veb-saytni yaratish uchun veb-dizayner nafaqat HTML & CSSni mukammal bilishi va badiiy sezgirlikka ega bo'lishi kerak, balki 'klassik' dasturlashni bilishi va ma'lumotlar bazasini tushunishi kerak. Saytlardan tashqari veb-dizaynerlar bannerlar, onlayn pochta kartochkalari, elektron prezentatsiyalarni ishlab chiqadilar.\n\n🎓 Kurs davomida quydagilarni o'rganasiz 👇\n\n✅ Photoshop dasturida ishlash\n✅ illustrator dasturida ishlash\n✅ Figma dasturida ishlash\n✅ Adobe XD dasturida ishlash\n\n📒 Kurs Davomiyligi - 2-3 oy\n\n💵 Kurs Narxi: 300 000 so'm/oy\n\n✅ @Termiz_ITcenterBot</b>")
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text_contains="front")
async def front_end(call: CallbackQuery):
    await call.message.answer("<b>Front-End Nima?\n\nFront-End dasturlovchi veb-saytning foydalanuvchiga ko’rinadigan qismini tayyorlash bilan shug’ullanadi. Masalan siz veb-saytlarda ko’radigan oddiygina tugma uchun ham Front-End dasturlovchi mehnat qilib kod yozadi. Ya’ni siz brauzer orqali ekranda ko’rib turadigan barcha narsani tayyorlash Front-End dasturchining vazifasi va mana shu tayyorlangan ishlarning jamlanmasi veb-saytning Front-End qismi deyiladi. Yanada soddaroq tushuntiradigan bo’lsam siz veb-sayt nomini brauzerga yozib, veb-saytga kirganingizda sizga ko’rinib turgan qismi Front-End qismi hisoblanadi.\n\n🎓 Kurs davomida quydagilarni o'rganasiz 👇\n\n✅ HTML va CSS texnologiyalari\n✅ Bootstrap va SASS texnologiyalari\n✅ JavaScript dasturlash tili\n✅ React va Redux texnologiyalari\n\n📒 Kurs Davomiyligi - 3-6 oy\n\n💵 Kurs Narxi: 350 000 so'm/oy\n\n✅ @Termiz_ITcenterBot</b>")
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text_contains="backe")
async def back_end(call: CallbackQuery):
    await call.message.answer("<b>Back-End Nima?\n\nAgar sizga dasturning tashqi ko'rinishidan ko'ra uning ishlash prinsiplari, logikasi qiziqroq bo'lsa unda siz backendga moyilroqsiz. Backendchini UI/UX bilan (User Interface/ User Experience) bilan ishi bo'lmaydi. Uning asosiy vazifasi frontdan keladigan so'rovlarni qabul qilib, qayta ishlash, bazaga saqlab qo'yish va biror logikani bajarishdan iborat bo'ladi. Backend Frontdan ko'ra biroz qiyinroq. O'rganadigan texnalogiyalar ham salmoqliroq.\n\n🎓 Kurs davomida quydagilarni o'rganasiz 👇\n\n✅ HTML va CSS texnologiyalari\n✅ JavaScript dasturlash tili\n✅ Node.js va Express.js texnologiyalari\n✅ MongoDB malumotlar bazasi\n\n📒 Kurs Davomiyligi - 4-6 oy\n\n💵 Kurs Narxi: 350 000 so'm/oy\n\n✅ @Termiz_ITcenterBot</b>")
    await call.message.delete()
    await call.answer(cache_time=60)
  
@dp.callback_query_handler(text_contains="savot")
async def savothonlik(call: CallbackQuery):
    await call.message.answer("<b>🖥 Kompyuter Savodxonligi\n\nIT-texnologiyasiga oid bilimlarni noldan boshlab yuqori darajaga ko'tarish. Bunda Windows operatsion tizimi, Office dasturlar paketi, standart dasturlar, internet browserlar va turli utilitalar haqida bilimga ega bo'lasiz.\n\n🎓 Kurs davomida quydagilarni o'rganasiz 👇\n\n✅ Word dasturida ishlash\n✅ Excel dasturida ishlash\n✅ PewerPoint dasturida ishlash\n✅ Google Docs bilan ishlash\n\n📒 Kurs Davomiyligi - 1-2 oy\n\n💵 Kurs Narxi: 250 000 so'm/oy\n\n✅ @Termiz_ITcenterBot</b>")
    await call.message.delete()
    await call.answer(cache_time=60)