import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        
        # Get the display surface
        self._display_surface = pygame.display.get_surface()

        # Sprite group setup
        self._visible_sprites = YSortCameraGroup()
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
                    self.player = Player((x, y),[self._visible_sprites], self._obstacle_sprites)


    def run(self):
        # Update and draw the game
        self._visible_sprites.custom_draw(self.player)
        self._visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        super().__init__()
        self._display_surface = pygame.display.get_surface()
        self._half_width = self._display_surface.get_size()[0] // 2
        self._half_height = self._display_surface.get_size()[1] // 2
        self._offset = pygame.math.Vector2()

    def custom_draw(self, player):
        # offset
        self._offset.x = player.rect.centerx - self._half_width
        self._offset.y = player.rect.centery - self._half_height

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self._offset
            self._display_surface.blit(sprite.image, offset_pos )
