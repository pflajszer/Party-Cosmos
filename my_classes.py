import pygame, random, sys, time
from abc import ABCMeta, abstractmethod



PLAYERLIVES = 3


# Classes:
# =======================================================================================================================

class Screen(object):
    
    def __init__(self, width, height):
        
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screenRect = pygame.Rect((0, 0), (self.width, self.height))

class Sprite(pygame.sprite.Sprite):

    def __init__(self, image, x, y, screen):
    
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.width = image.get_width() 
        self.height = image.get_height() 
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.screen = screen

    def move(self, dx, dy, stayInWindow=False):
        """ 
        Move the sprite. arguments: (x-axis, y-axis, True if want the sprite 
        to stay in window, False otherwise [default value is False.]).
        """
        self.rect.x += dx
        self.rect.y += dy
        if stayInWindow:
            self.rect.clamp_ip(pygame.Rect((0, 0), (1100, 600)))

    def draw(self):
        """ Display the sprite. """
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    @abstractmethod
    def spriteType(self):
        #returns the type of sprite we've created
        pass

class Player(Sprite):
    """ 
    Controlls the player.
    Arguments taken: controlls(player, key-left, key-right, key-down, key-up).
    """
    def __init__(self, image, x, y, screen):
        Sprite.__init__(self, image, x, y, screen)
        self.lives = PLAYERLIVES
        
    def contr(self, k1, k2, k3, k4, vel):
        keys = pygame.key.get_pressed()
        # go left
        if keys[k1]:
            self.move(-vel, 0, True)
        # go right
        if keys[k2]:
            self.move(vel, 0, True)
        # go down
        if keys[k3]:
            self.move(random.choice(range(-2,2)), vel, True)
        # go up
        if keys[k4]:
            self.move(random.choice(range(-2,2)), -vel, True)

    def spriteType(self):
        """ Returns the type of sprite we've created. """
        return 'player'
    

class Enemy(Sprite):

    def spriteType(self):
        """ Returns the type of sprite we've created. """
        #returns the type of sprite we've created
        return 'enemy'


class Background(Sprite):
    
    def spriteType(self):
        """ Returns the type of sprite we've created. """
        return 'background'

class HealthBar(Sprite):
    
    def spriteType(self):
        """ Returns the type of sprite we've created. """
        return 'health bar'


class Sounds(pygame.mixer.Sound):

    def __init__(self, load):
        self.load = load
        self.play = load.play

class Music(object):
    """ Music controlls """
    def __init__(self, load):
        self.load = load                                # —	Load a music file for playback
        self.play = pygame.mixer.music.play             # —	Start the playback of the music stream
        self.rewind = pygame.mixer.music.rewind	        # —	restart music
        self.stop = pygame.mixer.music.stop             # —	stop the music playback
        self.pause = pygame.mixer.music.pause           # —	temporarily stop music playback
        self.unpause = pygame.mixer.music.unpause       # —	resume paused music
        self.fadeout = pygame.mixer.music.fadeout       # —	stop music playback after fading out
        self.set_volume = pygame.mixer.music.set_volume # -	set the music volume
        self.state = 'playing'

class Text(object):
    
    def __init__(self, font, size, screen):
        self.load = pygame.font.SysFont(font, size)
        self.screen = screen
        self.width = 0
        self.height = 0
        
    def displayMsg(self, text, color, xy):
        """ Display the given message. """
        self.render = self.load.render(text, False, color)
        self.width = self.render.get_width()
        self.height = self.render.get_height()
        self.screen.blit(self.render, xy)
    

        
  
class Clock(object):

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.time = time.time()
        self.ticks = pygame.time.get_ticks()