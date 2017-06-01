import pygame
"""
@author lb809 on 6/1/2017
"""

# CONSTANTS
dimension = 500

# Initial Conditions
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")
frame = pygame.display.set_mode((dimension, dimension))

# COLOURS
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# CLASSES

class apple:

    def __init__(self, frame, x, y):
        self.dim = 20
        self.frame = frame
        self.x = x
        self.y = y

    def drawApple(self):
        pygame.draw.rect(frame, RED, (self.x, self.y, self.dim, self.dim))

    def checkCollisionWith(self, snake):
        pass
        # write collision code


class snake:

    def __init__(self, frame):
        self.frame = frame
        self.x = int(dimension / 2) - 10
        self.y = int(dimension / 2) - 10
        self.yv = 0
        self.xv = 0
        self.dim = 20
        self.snakeParts = []
        self.snakeParts.append([self.x, self.y])


    def drawSnake(self):
        for part in self.snakeParts:
            pygame.draw.rect(self.frame, GREEN, (part[0], part[1], self.dim, self.dim))

    def changeInY(self, dir):
        self.yv = dir * self.dim
        self.xv = 0

    def changeInX(self, dir):
        self.xv = dir * self.dim
        self.yv = 0

    def moveSnake(self):
        self.x += self.xv
        self.y += self.yv



def main():

    app = apple(frame, 150, 150)
    s = snake(frame)


    while True:
        frame.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    s.changeInY(-1)
                if event.key == pygame.K_s:
                    s.changeInY(1)
                if event.key == pygame.K_a:
                    s.changeInX(-1)
                if event.key == pygame.K_d:
                    print("BANTER")
                    s.changeInX(1)


        app.drawApple()
        s.moveSnake()
        s.drawSnake()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()