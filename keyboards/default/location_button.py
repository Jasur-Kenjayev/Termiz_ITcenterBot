from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                  
                                       KeyboardButton(text="🗺 Lokatsiya yuborish",
                                                      request_location=True)
                                                      ],
                                                      [
                                                      KeyboardButton(text="Orqaga ▶️"),
                                   ]
                               ])
                              
                              
