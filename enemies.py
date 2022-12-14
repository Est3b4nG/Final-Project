"""
Created by (Esteban Gómez) in  ${2022}
"""
import pyxel
import random
import time
import math

class Enemy1:
    """This class represents all the code related to the first type of enemy,
    how it moves, the image that appears, the lives that it has, and the
    punctuation that the player wins when he destroys it"""
    #We bring the values of position x and y from the board
    def __init__(self, x:int,y:int, lives:int=1):
        # position of the enemy in x (originally a random number)
        self.x= x
        # position of enemy in y (originally, -12)
        self.y= y
        # Declared here as 1
        self.lives=lives
        # Direction, if it is going down or up (we give value=! to represent when it is going down )
        # We are importing the image in the position 0,16 of the image bank 0, this image have diemnsion of 16x16 and
        # the colkey is black(0), we will use this vale in the board
        self.direction = 1
        #coordinates
        self.image = [0, 224, 240, 16, 16, 0]
        #The future punctuation the player will sum if he destroys the enemy
        self.puntuation = 0
        # We create this list to store the bullet that the enemy will shoot
        self.bullet_list = []


    def update(self, width, height):
        # the position in y will be equal to the movement per frame (2 (velocity in which it is going to move)),
        # and we multiply it by the direction in order to determine if it is going up or down
        # (-->self.y = self.y + 2 * self.direction) other way of writing it
        self.y += 2 * self.direction
        # Here I'm saying that when the enemy plane reaches the half of the
        # screen the direction will become -1, so up in the general formula instead of adding to frames it will
        # start to subtract two frames (self.y + 2 * (-1) --> self.y - 2)
        if self.y >= (height/2) or self.y < -20:
            self.direction *= -1
        if self.direction == 1:
            self.image = [0, 224, 240, 16, 16, 0]
        if self.direction == -1:
            #when the plain changes direction, we change the image
            # simulating it looks upwards
            self.image = [1, 37, 70, 16, 16, 0]


        if self.y < -20:
            #the enemy appears in a random position x
            self.x= random.randint(0,width)

        #when the enemy reaches the middle of the screen, it shoots
        if self.y >= height / 2:
            enemybullets = Enemies_bullets(self.x, self.y, self.image[3]/2, self.image[4])
            self.bullet_list.append(enemybullets)

        # For each bullet in the list, we use the method update that
        # describes the movement they do, when the bullet goes away from the
        # screen, we delete it
        for i in range(len(self.bullet_list) - 1, -1, -1):
            self.bullet_list[i].update(1)
            if self.bullet_list[i].position_y < 0 or self.lives <= 0:
                del(self.bullet_list[i])

        #when the enemy is destroyed, the punctuation changes to 1
        if self.lives <= 0:
            self.puntuation = 1

    def draw(self):
        #prints the plain on the screen if it is alive
            if self.lives>0:
                pyxel.blt(self.x, self.y, *self.image)
            #prints the bullets
            for bullet in self.bullet_list:
                bullet.draw()


class Enemy2:
    """This class represents all the code related to the second type of enemy,
        how it moves, the image that appears, the lives that it has, and the
        punctuation that the player wins when he destroys it"""
    def __init__(self, x, y):
        #position of the enemy
        self.x = x
        self.y = y
        #coordinates in the image bank
        self.image = (1, 1, 58, 11, 20, 0)
        #lives
        self.lives = 1
        #these parameters are used for the movement of the enemy (for the
        # circle )
        self.angle = 0
        self.change_angle = 7
        self.circle = False

        # We create this list to store the bullet that the enemy will shoot
        self.bullet_list=[]
        # The future punctuation the player will sum if he destroys the enemy
        self.puntuation = 0


    def update(self, width, height):
        #this descibes the movement, the plain enters, then does some
        # circles, and then it goes away
        if self.circle == False:
            self.x= self.x + 3
        if self.x >= width/4 and self.angle < 720:
            self.circle = True
        if self.circle == True:
            self.angle += self.change_angle
            self.x += 4 * math.cos(math.radians(self.angle))
            self.y += 4 * math.sin(math.radians(self.angle))
            if self.angle>= 360:
                self.circle=False

        # the possibility to shoot
        possibility = random.randint(1, 100)
        if possibility == 20:
            # when the possibility is reached, the plain shoots
            enemybullets = Enemies_bullets(self.x, self.y, self.image[3]/2, self.image[4])
            self.bullet_list.append(enemybullets)
        # For each bullet in the list, we use the method update that
        # describes the movement they do, when the bullet goes away from the
        # screen, we delete it
        for i in range(len(self.bullet_list) - 1, -1, -1):
            self.bullet_list[i].update(2)
            if self.bullet_list[i].position_y < 0 or self.lives <= 0:
                del(self.bullet_list[i])

        # when the enemy is destroyed, the punctuation changes to 3
        if self.lives <= 0:
            self.puntuation = 3


    def draw(self):
        # prints the plain on the screen if it is alive
        if self.lives>0:
            pyxel.blt(self.x, self.y, *self.image)
        #prints the bullets
        for bullet in self.bullet_list:
            bullet.draw()


