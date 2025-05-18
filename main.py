#this allows us to use code from
# the open-source pygame library
#throughout this file
import pygame
from constants import *
clock = pygame.time.Clock
dt = 0

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while 1 != 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()