import pygame
print("Initializing")
pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

white = pygame.Color(255, 255, 255)

pygame.font.init()

print(pygame.font.get_fonts())

font = pygame.font.Font('../font/Super Cool Personal Use.ttf', 120)
text = font.render('Penny de Byl', False, white)

font2 = pygame.font.Font('../font/Anthony Hunters.otf', 120)
text2 = font2.render('Penny de Byl', True, white)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(text, (10, 10))
    screen.blit(text2, (10, 130))
    pygame.display.update()
pygame.quit()
