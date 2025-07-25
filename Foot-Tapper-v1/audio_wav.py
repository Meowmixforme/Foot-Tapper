import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

def play_click_wav(device=None):
    fs = 44100
    duration = 0.2
    frequency = 440
    t = np.linspace(0, duration, int(fs*duration), False)
    wave = (0.5 * np.sin(2 * np.pi * frequency * t)).astype(np.float32)
    write('click.wav', fs, wave)
    data, samplerate = wave, fs
    sd.play(data, samplerate, device=device, blocking=True)