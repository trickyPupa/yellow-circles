from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor, QPainter
from random import randint, choices
from yc import Ui_Form
import sys


class NotYellow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
            x = self.geometry().width()
            y = self.geometry().height()
            r = randint(10, 250)
            self.circles.append((randint(-10, x - r), randint(49, y - r), r, r, QColor(*choices(range(0, 255), k=3))))
            for x, y, w, h, c in self.circles:
                qp.setBrush(c)
                qp.drawEllipse(x, y, w, h)
            qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = NotYellow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
