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

        scale = (parent.display[0]/parent.canvas[0], parent.display[1]/parent.canvas[1])

        self.yardSets = []
        self.yardSets.append(YardSet(scale, -1.8, 1.35, 1.2))
        self.yardSets.append(YardSet(scale, -1.3, 1.35, 0.8))
        self.yardSets.append(YardSet(scale, -0.8, 1.35, 0.5))
        self.yardSets.append(YardSet(scale, -0.3, 1.35, 1.0))
        self.yardSets.append(YardSet(scale,  0.2, 1.35, 1.2))
        self.yardSets.append(YardSet(scale,  0.7, 1.35, 0.8))
        self.yardSets.append(YardSet(scale,  1.2, 1.35, 0.5))
        self.yardSets.append(YardSet(scale,  1.7, 1.35, 1.0))

        self.yardSets.append(YardSet(scale, -1.8, -0.4, -0.7))
        self.yardSets.append(YardSet(scale, -1.3, -0.4, -0.8))
        self.yardSets.append(YardSet(scale, -0.8, -0.4, -1.4))
        self.yardSets.append(YardSet(scale, -0.3, -0.4, -0.9))
        self.yardSets.append(YardSet(scale,  0.2, -0.4, -0.7))
        self.yardSets.append(YardSet(scale,  0.7, -0.4, -0.8))
        self.yardSets.append(YardSet(scale,  1.2, -0.4, -1.4))
        self.yardSets.append(YardSet(scale,  1.7, -0.4, -0.9))

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

        for yardSet in self.yardSets:
            yardSet.draw()

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)