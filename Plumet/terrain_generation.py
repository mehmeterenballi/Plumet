import pygame as pg
from Hero import Config


class Rows(pg.sprite.Sprite):
    def __init__(self, pos, *groups):
        self.groups = groups[0], groups[1]
        self.hero = groups[2]

        pg.sprite.Sprite.__init__(self, self.groups)

        left_colon = pg.image.load('floor.png')
        left_colon = pg.transform.scale(left_colon, (217, 51))
        right_colon = pg.transform.flip(left_colon, 1, 0).convert_alpha()
        left_colon_rect = left_colon.get_rect()
        right_colon_rect = left_colon.get_rect()

        horizontal_gap = 100

        self.image = pg.Surface(
            (left_colon_rect.width + left_colon_rect.width + horizontal_gap, left_colon_rect.height))
        self.image.blit(left_colon, (0, 0))
        self.image.blit(right_colon, (left_colon_rect.width + horizontal_gap, 0))
        self.image.set_colorkey((0, 0, 0))
        self.image.convert_alpha()

        self.mask = pg.mask.from_surface(self.image)

        del left_colon_rect
        del right_colon_rect
        del left_colon
        del right_colon

        self.rect = self.image.get_rect()
        self.pos = pos.copy()
        self.rect.center = self.pos

    def update(self, time):
        speed = 100 * (((Config.score + 1) * 0.2) ** .05) * time

        if Config.isAlive:
            if Config.currentPos[1] < 400:
                self.pos[1] -= speed
            else:
                self.pos[1] -= speed * 3

            collided = pg.sprite.spritecollide(self, self.hero, False, pg.sprite.collide_mask)
            for c in collided:
                Config.currentPos[1] = self.rect.top - 32

            if self.rect.bottom < 0:
                self.kill()

            self.rect.center = self.pos
        else:
            print("Rows stopped")
