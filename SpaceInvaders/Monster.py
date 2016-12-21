from Main import pygame
from Constants import WHITE, DISPLAYWIDTH
"""
@author lb809 on 12/21/2016
"""


class monster:
    def __init__(self, screen, x):
        self.frame = screen
        self.x = x
        self.y = 100
        self.collision = False
        self.speed = 1

    def draw(self):
        pygame.draw.circle(self.frame, WHITE, (self.x, self.y), 30, 0)

    def move(self):
        self.x += self.speed

    def flickCollisionState(self):
        self.collision = True