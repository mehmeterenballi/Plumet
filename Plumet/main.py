try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    pass

import pygame as pg
import random
import scoring
from terrain_generation import *
import Hero

WIDTH, HEIGHT = 288, 512


def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)

    pg.display.set_caption("Plumet")

    bg = pg.image.load("bg.jpg")
    bg = pg.transform.scale(bg, (288, 512))
    bg.convert_alpha()

    bg_rect = bg.get_rect()

    background = pg.Surface((bg_rect.width * 2, bg_rect.height * 2))
    background.set_colorkey((0, 0, 0))
    background.blit(bg, (0, 0))
    background.blit(bg, (0, bg_rect.height))

    backgroundy = bg_rect.height * -1

    entr = pg.image.load("entrace.png")
    entr = pg.transform.scale(entr, (90, 90))
    entr.convert_alpha()

    entrace_rect = entr.get_rect()
    entrace = pg.Surface((entrace_rect.width, entrace_rect.height))
    entrace.set_colorkey((0, 0, 0))
    entrace.blit(entr, (0, 0))

    entraceY = 0
    screen.blit(entrace, (0, 0))

    entraceBool = True

    del bg_rect
    del bg
    del entrace_rect
    del entr

    score = 0

    allgroups = pg.sprite.Group()
    herogroup = pg.sprite.Group()
    rowsgroup = pg.sprite.Group()

    # terrain_spawn_time = 0
    # terrain_interval = 2

    terrain_pos_count = 0

    bg_color_interval = 0

    hero = Hero.Hero(screen, [150, 0], allgroups, herogroup)

    a = Rows([random.randint(50, 267), 512 + 26], allgroups, rowsgroup, herogroup)

    clock = pg.time.Clock()
    running = True

    while running:
        time = clock.tick() / 1000.0

        bg_color_interval += 1

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

        if Config.isAlive:
            score += 1
            Config.score = score

            backgroundy += time * 100
            screen.blit(background, (0, backgroundy))
            if backgroundy + 512 > HEIGHT:
                backgroundy = -512

            # terrain_spawn_time += time * (Config.score * 10 + 1) ** .02

            # if terrain_spawn_time > terrain_interval:
            #     pos = [random.randint(50, 267), 512 + 26]
            #     Rows(pos, allgroups, rowsgroup, herogroup)
            #     terrain_spawn_time = 0
            #     del pos

            speed = 100 * (((Config.score + 1) * 0.2) ** .05) * time
            terrain_pos_count -= speed * 3

            if terrain_pos_count > 430:
                pos = [random.randint(50, 267), 512 + 26]
                Rows(pos, allgroups, rowsgroup, herogroup)
                terrain_pos_count = 0
                del pos

            allgroups.update(time)
            allgroups.draw(screen)

            scoring.score_blitting(screen, score)

            if entraceBool:
                entraceY -= 35 * time
                screen.blit(entrace, (0, entraceY))
            if entraceY < -90:
                entraceBool = False

        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()
