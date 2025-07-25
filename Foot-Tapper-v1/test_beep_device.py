import sounddevice as sd
import numpy as np

fs = 44100
duration = 1.0
frequency = 440
device = 0  # Change to the correct index from above
t = np.linspace(0, duration, int(fs * duration), False)
wave = 0.5 * np.sin(2 * np.pi * frequency * t)
sd.play(wave, fs, device=device, blocking=True)