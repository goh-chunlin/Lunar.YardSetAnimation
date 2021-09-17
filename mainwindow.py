from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from openglwidget import OpenGLWidget

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.display=(1200,1000)
        self.canvas=(500,500)
        self.openglwidget = OpenGLWidget(self)
        self.openglwidget.setAttribute(Qt.WA_AlwaysStackOnTop)
        self.setCentralWidget(self.openglwidget)
        self.setWindowTitle("Yardset Animation with OpenGL")
        self.setGeometry(0,0,self.display[0],self.display[1])
        self.setFixedSize(self.display[0],self.display[1])