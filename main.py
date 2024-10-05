import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMainWindow, QPushButton
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont
import datetime

full_seconds = 0

class StopwatchWindow(QMainWindow):
    def __init__(self, full_seconds):
        super().__init__()
        self.setWindowTitle(f"Stopwatch")

        #app.setStyleSheet(custom_stylesheet_default) #comment to use a default white theme

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        font = QFont("Arial", 20, QFont.Weight.Bold)

        self.layout = QVBoxLayout(self.central_widget)
        self.label = QLabel(f"00:00:00", alignment=Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(font)
        self.layout.addWidget(self.label)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_timer)
        self.layout.addWidget(self.start_button)

        self.pause_button = QPushButton("Pause")
        self.pause_button.setStyleSheet("background-color: blue")
        self.pause_button.clicked.connect(self.pause_timer)
        self.layout.addWidget(self.pause_button)
        self.pause_button.hide()

        self.reset_button = QPushButton("Reset")
        self.reset_button.setStyleSheet("background-color: red")
        self.reset_button.clicked.connect(self.reset_timer)
        self.layout.addWidget(self. reset_button)
        self.reset_button.hide()

        self.full_seconds = full_seconds
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

    def start_timer(self):
        self.timer.start(1000)
        self.pause_button.show()
        self.reset_button.hide()
        self.start_button.hide()

    def pause_timer(self):
        self.timer.stop()
        self.pause_button.hide()
        self.reset_button.show()
        self.start_button.show()

    def reset_timer(self):
        self.timer.stop()
        self.full_seconds = 0
        self.label.setText("0:00:00")
        self.setWindowTitle(f"Stopwatch")
        self.reset_button.hide()

    def update_timer(self):
        self.full_seconds += 1
        timerApp = datetime.timedelta(seconds=self.full_seconds)
        self.label.setText(str(timerApp))
        self.setWindowTitle(f"Stopwatch: {self.full_seconds} seconds")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    custom_stylesheet_default = """
QWidget {
    background-color: black;
    color: white;
}
QPushButton {
    background-color: grey;
    color: white;
}
QPushButton:hover {
    background-color: lime;}

"""

    window = StopwatchWindow(full_seconds)
    window.show()
    sys.exit(app.exec())

