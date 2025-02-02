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
    
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Infinite loop
    while True:
        # Allows for exiting the infinite loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()