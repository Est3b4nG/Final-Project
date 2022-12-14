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

    def __init__(self, width, height, highest_puntuation):
        """The parameters are the width and height of the screen, and the highest puntuation"""
        # screen width
        self.width=width
        # screen height
        self.height = height
        # Which screen it will show (main screen, game screen, game over screen, or you win screen)
        self.scene = 1
        #If the game itself started (if True, the game starts)
        self.start_game=False
        #Puntuation of the player, starts bieng zero
        self.puntuation= 0
        #Highest puntuation the player has made, changes every time the player makes a higher score
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

        #Creates the background, by creating an object
        self.background= Background(0,0)

        #Creates a list where all the enemies (objects) will be stored
        self.list_enemies=[]
        #Creates a list where all the explosions (objects) will be stored
        self.list_explosions= []

        #Defines if you loose the game, run out of lives
        self.Game_Over = False

        #Create the enemies 1, we are doing a list of these enemies, because we can have more than one at a time
        self.list_enemy1= []
        # Number of enemy 1 that will be generated
        number_of_enemy1 = random.randint(1, 5)
        # Create the prevously calculated number of enemy 1
        for i in range(number_of_enemy1):
            # Place in whcih they appear in x axis
            appearence = random.randint(0, self.width)
            # The creation of each enemy1 in a random x and same height (-16)
            enemy1 = Enemy1(appearence, -16)
            # Append them to the list of enemy 1 that we created
            self.list_enemy1.append(enemy1)
            # Append them as a list to the global list of enemies
        self.list_enemies.append(self.list_enemy1)

        #We repeated the same process as for enemy 1, for each other type of enemy (we only change the place of
        # appearence and the number of them that appear)
        self.list_enemy2=[]
        number_of_enemy2 = random.randint(3, 5)
        appearence= -50
        for i in range(number_of_enemy2):
            appearence -= 10
            enemy2 = Enemy2(0 + appearence, self.height/4)
            self.list_enemy2.append(enemy2)
        self.list_enemies.append(self.list_enemy2)


        self.list_Bombardier = []
        bombardier = Bombardier(self.width, self.height)
        self.list_Bombardier.append(bombardier)
        self.list_enemies.append(self.list_Bombardier)

        #We create an empty list, because we don't want any superbombardier to appear at the beggining of the game
        self.list_SuperBombardier=[]
        self.list_enemies.append(self.list_SuperBombardier)

        #This variable will be used in the collisions algorithm, to avoid losing more than one life when colliding
        # with one enemy
        self.start_time_collision = time.time()

        #Variable used to define when the first enemies will appear
        self.time_of_appearence = time.time()

        #Used to define how often enemies will appear, it starts a frame count when the game starts.
        self.initial_frame = pyxel.frame_count

        #Used to increase the difficulty of the game
        self.difficulty= 0

        #Runs the game, always ín the last part of the init
        pyxel.run(self.update,self.draw)


    def update(self):
        """This function is executed at every frame, it makes the program
        work at every point"""
        # To quit the game
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if self.Game_Over == False:
            #If the person press space it changes the screen
            if self.scene == 1:
                if pyxel.btnp(pyxel.KEY_SPACE):
                    self.scene = 2
            if self.scene == 2:
                #The background starts moving
                self.background.update()
                # If the person press L, the game start
                if pyxel.btnp(pyxel.KEY_L):
                    self.start_game = True
                    #States the time and frame in which the game started
                    self.time_of_appearence = time.time()
                    self.initial_frame= pyxel.frame_count
                if self.start_game == True:
                    #Allows the player to move
                    self.player.update(self.width, self.height)
                    #If five seconds have passed wince the game started, enemies will start to appear
                    if time.time() - self.time_of_appearence > 5:

                        if self.player.lives > 0:

                            #Creates a loopin which each checks some conditions for each enemy (object)
                            for enemies in self.list_enemies:
                                for enemy in enemies:
                                    if enemy.lives >= 0:
                                        #makes the enemies move
                                        enemy.update(self.width,self.height)

                                        #Checks for each bullet of each enemy if they hit the player, if so,
                                        # a life will be subtracted to the player
                                        for bullet in enemy.bullet_list:
                                            if bullet.position_x > self.player.x and bullet.position_x <= self.player.x + \
                                                self.player.image[3] and bullet.position_y > self.player.y and \
                                                bullet.position_y <= self.player.y + self.player.image[4] and \
                                                    self.player.image == [0, 208, 240, 16, 16, 0]:
                                                self.player.lives -= 1
                                                #If they hit they dissapear, and an explosion will be generated
                                                enemy.bullet_list.remove(bullet)
                                                explosion = Explosion(self.player.x, self.player.y)
                                                explosion.image= [1,134, 77, 24, 20,0]
                                                self.list_explosions.append(explosion)

                                    #It checks if the player and the enemy collide, if so it generates and explosion
                                    # and subtract a life to the enemy and to the player
                                    if self.player.x + self.player.image[3] > enemy.x and enemy.x + enemy.image[3] > \
                                            self.player.x and self.player.y + self.player.image[4] > enemy.y and enemy.y + \
                                            enemy.image[4] > self.player.y:
                                                collision = True
                                                self.end_time_collision = time.time()
                                                #In order to avoid that the plaey loses several lives during the
                                                # collision with one enemy
                                                if collision == True:
                                                    if self.end_time_collision - self.start_time_collision > 2.0:
                                                        self.player.lives -= 1
                                                        enemy.lives -= 1
                                                        self.start_time_collision = time.time()
                                                        explosion = Explosion(self.player.x, self.player.y)
                                                        explosion.image = [1, 134, 77, 24, 20, 0]
                                                        self.list_explosions.append(explosion)

                                    #Check if a bullet of the player hits an enemy, it so, it subtracts a life to the
                                    # enemy (and remove the bullet)
                                    for bullet in self.player.list_bullets:
                                        if (bullet.position_x > enemy.x and bullet.position_x < enemy.x + enemy.image[3]) \
                                            and bullet.position_y > enemy.y and bullet.position_y < enemy.y + enemy.image[4]:
                                            enemy.lives -= 1
                                            self.puntuation += enemy.puntuation * 100
                                            self.player.list_bullets.remove(bullet)

                                    #If an enemy is destroyed it will generate an explosion, explosions vary
                                    # depending on the type of enemy that was destroyed
                                    if enemy.lives<=0:
                                        explosion = Explosion(enemy.x, enemy.y)
                                        if type(enemy)==SuperBombardier:
                                            explosion.image= [1,75, 3, 70, 47, 0]
                                        if type(enemy)==Bombardier:
                                            explosion.image=[1, 84, 71,26 ,24,0]
                                        self.list_explosions.append(explosion)
                                        enemies.remove(enemy)

                        #It increase the difficulty
                        if self.initial_frame % 2000 == 0:
                            self.difficulty += 10

                        #These if's describe how often new enemies will be generated, having into account the frame
                        # count and level of difficulty the game is on

                        if (pyxel.frame_count % (60 - self.difficulty)) == 0:
                            enemy1 = Enemy1(random.randint(0,self.width), -16)
                            self.list_enemies[0].append(enemy1)


                        if pyxel.frame_count % (200 - self.difficulty) == 0:
                            appearence_x = -50
                            quantity= pyxel.rndi(2,4)
                            appearence_y = pyxel.rndi(0, self.height//3)
                            for enemy in range (quantity):
                                appearence_x -= 10
                                enemy2 = Enemy2(0 + appearence_x, appearence_y)
                                self.list_enemies[1].append(enemy2)

                        if pyxel.frame_count % (100 - self.difficulty) == 0:
                            bombardier = Bombardier(self.width, self.height)
                            self.list_enemies [2].append(bombardier)

                        if (pyxel.frame_count - self.initial_frame) % 1500 == 0:
                            superbombardier= SuperBombardier(self.width,self.height)
                            self.list_enemies[3].append(superbombardier)

                #If the player loose all the lives we change the screen and clear the list of enemies
                if self.player.lives <= 0:
                    self.scene = 3
                    for list in self.list_enemies:
                        list.clear()
                #If the player reaches the frame_count 10000 he surpass the level, and change to scene 4
                if pyxel.frame_count - self.initial_frame == 10_000:
                    self.scene = 4

        #Here we clear some lists and return some objects to their original position, in order to have the game ready
        # if the player wants to play again
        if self.scene == 3 or self.scene == 4:
            self.Game_Over=True
            self.initial_frame = pyxel.frame_count
            if pyxel.btnp(pyxel.KEY_L):
                self.scene = 1
                self.player.lives = 3
                self.Game_Over = False
                self.start_game = False
                if self.highest_puntuation < self.puntuation:
                    self.highest_puntuation = self.puntuation
                self.puntuation = 0
                self.background = Background(0, 0)
                self.player = Player(self.width / 2, self.height - 30, 3)


    def draw(self):
        """This function draw all the elements on the board"""
        #Draw all the elements of scene 1
        if self.scene == 1:
            pyxel.cls(0)
            pyxel.blt(40, self.height / 3, 1, 0, 192,176,44,0)
            pyxel.text(self.width / 2 - 35, self.height / 2 + 10, "BE THE BEST PILOT", pyxel.frame_count % 10)
            pyxel.text(self.width / 2 - 40, self.height / 2 + 20, "Press Space to start", pyxel.frame_count % 10)
            pyxel.text(self.width / 2 - 60, 245, "Universidad Carlos III, 2022", 4)

        #Draw all the elements of scene 2, including the planes
        if self.scene == 2:
            pyxel.cls(5)
            self.background.draw()
            #If the game hasn't started yet, it shows these sentences, Only appear before the user press "space key"
            if self.start_game == False:
                pyxel.text(80, self.height / 2 -40, "Press L to start the game", pyxel.frame_count % 12)
                pyxel.text(80, self.height / 2 + 20, "Game Controls:", 0)
                pyxel.text(80, self.height / 2 + 40, "Move with the Arrows", 0)
                pyxel.text(80, self.height / 2 + 60, "Press Space Key to Shoot", 0)
                pyxel.text(80, self.height / 2 + 80, "Press Key Z to Avoid bullets", 0)

            # The actual score
            pyxel.text(10,10, "Actual Score:", 0)
            pyxel.text(10,20, str(self.puntuation), 0)

            # The highest score
            pyxel.text(self.width/2, 10, "Highest Score:", 0)
            pyxel.text(self.width/2, 20, str(self.highest_puntuation), 10)

            # The number of lives
            pyxel.text(10, self.height-10, "Lives:", 0)
            pyxel.text(40, self.height - 10, str(self.player.lives), 0)

            # The number of loops
            pyxel.text(60, self.height - 10, "Loops:", 0 )
            pyxel.text(90, self.height - 10, str(self.player.number_loops), 0)

            #Initialize the drawing of the player's plane (describes in the player's class)
            self.player.draw()

            # Draws each enemy created, the drawing is describes in their respective class
            for enemies in self.list_enemies:
                for enemy in enemies:
                    enemy.draw()
            # Draw the explosions, described in the explosions's class
            for explosions in self.list_explosions:
                 explosions.draw()


         #All the drawing that appear in the screen of game over
        if self.scene == 3:
            pyxel.cls(0)
            pyxel.text(self.width / 2 - 20, self.height / 2 - 15, "Game Over", pyxel.frame_count % 10)
            pyxel.text(self.width / 2 - 40, self.height / 2 , "Your puntuation was:", pyxel.frame_count % 10)
            pyxel.text(self.width / 2 - 12, self.height / 2 + 15, str(self.puntuation), pyxel.frame_count % 10)
            pyxel.text(self.width / 2 - 75, self.height / 2 + 30, "Press L to return to the main screen",
                       pyxel.frame_count % 10)

        #All the drawings of the screen that appear when you surpass the level
        if self.scene==4:
            pyxel.cls(0)
            pyxel.text(self.width / 2 - 20, self.height / 2 - 15, "You Won!", pyxel.frame_count % 10)
            pyxel.text(self.width / 2 - 40, self.height / 2, "Your puntuation was:", pyxel.frame_count % 10)
            pyxel.text(self.width / 2 - 12, self.height / 2 + 15, str(self.puntuation), pyxel.frame_count % 10)
