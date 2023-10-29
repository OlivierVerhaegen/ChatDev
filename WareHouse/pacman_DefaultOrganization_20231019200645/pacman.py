'''
This file contains the Pacman class which represents the Pacman character.
'''
import pygame
class Pacman:
    def __init__(self):
        self.x = 0
        self.y = 0
    def move(self, direction):
        if direction == "up":
            self.y -= 1
        elif direction == "down":
            self.y += 1
        elif direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1
    def update(self):
        # Update pacman logic here
        pass
    def draw(self, window):
        # Draw pacman here
        pass