import Constants
import pygame
import Bird
import PipeGenerator

"""
@author lb809 on 24/12/16
"""

pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()
frame = pygame.display.set_mode(Constants.SIZE)
pygame.display.set_caption(Constants.TITLE)

# TODO collision detection is still very buggy, and so is the gameplay.

def main():
    score = 0
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
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playerBird.whenSpaceIsPressed()
                if event.key == pygame.K_p:
                    pause()

        playerBird.updateBird()
        playerBird.drawBird()

        if frameCountIsDivisibleByNumber():
            pipes.append(PipeGenerator.pipe(frame, playerBird))
            score += 1

        if PipeArrayIsNotEmpty():
            for pipe in reversed(pipes):
                if pipe.offPage():
                    pipes.remove(pipe)
                else:
                    pipe.updatePipe()
                    pipe.drawPipe()
                    if pipe.collidedWithBird():
                        gameEnd(score)
                    else:
                        pipe.changeColourBackToOriginal()

        displayText("Score: " + str(score), 0, 0)
        pygame.display.flip()
        clock.tick(Constants.FPS)
        frameCount += 1

def displayText(stringDisplayed, x, y):
    scoreText = font.render(stringDisplayed, 1, Constants.BLACK)
    frame.blit(scoreText, (x, y))

def pause():
    pausedState = True
    quitState = True
    while pausedState and quitState:
        displayText("Game Paused", Constants.DISPLAYWIDTH / 2, Constants.DISPLAYHEIGHT / 2)
        displayText("'P' to resume", Constants.DISPLAYWIDTH / 2, Constants.DISPLAYHEIGHT/2 + 40)
        displayText("Press 'q' to quit the game.", Constants.DISPLAYWIDTH / 7, Constants.DISPLAYHEIGHT / 1.25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitState = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pausedState = False
                if event.key == pygame.K_q:
                    quitState = False

        pygame.display.flip()
        clock.tick(Constants.FPS)

    if not quitState:
        pygame.quit()


def gameEnd(scoreAchieved):

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    main()
                if event.key == pygame.K_q:
                    exit()

        #todo change the way the flying of the bird works. Seems quite dodgy at the moment.

        displayText("Score: " + str(scoreAchieved), Constants.DISPLAYWIDTH / 7, Constants.DISPLAYHEIGHT / 2.5)
        displayText("Game over you lose.", Constants.DISPLAYWIDTH / 7, Constants.DISPLAYHEIGHT / 2)
        displayText("Press 'n' for a new game.", Constants.DISPLAYWIDTH / 7, Constants.DISPLAYHEIGHT / 1.5)
        displayText("Press 'q' to quit the game.", Constants.DISPLAYWIDTH / 7, Constants.DISPLAYHEIGHT / 1.25)


        pygame.display.flip()
        clock.tick(Constants.FPS)

def displayText(stringDisplayed, x, y):
    scoreText = font.render(stringDisplayed, 1, Constants.BLACK)
    frame.blit(scoreText, (x, y))



if __name__ == "__main__":
    main()