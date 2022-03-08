#import essential modules
import pygame as pg
import sys
#initialise pygame modules
pg.init()

#set window size variables
WIDTH = 1280
HEIGHT = 720

#create screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
#define center of screen
screen_center = (
    (WIDTH - screen.get_width())/2,
    (HEIGHT - screen.get_height())/2
)
#set screen background
BG = (25, 250, 170)

#class created to instantiate the Player Character
#needs to be initialised later to be used in the event loop
class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pg.Surface((50, 50))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

#instantiate the player
player = Player()

run = True
#event loop
while run:
    #run through every event in the queue
    for event in pg.event.get():
        #if user clicks X button then exit program
        if event.type == pg.QUIT:
            run = False

    
        screen.fill(BG)

        #draws the surface/"player" on the main screen and positions
        #it in the middle of the screen
        screen.blit(player.surf, (WIDTH/2, HEIGHT/2))

        pg.display.update()
