import pygame
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

done = False

white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

rect_size = (10, 10)
mouse_down = False
button = (0, 0, 100, 30)


def CheckIfButtonPressed(mousePos):
    mx = mousePos[0]
    my = mousePos[1]

    if button[0] < mx < button[2] and button[1] < my < button[3]:
        print("Mouse over button")
    else:
        print("Mouse not on button")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEMOTION:
            CheckIfButtonPressed(pygame.mouse.get_pos())
    pygame.draw.rect(screen, green, button)
    pygame.display.update()
pygame.quit()
