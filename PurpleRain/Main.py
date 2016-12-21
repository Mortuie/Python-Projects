import pygame
import random
import RainDroplet

"""
@author lb809 on 20/12/16
@inspiration https://www.youtube.com/watch?v=KkyIDI6rQJI
"""

# initialising pygame & etc..
pygame.init()
pygame.mixer.init()

# Colours
PINK = (189, 144, 212)
PURPLE = (34, 21, 73)

# global variables
FPS = 60
displayHeight = 600
displayWidth = int((16 * displayHeight) / 9)
size = (displayWidth, displayHeight)
clock = pygame.time.Clock()
droplet = pygame.mixer.music.load("rain.mp3")
pygame.mixer.music.play()



def main():
    # running variable
    running = True

    # things for pygame to initialise
    frame = pygame.display.set_mode(size)
    pygame.display.set_caption("Purple Rain")

    # object array of rain
    rainDrops = []
    for i in range(500):
        rainDrops.append(RainDroplet.rain(frame, random.randint(0, displayWidth), random.randint(-50, displayHeight), random.randint(10, 13), random.randint(7, 13), PINK))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        frame.fill(PURPLE)

        for rainDroplets in rainDrops:
            rainDroplets.move()
            rainDroplets.checkOffScreen(displayWidth, displayHeight)
            rainDroplets.draw()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
