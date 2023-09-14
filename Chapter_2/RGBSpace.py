import pygame

print("Initializing")
pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False


def RG():
    for y in range(800):
        for x in range(1000):
            screen.set_at((x, y),
                          pygame.Color(int(x / screen_width * 255),
                                       int(y / screen_height * 255), 255))


def BG():
    for y in range(800):
        for x in range(1000):
            screen.set_at((x, y),
                          pygame.Color(0, int(x / screen_width * 255),
                                       int(y / screen_height * 255)))


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    BG()
    pygame.display.update()
pygame.quit()
