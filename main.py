# This hides the welcome message output by pygame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
# This allows us to use code from the open-source 
# pygame library throughout this file
import pygame    
# Asteroid game constants    
from constants import *


def main():
    pygame.init()
    game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Infinite loop
    while True:
        # Allows for exiting the infinite loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        game_screen.fill("black")
        pygame.display.flip()
        
        # Limits framerate to 60 FPS
        dt = (game_clock.tick(60) / 1000)


if __name__ == "__main__":
    main()