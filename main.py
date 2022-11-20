from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
import random
import sys


class Yellow_Circles_App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('app_design.ui', self)
        self.add_funcs_for_button()
        self.draw = False

    def add_funcs_for_button(self):
        self.draw_button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
            self.draw = False

    def paint(self):
        self.draw = True
        self.repaint()

    def draw_flag(self, qp):
        r = random.randint(0, 150)
        qp.setBrush(QColor(255, 216, 13))
        qp.drawEllipse(150 - r, 150 - r, 150 + (2 * r), 150 + (r * 2))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    yellow_circles = Yellow_Circles_App()
    yellow_circles.show()
    sys.exit(app.exec())
