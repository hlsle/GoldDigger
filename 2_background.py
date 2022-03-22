import pygame, os

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Goldl Miner")

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, "background.png"))

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    pygame.display.update()

pygame.quit()