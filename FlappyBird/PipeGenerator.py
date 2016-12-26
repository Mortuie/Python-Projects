import Constants
import random
import pygame

"""
@author lb809 on 26/12/16
Class performs algorithm to generate two random pipes with the same XCoordinate, but different heights.
"""

class pipe:
    def __init__(self, screen):
        self.frame = screen
        self.x = Constants.DISPLAYWIDTH - 60
        self.y = 0
        self.gap = random.randint(80, 100)
        self.speed = 2

        self.pipeWidth = random.randint(20, 35)
        self.height1 = random.randint(random.randint(10, 20), Constants.DISPLAYHEIGHT - (2 * self.pipeWidth))
        self.height2 = Constants.DISPLAYHEIGHT - (self.height1 + self.gap)

    def drawPipe(self):
        pygame.draw.rect(self.frame, Constants.BLACK,[self.x, self.y, self.pipeWidth, self.height1])
        pygame.draw.rect(self.frame, Constants.BLACK, [self.x, Constants.DISPLAYHEIGHT - self.height2, self.pipeWidth, self.height2])

    def movePipe(self):
        self.x -= self.speed

    def offPage(self):
        if self.x < (-1) * self.pipeWidth:
            return True
        return False