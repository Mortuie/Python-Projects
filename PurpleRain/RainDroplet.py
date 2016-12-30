import random
import pygame
import Constants

"""
@author lb809 on 20/12/16
"""

class rain:
    def __init__(self, screen):
        self.frame = screen
        self.x = random.randint(0, Constants.DISPLAYWIDTH)
        self.y = random.randint(-50, Constants.DISPLAYHEIGHT)
        self.speed = random.randint(10, 13)
        self.height = random.randint(7, 13)
        self.colour = Constants.PINK

        if self.rainIsFast():
            self.width = random.randint(2, 3)
        else:
            self.width = random.randint(1, 2)

    def draw(self):
        pygame.draw.rect(self.frame, self.colour, [self.x, self.y, self.width, self.height], 0)

    def rainIsFast(self):
        return self.speed > 11

    def moveRain(self):
        self.y += self.speed

    def checkOffScreen(self):
        if self.y > Constants.DISPLAYHEIGHT:
            self.y = random.randint(-50, 0)
            self.x = random.randint(0, Constants.DISPLAYWIDTH)
