import pygame
"""
@author lb809 on 6/1/2017
"""

# CONSTANTS
dimension = 600

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
class Snake:
    def __init__(self):
        self.headx = dimension / 2
        self.heady = dimension / 2
        self.speedx = 0
        self.speedy = 0

    def drawSnake(self):
        pygame.draw.rect(frame, GREEN, (self.headx, self.heady, 20, 20))

    def changeDirection(self, direction):
        self.speedx = 0
        self.speedy = 0
        if direction == 'n':
            self.speedy = -20
        elif direction == 'e':
            self.speedx = 20
        elif direction == 's':
            self.speedy = 20
        else:
            self.speedx = -20

    def moveSnake(self):
        self.headx += self.speedx
        self.heady += self.speedy


def main():
    user = Snake()

    while True:
        frame.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    user.changeDirection('n')
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    user.changeDirection('s')
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    user.changeDirection('w')
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    user.changeDirection('e')

        user.moveSnake()
        user.drawSnake()
        pygame.display.flip()
        clock.tick(6)


if __name__ == "__main__":
    main()
