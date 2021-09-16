from yardset import YardSet
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class OpenGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        QOpenGLWidget.__init__(self, parent)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(16)

        self.yardSet1 = YardSet(-0.8, 0.8, 0.74)
        self.yardSet2 = YardSet(-0.4, 0.8, 0)
        self.yardSet3 = YardSet(0, 0.8, 0.4)
        self.yardSet4 = YardSet(0.4, 0.8, -0.2)

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_COLOR_MATERIAL)
    
    def paintGL(self):

        glMatrixMode(GL_PROJECTION)
        glClearColor(0.8, 0.8, 0.8, 0.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.yardSet1.draw()
        self.yardSet2.draw()
        self.yardSet3.draw()
        self.yardSet4.draw()

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)