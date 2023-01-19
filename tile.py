import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self._image = pygame.image.load("../graphcs/test/rock.png").convert_alpha()
        self._rect = self._image.get_rect(topleft = pos)