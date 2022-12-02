"""
Created by (Esteban Gómez) in  ${2022}
"""
import pyxel

class Player:
    """This class will store all the functions related to the player"""
    def __init__(self, x: int, y: int ,lives: int):
        self.x = x           #position in x, originally we bring this value from the board (width/2)
        self.y = y           #The position in y, this originally is (height-30).
        self.lives = lives   #The lives of our plane
        self.list_bullets= []


        #The image of the plane is in coordinate 0,0 of the image bank 0, and have dimension of 16x16, the colkey is
        # black. We are going to use this image in the board to draw the players plane, we are only missing the
        # values of the position of the screen that were going to bring in the board.
        self.image = [0, 208, 240, 16, 16, 0]
        #print(self.image[3])
        #print(self.image[4])

        #You introduce the number of lives
    def update(self, width, height):

        plane_x_size = abs(self.image[3])
        plane_y_size = abs(self.image[4])
        """This method will move the plane"""
    # direction is determined by the key they pressed (coded in the board), range is the height or width of the
    # screen (depending on if you're moving in the x-axis or y-axis) this value is also given in the board.
        #if the position is smaller than the range (width) - the plane dimension in x-axis (if we don't do this,
        # the plane will get out of the screen until it reaches its top left part (from the plane image we imported),
        # this because the left upper prt is the origin point.
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x <= width - plane_x_size:
            self.x = self.x + 4
        #Here we don't subtract the dimension because we only want to move left until it touches the left part of the
        # image,and the origin point of the image is in the left part
        if pyxel.btn(pyxel.KEY_LEFT) and self.x > 0:
            self.x = self.x - 4
        #We don't subtrat thr dimension in y because the origin point is in the upper part of the image
        if pyxel.btn(pyxel.KEY_UP) and self.y > 0:
            self.y = self.y - 4
        #We have to subtract the dimension of the plane in order for it to compeltely stay in the screen because,
        # the origin is in the upper part, if we don't put it, the plane will move down until that point get to the
        # total heigth, and the plane will stop appearing in the screen.
        if pyxel.btn(pyxel.KEY_DOWN) and self.y < height - plane_y_size:
            self.y = self.y + 4

        if pyxel.btnp(pyxel.KEY_SPACE):
            bullets = Bullets(self.x, self.y)
            self.list_bullets.append(bullets)

        for i in range(len(self.list_bullets) - 1, -1, -1):
            self.list_bullets[i].update()
            if self.list_bullets[i].position_y < 0:
                del(self.list_bullets[i])



    def draw(self):
        offset= pyxel.frame_count
        if offset % 2== 0:
            self.image[3]= self.image[3] * -1

        pyxel.blt(self.x, self.y, *self.image)  # prints the image of the player


        for bullet in self.list_bullets:
            bullet.draw()


class Bullets:
    """These are the bullets of the player"""
    def __init__(self, position_x, position_y):
        self.position_x = position_x + 5
        self.position_y = position_y

        self.image=(0, 240, 240, 10, 5, 0)

    def update(self):
        self.position_y = self.position_y - 8

    def draw(self):
        pyxel.blt(self.position_x, self.position_y, *self.image)
