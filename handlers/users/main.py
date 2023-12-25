import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from data.config import ADMINS, CHANNELS
from keyboards.inline.manage_post import confirmation_keyboard, post_callback
from keyboards.default.edit import editt, nazat
from keyboards.default.tell import telle
from keyboards.default.keybordmenu import menu
from loader import dp, bot
from states.newpost import NewPost

#break state
@dp.message_handler(text= "Bekor qilish 🚫",state=NewPost)
async def enter_jj(message: Message, state: FSMContext):
	await state.finish()
	await message.answer("🏠",reply_markup=menu)

@dp.message_handler(text="📝 Kursga yozilish")
async def create_post(message: Message):
    await message.answer("<b>👨🏻‍🎓👩🏻‍🎓 Qaysi kursda o`qishni hohlaysiz</b>",reply_markup=editt)
    await NewPost.kursm.set()

@dp.message_handler(state=NewPost.kursm)
async def enter_messagee(message: Message, state: FSMContext):
    kursm = message.text

    await state.update_data(
        {"kursm": kursm}
    )
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer("<b>✏️ Familya ism Sharifingizni\nTo`liq Kiriting....</b>",reply_markup=nazat)
    await NewPost.next()
   
@dp.message_handler(state=NewPost.NewMessage)
async def enter_ism(message: Message, state: FSMContext):
    NewMessage = message.text
    await state.update_data(
        {"NewMessage": NewMessage}
    )
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer("<b>📅 Tug‘ilgan Sana (01.03.2002) shu Formatda✅</b>")
    await NewPost.next()
    
@dp.message_handler(state=NewPost.yosh)
async def entr_cityee(message: types.Message, state: FSMContext):
    yosh = message.text
    await state.update_data(
        {"yosh": yosh}
    )
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer("<b>🏘 Yashash manzilingiz (Tuman/Shahar ni Kiriting)</b>")
    await NewPost.next()
    
@dp.message_handler(state=NewPost.termiz)
async def entr_termiz(message: types.Message, state: FSMContext):
	termiz = message.text
	await state.update_data(
        {"termiz": termiz}
	)
	await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
	await message.answer("<b>📲 Telefon raqamingizni quyidagi tugma orqali yuboring👇</b>",reply_markup=telle)
	await NewPost.next()
	
@dp.message_handler(content_types='contact',state=NewPost.phone)
async def enter_phonee(message: types.Message, state: FSMContext):
	contact = message.contact
	username = message.from_user.username
	name = message.from_user.full_name
	id = message.from_user.id
	phone_num = contact.phone_number
	await bot.send_message(CHANNELS[1],f"<b>🛎New Phone📲 Information✅\n\n👤Nik 👉 {name}\n✍Lic 👉 @{username}\n🆔ID 👉 {id}\n📱Phone 👉 +{phone_num}</b>")
	await state.update_data(
        {"contact": contact}
	)
	data = await state.get_data()
	kursm = data.get("kursm")
	NewMessage = data.get("NewMessage")
	yosh = data.get("yosh")
	termiz = data.get("termiz")
	contact = data.get("contact")
	
	msg = "<b>🧾 Quyidagi ma`lumotlar qabul qilindi</b>\n\n"
	msg += f"<b>👤 F.I.SH</b> - {NewMessage}\n\n"
	msg += f"<b>📆 Tug`ilgan Sana</b> - {yosh}\n\n"
	msg += f"<b>🔍 Manzil</b> - {termiz}\n\n"
	msg += f"<b>📱 Telefon</b> - +{contact.phone_number}\n\n"
	msg += f"<b>📙 Kurs Nomi</b> - {kursm}\n\n"
	msg += f"<b>📡 Kanalimizga a'zo bo'ling👇\n\n✅ Kanal: @Termiz_ITCenter</b>"
	await NewPost.next()
	await message.answer("<b>✅Ma`lumotlarni barchasi to`griligiga e`tibor bering</b>",reply_markup=menu)
	await message.answer(msg,reply_markup=confirmation_keyboard)
  
@dp.message_handler(state=NewPost.phone)
async def m_phone(message: Message, state: FSMContext):
   await message.reply("<b>📲 Raqam Yuborish Tugmasi Orqali Yuboring Telefon Raqamingizni👇</b>",reply_markup=telle)
   
@dp.callback_query_handler(post_callback.filter(action="post"), state=NewPost.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        kursm = data.get("kursm")
        NewMessage = data.get("NewMessage")
        yosh = data.get("yosh")
        termiz = data.get("termiz")
        contact = data.get("contact")
        
        msg = "<b>🧾 Quyidagi ma`lumotlar qabul qilindi</b>\n\n"
        msg += f"<b>🧑‍🎓 F.I.SH</b> -  {NewMessage}\n\n"
        msg += f"<b>📆 Tug`ilgan Sanasi</b> - {yosh}\n\n"
        msg += f"<b>🔍 Manzili</b> - {termiz}\n\n"
        msg += f"<b>📱 Telefoni</b> - +{contact.phone_number}\n\n"
        msg += f"<b>📙 Tanlagan Kursi</b> - {kursm}\n\n"
        msg += "<b>✅ @Termiz_ITcenterBot</b>"
        mention = data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.answer("Tanlovingiz Uchun Raxmat😊", show_alert=True)
    await call.message.answer("<b>📨 Xabaringiz yuborildi. Tez orada siz bilan bog'lanamiz ✅</b>")
    
    await bot.send_message(CHANNELS[2], f"<b>👤 Foydalanuvchi {mention} Quydagi 📒 Kursga Yozilmoqchi👇</b>")
    await bot.send_message(CHANNELS[2],msg, parse_mode="HTML")
    
    await bot.send_message(CHANNELS[3], f"<b>👤 Foydalanuvchi {mention} Quydagi 📕 Kursga Yozilmoqchi👇</b>")
    await bot.send_message(CHANNELS[3],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callback.filter(action="cancel"), state=NewPost.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.answer("Malumotlarni rad etingiz❌", show_alert=True)
    await call.message.answer("<b>Malumotlaringiz rad etildi 🛑</b>")
    
@dp.message_handler(state=NewPost.Confirm)
async def enter_finshit(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi Kiritgan Malumotlaringizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
   

    
	