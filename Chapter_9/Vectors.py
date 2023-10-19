import pygame

from Grid import *
from Object import *
from Cube import *
from Button import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Settings import *

pygame.init()

pygame.display.set_caption('OpenGL in Python')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)

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

grid = Object("Grid")
grid.add_component(Transform((0, 0, -5)))
grid.add_component(Grid(0.5, 8, (0, 0, 255)))

objects_3D.append(grid)

clock = pygame.time.Clock()
fps = 120

def set_2D():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, ORTHO_SCREEN_WIDTH, 0, ORTHO_SCREEN_HEIGHT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())


def set_3D():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (SCREEN_WIDTH / SCREEN_HEIGHT), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)

trans: Transform = cube.get_component(Transform)
move_value = 0.1

while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                trans.move(pygame.Vector3(0, 0, -1))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        trans.move_x(-move_value)
    elif keys[pygame.K_RIGHT]:
        trans.move_x(move_value)
    elif keys[pygame.K_UP]:
        trans.move_y(move_value)
    elif keys[pygame.K_DOWN]:
        trans.move_y(-move_value)

    glPushMatrix()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    set_3D()
    for o in objects_3D:
        o.update(events)
    set_2D()
    for o in objects_2D:
        o.update(events)
    glPopMatrix()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
