from Constants import *
from Main import pygame

"""
@author lb809 on 21/12/16
"""

class bullet:
    def __init__(self, screen, x):
        self.frame = screen
        self.speed = 10
        self.x = x
        self.y = DISPLAYHEIGHT - 90

    def draw(self):
        pygame.draw.rect(self.frame, WHITE, [int(self.x), int(self.y), 6, 10], 0)

    def move(self):
        self.y -= self.speed