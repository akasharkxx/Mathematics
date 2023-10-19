from OpenGL.GL import *

class Grid():
    def __init__(self, interval, halfSize, color):
        self.interval = interval
        self.halfSize = halfSize
        self.color = color

    def draw(self):
        glColor3fv(self.color)
        glBegin(GL_LINES)
        for x in range(-self.halfSize, self.halfSize):
            for y in range(-self.halfSize, self.halfSize):
                glVertex3fv((x * self.interval, y * self.interval - 10, 0))
                glVertex3fv((x * self.interval, y * self.interval + 500, 0))
                glVertex3fv((y * self.interval - 10, x * self.interval, 0))
                glVertex3fv((y * self.interval + 500, x * self.interval, 0))
        glEnd()

