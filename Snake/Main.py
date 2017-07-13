import pygame
import random
"""
@author lb809 on 6/1/2017
"""

# CONSTANTS
DIMENSION = 600
MAX_BLOCK = (DIMENSION / 20) - 1

# Initial Conditions
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")
frame = pygame.display.set_mode((DIMENSION, DIMENSION))
f = pygame.font.SysFont(None, 12)

# COLOURS
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# CLASSES
class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drawApple(self):
        pygame.draw.rect(frame, RED, (self.x, self.y, 20, 20))


class BodyPart:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.bodyParts = []
        self.bodyParts.append(BodyPart(DIMENSION / 2, DIMENSION / 2))
        self.bodyParts.append(BodyPart(DIMENSION / 2, DIMENSION / 2))
        self.bodyParts.append(BodyPart(DIMENSION / 2, DIMENSION / 2))
        self.bodyParts.append(BodyPart(DIMENSION / 2, DIMENSION / 2))
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

    def addToTail(self):
        x = self.bodyParts[len(self.bodyParts) - 1].x
        y = self.bodyParts[len(self.bodyParts) - 1].y
        self.bodyParts.append(BodyPart(x, y))

    def moveSnake(self):
        i = len(self.bodyParts) - 1

        while i > 0:
            self.bodyParts[i].x = self.bodyParts[i - 1].x
            self.bodyParts[i].y = self.bodyParts[i - 1].y
            i -= 1

        self.bodyParts[0].x += self.speedx
        self.bodyParts[0].y += self.speedy

        # collision detection
        j = 1
        while j < len(self.bodyParts):
            if ((self.speedx != 0 or self.speedy != 0) and
                self.bodyParts[0].x == self.bodyParts[j].x and
                    self.bodyParts[0].y == self.bodyParts[j].y):

                return False
            j += 1

        if self.bodyParts[0].x < 0:
            # gone out the left of the screen
            self.bodyParts[0].x = DIMENSION
        elif self.bodyParts[0].x > DIMENSION:
            # gone out the right of the screen
            self.bodyParts[0].x = 0
        elif self.bodyParts[0].y < 0:
            # gone out the top of the page
            self.bodyParts[0].y = DIMENSION
        elif self.bodyParts[0].y > DIMENSION:
            # gone out of the bottom of the page
            self.bodyParts[0].y = 0

        return True

    def hasEatenApple(self, apples, score):
        f.render("NIIGA", 1, (255, 255, 255))
        for apple in apples:
            if (apple.x == self.bodyParts[0].x and
                    apple.y == self.bodyParts[0].y):
                apples.remove(apple)
                x = self.getRandomDimension()
                y = self.getRandomDimension()

                while x == self.bodyParts[0].x:
                    x = self.getRandomDimension()
                while y == self.bodyParts[0].y:
                    y = self.getRandomDimension()

                apples.append(Apple(x, y))
                self.addToTail()
                score += 10
                print(score)

    def getRandomDimension(self):
        return random.randint(0, MAX_BLOCK) * 20


def main():
    score = 0
    user = Snake()
    apples = []
    apples.append(Apple(60, 100))

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

        if not user.moveSnake():
            # end game
            print("SHALALALABANG")

        for apple in apples:
            apple.drawApple()

        user.hasEatenApple(apples, score)
        user.drawSnake()
        pygame.display.flip()
        clock.tick(6)


if __name__ == "__main__":
    main()
