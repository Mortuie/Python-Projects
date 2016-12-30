import pygame
import Constants

"""
@author lb809 on 24/12/16
"""

class bird:
    def __init__(self, screen):
        self.frame = screen
        self.x = int(Constants.DISPLAYWIDTH / 4)
        self.y = int(Constants.DISPLAYHEIGHT / 4)
        self.radius = 12
        self.velocity = 0
        self.gravity = 0.3

    def getBirdX(self):
        return self.x

    def getBirdY(self):
        return self.y

    def getBirdRadius(self):
        return self.radius

    def drawBird(self):
        pygame.draw.circle(self.frame, Constants.RED, (self.x, self.y), self.radius)

    def whenSpaceIsPressed(self):
        self.velocity -= 25 * self.gravity

    def updateBird(self):
        self.velocity += self.gravity
        self.y += int(self.velocity)

        if self.BelowBounds():
            self.y = Constants.DISPLAYHEIGHT - self.radius
            self.velocity = 0

        elif self.AboveBounds():
            self.y = self.radius
            self.velocity = 0

    def BelowBounds(self):
        return self.y > Constants.DISPLAYHEIGHT - self.radius

    def AboveBounds(self):
        return self.y < self.radius
