'''
This is the main file of the Pacman game. It initializes the game and handles the game loop.
'''
import pygame
from pygame.locals import *
from game import Game
# Initialize pygame
pygame.init()
# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pacman Game")
# Create a game instance
game = Game(window)
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_UP:
                game.move_pacman("up")
            elif event.key == K_DOWN:
                game.move_pacman("down")
            elif event.key == K_LEFT:
                game.move_pacman("left")
            elif event.key == K_RIGHT:
                game.move_pacman("right")
    # Update the game state
    game.update()
    # Draw the game
    game.draw()
    # Update the display
    pygame.display.update()
# Quit the game
pygame.quit()