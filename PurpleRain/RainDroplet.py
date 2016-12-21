import random
import pygame

"""
@author lb809 on 20/12/16
"""

class rain:
    def __init__(self, screen, x, y, speed, height, colour):
        self.x = x
        self.y = y
        self.speed = speed
        self.height = height
        self.colour = colour
        self.frame = screen

        if self.speed > 11:
            self.width = random.randint(2, 3)
        else:
            self.width = random.randint(1, 2)

    def draw(self):
        pygame.draw.rect(self.frame, self.colour, [self.x, self.y, self.width, self.height], 0)

    def move(self):
        self.y += self.speed

    def checkOffScreen(self, displayWidth, displayHeight):
        if self.y > displayHeight:
            self.y = random.randint(-50, 0)
            self.x = random.randint(0, displayWidth)
