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
class BodyPart:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.bodyParts = []
        self.bodyParts.append(BodyPart(dimension / 2, dimension / 2))
        self.bodyParts.append(BodyPart(dimension / 2, (dimension / 2) - 20))
        self.speedx = 0
        self.speedy = 0

    def drawSnake(self):
        for part in self.bodyParts:
            pygame.draw.rect(frame,
                             GREEN,
                             (part.x, part.y, 20, 20)
                             )

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
        i = len(self.bodyParts) - 1

        while i > 0:
            self.bodyParts[i].x = self.bodyParts[i - 1].x
            self.bodyParts[i].y = self.bodyParts[i - 1].y
            i -= 1

        self.bodyParts[0].x += self.speedx
        self.bodyParts[0].y += self.speedy


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
