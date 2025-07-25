from PySide6.QtWidgets import QLabel

class HeartbeatWidget(QLabel):
    def __init__(self):
        super().__init__()
        self.setMinimumHeight(40)
        self.setText("Ready!")
        self.beat_count = 0

    def pulse(self, count):
        sneaker = "👟" if count % 2 == 0 else ""
        line = "—" * (count % 16)
        self.setText(f"{line}{sneaker}")