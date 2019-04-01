#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Saturday, 23 March 2019 at 16:19

@author: Pawel Flajszer

Bugs and flaws:
- FPS optimisation. so far doesn't go further than ~25fps. print(FPSCLOCK) to check.
- pause the game and wait till fraction of the second before next level up, unpause, 
       the level goes up, pause again, etc
- Sound on/off toggle
- change lists iteration to group iteration when drawing sprites etc.

Bad design practices:
- from <moduleName> import * (can cause trouble)
- cluttered functions that perhaps could be simpler, and some of them could be class methods

TODO:
- implement more modes and make it a list. then access by "if item not in modes execute ..code".
- ability to shoot enemies
- smoke when accelerating


Game controls:
_______________________________________________________________________

                            General:

M                               - mute the music
P                               - pause the game
TAB                             - toggle tests

Player 1:                       Player 2:
arrow UP                        w               - move up
arrow DOWN                      s               - move down
arrow LEFT                      a               - move left
arrow RIGHT                     d               - move right  

_________________________________________________________________________
"""

# Import modules
import pygame, random, sys
from pygame.locals import *
from my_classes import *
from my_functions import *
from my_constants import *

# Developers controls:

#  value 'immortal' for never-ending game, 'hardcore' to start at level 1000
mode = None

# initialize all pygame modules:
pygame.init()
# screens:
screen = Screen(1100, 600)
state = RUNNING



# ========================================================================================================


if __name__ == '__main__':
    while state == RUNNING:
        main()

