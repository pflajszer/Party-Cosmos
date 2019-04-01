import pygame
from my_classes import Clock


# Constants:
FPSCLOCK = pygame.time.Clock()   # FPS setup
RUNNING, PAUSED, GAMEOVER, NEWGAME = 'running', 'paused', 'gameover', 'newgame'
RUNTIME = Clock()
LVLUP = pygame.USEREVENT+1
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Sprite image lists:
bgImgList = ['img/bg1.png',
                'img/bg2.png',
                'img/bg3.png']

playerImgList = ['img/player1.png',
                 'img/player2.png']

enemyImgList = ['img/enemy1.png', 
                'img/enemy2.png', 
                'img/enemy3.png']

healthBarImgList = ['img/health_bar1.png',
              'img/health_bar2.png',
              'img/health_bar3.png']

musicFiles = ['sounds/Hooligan.ogg']

soundFiles = ['sounds/hit.ogg',
              'sounds/gameover.ogg',
              'sounds/pause.ogg',
              'sounds/lvlup.ogg']
