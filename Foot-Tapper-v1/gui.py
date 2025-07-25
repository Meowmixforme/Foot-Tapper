from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QSlider, QComboBox, QHBoxLayout
)
from PySide6.QtCore import Qt, QTimer
from heartbeat import HeartbeatWidget
from metronome import Metronome
import sys

class MetronomeApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setWindowTitle("Foot-Tapper-v1 🕺🏼")

        self.layout = QVBoxLayout()
        self.window.setLayout(self.layout)

        # BPM controls
        bpm_layout = QHBoxLayout()
        self.bpm_label = QLabel("BPM: 120")
        self.bpm_slider = QSlider(Qt.Horizontal)
        self.bpm_slider.setRange(20, 300)
        self.bpm_slider.setValue(120)
        self.bpm_slider.valueChanged.connect(self.update_bpm)
        bpm_layout.addWidget(self.bpm_label)
        bpm_layout.addWidget(self.bpm_slider)
        self.layout.addLayout(bpm_layout)

        # Signature
        sig_layout = QHBoxLayout()
        self.signature_box = QComboBox()
        self.signature_box.addItems(["4/4", "3/4", "6/8", "5/4", "7/8"])
        sig_layout.addWidget(QLabel("Signature:"))
        sig_layout.addWidget(self.signature_box)
        self.layout.addLayout(sig_layout)

        # Subdivision
        sub_layout = QHBoxLayout()
        self.subdivision_box = QComboBox()
        self.subdivision_box.addItems(["Quarter", "Eighth", "Triplet", "Sixteenth"])
        sub_layout.addWidget(QLabel("Subdivision:"))
        sub_layout.addWidget(self.subdivision_box)
        self.layout.addLayout(sub_layout)

        # Tap tempo
        self.tap_tempo = QPushButton("Tap Tempo")
        self.tap_tempo.clicked.connect(self.tap)
        self.layout.addWidget(self.tap_tempo)

        # Start/Stop
        btn_layout = QHBoxLayout()
        self.start_btn = QPushButton("Start")
        self.stop_btn = QPushButton("Stop")
        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)
        self.layout.addLayout(btn_layout)

        # Heartbeat line visualization
        self.heartbeat = HeartbeatWidget()
        self.layout.addWidget(self.heartbeat)

        # Metronome logic
        self.metronome = Metronome(self.on_tick)
        self.tap_times = []

    def update_bpm(self, value):
        self.bpm_label.setText(f"BPM: {value}")
        self.metronome.set_bpm(value)

    def tap(self):
        import time
        now = time.time()
        self.tap_times.append(now)
        if len(self.tap_times) > 4:
            self.tap_times.pop(0)
        if len(self.tap_times) >= 2:
            intervals = [self.tap_times[i+1] - self.tap_times[i] for i in range(len(self.tap_times)-1)]
            avg_interval = sum(intervals) / len(intervals)
            bpm = int(60 / avg_interval)
            self.bpm_slider.setValue(bpm)
            self.update_bpm(bpm)

    def on_tick(self, is_accent):
        self.heartbeat.beat(is_accent)

    def start(self):
        self.metronome.configure(
            bpm=self.bpm_slider.value(),
            signature=self.signature_box.currentText(),
            subdivision=self.subdivision_box.currentText()
        )
        self.metronome.start()

    def stop(self):
        self.metronome.stop()

    def run(self):
        self.window.show()
        sys.exit(self.app.exec())