"""
Created by (Esteban Gómez) in  ${2022}
"""
import pyxel
import random
import time
from player import Player
from enemies import Enemy1
from enemies import Enemy2
from enemies import Bombardier
from enemies import SuperBombardier
from enemies import Explosion
from background import Background


class Board:
    """This class contains all the functions related to the functioning of
    the program"""

    def __init__(self, width, height, scene, highest_puntuation):
        """The parameters are the width and height of the screen"""
        self.width=width    #screen width
        self.height = height  #screen height
        self.scene = scene  #Which screen it will show, the main screen or the game screen
        self.start_game=False
        self.puntuation= 0
        self.highest_puntuation=highest_puntuation
        if self.highest_puntuation < self.puntuation:
            self.highest_puntuation = self.puntuation

        #This initialize pyxel
        pyxel.init(self.width, self.height, title="1942")

        #We import the images from the image bank
        pyxel.load("assets/resources.pyxres")

        #Creates the players plane (object) in the  middle of the lower part of the screen, the players have 3 lives
        # This are the values that the player class will take
        self.player = Player(self.width / 2, self.height - 30 ,3)

     #   self.bullets= Bullets(self.player.x, self.player.y)
        self.background= Background(0,0)
        self.list_enemies=[]
        self.list_explosions= []
        self.Game_Over = False
        #Create the enemies 1, we are doing a list of these enemies, because we can have more than one at a time

        self.list_enemy1= []
        number_of_enemy1 = random.randint(1, 10)      #Number of enemy one at the same time
        for i in range(number_of_enemy1):       #Create the prevously calculated number of enemies 1
            appearence = random.randint(0, self.width)  #Plave in whcih they appear in x axis
            # The creation of each enemy1 in a random x and same height (-16)
            enemy1 = Enemy1(appearence, -16)
            self.list_enemy1.append(enemy1)       #Append them to the list of enemy 1 that we created
        self.list_enemies.append(self.list_enemy1)

        self.list_enemy2=[]
        number_of_enemy2 = random.randint(3, 5)
        appearence= -50
        for i in range(number_of_enemy2):
            appearence -= 10
            enemy2 = Enemy2(0 + appearence, self.height/4)
            self.list_enemy2.append(enemy2)
        self.list_enemies.append(self.list_enemy2)


        self.list_SuperBombardier=[]
        #superbombardier= SuperBombardier(self.width,self.height)
        #self.list_SuperBombardier.append(superbombardier)
        self.list_enemies.append(self.list_SuperBombardier)

        self.list_Bombardier = []
        bombardier = Bombardier(self.width, self.height)
        self.list_Bombardier.append(bombardier)
        self.list_enemies.append(self.list_Bombardier)

        self.start_time_collision = time.time()

        self.time_of_appearence = time.time()
        self.initial_frame = pyxel.frame_count
        #Runs the game, always ín the last part of the init
        pyxel.run(self.update,self.draw)



    def update(self):
        """This function  is executed at every frame, it makes the program
        work at every point"""
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()        #To quit the game
        if self.Game_Over == False:
            if self.scene == 1:
                if pyxel.btnp(pyxel.KEY_SPACE):
                    self.scene = 2
            if self.scene == 2:
                self.background.update()
                if pyxel.btnp(pyxel.KEY_L):    #If the person press L, the game starts
                    self.start_game = True           #Makes the game start
                    self.time_of_appearence = time.time()
                    self.initial_frame= pyxel.frame_count
                if self.start_game == True:
                    self.player.update(self.width, self.height)

                    if time.time() - self.time_of_appearence > 5:

                        if self.player.lives > 0: #If the player have more than 0 lives, it will make the enemies 1 move

                            for enemies in self.list_enemies:
                                for enemy in enemies:
                                    if enemy.lives >= 0:
                                        enemy.update(self.width,self.height)    # the height of the screen, the place of appearence

                                        for bullet in enemy.bullet_list:
                                            self.hit_time_end = time.time()
                                            if bullet.position_x > self.player.x and bullet.position_x <= self.player.x + \
                                                self.player.image[3] and bullet.position_y > self.player.y and \
                                                bullet.position_y <= self.player.y + self.player.image[4] and \
                                                    self.player.image == [0, 208, 240, 16, 16, 0]:
                                                self.player.lives -= 1
                                                enemy.bullet_list.remove(bullet)

                                                explosion = Explosion(self.player.x, self.player.y)
                                                explosion.image= [1,134, 77, 24, 20,0]
                                                self.list_explosions.append(explosion)


                                    if self.player.x + self.player.image[3] > enemy.x and enemy.x + enemy.image[3] > \
                                            self.player.x and self.player.y + self.player.image[4] > enemy.y and enemy.y + \
                                            enemy.image[4] > self.player.y:
                                                collision = True
                                                self.end_time_collision = time.time()

                                                if collision == True:

                                                    if self.end_time_collision - self.start_time_collision > 2.0:
                                                        self.player.lives -= 1
                                                        enemy.lives -= 1
                                                        self.start_time_collision = time.time()
                                                        explosion = Explosion(self.player.x, self.player.y)
                                                        explosion.image = [1, 134, 77, 24, 20, 0]
                                                        self.list_explosions.append(explosion)


                                    for bullet in self.player.list_bullets:
                                        if (bullet.position_x > enemy.x and bullet.position_x < enemy.x + enemy.image[3]) \
                                            and bullet.position_y > enemy.y and bullet.position_y < enemy.y + enemy.image[4]:
                                            enemy.lives -= 1
                                            self.puntuation += enemy.puntuation * 100
                                            self.player.list_bullets.remove(bullet)

                                    if enemy.lives<=0:
                                        explosion = Explosion(enemy.x, enemy.y)
                                        if type(enemy)==SuperBombardier:
                                            explosion.image= [1,75, 3, 70, 47, 0]
                                        if type(enemy)==Bombardier:
                                            explosion.image=[1, 84, 71,26 ,24,0]
                                        self.list_explosions.append(explosion)
                                        enemies.remove(enemy)




                        if pyxel.frame_count % 60 == 0:
                            enemy1 = Enemy1(random.randint(0,self.width), -16)
                            self.list_enemies[0].append(enemy1)


                        if pyxel.frame_count % 200 == 0:
                            appearence_x = -50
                            quantity= pyxel.rndi(2,4)
                            appearence_y = pyxel.rndi(0, self.height//3)
                            for enemy in range (quantity):
                                appearence_x -= 10
                                enemy2 = Enemy2(0 + appearence_x, appearence_y)
                                self.list_enemies[1].append(enemy2)

                        if pyxel.frame_count % 100 == 0:
                            bombardier = Bombardier(self.width, self.height)
                            self.list_enemies [2].append(bombardier)

                        if (pyxel.frame_count - self.initial_frame) % 3000 == 0:
                            superbombardier= SuperBombardier(self.width,self.height)
                            self.list_enemies[3].append(superbombardier)


                if self.player.lives <= 0:
                    self.scene = 3
                    for list in self.list_enemies:
                        list.clear()

                if pyxel.frame_count - self.initial_frame == 10_000:
                    self.scene = 4

            print(pyxel.frame_count)

        if self.scene == 3 or self.scene == 4:
            self.Game_Over=True
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.scene = 1
                self.player.lives = 3
                self.Game_Over = False
                if self.highest_puntuation < self.puntuation:
                    self.highest_puntuation = self.puntuation
                self.puntuation = 0
                self.background = Background(0, 0)
                self.player = Player(self.width / 2, self.height - 30, 3)


    def draw(self):
        """This function draw all the elements on the board"""
        if self.scene == 1:
            pyxel.cls(0)
            pyxel.blt(40, self.height / 3, 1, 0, 192,176,44,0)
            pyxel.text(self.width / 2 - 35, self.height / 2 + 10, "BE THE BEST PILOT", pyxel.frame_count % 10)
            pyxel.text(self.width / 2 - 60, 245, "Universidad Carlos III, 2022", 4)

        if self.scene == 2:
            pyxel.cls(5)
            self.background.draw()
            if self.start_game == False:   #Only appear before the user press "space key"
                pyxel.text(80, self.height / 2, "Press L to start the game", pyxel.frame_count % 10)

            pyxel.text(10,10, "Actual Score:", 0)      #The actual score
            pyxel.text(10,20, str(self.puntuation), 0)

            pyxel.text(self.width/2, 10, "Highest Score:", 0)    #The highest score, that comes from a variable stored
            pyxel.text(self.width/2, 20, str(self.highest_puntuation), 10)

            pyxel.text(10, self.height-10, "Lives:", 0)    #The number of lives
            pyxel.text(40, self.height - 10, str(self.player.lives), 0)

            pyxel.text(60, self.height - 10, "Loops:", 0 )  # The number of lives
            pyxel.text(90, self.height - 10, str(self.player.number_loops), 0)


            self.player.draw()


            for enemies in self.list_enemies:              #prints everu enemy1 that we stored in the enemy1 list
                for enemy in enemies:
                    enemy.draw()
            for explosions in self.list_explosions:
                 explosions.draw()



        if self.scene == 3:
            """This draws the message of Game Over"""
            pyxel.cls(0)
            pyxel.text(self.width / 2 - 20, self.height / 2 - 15, "Game Over", pyxel.frame_count % 10)
            pyxel.text(self.width / 2 - 40, self.height / 2 , "Your puntuation was:", pyxel.frame_count % 10)
            pyxel.text(self.width / 2 - 12, self.height / 2 + 15, str(self.puntuation), pyxel.frame_count % 10)

        if self.scene==4:
            pyxel.cls(0)
            pyxel.text(self.width / 2 - 20, self.height / 2 - 15, "You Won!", pyxel.frame_count % 10)
            pyxel.text(self.width / 2 - 40, self.height / 2, "Your puntuation was:", pyxel.frame_count % 10)
            pyxel.text(self.width / 2 - 12, self.height / 2 + 15, str(self.puntuation), pyxel.frame_count % 10)
