from pygame import *
from circleshape import *
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", tuple(self.position), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, asteroid_field):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        
        random_angle = random.uniform(20, 50)
        new_vector1 = self.velocity.rotate(random_angle) * 1.2
        new_vector2 = self.velocity.rotate(random_angle * -1) *1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        if self.radius > ASTEROID_MIN_RADIUS:
            asteroid_field.spawn(new_radius, self.position, new_vector1)
            asteroid_field.spawn(new_radius, self.position, new_vector2)
            self.kill()
