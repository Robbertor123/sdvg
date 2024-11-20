import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtWidgets import QLabel, QLineEdit


class Arifmometr(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Арифмометр')
        self.setFixedSize(300, 90)

        self.first_value = QLineEdit(self)
        self.first_value.setText('0')
        self.first_value.move(10, 10)
        self.first_value.resize(40, 30)

        self.second_value = QLineEdit(self)
        self.second_value.setText('0')
        self.second_value.move(140, 10)
        self.second_value.resize(40, 30)

        self.add_button = QPushButton(self)
        self.add_button.setText('+')
        self.add_button.move(50, 10)
        self.add_button.resize(30, 30)

        self.substract_button = QPushButton(self)
        self.substract_button.setText('-')
        self.substract_button.move(80, 10)
        self.substract_button.resize(30, 30)

        self.multiply_button = QPushButton(self)
        self.multiply_button.setText('*')
        self.multiply_button.move(110, 10)
        self.multiply_button.resize(30, 30)

        self.result = QLineEdit(self)
        self.result.setText('0')
        self.result.setReadOnly(True)
        self.result.move(190, 10)
        self.result.resize(40, 30)

        self.label = QLabel(self)
        self.label.setText('=')
        self.label.move(180, 15)
        self.start()

    def start(self):
        self.add_button.clicked.connect(self.on_click)
        self.substract_button.clicked.connect(self.wow)
        self.multiply_button.clicked.connect(self.rex)

    def wow(self):
        self.result.setText(f"{int(self.first_value.text()) - int(self.second_value.text())}")

    def rex(self):
        self.result.setText(f"{int(self.first_value.text()) * int(self.second_value.text())}")

    def on_click(self):
        self.result.setText(f"{int(self.first_value.text()) + int(self.second_value.text())}")

#бу, испугался?
if __name__ == '__main__':
    app = QApplication(sys.argv)
    fc = Arifmometr()
    fc.show()
    sys.exit(app.exec())
