"""
Created by (Esteban Gómez) in  ${2022}
"""
import pyxel

class Background:
    def __init__(self, position_x, position_y):
        self.height = 255
        self.width = 255
        self.position_x = position_x
        self.position_island_y = position_y
        self.position_y_list=[]
        self.position_clouds_y=position_y
        for image in range(4):
            self.position_clouds_y -= 100
            self.position_y_list.append(self.position_clouds_y)

    def update(self):
        if self.position_island_y < self.height:
            self.position_island_y += 0.5
        for i in range(len(self.position_y_list)):
            if self.position_y_list[i] < self.height:
                self.position_y_list[i] += 0.5
            if self.position_y_list[i] >= self.height:
                self.position_y_list[i] = -100

    def draw(self):
        if self.position_island_y < self.height:
            pyxel.blt(self.position_x, self.position_island_y, 2, 0, 0, 255, 255, 0)
        for i in range(0, len(self.position_y_list)):
            pyxel.blt(self.position_x, self.position_y_list[i], 2, 0, 0, 255, 100, 0)
            if i == 3:
                if self.position_y_list[i] <= -100:
                    self.position_x_island2= pyxel.rndi(-50, self.width)
                pyxel.blt(self.position_x_island2, self.position_y_list[i], 0, 0, 0, 210, 100, 0)





