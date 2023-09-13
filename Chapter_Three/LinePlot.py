import pygame
print("Initializing")
pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
x_origin_offset = int(screen.get_width() / 2)
y_origin_offset = int(screen.get_height() / 2)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for x in range(-500, 500):
        screen.set_at((x + x_origin_offset, y_origin_offset), green)
    for y in range(-400, 400):
        screen.set_at((x_origin_offset, y + y_origin_offset), green)
    for x in range(-500, 500):
        y = int(10 * x - 100)
        screen.set_at((x + x_origin_offset, y + y_origin_offset), white)
    pygame.display.update()
pygame.quit()
