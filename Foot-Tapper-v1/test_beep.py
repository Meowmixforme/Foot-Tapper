import sounddevice as sd
import numpy as np

fs = 44100
duration = 1.0  # One second
frequency = 440
t = np.linspace(0, duration, int(fs * duration), False)
wave = 0.5 * np.sin(2 * np.pi * frequency * t)
sd.play(wave, fs, blocking=True)