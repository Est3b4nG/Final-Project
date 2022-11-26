"""
Created by (Esteban Gómez) in  ${2022}
"""
import pyxel
import time

class Enemy1:
    #We bring the values of position x and y from the board
    def __init__(self, x:int,y:int, lives:int=1):
        self.x= x    #position of the enemy in x (originally a random number)
        self.y= y    #position of enemy in y (originally, -12)
        self.lives=lives   #Declared here as 1
        self.direction = 1   #Direction, if it is going down or up (we give value=! to represent when it is going down )


        #We are importing the image in the position 0,16 of the image bank 0, this image have diemnsion of 16x16 and
        # the colkey is black(0), we will use this vale in the board
        self.image = (0,16, 0,16, 16, 0)


    def move(self, height,y:int):
        # the position in y will be equal to the movement per frame (2 (velocity in which it is going to move)),
        # and we multiply it by the direction in order to determine if it is going up or down
        self.y += 2 * self.direction    #(-->self.y = self.y + 2 * self.direction) other way of writing it
        if self.y >= (height/2):     #Here I'm saying that when the enemy plane reaches the half of the screen the
            # direction will become -1, so up in the general formula instead of adding to frames it will start to
            # subtract two frames (self.y + 2 * (-1) --> self.y - 2)
             self.direction *= -1





