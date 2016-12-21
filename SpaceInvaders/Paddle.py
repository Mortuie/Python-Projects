from Constants import ORANGE, DISPLAYWIDTH, DISPLAYHEIGHT
from Main import pygame

"""
@author lb809 on 21/12/16
"""

class paddle:
    def __init__(self, screen):
        self.frame = screen
        self.height = 30
        self.width = 100
        self.x = (DISPLAYWIDTH / 2) - (self.width / 2)
        self.y = DISPLAYHEIGHT - self.height - 20

        self.turretWidth = 12
        self.turretHeight = 20
        self.turretX = self.x + (self.width / 2) - (self.turretWidth / 2)
        self.turretY = self.y - self.turretHeight

    def draw(self):
        pygame.draw.rect(self.frame, ORANGE, [self.x, self.y, self.width, self.height], 0)
        pygame.draw.rect(self.frame, ORANGE, [self.turretX, self.turretY, self.turretWidth, self.turretHeight], 0)

    def move(self, moveBy):
        if self.x < 0:
            self.x = 0
            self.turretX = (self.width / 2) - (self.turretWidth / 2)
        elif self.x + self.width > DISPLAYWIDTH:
            self.x = DISPLAYWIDTH - self.width
            self.turretX = self.x + (self.width / 2) - (self.turretWidth / 2)
        else:
            self.x += moveBy
            self.turretX += moveBy

    def getPaddleX(self):
        return self.x + 47