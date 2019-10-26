import pygame as pg


class Config:
    currentPos = [150, 0]
    isAlive = True
    score = 0
    # dualRows = []
    lowestDualRowsPos = [0, 0]


class Hero(pg.sprite.Sprite):

    def __init__(self, screen, pos=[150, 0], *groups):
        # F = m * a
        # g = 9.8 m/s^2
        # upwards: v += g * t, downwards: v -= g * t
        # x = a*t^2 / 2
        # x = v * t
        self.g = 9.8  # gravity
        self.v = 400  # speed

        # self.x = self.v * self.time

        self.groups = groups[0], groups[1]
        pg.sprite.Sprite.__init__(self, self.groups)

        self.image_array = []

        for i in range(1, 10):
            self.image_array.append(pg.image.load("l{}.png" .format(str(i))).convert_alpha())
        for i in range(1, 10):
            self.image_array.append(pg.image.load("r{}.png" .format(str(i))).convert_alpha())

        self.image_array.append(pg.image.load("Standing.png").convert_alpha())

        self.current_pic = 18
        self.image = self.image_array[self.current_pic]
        self.image_orig = self.image.copy()
        self.rect = self.image.get_rect()
        self.screenrect = screen.get_rect()

        self.pos = pos.copy()
        self.rect.center = self.pos

        self.animationinterval = 0.2
        self.animationtime = 0

        self.flyinginterval = 0.5
        self.flyingtime = 0

        self.buttoninterval = self.flyinginterval / 2
        self.buttontime = 0

        self.right = False
        self.left = False
        self.standing = True
        self.isJump = False
        self.walkCount = 0
        self.jumpCount = 10

    def update(self, time):
        if Config.isAlive:
            Config.currentPos[1] += 200 * time
            self.pos = Config.currentPos
            self.rect.center = self.pos

            click = pg.mouse.get_pressed()
            mousePos = pg.mouse.get_pos()

            if click[0] == 1:
                if mousePos[0] < self.screenrect.width / 2:
                    if self.right is True:
                        self.walkCount = 0
                    self.left = True
                    self.walkCount += 1
                    self.current_pic = self.walkCount
                    self.image = self.image_array[self.current_pic]
                    if self.walkCount == 8:
                        self.walkCount = 0
                    Config.currentPos[0] -= 110 * time
                elif mousePos[0] > self.screenrect.width / 2:
                    if self.left is True:
                        self.walkCount = -1
                    self.right = True
                    self.walkCount -= 1
                    self.current_pic = abs(self.walkCount)
                    self.image = self.image_array[self.current_pic * -1]
                    if self.walkCount == -10:
                        self.walkCount = -1
                    Config.currentPos[0] += 110 * time
                else:
                    print("You clicked middle of the screen")

            if self.rect.bottom < -3:
                Config.isAlive = True
        else:
            print("Not Alive!")
