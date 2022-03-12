#import essential modules
from tracemalloc import start
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
    K_SPACE,
)


#initialise pygame modules
pg.init()
#set window icon image
game_icon = pg.image.load("textures/hopper.png")
pg.display.set_icon(game_icon)
#set window title
pg.display.set_caption("HOPPER")
#set window size variables
WIDTH = 1280
HEIGHT = 720
#create screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
#set screen background
BG = pg.image.load("textures/lv1bg.png").convert_alpha()
#create clock "game ticks"
clock = pg.time.Clock()
#set text font
score_font = pg.font.Font(None, 50)
#create reference variable for slime enemy sprite
slime_surf = pg.image.load("textures/enemy-0.png").convert_alpha()
slime_rect = slime_surf.get_rect(midbottom = (1250, 605))

#create reference variable for ground texture
ground_surf = pg.image.load("textures/grass.png").convert_alpha()



#initialize font for fps counter then return current value per game tick
fps_font = pg.font.SysFont("Arial", 18)
def display_fps():
    fps = str(int(clock.get_fps()))
    fps_text = fps_font.render(fps, 1, pg.Color("Coral"))
    return fps_text

def display_score():
    #start time used to reset score on new game
    current_time = pg.time.get_ticks() - start_time
    #round is used to remove the numbers after the decimal place
    score_surf = score_font.render(str("score: " + str(round(current_time/800)) + "m"), 
                                   False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (640, 100))
    screen.blit(score_surf, score_rect)




#class created to instantiate the Player Character
#needs to be initialised later to be used in the event loop
#class inherits "Sprite" function and draws an object on
#screen with the attrivute of "player"
class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        #attribute created for gravity manipulation
        self.gravity = 0
        self.run_frame_2 = pg.image.load("textures/player-frame-1.png").convert_alpha()
        self.run_frame_2= pg.transform.scale(self.run_frame_2, (128, 128))
        self.run_frame_3 = pg.image.load("textures/player-frame-2.png").convert_alpha()
        self.run_frame_3 = pg.transform.scale(self.run_frame_3, (128, 128))
        self.run_anim = [self.run_frame_2, self.run_frame_3]
        self.run_index = 0
        self.jump_frame_1 = pg.image.load("textures/player-jump-0.png").convert_alpha()
        self.jump_frame_1 = pg.transform.scale(self.jump_frame_1, (128, 128))
        self.jump_frame_2 = pg.image.load("textures/player-jump-2.png").convert_alpha()
        self.jump_frame_2 = pg.transform.scale(self.jump_frame_2, (128, 128))
        self.jump_anim = [self.jump_frame_1, self.jump_frame_2]
        self.jump_index = 0
        #created surface for the player
        self.surf = pg.image.load("textures/player-frame-0.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (128, 128))
        #creates rect for player, also useful for collision
        self.rect = self.surf.get_rect(midbottom = (80, 610))


    def player_anims(self):
        global player
        
        #jump animations
        if player.rect.bottom < 600:
            player.surf = player.jump_anim[0]
        
        else:
            player.run_index += 0.05
            if player.run_index >= len(player.run_anim): player.run_index = 0
            player.surf = player.run_anim[int(player.run_index)]

        #run animations



#instantiate the player
player = Player()

#starting conditions
game_active = True
run = True
start_time = 0
#game loop
while run:
    
    clock.tick(60)
    pressed_keys = pg.key.get_pressed()

    #run through every event in the queue / event loop
    for event in pg.event.get():
        #if user clicks X button then exit program
        if event.type == pg.QUIT:
            run = False


        #runs methods if main game state active
        if game_active:
            #check for key down event
            if event.type == KEYDOWN:
                #jump
                if event.key == K_SPACE and player.rect.bottom >= 600:
                    player.gravity = -17
        
        else:
            if event.type == KEYDOWN:
                game_active = True
                slime_rect.left = 1280
                start_time = pg.time.get_ticks()

    if game_active:
        #fill sky
        screen.blit(BG, (0, 0))

        #draw ground
        screen.blit(ground_surf, (0, 600))
        
        #draw slime enemy
        screen.blit(slime_surf, slime_rect)
        
        #logic to "respawn" snail after it leaves screen
        slime_rect.x -= 5
        if slime_rect.right <= -10: slime_rect.x = 1290

        #draw player
        screen.blit(player.surf, player.rect)
        player.player_anims()

        #handle jumping and landing on ground
        player.gravity += 0.62
        player.rect.y += player.gravity
        if player.rect.bottom >= 600: player.rect.bottom = 600

        #check for collision with slime
        if slime_rect.colliderect(player.rect):
            print("hit!")
            game_active = False

        #draw fps
        screen.blit(display_fps(), (10, 10))

        #draw score
        display_score()

    else:
        screen.fill((0, 0, 0))

    
    
    #redraw screen every tick
    pg.display.update()
        
