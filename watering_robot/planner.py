import pygame as pg 
import sys 

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption('Pure Pursuit Controller')
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN ):
            sys.exit()
    pg.display.update()