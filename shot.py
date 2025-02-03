import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, game_screen):
        pygame.draw.circle(game_screen, "blue", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt