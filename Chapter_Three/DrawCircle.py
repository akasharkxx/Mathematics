import math
import pygame
from pygame.locals import *
print("Initializing")
pygame.init()
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Naive circle")
done = False

white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)

radius = 50
center = (200, 200)

times_clicked = 0

def circle_points(x, y, center):
    screen.set_at((x + center[0], y + center[1]), white)
    screen.set_at((y + center[0], x + center[1]), white)
    screen.set_at((y + center[0], -x + center[1]), white)
    screen.set_at((x + center[0], -y + center[1]), white)
    screen.set_at((-x + center[0], -y + center[1]), white)
    screen.set_at((-y + center[0], -x + center[1]), white)
    screen.set_at((-y + center[0], x + center[1]), white)
    screen.set_at((-x + center[0], y + center[1]), white)
def plot_circle(radius, center):
    x = 0
    y = radius
    d = 5/4.0 - radius
    circle_points(x, y, center)
    while y > x:
        if d < 0:
            d = d + 2 * x + 3
            x += 1
        else:
            d = d + 2 * (x - y) + 5
            x = x + 1
            y = y - 1
        circle_points(x, y, center)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # for x in range(-50, 50):
    #     y = math.sqrt(math.pow(radius, 2) - math.pow(x, 2))
    #     screen.set_at((int(x + center[0]), int(y + center[1])), white)
    #     y = -math.sqrt(math.pow(radius, 2) - math.pow(x, 2))
    #     screen.set_at((int(x + center[0]), int(y + center[1])), white)
    plot_circle(50, (200, 200))

    pygame.display.update()
pygame.quit()
