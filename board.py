"""
Created by (Esteban Gómez) in  ${2022}
"""
import pyxel
import random
from player import Player
from enemies import Enemy1
from background import Clouds

class Board:
    """This class contains all the functions related to the functioning of
    the program"""

    def __init__(self, width, height, start_game):
        """The parameters are the width and height of the screen"""
        self.width=width    #screen width
        self.height=height  #screen height
        self.start_game=start_game  #Which screen it will show, the main screen or the game screen

        #This initialize pyxel
        pyxel.init(self.width, self.height, title="1942")

        #We import the images from the image bank
        pyxel.load("assets/resources.pyxres")

        #To make the maouse appear
        pyxel.mouse(True)

        #Creates the players plane (object) in the  middle of the lower part of the screen, the players have 3 lives
        # This are the values that the player class will take
        self.player = Player(self.width / 2, self.height - 30 ,3)

        appearence_of_cloud= random.randint(0, self.width)
        self.clouds= Clouds(appearence_of_cloud, -50)

        #Create the enemies 1, we are doing a list of these enemies, because we can have more than one at a time
        self.list_enemy1= []
        number_of_enemy1 = random.randint(1, 6)      #Number of enemy one at the same time
        for i in range(number_of_enemy1):       #Create the prevously calculated number of enemies 1
            appearence = random.randint(0, self.width)  #Plave in whcih they appear in x axis
            # The creation of each enemy1 in a random x and same height (-16)
            enemy1 = Enemy1(appearence, -16)
            self.list_enemy1.append(enemy1)       #Append them to the list of enemy 1 that we created

        #Runs the game, always ín the last part of the init
        pyxel.run(self.update,self.draw)


    def update(self):
        """This function  is executed at every frame, it makes the program
        work at every point"""
        if pyxel.btnp(pyxel.KEY_Q):     #to quit the game
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_SPACE):    #If the person press space, the game starts
            self.start_game=True           #Makes the game start
        if self.start_game==True:
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.player.move("right", self.width)       #Direction, maximum range in width or height
            if pyxel.btn(pyxel.KEY_LEFT):
                self.player.move("left",self.width)
            if pyxel.btn(pyxel.KEY_UP):
                self.player.move("up",self.height)
            if pyxel.btn(pyxel.KEY_DOWN):
                self.player.move("down",self.height)

            if self.player.lives > 0: #If the player have more than 0 lives, it will make the enemies 1 move
               self.clouds.move(self.width, self.height, -100)
               for enemy in self.list_enemy1:       #Moves each enemy1
                    enemy.move(self.height, -8)    # the height of the screen, the place of appearence

    def draw(self):
        """This function draw all the elements on the board"""
        pyxel.cls(5)     #Black background

        if self.start_game==False:   #Only appear before the user press "space key"
            pyxel.cls(0)
            pyxel.text(80, self.height / 2, "Press Space to start the game", pyxel.frame_count % 10)

        if self.start_game==True:     #When the game starts (User press space key)
            pyxel.text(10,10, "Actual Score:", 0)      #The actual score
      # pyxel.text(10,20, self.puntuation, 3)
            pyxel.text(self.width/2, 10, "Highest Score:", 0)    #The highest score, that comes from a variable stored
      #  pyxel.text(10, 10, self.highest_puntuation, 3)                                                   in the main
            pyxel.text(10, self.height-10, "Lives:", 0)    #The number of lives



            pyxel.blt(self.clouds.position_x, self.clouds.position_y, *self.clouds.image )

            pyxel.blt(self.player.x, self.player.y, *self.player.image)   #prints the image of the player

            for enemy in self.list_enemy1:              #prints everu enemy1 that we stored in the enemy1 list
                pyxel.blt(enemy.x,enemy.y, *enemy.image)    #positionx, positiony, (way of saying that it need to
                # take every value in the image tuple as one alone)
