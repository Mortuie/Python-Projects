import random

import Constants
import pygame
import Bird
import PipeGenerator
"""
@author lb809 on 24/12/16
"""

pygame.init()
clock = pygame.time.Clock()



def main():
    frameCount = 0

    gameRunning = True


    frame = pygame.display.set_mode(Constants.SIZE)
    pygame.display.set_caption(Constants.TITLE)

    playerBird = Bird.bird(frame)

    pipes = []

    while (gameRunning):
        frame.fill(Constants.WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playerBird.whenSpaceIsPressed()



        playerBird.updateBird()
        playerBird.drawBird()


        if (frameCount % 60 == 0):
            pipes.append(PipeGenerator.pipe(frame, playerBird))

        if (len(pipes) != 0):
            for pipe in reversed(pipes):
                if pipe.offPage():
                    pipes.remove(pipe)
                else:
                    pipe.drawPipe()
                    pipe.movePipe()
                    if pipe.collidedWithBird():
                        pipe.changeColourFromOriginal()
                    else:
                        pipe.changeColourBackToOriginal()



        pygame.display.flip()
        clock.tick(Constants.FPS)

        frameCount += 1




if __name__ == "__main__":
    main()