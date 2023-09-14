import pygame
print("Initializing")
pygame.init()
screen_width = 1024
screen_height = 1024
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Blue World')
done = False

white = pygame.Color(255, 255, 255)

background = pygame.image.load('../images/Bg.jpg')
ufo = pygame.image.load('../images/ufo.png')

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(background, (0, 0))
    for x in range(1, 9):
        screen.blit(ufo, (x * 100, x * 100))
    pygame.display.update()
pygame.quit()
