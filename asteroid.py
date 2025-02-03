import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, game_screen):
        pygame.draw.circle(game_screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Rotation of the 2 child asteroids
        random_angle = random.uniform(20, 50)
        left_child_velocity = self.velocity.rotate(random_angle)
        right_child_velocity = self.velocity.rotate(-random_angle)

        # Radius of the newly formed astroids after the split
        child_radius = self.radius - ASTEROID_MIN_RADIUS

        left_child = Asteroid(self.position.x, self.position.y, child_radius)
        left_child.velocity = left_child_velocity * 1.2

        right_child = Asteroid(self.position.x, self.position.y, child_radius)
        right_child.velocity = right_child_velocity * 1.2
