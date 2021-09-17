from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from random import seed
from random import random

class YardSet:
    seed(1)

    def __init__(self, scale, initX, initY, yardCraneInitY):
        self.scale = scale
        self.initX = self.scaleX(initX)
        self.initY = self.scaleY(initY)
        self.yardCrane1Y = self.scaleY(yardCraneInitY)
        self.yardCrane1Direction = -1
        self.hoistX = self.scaleX(0)
        self.hoistDirection = 1

    def draw(self):
        self.yardCrane1Y = self.yardCrane1Y + self.scaleY(0.002 * self.yardCrane1Direction)

        if (self.yardCrane1Y >= self.initY - self.scaleY(0.06)):
            self.yardCrane1Direction = -1
        elif (self.yardCrane1Y < self.initY - self.scaleY(1.15)):
            self.yardCrane1Direction = 1

        self.drawYardCrane(self.initX - self.scaleX(0.06), self.yardCrane1Y - self.scaleY(0.06), self.scaleX(0.37), self.scaleY(0.08))

        self.drawYardset(self.initX, self.initY, 10, 20)

    def drawYardset(self, initX, initY, numberOfRows, numberOfBays):
        containerWidth = self.scaleX(0.025)
        containerLength = self.scaleY(0.060)

        for i in range (0, numberOfRows):
            x = initX + containerWidth * i
            for j in range (0, numberOfBays):
                y = initY - containerLength * j
                self.drawContainerSlot(x, y, containerWidth, containerLength)

        self.drawYardCraneRail(initX - self.scaleX(0.03), initY + self.scaleY(0.04), numberOfBays * containerLength)
        self.drawYardCraneRail(initX - self.scaleX(0.03) + numberOfRows * containerWidth + self.scaleX(0.035), initY + self.scaleY(0.04), numberOfBays * containerLength)

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
        length = length + self.scaleY(0.08)

        glColor3f(1, 0, 0)
        glBegin(GL_POLYGON)
        glVertex3f(x, y, 0.0)
        glVertex3f(x + self.scaleX(0.025), y, 0.0)
        glVertex3f(x + self.scaleX(0.025), y + self.scaleY(0.040), 0.0)
        glVertex3f(x, y + self.scaleY(0.040), 0.0)        
        glEnd()

        glColor3f(1, 0, 0)
        glBegin(GL_LINES)
        glVertex3f(x + self.scaleX(0.013), y, 0.0)
        glVertex3f(x + self.scaleX(0.013), y - length, 0.0) 
        glEnd()

        glColor3f(1, 0, 0)
        glBegin(GL_POLYGON)
        glVertex3f(x, y - length, 0.0)
        glVertex3f(x + self.scaleX(0.025), y - length, 0.0)
        glVertex3f(x + self.scaleX(0.025), y - length - self.scaleY(0.040), 0.0)
        glVertex3f(x, y - length - self.scaleY(0.040), 0.0)        
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
        glVertex3f(x, y + length - self.scaleY(0.012), 0.0)
        glVertex3f(x + width, y + length - self.scaleY(0.012), 0.0) 
        glEnd()

        glBegin(GL_LINES)
        glVertex3f(x, y + self.scaleY(0.012), 0.0)
        glVertex3f(x + width, y + self.scaleY(0.012), 0.0) 
        glEnd()

        self.hoistX = self.hoistX + self.scaleX(0.002) * self.hoistDirection

        if (self.hoistX >= width):
            self.hoistDirection = -1
        elif (self.hoistX <= 0):
            self.hoistDirection = 1

        self.drawYardHoist(x + self.hoistX, y, length)

    def drawYardHoist(self, x, y, length):
        glColor3f(0.39, 0.27, 0)
        glBegin(GL_POLYGON)
        glVertex3f(x, y, 0.0)
        glVertex3f(x + self.scaleX(0.025), y, 0.0)
        glVertex3f(x + self.scaleX(0.025), y + length, 0.0)
        glVertex3f(x, y + length, 0.0)        
        glEnd()

    def scaleX(self, coordinate):
        return coordinate / self.scale[0]

    def scaleY(self, coordinate):
        return coordinate / self.scale[1]