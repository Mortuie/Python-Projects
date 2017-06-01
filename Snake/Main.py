import pygame
"""
@author lb809 on 6/1/2017
"""

# Initial Conditions
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")
frame = pygame.display.set_mode((500, 500))

# COLOURS
BLACK = (0, 0, 0)
RED = (255, 0, 0)
# CLASSES

class apple:

    def __init__(self, frame, x, y):
        self.dim = 40
        self.frame = frame
        self.x = x
        self.y = y



    def drawApple(self):
        pygame.draw.rect(frame, RED, (self.x, self.y), self.dim)


def main():

    app = apple(frame, 150, 150)


    while True:
        frame.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


        app.drawApple()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()