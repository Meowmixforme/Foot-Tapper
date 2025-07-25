import sounddevice as sd
import numpy as np

def play_click(accent=False, device=None):
    frequency = 880 if accent else 440
    duration = 0.2  # 200 ms, longer so it's audible
    fs = 44100
    t = np.linspace(0, duration, int(fs*duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    sd.play(wave, fs, device=device, blocking=True)