import pygame
print("Initializing")
pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

white = pygame.Color(255, 255, 255)

def to_pygame_coordinates (display, x, y) :
    return x, display.get_height() - y;

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    position = to_pygame_coordinates(screen, 100, 100)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))
    # screen.set_at(to_pygame_coordinates(screen, 100, 100), white)
    # screen.set_at(to_pygame_coordinates(screen, 200, 200), white)
    # screen.set_at((100, 100), white)
    # screen.set_at((150, 150), white)
    pygame.display.update()
pygame.quit()
