# keyboards.py

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def start_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(KeyboardButton("Последнее фото"))
    keyboard.row(KeyboardButton("Фото из школы"))
    keyboard.row(KeyboardButton("Пост об увлечении"))
    keyboard.row(KeyboardButton("Объясни gpt"))
    keyboard.row(KeyboardButton("Разница между sql и nosql"))
    keyboard.row(KeyboardButton("Расскажи историю первой любви"))
    keyboard.row(KeyboardButton("Ссылка на проект"))
    return keyboard
