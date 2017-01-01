import pygame
import Constants
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
    frame = pygame.display.set_mode(Constants.SIZE)
    pygame.display.set_caption("Space Invaders")
    playerPaddle = paddle(frame)
    movePaddleBy = 0

    # object arrays
    allBullets = []
    monsters = []

    for i in range(5):
        monsters.append(monster(frame, 175 * (i + 1)))

    def distanceBetweenTwoPoints(x1, y1, x2, y2):
        diffX = (x1 - x2) ** 2
        diffY = (y1 - y2) ** 2

        return (diffX + diffY) ** 0.5

    while running:
        frame.fill(Constants.BLACK)
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
            for a in reversed(allBullets):
                for b in reversed(monsters):
                    if distanceBetweenTwoPoints(a.x, a.y, b.x, b.y) < 30:
                        a.flickCollisionState()
                        b.flickCollisionState()

        if len(allBullets) != 0:
            for projectile in reversed(allBullets):
                if projectile.y < 0:
                    allBullets.remove(projectile)
                elif projectile.collision:
                    allBullets.remove(projectile)
                else:
                    projectile.move()
                    projectile.draw()

        for j in reversed(monsters):
            if j.collision:
                monsters.remove(j)
            else:
                if j.x + 30 == DISPLAYWIDTH or j.x - 30 == 0:
                    for h in reversed(monsters):
                        h.speed *= -1
                        h.y += 20
                j.move()
                j.draw()

        playerPaddle.move(movePaddleBy)
        playerPaddle.draw()
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()