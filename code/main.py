import pygame, sys
from settings import *
from level import Level
# from debug import debug

class Game():
    def __init__(self):
        
        # general setup
        pygame.init()
        self._screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Love Capture')
        self._clock = pygame.time.Clock()

        self._level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self._screen.fill('black')
            self._level.run()
            pygame.display.update()
            self._clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()