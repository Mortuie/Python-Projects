import pygame
import Constants

"""
@author lb809 on 24/12/16
"""

class bird:
    def __init__(self, screen):
        self.frame = screen
        self.x = int(Constants.DISPLAYWIDTH / 4)
        self.y = int(Constants.DISPLAYHEIGHT / 2)
        self.radius = 20
        self.velocity = 0
        self.gravity = 1

    def drawBird(self):
        pygame.draw.circle(self.frame, Constants.RED, (self.x, self.y), self.radius)

    def whenSpaceIsPressed(self):
        self.velocity -= 17 * self.gravity

    def updateBird(self):
        self.velocity += self.gravity
        self.y += self.velocity

        if self.BelowBounds():
            self.y = Constants.DISPLAYHEIGHT - self.radius
            self.velocity = 0

        elif self.AboveBounds():
            self.y = self.radius
            self.velocity = 0

    def BelowBounds(self):
        if self.y > Constants.DISPLAYHEIGHT - self.radius:
            return True
        return False

    def AboveBounds(self):
        if self.y < self.radius:
            return True
        return False