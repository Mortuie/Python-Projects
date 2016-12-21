import pygame
import random

"""
@author lb809 on 20/12/16
"""

# Colours
PINK = (189, 144, 212)
WHITE = (255, 255, 255)
PURPLE = (34, 21, 73)

# global variables
FPS = 45
displayHeight = 500
displayWidth = 800
size = (displayWidth, displayHeight)
clock = pygame.time.Clock()

class rain:
    def __init__(self, screen, x, y, speed, width, height):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.colour = PINK
        self.frame = screen

    def update(self):
        pygame.draw.rect(self.frame, self.colour, [self.x, self.y, self.width, self.height], 0)

    def move(self):
        self.y += self.speed

    def checkOffScreen(self):
        if self.y > displayHeight:
            self.y = random.randint(-50, 0)

def main():
    # running variable
    running = True
    # things for pygame to initialise
    pygame.init()
    frame = pygame.display.set_mode(size)
    pygame.display.set_caption("Rain Test")

    # object array of rain
    rainDrops = []
    for i in range(500):
        rainDrops.append(rain(frame, random.randint(0, displayWidth), random.randint(-50, displayHeight), random.randint(10, 13), random.randint(2, 4), 20))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        frame.fill(PURPLE)

        for rainDroplets in rainDrops:
            rainDroplets.move()
            rainDroplets.checkOffScreen()
            rainDroplets.update()

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
