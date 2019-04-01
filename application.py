#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Saturday, 23 March 2019 at 16:19

@author: Pawel Flajszer

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

