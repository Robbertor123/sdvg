import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtWidgets import QLCDNumber, QLabel, QLineEdit


class MiniCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Миникалькулятор')
        self.setFixedSize(400, 150)

        self.number_1 = QLineEdit(self)
        self.number_1.move(10, 10)
        self.number_1.resize(100, 30)

        self.number_2 = QLineEdit(self)
        self.number_2.move(10, 90)
        self.number_2.resize(100, 30)

        self.calculate_button = QPushButton(self)
        self.calculate_button.setText('->')
        self.calculate_button.move(170, 30)
        self.calculate_button.resize(30, 70)

        self.result_sum = QLCDNumber(self)
        self.result_sum.move(270, 10)
        self.result_sum.resize(110, 30)

        self.result_sub = QLCDNumber(self)
        self.result_sub.move(270, 45)
        self.result_sub.resize(110, 30)

        self.result_mul = QLCDNumber(self)
        self.result_mul.move(270, 80)
        self.result_mul.resize(110, 30)

        self.result_div = QLCDNumber(self)
        self.result_div.move(270, 115)
        self.result_div.resize(110, 30)

        self.start()

    def start(self):
        self.calculate_button.clicked.connect(self.on_click)

    def on_click(self):
        self.result_sum.display(f"{int(self.number_1.text()) + int(self.number_2.text())}")
        self.result_sub.display(f"{int(self.number_1.text()) - int(self.number_2.text())}")
        self.result_mul.display(f"{int(self.number_1.text()) * int(self.number_2.text())}")
        if self.number_2.text() != '0':
            a = float(f"{(int(self.number_1.text()) / int(self.number_2.text()))}")
            if a.is_integer():
                self.result_div.display(f"{(int(self.number_1.text()) / int(self.number_2.text()))}")
            else:
                self.result_div.display(f"{'%.3f' % (int(self.number_1.text()) / int(self.number_2.text()))}")
        else:
            self.result_div.display('Error')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fc = MiniCalculator()
    fc.show()
    sys.exit(app.exec())
