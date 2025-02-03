import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0

    # Returns a list of 3 coordinates that draw a triangle for use in draw method
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # Draws player model on a screen
    def draw(self, game_screen):
        pygame.draw.polygon(game_screen, "white", self.triangle(), 2)

    # Used to rotate player model
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
    
    # Changes the player recorded position
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # Updates the current player position on screen
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Left rotate
        if keys[pygame.K_a]:
            self.rotate(-dt)
        # Right rotate
        if keys[pygame.K_d]:
            self.rotate(dt)

        # Up movement
        if keys[pygame.K_s]:
            self.move(-dt)
        # Down movement
        if keys[pygame.K_w]:
            self.move(dt)