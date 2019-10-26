import pygame as pg


def score_blitting(win, score):
    screen_width, screen_height = 288, 512
    score_image = [pg.image.load('%d.png' % decimal) for decimal in range(0, 10)]

    if 10 > score >= 0:
        win.blit(score_image[score], (screen_width / 2, 0))
    elif 100 > score >= 10:
        units_digit = score % 10
        tens_digit = int((score - units_digit) / 10)
        win.blit(score_image[tens_digit], (screen_width / 2 - 10, 0))
        win.blit(score_image[units_digit], (screen_width / 2 + 10, 0))
    elif 1000 > score >= 100:
        units_digit = score % 10
        tens_digit = int(((score - units_digit) % 100) / 10)
        hundreds_digit = int((score - tens_digit * 10 - units_digit) / 100)
        win.blit(score_image[hundreds_digit], (screen_width / 2 - 36, 0))
        win.blit(score_image[tens_digit], (screen_width / 2 - 12, 0))
        win.blit(score_image[units_digit], (screen_width / 2 + 12, 0))
    elif 10000 > score >= 1000:
        units_digit = score % 10
        tens_digit = int(((score % 100) - units_digit) / 10)
        hundreds_digit = int(((score - (score % 100)) % 1000) / 100)
        thousands_digit = int((score - (score % 1000)) / 1000)
        win.blit(score_image[thousands_digit], (screen_width / 2 - 48, 0))
        win.blit(score_image[hundreds_digit], (screen_width / 2 - 24, 0))
        win.blit(score_image[tens_digit], (screen_width / 2, 0))
        win.blit(score_image[units_digit], (screen_width / 2 + 24, 0))
    elif 100000 > score >= 10000:
        units_digit = score % 10
        tens_digit = int(((score % 100) - units_digit) / 10)
        hundreds_digit = int(((score - tens_digit * 10 - units_digit) % 1000) / 100)
        thousands_digit = int(((score - hundreds_digit * 100 - tens_digit * 10 - units_digit) % 10000) / 1000)
        ten_thousands_digit = int((score - (score % 10000)) / 10000)
        win.blit(score_image[hundreds_digit], (screen_width / 2 - 12, 0))
        win.blit(score_image[tens_digit], (screen_width / 2 + 12, 0))
        win.blit(score_image[units_digit], (screen_width / 2 + 36, 0))
        win.blit(score_image[thousands_digit], (screen_width / 2 - 36, 0))
        win.blit(score_image[ten_thousands_digit], (screen_width / 2 - 60, 0))
    else:
        print("Game Completed")
