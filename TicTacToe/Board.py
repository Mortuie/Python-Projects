import pygame
import Constants
import Pieces
"""
@author lb809 on 1/4/2017
"""

class board:

    def __init__(self, frame):
        self.frame = frame
        self.dimensions = 3
        self.currentBoard = [[], [], []]

    def createBoard(self):

        coordX = 50
        coordY = 50

        for height in range(3):
            for width in range(3):

                self.currentBoard[height].append(Pieces.piece(self.frame, coordX, coordY, 1))

                coordX += 100

                print(str(height) + " " + str(width))

            coordY += 100
            coordX = 50

    def drawBoard(self):

        linesThatNeedToBeDrawn = self.dimensions - 1

        for i in range(linesThatNeedToBeDrawn):
            pygame.draw.line(self.frame, Constants.BLACK, ((i+1) * 100, 0), ((i+1) * 100, (linesThatNeedToBeDrawn+1) * 100))
            pygame.draw.line(self.frame, Constants.BLACK, (0, (i+1) * 100), ((linesThatNeedToBeDrawn+1) * 100, (i+1) * 100))

        for i in range(self.dimensions):
            for j in range(self.dimensions):
                self.currentBoard[i][j].drawPiece()


