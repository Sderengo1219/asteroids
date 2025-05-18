#this allows us to use code from
# the open-source pygame library
#throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
from asteroidfield import *
from asteroid import *
from sys import *
from shot import *

clock = pygame.time.Clock()
dt = 0
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
asteroidfield = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    asteroid_field = AsteroidField()
    while 1 != 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        for each in drawable:
            each.draw(screen)

        for each in asteroids:
            if each.does_collide(player) == True:
                print("Game Over!")
                exit()


        dt = clock.tick(60) / 1000
        updatable.update(dt)
        pygame.display.flip()

if __name__ == "__main__":
    main()