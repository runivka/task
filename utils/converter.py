# utils/converter.py

import subprocess

def convert_ogg_to_wav(ogg_path, wav_path):
    command = ["ffmpeg", "-i", ogg_path, "-acodec", "pcm_s16le", "-ac", "1", "-ar", "16000", wav_path]
    subprocess.run(command, check=True)
