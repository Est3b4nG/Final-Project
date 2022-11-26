"""
Created by (Esteban Gómez) in  ${2022}
"""

import random
class Clouds:
    "Everything related to the clouds"

    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

        self.image=(1, 32, 80, 45, 35, 0)

    def move(self, width, height, position_y):
        self.position_y+= 2
        if self.position_y > height:
            self.position_y = position_y
        if self.position_y < 0 - self.image[4]:
            self.position_x = random.randint(0, width)

