import pygame

from Object import *
from Cube import *
from Button import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 800
screen_height = 600

pygame.display.set_caption('OpenGL in Python')
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)

done = False

white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

objects_3D = []
objects_2D = []

cube = Object("Cube")
cube.add_component(Transform((0, 0, -5)))
cube.add_component(Cube(GL_POLYGON, '../images/brick.tif'))
objects_3D.append(cube)

button1 = Object("Button")
button1.add_component(Button(screen, (0, 0), 100, 50, white, green, blue))
objects_2D.append(button1)

clock = pygame.time.Clock()
fps = 30

def set_2D():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, screen.get_width(), 0, screen.get_height())
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())

def set_3D():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width/screen_height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glPushMatrix()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    set_3D()
    for o in objects_3D:
        o.update()
    set_2D()
    for o in objects_2D:
        o.update()
    glPopMatrix()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
