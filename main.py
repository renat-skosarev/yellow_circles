import random
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.some_button.clicked.connect(self.paint_yellow_circles)

    def paint_yellow_circles(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter()
            painter.begin(self)
            painter.setPen(QColor('yellow'))
            for i in range(5):
                painter.setBrush(QColor(255, 255, 0, random.randint(30, 150)))
                x = random.randint(0, self.width() - 100)
                y = random.randint(0, self.height() - 100)
                diameter = random.randint(50, 200)
                painter.drawEllipse(x, y, diameter, diameter)
            painter.end()
            self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
