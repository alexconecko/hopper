#import essential modules
import pygame as pg
import sys

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
#set window size variables
WIDTH = 1280
HEIGHT = 720
#create screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
#set screen background
BG = (25, 250, 170)


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

    #move the sprite based on keypresses    
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -15)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 15)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-15, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(15, 0)

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

        #references keys pressed to a variable then utilises
        #player class update method to move sprite based on values
        #within the methods code block
        pressed_keys = pg.key.get_pressed()
        player.update(pressed_keys)

        screen.fill(BG)

        #draws the surface/"player" on the main screen and positions
        #it in the middle of the screen
        screen.blit(player.surf, player.rect)

        pg.display.update()
