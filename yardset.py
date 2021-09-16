from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from random import seed
from random import random

class YardSet:
    seed(1)

    def __init__(self, initX, initY, yardCraneInitY):
        self.initX = initX
        self.initY = initY
        self.yardCrane1Y = yardCraneInitY
        self.yardCrane1Direction = -1
        self.hoistX = 0
        self.hoistDirection = 1

    def draw(self):
        self.yardCrane1Y = self.yardCrane1Y + 0.002 * self.yardCrane1Direction

        if (self.yardCrane1Y >= self.initY - 0.06):
            self.yardCrane1Direction = -1
        elif (self.yardCrane1Y < self.initY - 1.15):
            self.yardCrane1Direction = 1

        self.drawYardCrane(self.initX - 0.06, self.yardCrane1Y - 0.06, 0.25 + 0.12, 0.08)

        self.drawYardset(self.initX, self.initY, 10, 20)

    def drawYardset(self, initX, initY, numberOfRows, numberOfBays):
        containerWidth = 0.025
        containerLength = 0.060

        for i in range (0, numberOfRows):
            x = initX + containerWidth * i
            for j in range (0, numberOfBays):
                y = initY - containerLength * j
                self.drawContainerSlot(x, y, containerWidth, containerLength)

        self.drawYardCraneRail(initX - 0.03, initY + 0.04, numberOfBays * containerLength)
        self.drawYardCraneRail(initX - 0.03 + numberOfRows * containerWidth + 0.035, initY + 0.04, numberOfBays * containerLength)

    def drawContainerSlot(self, x, y, width, length):
        y = y - length

        glColor3f(1, 0, 0)
        glBegin(GL_LINE_LOOP)
        glVertex3f(x, y, 0.0)
        glVertex3f(x + width, y, 0.0)
        glVertex3f(x + width, y + length, 0.0)
        glVertex3f(x, y + length, 0.0)        
        glEnd()
    
    def drawYardCraneRail(self, x, y, length):
        length = length + 0.08

        glColor3f(1, 0, 0)
        glBegin(GL_POLYGON)
        glVertex3f(x, y, 0.0)
        glVertex3f(x + 0.025, y, 0.0)
        glVertex3f(x + 0.025, y + 0.040, 0.0)
        glVertex3f(x, y + 0.040, 0.0)        
        glEnd()

        glColor3f(1, 0, 0)
        glBegin(GL_LINES)
        glVertex3f(x + 0.013, y, 0.0)
        glVertex3f(x + 0.013, y - length, 0.0) 
        glEnd()

        glColor3f(1, 0, 0)
        glBegin(GL_POLYGON)
        glVertex3f(x, y - length, 0.0)
        glVertex3f(x + 0.025, y - length, 0.0)
        glVertex3f(x + 0.025, y - length - 0.040, 0.0)
        glVertex3f(x, y - length - 0.040, 0.0)        
        glEnd()

    def drawYardCrane(self, x, y, width, length):
        glColor3f(0.39, 0.27, 0)
        glBegin(GL_LINE_LOOP)
        glVertex3f(x, y, 0.0)
        glVertex3f(x + width, y, 0.0)
        glVertex3f(x + width, y + length, 0.0)
        glVertex3f(x, y + length, 0.0)        
        glEnd()

        glBegin(GL_LINES)
        glVertex3f(x, y + length - 0.012, 0.0)
        glVertex3f(x + width, y + length - 0.012, 0.0) 
        glEnd()

        glBegin(GL_LINES)
        glVertex3f(x, y + 0.012, 0.0)
        glVertex3f(x + width, y + 0.012, 0.0) 
        glEnd()

        self.hoistX = self.hoistX + 0.002 * self.hoistDirection

        if (self.hoistX >= width):
            self.hoistDirection = -1
        elif (self.hoistX <= 0):
            self.hoistDirection = 1

        self.drawYardHoist(x + self.hoistX, y, length)

    def drawYardHoist(self, x, y, length):
        glColor3f(0.39, 0.27, 0)
        glBegin(GL_POLYGON)
        glVertex3f(x, y, 0.0)
        glVertex3f(x + 0.025, y, 0.0)
        glVertex3f(x + 0.025, y + length, 0.0)
        glVertex3f(x, y + length, 0.0)        
        glEnd()