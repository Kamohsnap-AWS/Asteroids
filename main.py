def startup():
    # This hides the welcome message output by pygame
    import os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    # This allows us to use code from the open-source 
    # pygame library throughout this file
    import pygame    
# Asteroid game constants    
from constants import *


def main():
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    startup()
    main()