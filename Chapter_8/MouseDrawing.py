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

color_list = []
color_list.append(white)
color_list.append(blue)
color_list.append(red)
color_list.append(green)

current_color = color_list[0]

rect_size = (10, 10)

def draw_rect():
    pygame.draw.rect(screen, white, (pygame.mouse.get_pos(), rect_size))


mouse_down = False
last_mouse_pos = (0, 0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == KEYDOWN:
            if event.key == K_0:
                current_color = color_list[0]
            if event.key == K_1:
                current_color = color_list[1]
            if event.key == K_2:
                current_color = color_list[2]
            if event.key == K_3:
                current_color = color_list[3]
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouse_down = True
            last_mouse_pos = pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            mouse_down = False
        elif event.type == MOUSEMOTION and mouse_down == True:
            pygame.draw.line(screen, current_color, last_mouse_pos, pygame.mouse.get_pos(), 5)
            last_mouse_pos = pygame.mouse.get_pos()
            # draw_rect()

    pygame.display.update()
pygame.quit()
