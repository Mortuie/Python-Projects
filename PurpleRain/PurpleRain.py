import pygame
import random

"""
@author lb809 on 20/12/16
@inspiration https://www.youtube.com/watch?v=KkyIDI6rQJI
"""

# Colours
PINK = (189, 144, 212)
PURPLE = (34, 21, 73)

# global variables
pygame.init()
pygame.mixer.init()
FPS = 60
displayHeight = 900
displayWidth = 900
size = (displayWidth, displayHeight)
clock = pygame.time.Clock()
droplet = pygame.mixer.music.load("rain.mp3")
pygame.mixer.music.play()

class rain:
    def __init__(self, screen, x, y, speed, height):
        self.x = x
        self.y = y
        self.speed = speed

        self.height = height
        self.colour = PINK
        self.frame = screen

        if self.speed > 11:
            self.width = random.randint(2, 3)
        else:
            self.width = random.randint(1, 2)

    def draw(self):
        pygame.draw.rect(self.frame, self.colour, [self.x, self.y, self.width, self.height], 0)

    def move(self):
        self.y += self.speed

    def checkOffScreen(self):
        if self.y > displayHeight:
            self.y = random.randint(-50, 0)
            self.x = random.randint(0, displayWidth)


def main():
    # running variable
    running = True

    # things for pygame to initialise

    frame = pygame.display.set_mode(size)
    pygame.display.set_caption("Purple Rain")

    # object array of rain
    rainDrops = []
    for i in range(500):
        rainDrops.append(rain(frame, random.randint(0, displayWidth), random.randint(-50, displayHeight), random.randint(10, 13), random.randint(7, 13)))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        frame.fill(PURPLE)

        for rainDroplets in rainDrops:
            rainDroplets.move()
            rainDroplets.checkOffScreen()
            rainDroplets.draw()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
