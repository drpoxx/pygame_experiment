import pygame

from tiles import Tile
from player import Player
from settings import tile_size, screen_width

class Level:
    def __init__(self, level_data, surface):

        # Level setup.
        self.display_surface = surface 
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for cell_index, cell in enumerate(row):
                # Get the x, y coordinate on each loop.
                x = cell_index * tile_size
                y = row_index * tile_size

                # Place the map tiles.
                if cell == "X":
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)

                # Place the player tile.
                elif cell == "P":
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        # Logic to move the player and/or the screen by scrolling the map.
        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def run(self):
        # ------ Tiles ------
        # Scroll through the map based on player movement as well as draw the
        # map tiles.
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # ------ Player ------
        self.player.update()
        self.player.draw(self.display_surface)
        self.scroll_x()
        

