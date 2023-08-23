# handlers/voice_handlers.py

from aiogram import types
from utils import converter, recognizer
from handlers import text_handlers
import logging
import os

# Сопоставление ключевых слов с командами
KEYWORDS_TO_COMMANDS = {
    "последнее фото": "последнее фото",
    "фото из школы": "фото из школы",
    "пост об увлечении": "пост об увлечении",
    "объясни": "объясни gpt",
    "что такое": "что такое sql и nosql",
    "расскажи историю первой любви":  "расскажи историю первой любви",
    'ссылка на проект': 'ссылка на проект'

}
def levenshtein_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]


async def voice(message: types.Message, bot):
    try:
        ogg_path = 'voice.ogg'
        await message.voice.download(ogg_path)
        wav_path = 'voice.wav'
        converter.convert_ogg_to_wav(ogg_path, wav_path)
        recognized_text = recognizer.recognize_voice_from_wav(wav_path).lower()

        min_distance = float('inf')
        recognized_command = None
        for keyword, command in KEYWORDS_TO_COMMANDS.items():
            distance = levenshtein_distance(keyword, recognized_text)
            if distance < min_distance:
                min_distance = distance
                recognized_command = command

        # Можно задать пороговое значение, например, 3, чтобы определить, считается ли распознанный текст достаточно близким к одной из команд
        threshold = 3
        if 'объясни' in recognized_text:
            message.text = "объясни gpt"
            await text_handlers.handle_command(message, bot)
        elif 'разница' in recognized_text:
            message.text = "разница между sql и nosql"
            await text_handlers.handle_command(message, bot)
        elif min_distance <= threshold:
            message.text = recognized_command
            await text_handlers.handle_command(message, bot)
        else:
            await message.answer(f"Я не смог распознать вашу команду. Вы сказали: \"{recognized_text}\"")


    except Exception as e:
        logging.error(f"Error processing voice: {e}")
        await message.answer("Произошла ошибка при обработке вашего голоса.")
    finally:
        # Удаление временных файлов
        if os.path.exists(ogg_path):
            os.remove(ogg_path)
        if os.path.exists(wav_path):
            os.remove(wav_path)
