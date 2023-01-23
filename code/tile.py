import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, group, sprite_type, surf = pygame.Surface((TILESIZE,TILESIZE))):
        super().__init__(group)
        self._sprite_type = sprite_type
        self.image = surf
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft = (pos[0], pos[1]-TILESIZE))

        else:
            self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)