import pygame

from tiles import Tile
from player import Player
from settings import tile_size, screen_width

class Level:
    def __init__(self, level_data, surface):

        # Level setup.
        self.display_surface = surface 
        self.setup_level(level_data)
        # Used for the shift of the level when moving. Default to 0.
        self.world_shift = 0
        # Needed to store the side of the collision when the player collides with objects on the x-axis.
        self.current_x = 0

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

    def horizontal_movement_collision(self):
        player = self.player.sprite
        # NOTE: handle the player movement in the level not in the player class.
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                # Need to figure out if collision is left or right.
                if player.direction.x < 0:
                    # Left side collision.
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    # Right side collision.
                    player.rect.right = sprite.rect.left
                    player.on_left = True
                    self.current_x = player.rect.right
        
        # Complicated collision logic. Player could continue run into object hence comparison with the historical collision.
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    def vertical_movement_collision(self):
        player = self.player.sprite
        # NOTE: handle the player movement in the level not in the player class.
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                # Need to figure out if collision is left or right.
                if player.direction.y > 0:
                    # Bottom side collision.
                    player.rect.bottom = sprite.rect.top
                    # Cancel the gravity out so no buildup appears.
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    # Top side collision.
                    player.rect.top = sprite.rect.bottom
                    # Cancel out any movement buildup.
                    player.direction.y = 0
                    player.on_ceiling = True

        # Reset the status if in movement.
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False


    def run(self):
        # ------ Tiles ------
        # Scroll through the map based on player movement as well as draw the
        # map tiles.
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # ------ Player ------
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
        
        

