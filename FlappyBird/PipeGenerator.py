import Constants
import random
import pygame

"""
@author lb809 on 26/12/16
Class performs algorithm to generate two random pipes with the same XCoordinate, but different heights.
"""

class pipe:
    def __init__(self, screen, bird):
        self.frame = screen
        self.playerBird = bird
        self.colour = Constants.GREEN
        self.x = Constants.DISPLAYWIDTH
        self.y = 0
        self.gap = random.randint(100, 130)
        self.speed = 2

        self.pipeWidth = random.randint(30, 35)
        self.height1 = random.randint(random.randint(25, 35), Constants.DISPLAYHEIGHT - (4*self.pipeWidth))
        self.height2 = Constants.DISPLAYHEIGHT - (self.height1 + self.gap)

        self.birdX = self.playerBird.getBirdX()
        self.birdY = self.playerBird.getBirdY()
        self.birdRadius = self.playerBird.getBirdRadius()

    def drawPipe(self):
        pygame.draw.rect(self.frame, self.colour, [self.x, self.y, self.pipeWidth, self.height1])
        pygame.draw.rect(self.frame, self.colour, [self.x, Constants.DISPLAYHEIGHT - self.height2, self.pipeWidth, self.height2])

    # TODO collision detection isn't working properly... Need this fixed.
    def collidedWithBird(self):
        return self.withinXBounds() and self.withinYBounds()

    def withinXBounds(self):
        return (self.x <= self.birdX + self.birdRadius) and (self.x + self.pipeWidth >= self.birdX - self.birdRadius)

    def withinYBounds(self):
        return (self.height1 >= self.birdY - self.birdRadius) or (self.height1 + self.gap <= self.birdY + self.birdRadius)

    def changeColourFromOriginal(self):
        self.colour = Constants.RED

    def changeColourBackToOriginal(self):
        self.colour = Constants.GREEN

    def updatePipe(self):
        self.x -= self.speed

    def offPage(self):
        return self.x < (-1) * self.pipeWidth