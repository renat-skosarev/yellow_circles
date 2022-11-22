import random
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor

from UI import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.flag = False
        self.some_button.clicked.connect(self.paint_yellow_circles)

    def paint_yellow_circles(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter()
            painter.begin(self)
            for i in range(5):
                x = random.randint(0, self.width() - 100)
                y = random.randint(0, self.height() - 100)
                diameter = random.randint(50, 200)
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                transparency = random.randint(30, 200)
                color = QColor(r, g, b, transparency)
                painter.setPen(color)
                painter.setBrush(color)
                painter.drawEllipse(x, y, diameter, diameter)
            painter.end()
            self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
