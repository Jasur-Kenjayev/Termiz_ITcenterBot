from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗞 IT-Park haqida"),
        ],
       [
       	KeyboardButton(text="📝 Kursga yozilish"),
       	KeyboardButton(text="📚 Kurslarimiz"),
       ],
      [
      	KeyboardButton(text="📍Lokatsiya"),
       	KeyboardButton(text="📞 Bog'lanish"),
       ],
    ],
    resize_keyboard=True,
)
