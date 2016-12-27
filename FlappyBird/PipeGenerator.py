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
        self.x = Constants.DISPLAYWIDTH - 60
        self.y = 0
        self.gap = random.randint(90, 120)
        self.speed = 2


        self.pipeWidth = random.randint(30, 35)
        self.height1 = random.randint(random.randint(25, 35), Constants.DISPLAYHEIGHT - (3*self.pipeWidth))
        self.height2 = Constants.DISPLAYHEIGHT - (self.height1 + self.gap)

    def collidedWithBird(self):
        birdX = self.playerBird.getBirdX()
        birdY = self.playerBird.getBirdY()

        if self.x <= birdX and birdX <= self.x+self.pipeWidth and (birdY <= self.height1 or birdY >= self.height1+self.gap):
            return True
        return False

    def changeColourFromOriginal(self):
        self.colour = Constants.RED

    def changeColourBackToOriginal(self):
        self.colour = Constants.GREEN

    def drawPipe(self):
        pygame.draw.rect(self.frame, self.colour,[self.x, self.y, self.pipeWidth, self.height1])
        pygame.draw.rect(self.frame, self.colour, [self.x, Constants.DISPLAYHEIGHT - self.height2, self.pipeWidth, self.height2])

    def movePipe(self):
        self.x -= self.speed

    def offPage(self):
        if self.x < (-1) * self.pipeWidth:
            return True
        return False