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
BG = (135, 206, 235)
#create clock "game ticks"
clock = pg.time.Clock()
#set text font
score_font = pg.font.Font(None, 50)
#create reference variable for slime enemy sprite
slime_surf = pg.image.load("textures/enemy-0.png").convert_alpha()
slime_surf = pg.transform.scale(slime_surf, (128, 128))
slime_rect = slime_surf.get_rect(bottomright = (1250, 635))
#create reference variable for ground texture
ground_surf = pg.image.load("textures/grass.png").convert_alpha()
#create score surface
score_surf = score_font.render("Score", False, (215, 215, 210))


#initialize font for fps counter then return current value per game tick
fps_font = pg.font.SysFont("Arial", 18)
def display_fps():
    fps = str(int(clock.get_fps()))
    fps_text = fps_font.render(fps, 1, pg.Color("Coral"))
    return fps_text




#class created to instantiate the Player Character
#needs to be initialised later to be used in the event loop
#class inherits "Sprite" function and draws an object on
#screen with the attrivute of "player"
class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        #created surface for the player
        self.surf = pg.image.load("textures/player-frame-0.png")
        self.surf = pg.transform.scale(self.surf, (128, 128))
        #creates rect for player, also useful for collision
        self.rect = self.surf.get_rect(midbottom = (80, 600))
        #used for sprite animation
        self.frame = 0
        



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


        #references keys pressed to a variable then utplayer_surf = pg.image.load("textures/player-frame-0.png")ilises
        #player class update method to move sprite based on values
        #within the methods code block
        pressed_keys = pg.key.get_pressed()


        screen.fill(BG)

    
        screen.blit(ground_surf, (0, 600))
        
        screen.blit(score_surf, (570, 50))
        
        screen.blit(slime_surf, slime_rect)

        screen.blit(player.surf, player.rect)
        screen.blit(display_fps(), (10, 10))

        pg.display.update()
        clock.tick(60)
