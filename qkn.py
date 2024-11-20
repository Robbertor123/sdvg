import sys
import random

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtWidgets import QLabel, QLCDNumber


class NimStrikesBack(QWidget):
    def __init__(self):
        super().__init__()

        self.Y = random.randint(1, 10)
        self.Z = random.randint(-10, -1)
        self.k = 10
        self.X = random.randint(1, 20)

        self.setWindowTitle('Ним наносит ответный удар')
        self.setFixedSize(400, 440)

        self.result_label = QLabel(self)
        self.result_label.setText('          Привет, начинаем игру!                                                  ')
        self.result_label.move(100, 15)

        self.btnp = QPushButton(self)
        self.btnp.setText('+' + str(self.Y))
        self.btnp.move(40, 70)
        self.btnp.resize(80, 40)

        self.btnm = QPushButton(self)
        self.btnm.setText(str(self.Z))
        self.btnm.move(280, 70)
        self.btnm.resize(80, 40)

        self.q = QLabel(self)
        self.q.setText('Осталось ходов')
        self.q.move(40, 190)

        self.qwa = QLabel(self)
        self.qwa.setText('Текущее число')
        self.qwa.move(40, 320)

        self.result = QLCDNumber(self)
        self.result.display(self.k)
        self.result.move(270, 180)
        self.result.resize(110, 40)

        self.qw = QLCDNumber(self)
        self.qw.display(self.X)
        self.qw.move(270, 310)
        self.qw.resize(110, 40)

        self.ok()
        self.start()

    def ok(self):
        if self.k <= 0:
            if self.X == 0:
                self.result_label.setText("Вы победили, начинаем новую игру")
            else:
                self.result_label.setText("Вы проиграли, начинаем новую игру")
            self.Y = random.randint(1, 10)
            self.Z = random.randint(-10, -1)
            self.k = 10
            self.X = random.randint(1, 20)
            self.qw.display(self.X)
            self.result.display(self.k)
            self.btnp.setText('+' + str(self.Y))
            self.btnm.setText(str(self.Z))

    def start(self):
        self.btnp.clicked.connect(self.on_click)
        self.btnm.clicked.connect(self.wow)

    def wow(self):
        self.result_label.setText('')
        self.k -= 1
        self.result.display(self.k)
        self.X += self.Z
        self.qw.display(self.X)
        self.ok()

    def on_click(self):
        self.result_label.setText('')
        self.k -= 1
        self.result.display(self.k)
        self.X += self.Y
        self.qw.display(self.X)
        self.ok()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fc = NimStrikesBack()
    fc.show()
    sys.exit(app.exec())
