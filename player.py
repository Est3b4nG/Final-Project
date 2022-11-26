"""
Created by (Esteban Gómez) in  ${2022}
"""

class Player:
    """This class will store all the functions related to the player"""
    def __init__(self, x: int, y: int ,lives: int):
        self.x = x           #position in x, originally we bring this value from the board (width/2)
        self.y = y           #The position in y, this originally is (height-30).
        self.lives = lives   #The lives of our plane


        #The image of the plane is in coordinate 0,0 of the image bank 0, and have dimension of 16x16, the colkey is
        # black. We are going to use this image in the board to draw the players plane, we are only missing the
        # values of the position of the screen that were going to bring in the board.
        self.image = (0, 0, 0, 16, 16, 0)

        #You introduce the number of lives
        self.lives = 3

    # direction is determined by the key they pressed (coded in the board), range is the height or width of the
    # screen (depending on if you're moving in the x-axis or y-axis) this value is also given in the board.
    def move(self, direction:str, range:int):
        """This method will move the plane"""
        plane_x_size= self.image[3]     #it is the dimension (width) of the plane
        plane_y_size= self.image[4]     #It is the dimension (height) of the plane

        #if the position is smaller than the range (width) - the plane dimension in x-axis (if we don't do this,
        # the plane will get out of the screen until it reaches its top left part (from the plane image we imported),
        # this because the left upper prt is the origin point.
        if direction.lower() == "right" and self.x < range - plane_x_size:
            self.x= self.x + 4
        #Here we don't subtract the dimension because we only want to move left until it touches the left part of the
        # image,and the origin point of the image is in the left part
        elif direction.lower() == "left" and self.x > 0:
            self.x = self.x - 4
        #We don't subtrat thr dimension in y because the origin point is in the upper part of the image
        elif direction.lower()== "up" and self.y > 0:
            self.y = self.y - 4
        #We have to subtract the dimension of the plane in order for it to compeltely stay in the screen because,
        # the origin is in the upper part, if we don't put it, the plane will move down until that point get to the
        # total heigth, and the plane will stop appearing in the screen.
        elif direction.lower()=="down" and self.y< range- plane_y_size:
            self.y = self.y + 4




