import pygame
from pygame import *
print("Initializing")
pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

white = pygame.Color(255, 255, 255)

times_clicked = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            if times_clicked == 0:
                point1 = pygame.mouse.get_pos()
            elif times_clicked == 1:
                point2 = pygame.mouse.get_pos()
            elif times_clicked == 2:
                point3 = pygame.mouse.get_pos()

            times_clicked += 1

            if times_clicked > 2:
                pygame.draw.polygon(screen, white, (point1, point2, point3))
                times_clicked = 0

    pygame.display.update()
pygame.quit()
