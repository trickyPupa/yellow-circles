from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor, QPainter
from PyQt5 import uic
from random import randint
import sys


class Yellow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('yc.ui', self)
        self.check = 0
        self.btn.clicked.connect(self.run)
        self.circles = []

    def run(self):
        self.check = 1
        self.repaint()
        self.check = 0

    def paintEvent(self, event):
        if self.check:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            x = self.geometry().width()
            y = self.geometry().height()
            r = randint(10, 200)
            self.circles.append((randint(0, x - r), randint(49, y - r), r, r))
            for x, y, w, h in self.circles:
                qp.drawEllipse(x, y, w, h)
            qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Yellow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
