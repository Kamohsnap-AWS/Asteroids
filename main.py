# This hides the welcome message output by pygame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
# This allows us to use code from the open-source 
# pygame library throughout this file
import pygame    
# Asteroid game constants    
from constants import *
# Asteroid player class
from player import Player
# Class that generates a single asteroid
from asteroid import Asteroid
# Class that generates astroid field
from asteroidfield import AsteroidField


def main():
    pygame.init()
    game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    # Creates updatable, drawable and asteroids groups 
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Adds Player class to both updatables and drawables groups
    Player.containers = (updatables, drawables)
    # Adds Asteroid class to updatables, drawables and asteroids groups
    Asteroid.containers = (asteroids, updatables, drawables)
    # Adds AsteroidField class to updatable group
    AsteroidField.containers = (updatables)

    # Initializes player object
    x, y =  (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)
    player = Player(x, y)

    # Intitialized asteroid field object
    asteroid_field = AsteroidField()

    

    # Infinite loop
    while True:
        # Allows for exiting the infinite loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        game_screen.fill("black")

        # Updates player model based on given inputs
        updatables.update(dt)
        # Draws player model on screen
        for drawable in drawables:
            drawable.draw(game_screen)
        

        pygame.display.flip()
        
        # Limits framerate to 60 FPS
        dt = (game_clock.tick(60) / 1000)


if __name__ == "__main__":
    main()