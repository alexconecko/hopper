#import essential modules
from cgitb import text
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
BG = (135, 206, 235)
#sets game frames per second
FPS = 60
#create clock "game ticks"
clock = pg.time.Clock()
#set text font
score_font = pg.font.Font(None, 50)
player_surf = 
#create reference variable for ground texture
ground_surf = pg.image.load("textures/grass.png")
#create score surface
score_surf = score_font.render("Score", False, (215, 215, 210))


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
        #creates rect for player, also useful for collision
        self.rect = self.surf.get_rect()
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
        screen.blit(ground_surf, (0, 600))
        screen.blit(score_surf, (570, 50))

        pg.display.update()
