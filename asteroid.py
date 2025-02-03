import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, game_screen):
        pygame.draw.circle(game_screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt