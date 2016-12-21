import pygame
from Constants import *
from Paddle import *
from Bullet import *
from Monster import *

"""
@author lb809 on 21/12/16
"""

# initialising pygame
pygame.init()
clock = pygame.time.Clock()

def main():
    running = True
    frame = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Space Invaders")
    playerPaddle = paddle(frame)
    movePaddleBy = 0


    allBullets = []
    monsters = []

    for i in range(5):
        monsters.append(monster(frame, 175 * (i + 1)))


    while running:
        frame.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    movePaddleBy = 10
                if event.key == pygame.K_a:
                    movePaddleBy = -10
                if event.key == pygame.K_SPACE:
                    allBullets.append(bullet(frame, playerPaddle.getPaddleX()))
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    movePaddleBy = 0


        if len(allBullets) != 0:
            for projectile in reversed(allBullets):
                if projectile.y < 0:
                    allBullets.remove(projectile)
                else:
                    projectile.move()
                    projectile.draw()

        for j in reversed(monsters):
            j.draw()

        playerPaddle.move(movePaddleBy)
        playerPaddle.draw()
        pygame.display.flip()
        clock.tick(FPS)



if __name__ == "__main__":
    main()