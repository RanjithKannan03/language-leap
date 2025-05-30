from os import getenv
from pathlib import Path

import sounddevice as sd
import soundfile as sf


# TTS_WAV_PATH = r'..\audio\tts.wav'
TTS_WAV_PATH = Path(__file__).resolve().parent.parent / r'audio\tts.wav'
INGAME_PUSH_TO_TALK_KEY = getenv('INGAME_PUSH_TO_TALK_KEY')


def play_voice(device_id):
    data, fs = sf.read(TTS_WAV_PATH, dtype='float32')
    sd.play(data, fs, device=device_id)
    sd.wait()

if __name__=='__main__':
    play_voice(19)
