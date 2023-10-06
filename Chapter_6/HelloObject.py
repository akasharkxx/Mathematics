import pygame
from Cube import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Object import *
from Transform import *

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
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 0, 0, 1))
glEnable(GL_LIGHT0)
glMaterialfv(GL_FRONT, GL_DIFFUSE, (0, 1, 0, 1))

objects = []

cube = Object("Cube")
cube.add_component(Transform((0, -1, 0)))
cube.add_component(Cube(GL_POLYGON, "../images/brick.tif"))

objects.append(cube)

cube2 = Object("Cube2")
cube2.add_component(Transform((0, 1, 0)))
cube2.add_component(Cube(GL_POLYGON, "../images/brick2.tif"))

objects.append(cube2)

clock = pygame.time.Clock()
fps = 60
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(1, 1, 0, 1)
    for obj in objects:
        obj.update()
    pygame.display.flip()
    # pygame.time.wait(16)
    # print('tick={}, fps={}'.format(clock.tick(), clock.get_fps()))
    clock.tick(fps)
pygame.quit()