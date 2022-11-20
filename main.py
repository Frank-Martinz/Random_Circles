from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint
from app_design import Ui_MainWindow
import sys


class Yellow_Circles_App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        r = randint(0, 150)
        qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        qp.drawEllipse(150 - r, 150 - r, 150 + (2 * r), 150 + (r * 2))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    yellow_circles = Yellow_Circles_App()
    yellow_circles.show()
    sys.exit(app.exec())
