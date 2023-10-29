'''
This file contains the Game class which represents the Pacman game.
'''
import pygame
from pacman import Pacman
class Game:
    def __init__(self, window):
        self.window = window
        self.pacman = Pacman()
        self.score = 0
    def move_pacman(self, direction):
        self.pacman.move(direction)
    def update(self):
        # Update game logic here
        self.pacman.update()
    def draw(self):
        # Draw game objects here
        self.window.fill((0, 0, 0))  # Clear the window
        self.pacman.draw(self.window)  # Draw the pacman
        pygame.display.update()  # Update the display