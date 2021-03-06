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

        for width in range(3):
            for height in range(3):

                self.currentBoard[width].append(Pieces.piece(self.frame, coordX, coordY, 0))

                coordX += 100

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

    def playerPressed(self, x, y):
        self.currentBoard[int(y/100)][int(x/100)].changeTypeOfPiece(1)

    def botPressed(self):
        hasBotMoved = False

        for i in range(3):
                for j in range(3):
                    if not hasBotMoved and self.currentBoard[i][j].isAnEmptyTile():
                        self.currentBoard[i][j].changeTypeOfPiece(2)
                        hasBotMoved = True


        #TODO add some win check and add some Algorithm

    def hasGameBeenWon(self, whichPlayerAreYouChecking):
        # return 0 if game hasn't been won
        # return 1 if player has
        # return 2 if bot has

        

        pass
