import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMainWindow, QPushButton
from PyQt6.QtCore import Qt, QTimer
import datetime

full_seconds = 0

class StopwatchWindow(QMainWindow):
    def __init__(self, full_seconds):
        super().__init__()
        self.setWindowTitle("Stopwatch")

        app.setStyleSheet(custom_stylesheet_default) #comment to use a default white theme

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.label = QLabel(f"{full_seconds}", alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label)

        start_button = QPushButton("Start")
        start_button.clicked.connect(self.start_timer)
        self.layout.addWidget(start_button)

        pause_button = QPushButton("Pause")
        pause_button.setStyleSheet("background-color: blue")
        pause_button.clicked.connect(self.pause_timer)
        self.layout.addWidget(pause_button)

        reset_button = QPushButton("Reset")
        reset_button.setStyleSheet("background-color: red")
        reset_button.clicked.connect(self.reset_timer)
        self.layout.addWidget(reset_button)

        self.full_seconds = full_seconds
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

    def start_timer(self):
        self.timer.start(1000)

    def pause_timer(self):
        self.timer.stop()

    def reset_timer(self):
        self.timer.stop()
        self.full_seconds = 0
        self.label.setText("0:00:00")

    def update_timer(self):
        self.full_seconds += 1
        timerApp = datetime.timedelta(seconds=self.full_seconds)
        self.label.setText(str(timerApp))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    custom_stylesheet_default = """
QWidget {
    background-color: black;
    color: white;
}
QLineEdit {
    background-color: pink;
    color: black;
}
QLine {
    color: grey;
}
QPushButton {
    background-color: grey;  /* Red buttons */
    color: white;  /* Text color */
}
QPushButton:hover {
    background-color: #cc0000;  /* Darker red on hover
}
QMenu {
    background-color: #1a1a1a;
    color: black;
}
QMenu::item {
    background-color: grey;
    color: black;
}
QProgressBar {
    border: 2px solid grey;
    text-align: center;
}
QProgressBar::chunk {
    background-color: red;
}
"""

    window = StopwatchWindow(full_seconds)
    window.show()
    sys.exit(app.exec())

