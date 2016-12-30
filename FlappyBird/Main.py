import Constants
import pygame
import Bird
import PipeGenerator

"""
@author lb809 on 24/12/16
"""

pygame.init()
clock = pygame.time.Clock()
frame = pygame.display.set_mode(Constants.SIZE)
pygame.display.set_caption(Constants.TITLE)

def main():
    frameCount = 0
    gameRunning = True

    playerBird = Bird.bird(frame)
    pipes = []

    def frameCountIsDivisibleByNumber():
        return frameCount % 90 == 0

    def PipeArrayIsNotEmpty():
        return len(pipes) != 0

    while gameRunning:
        frame.fill(Constants.WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playerBird.whenSpaceIsPressed()

        playerBird.updateBird()
        playerBird.drawBird()

        if frameCountIsDivisibleByNumber():
            pipes.append(PipeGenerator.pipe(frame, playerBird))

        if PipeArrayIsNotEmpty():
            for pipe in reversed(pipes):
                if pipe.offPage():
                    pipes.remove(pipe)
                else:
                    pipe.updatePipe()
                    pipe.drawPipe()
                    if pipe.collidedWithBird():
                        pipe.changeColourFromOriginal()
                    else:
                        pipe.changeColourBackToOriginal()

        pygame.display.flip()
        clock.tick(Constants.FPS)
        frameCount += 1


if __name__ == "__main__":
    main()