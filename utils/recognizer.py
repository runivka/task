# utils/recognizer.py

from vosk import Model, KaldiRecognizer
from settings import VOSK_MODEL_PATH
import json

model = Model(VOSK_MODEL_PATH)

def recognize_voice_from_wav(wav_path):
    with open(wav_path, "rb") as f:
        rec = KaldiRecognizer(model, 16000)
        data = f.read()
        rec.AcceptWaveform(data)
        result = json.loads(rec.FinalResult())
        return result.get("text", "").lower()
