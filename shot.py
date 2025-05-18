from circleshape import *
from constants import SHOT_RADIUS

class Shot(CircleShape):
    containers = None
    
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x, y , SHOT_RADIUS)
        if Shot.containers:
            for container in Shot.containers:
                container.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", tuple(self.position), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt