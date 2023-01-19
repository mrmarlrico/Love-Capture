import pygame

class Level:
    def __init__(self):
        
        # Get the display surface
        self._display_surf = pygame.display.get_surface()
        
        # Sprite group setup
        self._visible_sprites = pygame.sprite.Group()
        self._obstacle_sprites = pygame.sprite.Group()
    
    def run(self):
        pass