import pygame
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT)
pygame.init()

screen = pygame.display.set_mode([400, 700])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (200, 600), 50)

    pygame.display.flip()

pygame.quit()
