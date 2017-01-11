import pygame
import Constants
"""
@author lb809 on 08/01/17
"""

imageX = pygame.image.load("mediaFiles/x.png")
imageO = pygame.image.load("mediaFiles/o.png")

class piece:
    def __init__(self, frame, x, y, type):
        self.frame = frame
        self.x = x
        self.y = y
        self.type = type

    def drawPiece(self):
        if self.type != 0:
            if self.type == 1:
                self.frame.blit(imageX, (self.x - Constants.DISPLACEMENT, self.y - Constants.DISPLACEMENT))
            else:
                self.frame.blit(imageO, (self.x - Constants.DISPLACEMENT, self.y - Constants.DISPLACEMENT))


    def changeTypeOfPiece(self, differentType):
        self.type = differentType

    def isAnEmptyTile(self):
        return self.type == 0

    def getTypeTile(self):
        return self.type