import sounddevice as sd
import numpy as np

# Play drum sound

def play_drum():
    """Simulates a snare drum sound using a short burst of noise."""
    fs = 44100
    duration = 0.08
    t = np.linspace(0, duration, int(fs * duration), False)
    noise = np.random.normal(0, 0.4, t.shape)
    envelope = np.exp(-40 * t)
    drum_wave = noise * envelope
    sd.play(drum_wave, fs, blocking=False)

# Play cymbal sound

def play_cymbal(soft=True):
    """Simulates a (soft) cymbal sound using filtered noise."""
    fs = 44100
    duration = 0.12
    t = np.linspace(0, duration, int(fs * duration), False)
    noise = np.random.normal(0, 0.25 if soft else 0.5, t.shape)
    mod = np.sin(2 * np.pi * 8000 * t)
    cymbal_wave = noise * mod * np.exp(-15 * t)
    sd.play(cymbal_wave, fs, blocking=False)