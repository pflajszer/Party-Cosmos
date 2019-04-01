from application import *
from pygame.locals import *
from my_classes import *
from my_constants import *

import pygame
import random


def draw_sprites(passedEnemies, backgrounds, playerGroup, enemies, num_of_enemies, \
                 enVel, level, bgVel, state, health_bars1, health_bars2, p1, p2):
    """ 
    Draws all the sprites and modifies them
    Wrapper function for:
    - bg_speed_change_and_respawn,
    - mob_reset, 
    - mob_speed_change.
    """
    for bg in backgrounds:
        bg.draw()
    for bg in backgrounds[1:]:
        bg_speed_change_and_respawn(bg, bgVel, level)
    for player in playerGroup:
        if player.alive():
            player.draw()
    for hb1 in health_bars1[0:p1.lives]:
        hb1.draw()
    for hb2 in health_bars2[0:p2.lives]:
        hb2.draw()
    for enemy in enemies[0:num_of_enemies]:
        if mob_reset(enemy, state):
            passedEnemies += 1
        mob_speed_change(enemy, enVel, level)
        enemy.draw()
    return passedEnemies



def mob_reset(enemy, state):
    """ If the enemy passes the bottom of the screen, respawn it to the top."""
    if enemy.rect.y > screen.height and state == RUNNING:
        enemy.rect.x = random.choice(range(0, screen.width))
        enemy.rect.y = random.choice(range(-1000, -50))
        return True
    return False


def mob_speed_change(enemy, enVel, level):
    """ Change the enemy falling speed depending on the level. """
    if level < 6:
        enemy.move(0, enVel)
    elif level >= 6 and level < 20:
        enemy.move(random.choice(range(-2,2)), enVel+3)
    elif level >= 20 and level < 35:
        enemy.move(random.choice(range(-5,5)), enVel+6)
    elif level >= 35 and level < 40:
        enemy.move(random.choice(range(-8,8)), enVel+9)
    else:
        enemy.move(random.choice(range(-12,12)), enVel+12)


def collision_check(playerGroup, enemyGroup, p1, p2, impactSound, screen):
    """ 
    Check for collision of any sprite with any other sprite. 
    Move sprites away from the screen to avoid more collision detection.
    """
    if pygame.sprite.spritecollideany(p1, enemyGroup) and p1.alive():
        p1.lives -= 1
        p1.rect.x = 0
        p1.rect.y = screen.height - p1.height
        impactSound.play()
    if pygame.sprite.spritecollideany(p2, enemyGroup) and p2.alive():
        p2.lives -= 1
        impactSound.play()
        p2.rect.x = 0
        p2.rect.y = screen.height - p1.height
    if pygame.sprite.collide_rect(p1, p2):
        p1.lives -= 1
        p2.lives -= 1
        impactSound.play()
        p1.rect.x = 0
        p1.rect.y = screen.height - p1.height
        p2.rect.x = screen.width
        p2.rect.y = screen.height - p2.height


def bg_speed_change_and_respawn(bg, bgVel, level):
    """
    Change the background scrolling speed depending on the level.
    Last two lines: If the enemy passes the bottom of the screen, respawn it to the top.
    """
    if level < 3:
        bg.move(0, bgVel)
    elif level >= 3 and level < 10:
        bg.move(0, bgVel+3)
    elif level >= 10 and level < 20:
        bg.move(0, bgVel+6)
    elif level >= 20 and level < 25:
        bg.move(0, bgVel+9)
    else:
        bg.move(0, bgVel+12)
    if bg.rect.y > screen.height:
        bg.rect.y = -screen.height-50



def state_check(state, keys, pauseSound, gameOverSound, playerGroup, level, num_of_enemies, gameMusic):
    """ Check the state of the app. Can be RUNNING, PAUSED, or GAMEOVER. """
    for player in playerGroup:
        if player.lives < 1:
            player.kill()
            playerGroup.remove(player)
            del player
    if len(playerGroup) == 0 and state != GAMEOVER:
        gameOverSound.play()
        state = GAMEOVER
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == LVLUP and state == RUNNING:
            level += 1
            num_of_enemies = level * 5
        if event.type == pygame.KEYDOWN and state == NEWGAME:
            if event.key == K_RETURN:
                state = RUNNING
        if event.type == pygame.KEYDOWN and gameMusic.state == 'playing':
            if event.key == K_m:
                gameMusic.pause()
                gameMusic.state = 'paused'
        elif event.type == pygame.KEYDOWN and gameMusic.state == 'paused':
            if event.key == K_m:
                gameMusic.unpause()
                gameMusic.state = 'playing'
        if event.type == pygame.KEYDOWN and state == GAMEOVER:
            if event.key == K_RETURN:
                main()
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit(10)
        if event.type == pygame.KEYDOWN and state == RUNNING:
            if event.key == K_p:
                pauseSound.play()
                state = PAUSED
        elif event.type == pygame.KEYDOWN and state == PAUSED:
            if event.key == K_p:
                pauseSound.play()
                state = RUNNING

    return state, level, num_of_enemies


    #return level, num_of_enemies

