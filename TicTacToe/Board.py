import pygame
import Constants
"""
@author lb809 on 1/4/2017
"""

class board:
    currentBoard = []
    def __init__(self, frame, size):
        self.frame = frame
        self.dimensions = size

    def createBoard(self):
        for width in range(self.dimensions):
            self.currentBoard.append([])
            for height in range(self.dimensions):
                self.currentBoard[width].append(0)

    def drawBoard(self):
        limit = self.dimensions - 1
        for i in range(limit):
            pygame.draw.line(self.frame, Constants.BLACK, ((i+1) * 100, 0), ((i+1) * 100, (limit+1) * 100))
            pygame.draw.line(self.frame, Constants.BLACK, (0, (i+1) * 100), ((limit+1) * 100, (i+1) * 100))