class Bombardier:
    """This class represents all the code related to the bombardier,
    how it moves, the image that appears, the lives that it has, and the
    punctuation that the player wins when he destroys it"""
    def __init__(self, width, height):
        #width and height of the screen
        self.width = width
        self.height = height
        #number of lives
        self.lives = 5
        #coordinates of the image bank
        self.image = (1, 0, 109, 40, 23, 0)
        #position
        self.x = width / 2
        self.y = -self.image[4]
        # We create this list to store the bullet that the enemy will shoot
        self.bullet_list = []
        # these are 3 random directions that the plane can have
        direction = (-1, 0, 1)
        self.direction1 = random.choice(direction)
        self.direction2 = random.choice(direction)
        self.direction3 = random.choice(direction)
        #punctuation for the score of the player
        self.puntuation = 2

    def update(self, width, height):
        #every 20 frames the bombardier shoots a bullet
        if pyxel.frame_count % 20 == 0:
            enemybullets = Enemies_bullets(self.x, self.y, self.image[3] / 2, self.image[4])
            self.bullet_list.append(enemybullets)
        # For each bullet in the list, we use the method update that
        # describes the movement they do, when the bullet goes away from the
        # screen, we delete it
        for i in range(len(self.bullet_list) - 1, -1, -1):
            self.bullet_list[i].update(3)
            if self.bullet_list[i].position_y < 0 or self.lives <= 0:
                del (self.bullet_list[i])

        #the enemy changes its direction three times in a random way,
        # that we stored in the init, and a fourth time to go for the left
        # side
        if self.y <= self.height * 0.2:
            self.x += self.direction1
            self.y = self.y + 1
        elif self.y <= self.height * 0.4:
            self.x += self.direction2
            self.y = self.y + 1
        elif self.y <= self.height * 0.6:
            self.x += self.direction3
            self.y = self.y + 1
        else:
            self.x += 2

        #when the enemy is destroyes, the playes score is 5
        if self.lives <= 0:
            self.puntuation = 5

    def draw(self):
        # prints the plain on the screen if it is alive
        if self.lives > 0:
            pyxel.blt(self.x, self.y, *self.image)
        #prints the bullets
        for bullet in self.bullet_list:
            bullet.draw()


class SuperBombardier:
    """This class includes everything related to the Super Bombardier"""
    def __init__(self, width, height):
        """We declare all the variable that we will use for the Super Bombardier"""
        #Width and height of the screen, number of lives, image in the bank
        self.width = width
        self.height = height
        self.lives = 20
        self.image = (1, 0, 0, 70, 57, 0)
        #It can appear in any number in this range
        self.x = random.uniform(0, self.width / 4)
        #Will appear just before it can be seen on the screen
        self.y= height + self.image[4]
        self.puntuation = 0
        #Their list of bullets
        self.bullet_list = []
        #This variable are used to specify how often will the plane shoot
        self.time_shot_start = time.time()
        self.time_shot_end = time.time()


    def update(self, width, height):
        """It has all the code related the movement of the plane"""
        #It moves diagonally
        if self.y > height / 2 - self.image[4]:
            self.x += 0.25
            self.y -= 1
        if self.lives<=0:
            #When it is destroyed it will give this puntuation that will be multiplies by 10 in the board
            self.puntuation = 10

        self.time_shot_end = time.time()

        #It starts shooting when it get to the middle of the screen, and every 5 seconds
        # It creates the bullet of the superbombardier, creates five bullets
        if self.y == ((height // 2) - self.image[4]) and pyxel.frame_count % 10 == 0 and \
                int(self.time_shot_end-self.time_shot_start) % 5 == 0:
            for i in range(5):
                enemybullets = Enemies_bullets(self.x, self.y, self.image[3]/2, self.image[4])
                self.bullet_list.append(enemybullets)

        #if the time since the shot end is greater than 6, it resets to zero the value of the start timer,
        # this for making the superbombardier to shoot again after five seconds.
        if self.time_shot_end == 6:
            self.time_shot_start = 0

        #It deletes the bullet sif they exit the screen
        for i in range(len(self.bullet_list) - 1, -1, -1):
            self.bullet_list[i].update(4)
            if self.bullet_list[i].position_y < 0 or self.lives <= 0:
                del(self.bullet_list[i])



    def draw(self):
        """This function draw the superbombardier and its bullets"""
        #It draws the plane only if it hasn't been destroyed
        if self.lives > 0:
            pyxel.blt(self.x, self.y, *self.image)
        #It draws every bulelt in the list of bullets prevoiusly created
        for bullet in self.bullet_list:
            bullet.draw()


class Explosion:
    def __init__(self, position_x, position_y):
        #positions where the explosion happens
        self.position_x = position_x
        self.position_y = position_y
        #coordinates on the image bank (if the explosion is bigger we change
        # them in the board)
        self.image= [1, 41, 179, 12, 12, 0]
        #moment when the explosion begins
        self.frame_start = pyxel.frame_count
    def draw(self):
        #since the explosion begins, it will be printed until 12 frames pass
        if pyxel.frame_count-self.frame_start < 12:
            pyxel.blt(self.position_x, self.position_y, *self.image)



class Enemies_bullets:
    """These are the bullets of the enemies, their movements and their
    images """
    def __init__(self, position_x, position_y, appearence_x, appearence_y):
        #This avoids the bullets to appear in the left upper corner of the image; it make them appear from the center
        # of the plane
        self.position_x = position_x + appearence_x
        self.position_y = position_y + appearence_y
        #their direction is random
        self.direction= random.choice([3, 2, 0, -2,-3])
        #coordinates on the image bank
        self.image=(0, 192, 240, 4, 4, 0)

    def update(self, type):
        #if the enemy is enemy1 or enemy2, the bullet goes downward
        if type == 1 or type == 2:
            self.position_y = self.position_y + 3

        #if it is a bombardier or a superbombardier, the bullets move in a
        # random direction, diagonal or straight
        if type == 3 or type == 4:
            self.position_x += self.direction
            self.position_y += 3


    def draw(self):
        #prints the bullets
        pyxel.blt(self.position_x + (self.image[3]), self.position_y + (self.image[4]), *self.image)
