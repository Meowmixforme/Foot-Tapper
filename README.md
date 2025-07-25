# 👟 Foot-Tapper Metronome

**Foot-Tapper** is a collection of free, open-source desktop metronomes for musicians, built in Python.  


---

## Versions

### v1: Beep & Heartbeat Metronome

- Simple beep sound on each beat
- Adjustable BPM (40–240)
- Time signature support - create your own tap tempo by clicking
- **Heartbeat line visualisation**: A moving ASCII heartbeat line shows the beat visually
- Minimal GUI for quick setup
- Ideal for practising with both auditory and visual cues


<img width="413" height="441" alt="Screenshot 2025-07-25 054119" src="https://github.com/user-attachments/assets/431e3a01-438e-4055-85bc-31383ed37d8a" />


**File:** `Foot-Tapper-v1.py`

---

### v2: Drum/Cymbal & Sneaker Tap Metronome

- Drum and soft cymbal sounds alternate for a more musical experience
- Adjustable BPM, time signature, and rhythmic subdivision (quarter, eighth, sixteenth)
- **Sneaker tap visualisation**: A sneaker emoji 👟 "taps" across the screen in time with the beat
- Modern PySide6 GUI
- Modular code using OOP and SOLID principles for easy extension
- Perfect for musicians wanting a richer practice tool with engaging visual feedback


<img width="603" height="306" alt="Screenshot 2025-07-25 054643" src="https://github.com/user-attachments/assets/34b260c9-76cc-4ce3-9d57-ade862d893f4" />


**Files:**  
- `Foot-Tapper.py` (launcher for v2)
- `gui.py` (app GUI logic)
- `metronome.py` (timing and threading)
- `audio.py` (sound synthesis)
- `heartbeat.py` (visualisation widget)

---

## Installation & Usage

### 1. Install Python 3.8+ (recommended: 3.10+)

### 2. Install dependencies

```sh
pip install -r requirements.txt
```

### 3. Run your chosen version

#### v1: Beep & Heartbeat

```sh
python Foot-Tapper-v1.py
```

#### v2: Drum/Cymbal & Sneaker Tap

```sh
python Foot-Tapper.py
```

---

## File Structure

- `Foot-Tapper-v1.py` — Original beep-based metronome (single file, heartbeat visualisation)
- `Foot-Tapper.py` — Launcher for v2
- `gui.py` — User interface logic
- `metronome.py` — Metronome timing and thread control
- `audio.py` — Drum and cymbal sound synthesis
- `heartbeat.py` — Sneaker tap visualisation widget for v2
- `requirements.txt` — Python dependencies

---

## Licence

MIT Licence — free for personal or commercial use.

---

## Credits

- Python, PySide6, numpy, sounddevice
- Designed for musicians, by musicians

---

## Troubleshooting

- If you can't hear sounds, check your speaker/headphone setup and Python audio permissions.

---

Happy practising with Foot-Tapper!
