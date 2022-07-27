import pygame
from tiles import Tile
from settings import tile_size, screen_width
from player import Player


class Level:
    def __init__(self, level_data, surface):

        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, column in enumerate(row):
                x = col_index*tile_size
                y = row_index*tile_size
                if column == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if column == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        v_x = player.v.x

        if player_x < screen_width/4 and v_x < 0:
            self.world_shift = 8
            player.s = 0
        elif player_x > screen_width - (screen_width/4) and v_x > 0:
            self.world_shift = -8
            player.s = 0
        else:
            self.world_shift = 0
            player.s = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.v.x*player.s

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.v.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.v.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_g()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.v.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.v.y = 0
                elif player.v.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.v.y = 0

    def run(self):

        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # player
        self.player.update()
        self.player.draw(self.display_surface)
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
