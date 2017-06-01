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




class snake:
    bodyDimension = 20

    xVel = 0
    yVel = 0

    snakeParts = []

    def __init__(self, frame):
        self.frame = frame
        self.snakeParts.append([dimension / 2, dimension / 2])


    def drawSnake(self):
        for part in self.snakeParts:
            pygame.draw.rect(self.frame, GREEN, (part[0], part[1], self.bodyDimension, self.bodyDimension))


    def changeX(self, dir):
        self.xVel = 20 * dir
        self.yVel = 0


    def changeY(self, dir):
        self.xVel = 0
        self.yVel = 20 * dir

    def moveSnake(self):
        for i in range(len(self.snakeParts)):
            if i == 0:
                self.snakeParts[i][0] += self.xVel
                self.snakeParts[i][1] += self.yVel
            else:
                self.snakeParts[i][0] == self.snakeParts[i-1][0]
                self.snakeParts[i][1] == self.snakeParts[i-1][1]


    def collisionWith(self, listOfApples):
        for a in reversed(listOfApples):
            if a.x == self.snakeParts[0][0] and a.y == self.snakeParts[0][1]:
                listOfApples.remove(a)

    def checkOffScreen(self):
        if self.snakeParts[0][0] >= dimension:
            self.snakeParts[0][0] = (-1) * self.bodyDimension
        elif self.snakeParts[0][0] < 0:
            self.snakeParts[0][0] = dimension
        elif self.snakeParts[0][1] >= dimension:
            self.snakeParts[0][1] = (-1) * self.bodyDimension
        elif self.snakeParts[0][1] < 0:
            self.snakeParts[0][1] = dimension



def main():
    appleLst = []
    appleLst.append(apple(frame, 150, 150))
    s = snake(frame)


    while True:
        frame.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    s.changeY(-1)
                if event.key == pygame.K_s:
                    s.changeY(1)
                if event.key == pygame.K_a:
                    s.changeX(-1)
                if event.key == pygame.K_d:
                    s.changeX(1)

        s.collisionWith(appleLst)
        s.checkOffScreen()

        for a in appleLst:
            a.drawApple()

        s.moveSnake()
        s.drawSnake()

        pygame.display.flip()
        clock.tick(6)


if __name__ == "__main__":
    main()