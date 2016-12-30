import pygame
import RainDroplet
import Constants

"""
@author lb809 on 20/12/16
@inspiration https://www.youtube.com/watch?v=KkyIDI6rQJI
"""

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
droplet = pygame.mixer.music.load("rain.mp3")
pygame.mixer.music.play()

def main():
    gameRunning = True

    frame = pygame.display.set_mode(Constants.SIZE)
    pygame.display.set_caption("Purple Rain")

    rainDrops = []
    for number in range(500):
        rainDrops.append(RainDroplet.rain(frame))

    while gameRunning:
        frame.fill(Constants.PURPLE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False

        for rainDroplets in rainDrops:
            rainDroplets.checkOffScreen()
            rainDroplets.moveRain()
            rainDroplets.draw()

        pygame.display.flip()
        clock.tick(Constants.FPS)

if __name__ == "__main__":
    main()
