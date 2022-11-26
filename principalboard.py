"""
Created by (Esteban Gómez) in  ${2022}
"""
import pyxel


class Principalboard:
    """This class have all the code related to the main screen before the games starts"""

    def __init__(self, width, height, start_game):

        self.width=width
        self.height=height
        self.start_game=start_game

        pyxel.init(self.width,self.height,title="1942")
        pyxel.load("assets/resources.pyxres")

        pyxel.run(self.update,self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.start_game=True


    def draw(self):
        pyxel.text(118, self.height/2 , "1942" ,pyxel.frame_count%10)
        pyxel.text(self.width / 2 - 60, self.height/2+10, "Choose the number of lives", pyxel.frame_count%10)
        pyxel.text(self.width/2- 60, 245, "Universidad Carlos III, 2022", 4)





#Principalboard(260 , 260, False)