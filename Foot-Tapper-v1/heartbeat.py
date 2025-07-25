from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import QTimer, QRectF

class HeartbeatWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(100)
        self.setMaximumHeight(100)
        self.beat_data = [0.0] * 200  # 200 samples for the graph
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_graph)
        self.timer.start(20)  # update every 20 ms

    def beat(self, is_accent):
        # Simulate a heartbeat spike
        spike = 1.0 if is_accent else 0.5
        self.beat_data[-1] = spike

    def update_graph(self):
        # Move data left, add 0 at end
        self.beat_data = self.beat_data[1:] + [0.0]
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = self.rect()
        painter.fillRect(rect, QColor(30, 30, 30))
        pen = QPen(QColor(0, 255, 0), 2)
        painter.setPen(pen)

        h = rect.height()
        w = rect.width()
        N = len(self.beat_data)
        for i in range(N - 1):
            x1 = int((i / N) * w)
            x2 = int(((i+1) / N) * w)
            y1 = int(h / 2 - self.beat_data[i] * (h / 2 - 10))
            y2 = int(h / 2 - self.beat_data[i+1] * (h / 2 - 10))
            painter.drawLine(x1, y1, x2, y2)