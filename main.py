# File created by Dominic Grizelj
# gIT GITHUB    
# Build file and folder structures
# Create libraries
# testing github changes
# I changed something - I changed something else tooooo!

# This file was created by: Chris Cozort
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: 

# import libs
import pygame as pg
import random
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

def get_mouse_now():
    x,y = pg.mouse.get_pos()
    return (x,y)

# init pg and create window
pg.init()
# init sound mixer
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My first game...")
clock = pg.time.Clock() 


all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()
player = Player()

enemy1 = Mob(80,80)
enemy2 = Mob(80,80)
enemy3 = Mob(80,80)
enemy4 = Mob(80,80)

all_sprites.add(player)
all_sprites.add(enemy1)
all_sprites.add(enemy2)
all_sprites.add(enemy3)
all_sprites.add(enemy4)

# game loop that run 20 time
for i in range(1,20):
    # instantiates 20 mobs, but stop at 19... randomly between 30-90 height and width
    m = Mob(randint(8,10), randint(8,10))
    # adding it to al sprites group
    all_sprites.add(m)
    # enemies.add(m)

while RUNNING:
    #  keep loop running at the right speed
    clock.tick(FPS)
    ### process input events section of game loop
    for event in pg.event.get():
        # check for window closing
        if event.type == pg.QUIT:
            RUNNING = False
            # break
    # print(get_mouse_now())
    ### update section of game loop (if updates take longer the 1/30th of a second, you will get laaaaag...)
    all_sprites.update()

    blocks_hit_list = pg.sprite.spritecollide(player, enemies, True)
    for block in blocks_hit_list:
        # print(enemies)
        pass
    ### draw and render section of game loop
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # double buffering draws frames for entire screen
    pg.display.flip()
    # pg.display.update() -> only updates a portion of the screen
# ends program when loops evaluates to false
pg.quit()