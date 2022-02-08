import pygame
from settings import *
from tile import Tile
from player import Player


class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        # spite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.abstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def run(self):
        # update and draw the game
        self.visible_sprites.draw(self.display_surface)

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.abstacle_sprites])
                if col == 'p':
                    Player((x, y), [self.visible_sprites])
