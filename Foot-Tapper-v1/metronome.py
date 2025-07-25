import threading
import time
from audio import play_click

class Metronome:
    def __init__(self, tick_callback):
        self.bpm = 120
        self.signature = "4/4"
        self.subdivision = "Quarter"
        self.running = False
        self.thread = None
        self.tick_callback = tick_callback

    def configure(self, bpm, signature, subdivision):
        self.bpm = bpm
        self.signature = signature
        self.subdivision = subdivision

    def set_bpm(self, bpm):
        self.bpm = bpm

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.run, daemon=True)
            self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def run(self):
        beats_per_bar = int(self.signature.split('/')[0])
        subdivision_map = {"Quarter": 1, "Eighth": 2, "Triplet": 3, "Sixteenth": 4}
        subdivision = subdivision_map.get(self.subdivision, 1)
        beat_interval = 60 / self.bpm / subdivision

        count = 0
        while self.running:
            accent = count % (beats_per_bar * subdivision) == 0
            play_click(accent)
            self.tick_callback(accent)
            time.sleep(beat_interval)
            count += 1