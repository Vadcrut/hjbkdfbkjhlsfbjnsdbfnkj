import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QColor, QPainter
from random import randint

class OK(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.t = False

        self.pushButton.clicked.connect(self.drawfield)


    def drawfield(self):
        self.t =True
        self.update()

    def paintEvent(self, event):
        if self.t:
            qp = QPainter()
            qp.begin(self)
            r = randint(0, 100)
            qp.setBrush(QColor(255, 204, 0))
            qp.drawEllipse(150, 150, r, r)
            qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OK()
    ex.show()
    sys.exit(app.exec_())
