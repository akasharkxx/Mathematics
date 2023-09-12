import pygame

print("Initializing")
pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
white = pygame.Color(255, 255, 255)


def draw_star(x, y, size):
    pygame.draw.rect(screen, white, (x, y, size, size))


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    draw_star(100, 250, 20)
    draw_star(250, 100, 20)
    draw_star(400, 180, 20)
    draw_star(440, 400, 20)
    draw_star(400, 430, 20)
    draw_star(360, 460, 20)
    draw_star(440, 700, 20)
    draw_star(680, 600, 20)

    pygame.display.update()
pygame.quit()
