# main.py

import logging
from aiogram import Bot, Dispatcher, types
from settings import TOKEN
from handlers import text_handlers, voice_handlers
from keyboards import start_keyboard

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    intro_message = """
    Привет, я Никита Лобанов! Этот бот поможет поближе со мной познакомиться!
    Ты можешь написать, сказать в голосовом сообщении или выбрать из меню вот эти команды:
    """
    await message.answer(intro_message, reply_markup=start_keyboard())

@dp.message_handler(content_types=['text'])
async def handle_text(message: types.Message):
    await text_handlers.handle_command(message, bot)

@dp.message_handler(content_types=['voice'])
async def handle_voice(message: types.Message):
    await voice_handlers.voice(message, bot)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