def new_game_menu(bg1, newGameTxt, gameOverTxt):
    """ Display game over menu. """
    bg1.draw()
    gameOverTxt.displayMsg('WELCOME', WHITE, ((screen.width // 2) - (gameOverTxt.width // 2), \
                                                (screen.height // 2) - (gameOverTxt.height // 2)))
    newGameTxt.displayMsg('press ENTER to start a new game', WHITE, ((screen.width // 2) - (newGameTxt.width // 2), \
                                                (screen.height // 2) - ((newGameTxt.height // 2) - 50)))


def paused_game_menu(bg1, pauseTxt):
    """ Display pause game menu. """
    bg1.draw()
    pauseTxt.displayMsg('GAME PAUSED', WHITE, ((screen.width // 2) - (pauseTxt.width // 2), \
                                               (screen.height // 2) - (pauseTxt.height // 2)))
                                            


def game_over_menu(bg1, newGameTxt, gameOverTxt, pressEscTxt, gameOverSound):
    """ Display game over menu. """
    bg1.draw()
    gameOverTxt.displayMsg('GAME OVER', WHITE, ((screen.width // 2) - (gameOverTxt.width // 2), \
                                                (screen.height // 2) - (gameOverTxt.height // 2)))
    newGameTxt.displayMsg('press ENTER to go to the main menu', WHITE, (screen.width // 2 - newGameTxt.width // 2, \
                                                screen.height // 2 - newGameTxt.height // 2 + 50))
    pressEscTxt.displayMsg('press ESC to quit the game', WHITE, (screen.width // 2 - pressEscTxt.width // 2, \
                                                screen.height // 2 - pressEscTxt.height // 2 + 100))


def display_stats(stdTxt, passedEnemies, level):
    """ Display user stats. """
    stdTxt.displayMsg(f'passed enemies: {str(passedEnemies)}', WHITE, (15,15))
    stdTxt.displayMsg(f'level: {str(level)}', WHITE, (15,40))


def display_tests(stdTxt, state, timer, FPSCLOCK, num_of_enemies, keys, p1, p2):
    """ When holding "t" button display the test statistics. """
    x = 850
    y = 20
    if keys[K_TAB]:
        stdTxt.displayMsg(f'p1.lives:.............{p1.lives}', WHITE, (x, y+180))
        stdTxt.displayMsg(f'p2.lives:.............{p2.lives}', WHITE, (x, y+150))
        stdTxt.displayMsg(f'state:.............{state}', WHITE, (x, y+120))
        stdTxt.displayMsg(f'ticks:.............{timer.ticks}', WHITE, (x, y+90))
        stdTxt.displayMsg(f'runtime:........{round(timer.time - RUNTIME.time, 2)}', WHITE, (x, y+60))
        stdTxt.displayMsg(f'fps:................{round(FPSCLOCK.get_fps(), 2)}', WHITE, (x, y+30))
        stdTxt.displayMsg(f'enemies........{num_of_enemies}', WHITE, (x, y))



def main():
    """ Main function of the game. """

    # Changing variables:
    # ====================================================================================================



    # Sprites initialisation: 
# ====================================================================================================

    # Background sprites:
    bg1 = Background(pygame.image.load(bgImgList[0]).convert(), 0, 0, screen.screen)
    bg2 = Background(pygame.image.load(bgImgList[1]).convert_alpha(), 0, 0, screen.screen)
    bg3 = Background(pygame.image.load(bgImgList[2]).convert_alpha(), 0, -screen.height, screen.screen)

    # Health bars:
    # left health bar
    healthBar1 = HealthBar(pygame.image.load(healthBarImgList[0]).convert_alpha(), 0, 0, screen.screen)
    healthBar2 = HealthBar(pygame.image.load(healthBarImgList[1]).convert_alpha(), 0, 0, screen.screen)
    healthBar3 = HealthBar(pygame.image.load(healthBarImgList[2]).convert_alpha(), 0, 0, screen.screen)
    # move the health bars to positions
    healthBar1.move(20, screen.height - healthBar1.height - 20)
    healthBar2.move(19 + healthBar2.width, screen.height - healthBar1.height - 20)
    healthBar3.move(19 + healthBar2.width + healthBar3.width, screen.height - healthBar1.height - 20)
    # right health bar
    healthBar4 = HealthBar(pygame.image.load(healthBarImgList[0]).convert_alpha(), 0, 0, screen.screen)
    healthBar5 = HealthBar(pygame.image.load(healthBarImgList[1]).convert_alpha(), 0, 0, screen.screen)
    healthBar6 = HealthBar(pygame.image.load(healthBarImgList[2]).convert_alpha(), 0, 0, screen.screen)
    # move the health bars to positions
    healthBar4.move(screen.width - (healthBar4.width*3) - 20, screen.height - healthBar1.height - 20)
    healthBar5.move(screen.width - (healthBar4.width*2) - 21, screen.height - healthBar1.height - 20)
    healthBar6.move(screen.width - healthBar4.width - 21, screen.height - healthBar1.height - 20)

    # Player sprites:
    p1 = Player(pygame.image.load(playerImgList[0]).convert_alpha(),
            screen.width // 3, screen.height - 100, screen.screen)
    p2 = Player(pygame.image.load(playerImgList[1]).convert_alpha(),
            screen.width - (screen.width // 3), screen.height - 100, screen.screen)

    # Sprite lists
    backgrounds = [bg1, bg2, bg3]
    health_bars1 = [healthBar1, healthBar2, healthBar3]
    health_bars2 = [healthBar4, healthBar5, healthBar6]
    players = [p1, p2]
    enemies = [Enemy(pygame.image.load(random.choice(enemyImgList)).convert_alpha(), 
                random.choice(range(0, screen.width)), random.choice(range(-4000, -50)), 
                screen.screen) for nums in range(0,300)]


    # Sprite groups:
    playerGroup = pygame.sprite.Group()
    enemyGroup = pygame.sprite.Group()

    # Add sprites to groups:
    for player in players:
        player.add(playerGroup)
    for enemy in enemies:
        enemy.add(enemyGroup)


    # sound sprites:
    gameMusic = Music(pygame.mixer.music.load(musicFiles[0]))
    impactSound = Sounds(pygame.mixer.Sound(soundFiles[0]))
    gameOverSound = Sounds(pygame.mixer.Sound(soundFiles[1]))
    pauseSound = Sounds(pygame.mixer.Sound(soundFiles[2]))
    lvlUpSound = Sounds(pygame.mixer.Sound(soundFiles[3]))

    # text sprites:
    stdTxt = Text('Helvetica', 30, screen.screen)
    pauseTxt = Text('Helvetica', 60, screen.screen)
    gameOverTxt = Text('Helvetica', 90, screen.screen)
    newGameTxt = Text('Helvetica', 50, screen.screen)
    pressEscTxt = Text('Helvetica', 50, screen.screen)


    state = NEWGAME                  # initial state of the game
    passedEnemies = 0                # counter of passed enemies
    if mode == 'hardcore':
        level = 500
    else:                            # level number
        level = 1                    
    num_of_enemies = level * 5       # amount of enemies increased every level
    levelUpTime = 10000              # miliseconds between every time level increases

    # Velocities:
    bgVel = 3
    plVel = 10                       
    enVel = 3

    # Main program:
    # ====================================================================================================
    gameMusic.play(5)
    pygame.time.set_timer(LVLUP, levelUpTime)
   
   
    while True:
        # Main loop variable assignments:
        timer = Clock()
        keys = pygame.key.get_pressed()
        state, level, num_of_enemies = state_check(state, keys, pauseSound, gameOverSound, players, level, num_of_enemies, gameMusic)
        
        # Running game code:
        if state == RUNNING:
            passedEnemies = draw_sprites(passedEnemies, backgrounds, playerGroup, enemies, num_of_enemies, 
                                         enVel, level, bgVel, state, health_bars1, health_bars2, p1, p2)
            p1.contr(pygame.K_a, pygame.K_d, pygame.K_s, pygame.K_w, plVel)
            p2.contr(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP, plVel)
            if mode != 'immortal':
                collision_check(playerGroup, enemyGroup, p1, p2, impactSound, screen)
        
        # Paused game code
        if state == PAUSED:
            paused_game_menu(bg1, pauseTxt)
        
        # Game over code
        if state == GAMEOVER:
            game_over_menu(bg1, newGameTxt, gameOverTxt, pressEscTxt, gameOverSound)
        
        if state == NEWGAME:
            new_game_menu(bg1, newGameTxt, gameOverTxt)

        
        # Display stats and test:
        display_stats(stdTxt, passedEnemies, level)
        display_tests(stdTxt, state, timer, FPSCLOCK, num_of_enemies, keys, p1, p2)


        FPSCLOCK.tick(40)
        pygame.display.update()
