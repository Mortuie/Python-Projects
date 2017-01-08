from Board import board
import pygame
import Constants

"""
@author lb809 on 1/4/2017
"""
pygame.init()
clock = pygame.time.Clock()



def main():
    gameRunning = True
    size = 3 # int(input("Size of the board: "))

    frame = pygame.display.set_mode((size*100, size*100))
    pygame.display.set_caption("TicTacToe")

    gameBoard = board(frame, size)
    gameBoard.createBoard()

    while gameRunning:
        frame.fill(Constants.WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False


        gameBoard.drawBoard()
        clock.tick(Constants.FPS)
        pygame.display.flip()



if __name__ == "__main__":
    main()
