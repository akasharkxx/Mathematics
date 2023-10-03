import pygame
from Cube import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')
done = False

white = pygame.Color(255, 255, 255)
glMatrixMode(GL_PROJECTION)
# gluPerspective(30, (screen_width / screen_height), 0.1, 100.0)
gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)
# glOrtho(-1, 1, 1, -1, 0.1, 100.0)
glTranslatef(0.0, 0.0, -3.0)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 1, 0, 1))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 0, 1))
glLightfv(GL_LIGHT0, GL_SPECULAR, (0, 1, 1, 1))
glEnable(GL_LIGHT0)
glLight(GL_LIGHT1, GL_POSITION, (-5, 5, 0, 1))
glLightfv(GL_LIGHT1, GL_DIFFUSE, (0, 0, 1, 1))
glEnable(GL_LIGHT1)
cube = Cube()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(1, 1, 0, 1)
    cube.draw()
    pygame.display.flip()
    pygame.time.wait(16)
pygame.quit()