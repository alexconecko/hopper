#import essential modules
import pygame as pg
import sys
#import random for random numbers
import random
import math

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


#initialise pygame modules
pg.init()
#set window title
pg.display.set_caption("untitled rpg")
#set window size variables
WIDTH = 1280
HEIGHT = 720
#create screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
#set screen background
BG = (25, 250, 170)
#sets game frames per second
FPS = 60
#create clock "game ticks"
clock = pg.time.Clock()




#class created to instantiate the Player Character
#needs to be initialised later to be used in the event loop
#class inherits "Sprite" function and draws an object on
#screen with the attrivute of "player"
class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        #created surface for the player
        self.surf = pg.Surface((50, 50))
        self.surf.fill((255, 255, 255))
        self.playerX = 0
        self.playerY = 0
        #creates rect for player, also useful for collision
        self.rect = self.surf.get_rect()
        #movement speed variable
        self.speed = 10
        #used for sprite animation
        self.frame = 0

    #stop player from leaving boundaries    
    def in_bounds(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH;
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT



#instantiate the player
player = Player()


run = True
#event loop
while run:

    clock.tick(60)
    
    #run through every event in the queue
    for event in pg.event.get():
        #if user clicks X button then exit program
        if event.type == pg.QUIT:
            run = False

    
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                print("down")
                player.rect.move_ip(0, 25)

        #references keys pressed to a variable then utilises
        #player class update method to move sprite based on values
        #within the methods code block
        pressed_keys = pg.key.get_pressed()
        #call in bounds method
        player.in_bounds()

        screen.fill(BG)

        #draws the surface/"player" on the main screen and positions
        #it in the middle of the screen
        screen.blit(player.surf, player.rect)

        pg.display.update()
