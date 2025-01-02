import pygame
from constants import *
from player import Player

def main():
    # initialize pygame
    pygame.init()

    # set display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # set clock
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # limit framerate to 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
