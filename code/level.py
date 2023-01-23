import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        
        # Get the display surface
        self._display_surface = pygame.display.get_surface()

        # Sprite group setup
        self._visible_sprites = pygame.sprite.Group()
        self._obstacle_sprites = pygame.sprite.Group()

        # Sprite setup
        self.create_map()
    
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self._visible_sprites,self._obstacle_sprites])
                if col == 'p':
                    Player((x, y),[self._visible_sprites], self._obstacle_sprites)


    def run(self):
        # Update and draw the game
        self._visible_sprites.draw(self._display_surface)
        self._visible_sprites.update()