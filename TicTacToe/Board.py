import pygame
import Constants
import Pieces
"""
@author lb809 on 1/4/2017
"""

class board:
    currentBoard = []
    def __init__(self, frame, size):
        self.frame = frame
        self.dimensions = size


    def createBoard(self):

        coordX = 50
        coordY = 50

        for width in range(1, (self.dimensions**2) + 1):
            #print(str(coordX) + " " + str(coordY))

            self.currentBoard.append(Pieces.piece(self.frame, coordX, coordY, 0))

            if width % 3 == 0:
                coordY += 100
                coordX = 50
            else:
                coordX += 100

    def drawBoard(self):

        linesThatNeedToBeDrawn = self.dimensions - 1
        for i in range(linesThatNeedToBeDrawn):
            pygame.draw.line(self.frame, Constants.BLACK, ((i+1) * 100, 0), ((i+1) * 100, (linesThatNeedToBeDrawn+1) * 100))
            pygame.draw.line(self.frame, Constants.BLACK, (0, (i+1) * 100), ((linesThatNeedToBeDrawn+1) * 100, (i+1) * 100))

        for obj in self.currentBoard:
            obj.drawPiece()



