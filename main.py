import pygame as pg
import sys
pg.init()

#set window size variables
WIDTH = 1280
HEIGHT = 720

#create screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
BG = (25, 250, 170)


run = True

#event loop
while run:
    for event in pg.event.get():

        if event.type == pg.QUIT:
            run = False

    
        screen.fill(BG)
        pg.display.update()
        