"""
Created by (Esteban Gómez) in  ${2022}
"""
import pyxel
import random
import time

class Enemy1:
    #We bring the values of position x and y from the board
    def __init__(self, x:int,y:int, lives:int=1):
        self.x= x    #position of the enemy in x (originally a random number)
        self.y= y    #position of enemy in y (originally, -12)
        self.lives=lives   #Declared here as 1
        self.direction = 1   #Direction, if it is going down or up (we give value=! to represent when it is going down )
   #     self.last_x= -10
  #      self.last_y = -10
        self.list_explosion = []
        #We are importing the image in the position 0,16 of the image bank 0, this image have diemnsion of 16x16 and
        # the colkey is black(0), we will use this vale in the board
        self.image = (0, 224, 240, 16, 16, 0)
        self.puntuation = 0
        self.enemy1_bullet_list= []


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
            enemybullets = Enemies_bullets(self.x, self.y)
            self.enemy1_bullet_list.append(enemybullets)

        for i in range(len(self.enemy1_bullet_list) - 1, -1, -1):
            self.enemy1_bullet_list[i].update(1)
            if self.enemy1_bullet_list[i].position_y < 0 or self.lives <= 0:
                del(self.enemy1_bullet_list[i])



        if self.lives <= 0:
            self.puntuation = 1

            last_x= self.x
            last_y = self.y
          #  print(last_x)

            explosion= Explosion(100, 200, self.lives)
            self.list_explosion.append(explosion)

    def draw(self):
            if self.lives>0:
                pyxel.blt(self.x, self.y, *self.image)
           # if self.lives<=0:
            #    for explosion in self.list_explosion:
            #        explosion.draw()
            for bullet in self.enemy1_bullet_list:
                bullet.draw()

class SuperBombardier:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.lives = 100
        self.image = (1, 0, 0, 64, 55, 0)
        self.x = random.uniform(0, self.width / 4)
        self.y= height-8
        self.puntuation = 0
        self.superbombardier_bullet_list=[]

        self.time_shot_start = time.time()
        self.time_shot_end = time.time()


    def update(self, width, height):
        if self.y > height / 2 - self.image[4]:
            self.x += 0.25
            self.y -= 1
        if self.lives<=0:
            self.puntuation = 5

        self.time_shot_end = time.time()
        print(int(self.time_shot_end - self.time_shot_start))
        if self.y == ((height // 2) - self.image[4]) and int(self.time_shot_end-self.time_shot_start) % 5 == 0:
            for bullet in range(5):
                enemybullets = Enemies_bullets(self.x, self.y)
                self.superbombardier_bullet_list.append(enemybullets)
        if self.time_shot_end==6:
            self.time_shot_start = 0



        for i in range(len(self.superbombardier_bullet_list) - 1, -1, -1):
            self.superbombardier_bullet_list[i].update(4)
            if self.superbombardier_bullet_list[i].position_y < 0 or self.lives <= 0:
                del(self.superbombardier_bullet_list[i])



    def draw(self):
        if self.lives > 0:
            pyxel.blt(self.x, self.y, *self.image)
        for bullet in self.superbombardier_bullet_list:
            bullet.draw()


class Explosion:
    def __init__(self, position_x, position_y,lives):
        self.position_x = position_x
        self.position_y = position_y
        self.lives=lives
        self.image= [1, 0, 7, 22, 21, 0]
    def draw(self):
            pyxel.blt(self.position_x, self.position_y, *self.image)



class Enemies_bullets:
    """These are the bullets of the player"""
    def __init__(self, position_x, position_y):
        self.position_x = position_x + 25
        self.position_y = position_y + 15

        self.image=(0, 192, 240, 4, 4, 0)

    def update(self, type):
        if type==1:
            self.position_y = self.position_y + 3

        if type==4:
            self.position_y += 3
            direction= [-3, 0, 3]
            self.position_x= self.position_x + random.choice(direction)

    def draw(self):
        pyxel.blt(self.position_x + (self.image[3]), self.position_y + (self.image[4]), *self.image)


