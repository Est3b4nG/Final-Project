"""
Created by (Esteban Gómez) in  ${2022}
"""
import pyxel
import random
import time
import math

class Enemy1:
    #We bring the values of position x and y from the board
    def __init__(self, x:int,y:int, lives:int=1):
        self.x= x    #position of the enemy in x (originally a random number)
        self.y= y    #position of enemy in y (originally, -12)
        self.lives=lives   #Declared here as 1
        self.direction = 1   #Direction, if it is going down or up (we give value=! to represent when it is going down )
        self.list_explosion = []
        #We are importing the image in the position 0,16 of the image bank 0, this image have diemnsion of 16x16 and
        # the colkey is black(0), we will use this vale in the board
        self.image = (0, 224, 240, 16, 16, 0)
        self.puntuation = 0
        self.bullet_list = []


    def update(self, width, height):
        # the position in y will be equal to the movement per frame (2 (velocity in which it is going to move)),
        # and we multiply it by the direction in order to determine if it is going up or down
        self.y += 2 * self.direction    #(-->self.y = self.y + 2 * self.direction) other way of writing it
        if self.y >= (height/2) or self.y < -20:     #Here I'm saying that when the enemy plane reaches the half of the
            # screen the direction will become -1, so up in the general formula instead of adding to frames it will
            # start to subtract two frames (self.y + 2 * (-1) --> self.y - 2)
             self.direction *= -1
        if self.y < -20:
            self.x= random.randint(0,width)
        if self.y >= height / 2:
            enemybullets = Enemies_bullets(self.x, self.y, self.image[3]/2, self.image[4])
            self.bullet_list.append(enemybullets)

        for i in range(len(self.bullet_list) - 1, -1, -1):
            self.bullet_list[i].update(1)
            if self.bullet_list[i].position_y < 0 or self.lives <= 0:
                del(self.bullet_list[i])

        if self.lives <= 0:
            self.puntuation = 1
      #      explosion = Explosion(self.x, self.y)
       #     self.list_explosion.append(explosion)

    def draw(self):
            if self.lives>0:
                pyxel.blt(self.x, self.y, *self.image)
            for bullet in self.bullet_list:
                bullet.draw()
            else:
                for explosion in self.list_explosion:
                    explosion.draw()


class Enemy2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = (1, 1, 58, 11, 20, 0)
        self.lives = 3
        self.angle = 0
        self.change_angle = 7
        self.bullet_list=[]
        self.puntuation = 0
        self.circle = False

    def update(self, width, height):
        possibility= random.randint(1, 100)
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

        if possibility == 20:
            enemybullets = Enemies_bullets(self.x, self.y, self.image[3]/2, self.image[4])
            self.bullet_list.append(enemybullets)
        for i in range(len(self.bullet_list) - 1, -1, -1):
            self.bullet_list[i].update(2)
            if self.bullet_list[i].position_y < 0 or self.lives <= 0:
                del(self.bullet_list[i])

        if self.lives <= 0:
            self.puntuation = 3


    def draw(self):
        pyxel.blt(self.x, self.y, *self.image)
        for bullet in self.bullet_list:
            bullet.draw()


class Bombardier:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.lives = 5
        self.image = (1, 0, 109, 40, 23, 0)
        self.x = width / 2
        self.y = -self.image[4]
        direction = (-1, 0, 1)
        self.bullet_list = []
        self.direction1 = random.choice(direction)
        self.direction2 = random.choice(direction)
        self.direction3 = random.choice(direction)
        self.puntuation = 2

    def update(self, width, height):
        if pyxel.frame_count % 20 == 0:
            enemybullets = Enemies_bullets(self.x, self.y, self.image[3] / 2, self.image[4])
            self.bullet_list.append(enemybullets)
        for i in range(len(self.bullet_list) - 1, -1, -1):
            self.bullet_list[i].update(3)
            if self.bullet_list[i].position_y < 0 or self.lives <= 0:
                del (self.bullet_list[i])

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


    def draw(self):
        if self.lives > 0:
            pyxel.blt(self.x, self.y, *self.image)
        for bullet in self.bullet_list:
            bullet.draw()

class SuperBombardier:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.lives = 100
        self.image = (1, 0, 0, 62, 57, 0)
        self.x = random.uniform(0, self.width / 4)
        self.y= height + self.image[4]
        self.puntuation = 0
        self.bullet_list = []

        self.time_shot_start = time.time()
        self.time_shot_end = time.time()


    def update(self, width, height):
        if self.y > height / 2 - self.image[4]:
            self.x += 0.25
            self.y -= 1
        if self.lives<=0:
            self.puntuation = 5

        self.time_shot_end = time.time()

        if self.y == ((height // 2) - self.image[4]) and pyxel.frame_count % 10 == 0 and \
                int(self.time_shot_end-self.time_shot_start) % 5 == 0:
            for i in range(5):
                enemybullets = Enemies_bullets(self.x, self.y, self.image[3]/2, self.image[4])
                self.bullet_list.append(enemybullets)

        if self.time_shot_end==6:
            self.time_shot_start = 0


        for i in range(len(self.bullet_list) - 1, -1, -1):
            self.bullet_list[i].update(4)
            if self.bullet_list[i].position_y < 0 or self.lives <= 0:
                del(self.bullet_list[i])



    def draw(self):
        if self.lives > 0:
            pyxel.blt(self.x, self.y, *self.image)
        for bullet in self.bullet_list:
            bullet.draw()

class Explosion:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.image= [1, 211, 216, 12, 12, 0]
        self.end_collision= time.time()
    def draw(self):
        if pyxel.frame_count == pyxel.frame_count:
                pyxel.blt(self.position_x, self.position_y, *self.image)



class Enemies_bullets:
    """These are the bullets of the player"""
    def __init__(self, position_x, position_y, appearence_x, apperence_y):
        self.position_x = position_x + appearence_x
        self.position_y = position_y + apperence_y
        self.direction= random.choice([3, 2, 0, -2,-3])

        self.image=(0, 192, 240, 4, 4, 0)

    def update(self, type):
        if type==1:
            self.position_y = self.position_y + 3

        if type==2:
            self.position_y = self.position_y + 3

        if type==3:
            self.position_x += self.direction
            self.position_y += 3

        if type==4:
            self.position_x += self.direction
            self.position_y += 3


    def draw(self):
        pyxel.blt(self.position_x + (self.image[3]), self.position_y + (self.image[4]), *self.image)

