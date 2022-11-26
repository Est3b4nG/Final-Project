"""
Created by (Esteban Gómez) in  ${2022}
"""

import pyxel

position=[65,110]
def move(x,y):
    if pyxel.btn(pyxel.KEY_RIGHT) and x==137:
        x=x
    elif pyxel.btn(pyxel.KEY_RIGHT):
        x = x + 2
    elif pyxel.btn(pyxel.KEY_LEFT) and x==5:
        x = x
    elif pyxel.btn(pyxel.KEY_LEFT):
        x = x - 2
    elif pyxel.btn(pyxel.KEY_UP) and y==0:
        y = y
    elif pyxel.btn(pyxel.KEY_UP):
        y = y - 2
    elif pyxel.btn(pyxel.KEY_DOWN) and y==140:
        y = y
    elif pyxel.btn(pyxel.KEY_DOWN):
        y = y + 2
    return x,y

def update():
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
    else:
        position[0], position[1] = move(position[0], position[1])

def draw():
    pyxel.cls(0)
    pyxel.blt(position[0], position[1], 0, 0, 0 , 13, 9, colkey=0)
    x= pyxel.frame_count % Width
    y= pyxel.frame_count % Height
    pyxel.blt(x,y, 0, 16, 0 , 13, 9, colkey=0)


Width= 150
Height=150
Caption="Player Aircraft"

pyxel.init(Width, Height, title=Caption)
pyxel.load("assets/resources.pyxres")

pyxel.run(update,draw)
