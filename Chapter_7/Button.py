import pygame.mouse
from OpenGL.GL import *
from Utils import *

class Button:
    def __init__(self, screen, position, width, height, color, o_color, p_color):
        self.screen = screen
        self.position = position
        self.width = width
        self.height = height
        self.normal_color = color
        self.over_color = o_color
        self.pressed_color = p_color

    def draw(self, events):
        mouse_pos = pygame.mouse.get_pos()
        mx = map_value(mouse_pos[0], 0, 800, 0, 1600)
        my = map_value(mouse_pos[1], 0, 600, 1200, 0)

        print(mx)
        print(my)
        glPushMatrix()
        glLoadIdentity()

        if (self.position[0] < mx < (self.position[0] + self.width) and
                self.position[1] < my < (self.position[1] + self.height)):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    glColor3f(self.pressed_color[0], self.pressed_color[1], self.pressed_color[2])
                else:
                    glColor3f(self.over_color[0], self.over_color[1], self.over_color[2])
            print('over')
        else:
            glColor3f(self.normal_color[0], self.normal_color[1], self.normal_color[2])
        glBegin(GL_POLYGON)
        glVertex2f(self.position[0], self.position[1])
        glVertex2f(self.position[0] + self.width, self.position[1])
        glVertex2f(self.position[0] + self.width, self.position[1] + self.height)
        glVertex2f(self.position[0], self.position[1] + self.height)
        glEnd()
        glPopMatrix()
