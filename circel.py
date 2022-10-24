
import pygamebg
import pygame as pg
(sirina, visina) = (3000, 3000)
prozor = pygamebg.open_window (sirina, visina, "circeln't")

def invet(a,b,c):
    a,b,c = a,b,c
    a,b,c = abs (255-a), abs (255-b), abs (255-c)
    return(a,b,c)

#program
a = 0
b = 0
prozor.fill((0,0,255))
for i in range (690):
    a = 0
    for i in range (1069):
        pg.draw.ellipse (prozor, (0,0,0), (a,b, 69,69),2)
        a = a + 25
    b = b + 25
    

#kraj programa#

pygamebg.wait_loop ()
