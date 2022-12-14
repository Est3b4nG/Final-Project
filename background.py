"""
Created by (Esteban Gómez) in  ${2022}
"""
import pyxel

class Background:
    """This class stores all related to the background and its movement"""
    #position_x and position_y will be 0,0; the place where the first background will appear
    def __init__(self, position_x, position_y):
        """Describe all the variables used in order for the background to work"""
        self.height = 255
        self.width = 255
        #This position should not change, the background doesn't move in the x-axis
        self.position_x = position_x
        #The position in y of the first image, that will disappear when it reaches the lower part of the screen
        self.position_island_y = position_y
        #The positions in y of the other images that will generate the loop
        self.position_y_list=[]
        self.position_clouds_y=position_y
        #It creates 4 background, each one 100 pyxels upper than the last one
        for image in range(4):
            self.position_clouds_y -= 100
            self.position_y_list.append(self.position_clouds_y)

    def update(self):
        """This function is responsible for the movement of the images of the background"""
        #If the first image hasn't reach the lower part of the screen it will keep moving at a speed of 0,5 pyxels per
        # frame
        if self.position_island_y < self.height:
            self.position_island_y += 0.5
        #for every image, if it hasn't reached the total height of the screen, it will move down, when it reaches it,
        # it will travel to 100 pyxels before the begginning of the screen, and then it will repeat the process
        # (creates infiinite movmeent in the background)
        for i in range(len(self.position_y_list)):
            if self.position_y_list[i] < self.height:
                self.position_y_list[i] += 0.5
            if self.position_y_list[i] >= self.height:
                self.position_y_list[i] = -100

    def draw(self):
        """Draws all the images used for the background"""
        #Draws the first island, but only when it appear on the screen, to avoid wasting resources
        if self.position_island_y < self.height:
            pyxel.blt(self.position_x, self.position_island_y, 2, 0, 0, 255, 255, 0)
        #Draws a segment of clouds multiple times, we needed to do it several times because the image bank had not a
        # lot of space, and we needed to cover the 255 pyxels of hour screen (we reused the same image)
        for i in range(0, len(self.position_y_list)):
            pyxel.blt(self.position_x, self.position_y_list[i], 2, 0, 0, 255, 100, 0)
            #Every three repetitions we draw a different island, that will also move through the screen in the same way
            #This is an extra element, that will appear at a different point in x every time, to simulate that
            # they're different islands
            if i == 3:
                if self.position_y_list[i] <= -100:
                    self.position_x_island2= pyxel.rndi(-50, self.width)
                pyxel.blt(self.position_x_island2, self.position_y_list[i], 0, 0, 0, 210, 100, 0)






