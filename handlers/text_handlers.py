# handlers/text_handlers.py

from aiogram import types


async def handle_command(message: types.Message, bot):
    user_input = message.text.lower()

    if user_input == 'последнее фото':
        await message.answer("Вот моё селфи!")
        await bot.send_photo(chat_id=message.chat.id, photo=open('photos/Selfie.png', 'rb'))

    elif user_input == 'фото из школы':
        await message.answer("Вот моё фото со школы!")
        await bot.send_photo(chat_id=message.chat.id, photo=open('photos/School.png', 'rb'))

    elif user_input == 'пост об увлечении':
        await message.answer("Вот мой пост об увлечении!")
        await message.answer("""Хочу рассказать вам о своем увлечении, которое стало для меня невероятным хобби – битбокс. 🎶
Что это такое? Это как магия звуков, которую можно создавать только своим голосом и ртом. Я могу имитировать ударные инструменты, воссоздавать мелодии и добавлять к ним крутые эффекты – все это только с помощью звуков, которые я создаю своим голосом.
Битбокс – это не только забавное занятие, но и настоящее музыкальное искусство. Я улучшаю свой музыкальный слух, развиваю ритмичность и экспериментирую с новыми звуками. 
Но я пока не выступал на сцене :(. Надеюсь, это когда-нибудь произойдет. ^_^""")
        # Здесь вы можете отправить ссылку на пост или сам текст поста.

    elif user_input == 'объясни gpt':
        await message.answer("Объяснение gpt!")
        await bot.send_voice(chat_id=message.chat.id, voice=open('my_voice/gpt.ogg', 'rb'))

    elif user_input == 'разница между sql и nosql':
        await message.answer("Вот разница между SQL и NoSQL!")
        await bot.send_voice(chat_id=message.chat.id, voice=open('my_voice/sql_nosql.ogg', 'rb'))

    elif user_input == 'расскажи историю первой любви':
        await message.answer("Рассказ о первой любви......")
        await bot.send_voice(chat_id=message.chat.id, voice=open('my_voice/firstlove.ogg', 'rb'))
    elif user_input == 'ссылка на проект':
        await message.answer("https://github.com/runivka/task.git")
    else:
        await message.answer(
            "Прошу прощения, я не понял ваш запрос. Попробуйте снова или воспользуйтесь командой /start для вывода списка доступных команд.")
