
import random
import pyxel


class Background:
    def __init__(self, position_1x, position_1y):
        self.height = 255
        self.position_1x = position_1x
        self.position_1y = position_1y
        self.position_2x= position_1x
        self.position_2y = position_1y - 100
        self.position_3x = position_1x
        self.position_3y = position_1y - 200
        self.position_4x= position_1x
        self.position_4y = position_1y - 300

    def update(self):
        if self.position_1y < self.height:
            self.position_1y += 0.5
        if self.position_2y < self.height:
            self.position_2y += 0.5
        if self.position_2y == self.height:
            self.position_2y = -100
        if self.position_3y < self.height:
            self.position_3y += 0.5
        if self.position_3y == self.height:
            self.position_3y = -100
        if self.position_3y < -100:
            self.position_3x = random.randint(-50 , self.height//4)
        if self.position_4y < self.height:
            self.position_4y += 0.5
        if self.position_4y == self.height:
            self.position_4y = -100




    def draw(self):
        pyxel.blt(self.position_1x, self.position_1y, 2, 0, 0, 255, 260, 0)
        pyxel.blt(self.position_2x, self.position_2y, 2, 0, 0, 255, 100, 0)
        pyxel.blt(self.position_3x, self.position_3y, 0, 0, 0, 175, 79, 0)
        pyxel.blt(self.position_4x, self.position_4y, 2, 0, 0, 255, 100, 0)


class Clouds:
    "Everything related to the clouds"

    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

        self.image=(1, 32, 80, 45, 35, 0)


    def update(self, width, height, position_y):
        self.position_y += 2
        if self.position_y > height:
            self.position_y = position_y
        if self.position_y < 0 - self.image[4]:
            self.position_x = random.randint(0, width)

    def draw(self):
        pyxel.blt(self.position_x, self.position_y, *self.image)





