from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

editt = ReplyKeyboardMarkup(
    keyboard = [
        [
        KeyboardButton(text="🎨 Web-Dizayn"),
        ],
        [
            KeyboardButton(text="🌐 Front-End Dasturlash"),
            KeyboardButton(text="🧩 Beck-End Dasturlash"),
        ],
        [   
            
            KeyboardButton(text="🖥 Kompyuter Savodxonligi"),
       ],
       [
       	KeyboardButton(text="Bekor qilish 🚫"),
       ],
    ],
    resize_keyboard=True
)

nazat = ReplyKeyboardMarkup(
    keyboard = [
        [
        	KeyboardButton(text="Bekor qilish 🚫"),
        ],
     ],
     resize_keyboard=True
)
