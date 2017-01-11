from Board import board
import pygame
import Constants
import random

"""
@author lb809 on 1/4/2017
"""

pygame.init()
clock = pygame.time.Clock()


def main():
    gameRunning = True
    playerMove = random.choice([True, False])

    frame = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("TicTacToe")

    gameBoard = board(frame)
    gameBoard.createBoard()


    while gameRunning:
        frame.fill(Constants.WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and playerMove:
                    positionOfMouse = pygame.mouse.get_pos()
                    gameBoard.playerPressed(positionOfMouse[0], positionOfMouse[1])
                    playerMove = False

        if not playerMove:
            gameBoard.botPressed()
            playerMove = True

        gameBoard.drawBoard()
        clock.tick(Constants.FPS)
        pygame.display.flip()



if __name__ == "__main__":
    main()
