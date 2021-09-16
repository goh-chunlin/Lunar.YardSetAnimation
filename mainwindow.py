from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from openglwidget import OpenGLWidget

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.openglwidget = OpenGLWidget(self)
        self.setCentralWidget(self.openglwidget)
        self.setWindowTitle("Yardset Animation with OpenGL")
        self.setGeometry(0,0,500,500)
        self.setFixedSize(500,500)