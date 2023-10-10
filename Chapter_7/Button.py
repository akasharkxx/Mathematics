from OpenGL.GL import *

class Button:
    def __init__(self, screen, position, width, height, color, o_color, p_color):
        self.screen = screen
        self.position = position
        self.width = width
        self.height = height
        self.normal_color = color
        self.over_color = o_color
        self.pressed_color = p_color

    def draw(self):
        glPushMatrix()
        glLoadIdentity()
        glColor3f(self.normal_color[0],
                  self.normal_color[1],
                  self.normal_color[2])
        glBegin(GL_POLYGON)
        glVertex2f(self.position[0], self.position[1])
        glVertex2f(self.position[0] + self.width, self.position[1])
        glVertex2f(self.position[0] + self.width, self.position[1] + self.height)
        glVertex2f(self.position[0], self.position[1] + self.height)
        glEnd()
        glPopMatrix()