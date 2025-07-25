from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QSlider, QComboBox, QHBoxLayout
)
from PySide6.QtCore import Qt, QTimer
import sys
from metronome import Metronome
from heartbeat import HeartbeatWidget

class FootTapperApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("👟 Foot-Tapper Metronome v2")
        self.setMinimumWidth(400)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # BPM slider
        bpm_layout = QHBoxLayout()
        self.bpm_label = QLabel("BPM: 120")
        self.bpm_slider = QSlider(Qt.Horizontal)
        self.bpm_slider.setRange(40, 240)
        self.bpm_slider.setValue(120)
        self.bpm_slider.valueChanged.connect(self.update_bpm)
        bpm_layout.addWidget(self.bpm_label)
        bpm_layout.addWidget(self.bpm_slider)
        self.layout.addLayout(bpm_layout)

        # Time signature
        ts_layout = QHBoxLayout()
        self.ts_label = QLabel("Time Signature:")
        self.ts_box = QComboBox()
        self.ts_box.addItems(["2/4", "3/4", "4/4", "5/4", "6/8"])
        self.ts_box.setCurrentText("4/4")
        ts_layout.addWidget(self.ts_label)
        ts_layout.addWidget(self.ts_box)
        self.layout.addLayout(ts_layout)

        # Subdivision
        sub_layout = QHBoxLayout()
        self.sub_label = QLabel("Subdivision:")
        self.sub_box = QComboBox()
        self.sub_box.addItems(["Quarter", "Eighth", "Sixteenth"])
        sub_layout.addWidget(self.sub_label)
        sub_layout.addWidget(self.sub_box)
        self.layout.addLayout(sub_layout)

        # Heartbeat visualization
        self.heartbeat = HeartbeatWidget()
        self.layout.addWidget(self.heartbeat)

        # Start/Stop buttons
        btn_layout = QHBoxLayout()
        self.start_btn = QPushButton("Start")
        self.stop_btn = QPushButton("Stop")
        self.start_btn.clicked.connect(self.start_metronome)
        self.stop_btn.clicked.connect(self.stop_metronome)
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)
        self.layout.addLayout(btn_layout)

        # Metronome instance
        self.metronome = Metronome(
            bpm=self.bpm_slider.value(),
            beats_per_bar=int(self.ts_box.currentText().split('/')[0]),
            subdivision=self.get_subdivision(),
            tick_callback=self.visual_tick
        )

        # Update config when controls change
        self.ts_box.currentTextChanged.connect(self.config_changed)
        self.sub_box.currentTextChanged.connect(self.config_changed)

        # Timer for UI updates
        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.refresh_visual)
        self.timer.start()

        self.last_tick = 0

    def get_subdivision(self):
        sub = self.sub_box.currentText()
        return {"Quarter": 1, "Eighth": 2, "Sixteenth": 4}[sub]

    def update_bpm(self):
        bpm = self.bpm_slider.value()
        self.bpm_label.setText(f"BPM: {bpm}")
        self.config_changed()

    def config_changed(self):
        bpm = self.bpm_slider.value()
        beats_per_bar = int(self.ts_box.currentText().split('/')[0])
        subdivision = self.get_subdivision()
        self.metronome.update(bpm, beats_per_bar, subdivision)

    def start_metronome(self):
        self.metronome.tick_callback = self.visual_tick
        self.metronome._running = True
        if not self.metronome.is_alive():
            self.metronome = Metronome(
                bpm=self.bpm_slider.value(),
                beats_per_bar=int(self.ts_box.currentText().split('/')[0]),
                subdivision=self.get_subdivision(),
                tick_callback=self.visual_tick
            )
            self.metronome.start_metronome()
        else:
            self.metronome.start_metronome()

    def stop_metronome(self):
        self.metronome.stop_metronome()

    def visual_tick(self, count):
        self.last_tick = count
        self.heartbeat.pulse(count)

    def refresh_visual(self):
        self.heartbeat.pulse(self.last_tick)

def main():
    app = QApplication(sys.argv)
    window = FootTapperApp()
    window.show()
    sys.exit(app.exec())