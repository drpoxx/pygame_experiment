import pygame
import sys

from settings import *
from level import Level
from player import Player

# Setup pygame
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_heigt))
clock = pygame.time.Clock()
level = Level(levle_map, screen)

# Run Game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")
    level.run()

    pygame.display.update()
    clock.tick(60)
