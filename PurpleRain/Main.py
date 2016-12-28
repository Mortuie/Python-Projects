import pygame
import random
import RainDroplet
import Constants

"""
@author lb809 on 20/12/16
@inspiration https://www.youtube.com/watch?v=KkyIDI6rQJI
"""

# initialising pygame & etc..
pygame.init()
pygame.mixer.init()


clock = pygame.time.Clock()
droplet = pygame.mixer.music.load("rain.mp3")
pygame.mixer.music.play()


def main():
    running = True

    frame = pygame.display.set_mode(Constants.SIZE)
    pygame.display.set_caption("Purple Rain")

    rainDrops = []
    for i in range(500):
        rainDrops.append(RainDroplet.rain(frame, random.randint(0, Constants.DISPLAYWIDTH), random.randint(-50, Constants.DISPLAYHEIGHT), random.randint(10, 13), random.randint(7, 13), Constants.PINK))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        frame.fill(Constants.PURPLE)

        for rainDroplets in rainDrops:
            rainDroplets.move()
            rainDroplets.checkOffScreen(Constants.DISPLAYWIDTH, Constants.DISPLAYHEIGHT)
            rainDroplets.draw()

        pygame.display.flip()
        clock.tick(Constants.FPS)

if __name__ == "__main__":
    main()
