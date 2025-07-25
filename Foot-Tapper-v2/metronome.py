import threading
import time
from audio import play_drum, play_cymbal

class Metronome(threading.Thread):
    def __init__(self, bpm=120, beats_per_bar=4, subdivision=1, tick_callback=None):
        super().__init__()
        self.bpm = bpm
        self.beats_per_bar = beats_per_bar
        self.subdivision = subdivision
        self.tick_callback = tick_callback
        self._running = False
        self.count = 0
        self.daemon = True

    def run(self):
        self.count = 0
        beat_interval = 60 / self.bpm / self.subdivision
        while self._running:
            # Drum on every beat, cymbal on every other beat
            if self.count % 2 == 0:
                play_drum()
            else:
                play_cymbal(soft=True)
            if self.tick_callback:
                self.tick_callback(self.count)
            time.sleep(beat_interval)
            self.count += 1

    def start_metronome(self):
        if not self._running:
            self._running = True
            if not self.is_alive():
                self.start()

    def stop_metronome(self):
        self._running = False

    def update(self, bpm, beats_per_bar, subdivision):
        self.bpm = bpm
        self.beats_per_bar = beats_per_bar
        self.subdivision = subdivision