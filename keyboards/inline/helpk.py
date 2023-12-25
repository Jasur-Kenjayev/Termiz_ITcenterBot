from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
      InlineKeyboardButton(text="🌐 Front-End Dasturlash 🌐", callback_data="front"),
   
       ],
       [
        InlineKeyboardButton(text="🧩 Beck-End Dasturlash 🧩",callback_data="backe"),
       ],
       [
       InlineKeyboardButton(text="🎨 Web Dizayn 🎨", callback_data="web"),
       ],
       [ InlineKeyboardButton(text="👨‍💻Kompyuter Savodxonligi👨‍💻",callback_data="savot"),
    ],
])
