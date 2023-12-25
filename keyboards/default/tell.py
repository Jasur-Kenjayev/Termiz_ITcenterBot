from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

telle = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="📲 Raqam Yuborish",
                                                      request_contact=True),
                                                      ],
                                                      [
                                                      KeyboardButton(text="Bekor qilish 🚫"),
                                   ]
                               ])
