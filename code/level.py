import pygame
from settings import *
from tile import Tile
from player import Player
from support import import_csv_layout
from support import import_folder
from random import choice

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
        layouts = {
            'boundary': import_csv_layout("../map/map_FloorBlocks.csv"),
            'grass': import_csv_layout("../map/map_Grass.csv"),
            'object': import_csv_layout("../map/map_Objects.csv")
            
        }
        graphics = {
            'grass': import_folder('../graphics/Grass'),
            'objects': import_folder('../graphics/objects')
        }
        for style,layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        #  Create the boundary tile
                        if style == 'boundary':
                            Tile((x,y), [self._obstacle_sprites], 'invisible')
                        # Create the grass tile
                        if style == 'grass':
                            random_grass_img = choice(graphics['grass'])
                            Tile((x,y), [self._visible_sprites, self._obstacle_sprites], 'grass', random_grass_img)
                        # Create the object tile
                        if style == 'object':
                            surf = graphics['objects'][int(col)]
                            Tile((x,y), [self._visible_sprites,self._obstacle_sprites],'object', surf)
        self.player = Player((2000, 1400),[self._visible_sprites], self._obstacle_sprites)


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

        # Create the floor map
        self._floor_surf = pygame.image.load('../graphics/tilemap/ground.png').convert()
        self._floor_rect = self._floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self, player):
        # offset
        self._offset.x = player.rect.centerx - self._half_width
        self._offset.y = player.rect.centery - self._half_height

        # Drawing the floor
        floor_offset_pos = self._floor_rect.topleft - self._offset
        self._display_surface.blit(self._floor_surf, floor_offset_pos)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self._offset
            self._display_surface.blit(sprite.image, offset_pos )
