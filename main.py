
"""
AUHTHOR: KHALED BADRAN
"""

import pygame
import random
import math 
from pygame import mixer

from util.items import *
from util.button import Button


pygame.init()

# Defining some important constants and variables:-
#############################################
(WIDTH, HEIGHT) = (900, 600)
DISPLAY_SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
OFFSET_WIDTH  = WIDTH-70
OFFSET_HEIGHT_UP = 30
OFFSET_HEIGHT_DOWN = HEIGHT-35

BUTTON_COLOR = (4, 30, 66) #Sailor Blue
BUTTON_HOVER_OVER_COLOR = (249, 87, 0) #Orange 
TEXT_COLOR = (249, 87, 0)
BUTTON_TEXT_HOVER_OVER_COLOR = (4, 30, 66)
BUTTON_BORDER_COLOR = (95, 95, 96) #Grey
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
WHITE = (255,255,255)

# to center the x coordinate of buttons:
# x = (width of the display_screen/2) - (the button_width/2)
x_coordinate_of_buttons = WIDTH/2 - BUTTON_WIDTH//2

best_score = 0

icon_img = pygame.image.load("util/images/icon.png")
background_img = pygame.image.load("util/images/background.png")
intro_img = pygame.image.load("util/images/intro.png")
difficulty_img = pygame.image.load("util/images/difficulty.png")
how_to_play_img = pygame.image.load("util/images/how_to_play.png")
sound_img = pygame.image.load("util/images/sound.png")
mute_img = pygame.image.load("util/images/mute.png")
music_img = sound_img

tank_bullet_sound = mixer.Sound("util/sounds/fire.wav")
#############################################

pygame.display.set_icon(icon_img)
pygame.display.set_caption("WARGAME")


def blit_text(txt: str, font_size, pos, color):
    """ to draw a text on the display_screen/display_window.
    Args:
        txt (str): text to be blitted
        font_size (int): size of the font.
        pos ((int,int) tuple): position of the text to be blitted.
        color ((R,G,B) tuple): color of the text
    """
    font = pygame.font.Font("freesansbold.ttf", font_size)
    text = font.render(txt, True, color)
    DISPLAY_SCREEN.blit(text, pos)


def craete_introduction_buttons():
    """ create the PLAY button, QUIT button and how to play button.
    Returns: 
        Tuple: tuple of the created buttons 
    """    
    play_button = Button(BUTTON_COLOR, BUTTON_HOVER_OVER_COLOR, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, TEXT_COLOR, BUTTON_TEXT_HOVER_OVER_COLOR, "PLAY")
    quit_button = Button(BUTTON_COLOR, BUTTON_HOVER_OVER_COLOR, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, TEXT_COLOR, BUTTON_TEXT_HOVER_OVER_COLOR, "QUIT")
    how_button  = Button(BUTTON_COLOR, BUTTON_HOVER_OVER_COLOR, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, TEXT_COLOR, BUTTON_TEXT_HOVER_OVER_COLOR, "how to play")

    #fix the position of the buttons based on their sizes:-
    play_button.x = x_coordinate_of_buttons
    play_button.y = HEIGHT/2 

    quit_button.x = x_coordinate_of_buttons
    quit_button.y = play_button.y+BUTTON_HEIGHT+10

    how_button.x = x_coordinate_of_buttons
    how_button.y = quit_button.y+BUTTON_HEIGHT+10

    return (play_button, quit_button, how_button)


def show_how_to_play():
    """display the game rules and show the player how to play the game.
    """
    back_button   = Button(BUTTON_COLOR, BUTTON_HOVER_OVER_COLOR, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, TEXT_COLOR, BUTTON_TEXT_HOVER_OVER_COLOR, "BACK")
    back_button.x = x_coordinate_of_buttons
    back_button.y = HEIGHT-80
    while True:
        DISPLAY_SCREEN.blit(how_to_play_img, (0, 0))
        back_button.blit(DISPLAY_SCREEN, BUTTON_BORDER_COLOR)
        mouse_position = pygame.mouse.get_pos() # get the position of the mouse

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if back_button.is_clicked(mouse_position, event):
                start_intro()

        if back_button.is_hovered_over(mouse_position):
            back_button.blit_hovered_over(DISPLAY_SCREEN)

        pygame.display.update()


def craete_difficulty_buttons():
    """ create the EASY button, MEDIUM button and the HARD button.
    Returns: 
        Tuple: tuple of the created buttons 
    """    
    easy_button  = Button(BUTTON_COLOR, BUTTON_HOVER_OVER_COLOR, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, TEXT_COLOR, BUTTON_TEXT_HOVER_OVER_COLOR, "EASY")
    medium_button  = Button(BUTTON_COLOR, BUTTON_HOVER_OVER_COLOR, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, TEXT_COLOR, BUTTON_TEXT_HOVER_OVER_COLOR, "MEDIUM")
    hard_button  = Button(BUTTON_COLOR, BUTTON_HOVER_OVER_COLOR, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, TEXT_COLOR, BUTTON_TEXT_HOVER_OVER_COLOR, "HARD")

    #fix the position of the buttons based on their sizes:-
    easy_button.x = x_coordinate_of_buttons
    easy_button.y = HEIGHT/2 

    medium_button.x = x_coordinate_of_buttons
    medium_button.y = easy_button.y+BUTTON_HEIGHT+10

    hard_button.x = x_coordinate_of_buttons
    hard_button.y = medium_button.y+BUTTON_HEIGHT+10

    return (easy_button, medium_button, hard_button)


def select_difficulty():
    """enable the user/player to select the difficulty of the game
    """
    (easy_button, medium_button, hard_button) = craete_difficulty_buttons()
    run = True
    while run:
        DISPLAY_SCREEN.blit(difficulty_img, (0, 0))
        easy_button.blit(DISPLAY_SCREEN, BUTTON_BORDER_COLOR)
        medium_button.blit(DISPLAY_SCREEN, BUTTON_BORDER_COLOR)
        hard_button.blit(DISPLAY_SCREEN, BUTTON_BORDER_COLOR)

        mouse_position = pygame.mouse.get_pos() # get the position of the mouse

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if easy_button.is_clicked(mouse_position, event):
                run = False # to stop running the select_difficulty screen
                start_game("easy")
            if medium_button.is_clicked(mouse_position, event):
                run = False # to stop running the select_difficulty screen
                start_game("medium")
            if hard_button.is_clicked(mouse_position, event):
                run = False # to stop running the select_difficulty screen
                start_game("hard")

        # change the color of the buttons when the player/user hovers over them.
        if easy_button.is_hovered_over(mouse_position):
            easy_button.blit_hovered_over(DISPLAY_SCREEN)
        elif medium_button.is_hovered_over(mouse_position):
            medium_button.blit_hovered_over(DISPLAY_SCREEN)
        elif hard_button.is_hovered_over(mouse_position):
            hard_button.blit_hovered_over(DISPLAY_SCREEN)
        
        pygame.display.update()


def start_intro(txt_list = []):
    """ start the introduction of the game. 
    Args:
        txt_list ([str] list of strings): list of strings to be blitted on the display_screen/display_window. Default = [].
    """
    (play_button, quit_button, how_button) = craete_introduction_buttons()

    run = True
    while run:
        DISPLAY_SCREEN.blit(intro_img, (0, 0))
        play_button.blit(DISPLAY_SCREEN, BUTTON_BORDER_COLOR)
        quit_button.blit(DISPLAY_SCREEN, BUTTON_BORDER_COLOR)
        how_button.blit(DISPLAY_SCREEN, BUTTON_BORDER_COLOR)
        mouse_position = pygame.mouse.get_pos() # get the position of the mouse
        
        if txt_list: # to blit the current score and best score  
            height_for_txt = HEIGHT/3  
            for txt in txt_list:
                blit_text(txt, 25, (WIDTH/2-100, height_for_txt), WHITE)
                height_for_txt += 30  # to make some vertical space between texts 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if play_button.is_clicked(mouse_position, event):
                run = False # to stop running the introductory screen
                select_difficulty()
            if quit_button.is_clicked(mouse_position, event):
                pygame.quit()
            if how_button.is_clicked(mouse_position, event):
                run = False # to stop running the introductory screen
                show_how_to_play()

        # change the color of the buttons when the player/user hovers over them.
        if play_button.is_hovered_over(mouse_position):
            play_button.blit_hovered_over(DISPLAY_SCREEN)
        elif quit_button.is_hovered_over(mouse_position):
            quit_button.blit_hovered_over(DISPLAY_SCREEN)
        elif how_button.is_hovered_over(mouse_position):
            how_button.blit_hovered_over(DISPLAY_SCREEN)
        
        pygame.display.update()
    

def create_enemies(enemy_list, n):
    """fill the enemy_list with enemy soldiers.

    Args:
        enemy_list ([Soldier] list of Soldier): list to be filled with soldiers
        n (int): number of soldiers to be created
    """
    while len(enemy_list) < n:
        rand_x = random.randint(WIDTH-250, OFFSET_WIDTH)
        rand_y = random.randint(OFFSET_HEIGHT_UP, OFFSET_HEIGHT_DOWN)
        enemy_sol_to_add = Soldier(rand_x, rand_y)

        #to ditsribute the enemies in a good way
        enough_free_distance = True
        for enemy_sol in enemy_list:
            if  abs(enemy_sol.x - enemy_sol_to_add.x) < 40 and abs(enemy_sol.y - enemy_sol_to_add.y) < 40: 
                enough_free_distance = False
                break
        if enough_free_distance:
            enemy_list.append(enemy_sol_to_add)


def is_tank_fired(tank, soldiers:[]): 
    """ check whether any bullet from any soldier hits the tank or not. 

    Args:
        tank (Tank): tank represents the player
        soldiers ([Soldier] list of Soldier): list of soldiers

    Returns:
        boolean: True if any bullet from any soldier hits the tank. False otherwise.
    """
    for s in soldiers:
        for bullet in s.fired_bullets:
            # distance distance between two points in 2d-coordinate d =√((x_2-x_1)²+(y_2-y_1)²)
            if math.sqrt( math.pow(tank.x+15-bullet.x,2) + math.pow(tank.y+25-bullet.y, 2) ) < 20:
                s.fired_bullets.remove(bullet)
                return True
    
    return False


def is_soldier_fired(tank_bullets, enemy_soldier):  
    """check whether any bullet from the tank kills/hits any soldier. 

    Args:
        tank_bullets ([TankBullet] list of TankBullet): [description]
        enemy_soldier ([Soldier] list of Soldier): list of enemy soldiers

    Returns:
        boolean: True if any bullet from the tank kills/hits any soldier. False otherwise.
    """
    for bullet in tank_bullets:
        # distance distance between two points in 2d-coordinate d =√((x_2-x_1)²+(y_2-y_1)²)
        if math.sqrt( math.pow(bullet.x-enemy_soldier.x,2) + math.pow(bullet.y-5-enemy_soldier.y, 2) ) < 20:
            return True
    return False


def blit_sound_button(): 
    """display the sound and the mute symbol and check whether the sound should be played or not.

    Returns:
        boolean: True if the sound should be played. False otherwise.
    """
    global music_img

    pygame.draw.rect(DISPLAY_SCREEN, BUTTON_BORDER_COLOR, (WIDTH/2-5, 2, 30, 25))
    DISPLAY_SCREEN.blit(music_img, (WIDTH/2, 3))

    mouse_position = pygame.mouse.get_pos() # get the position of the mouse
    if WIDTH/2-5 < mouse_position[0] < (WIDTH/2-5)+30 and 2 < mouse_position[1] < 2+25:
        pygame.draw.rect(DISPLAY_SCREEN, BUTTON_HOVER_OVER_COLOR, (WIDTH/2-5, 2, 30, 25))
        DISPLAY_SCREEN.blit(music_img, (WIDTH/2, 3))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # if left button of the mouse is clicked
                    if music_img == sound_img:
                        music_img = mute_img
                    else:   
                        music_img = sound_img
                    DISPLAY_SCREEN.blit(music_img, (WIDTH/2, 3))
    return music_img == sound_img
    

def start_game(difficulty):
    """start the wargame 
    """
    tank = Tank(50, HEIGHT//2-80) 
    enemy_soldiers = [] 
    
    if difficulty == "easy":
        n = 10
    elif difficulty == "medium":
        n = 15
    else:
        n = 25
    create_enemies(enemy_soldiers, n)

    tank_y_movement = 0 # the tank can only move upward and downward but not forward and not backward
    current_score = 0
    global best_score # to access the golbal variable best_score
      
    while True:
        DISPLAY_SCREEN.blit(background_img, (0, 0))
        #draw the borders of the playing field.
        pygame.draw.line(DISPLAY_SCREEN, (100,0,0), (200,OFFSET_HEIGHT_UP), (200,HEIGHT), 3) # vertical line
        pygame.draw.line(DISPLAY_SCREEN, (100,0,0), (0,OFFSET_HEIGHT_UP), (WIDTH,OFFSET_HEIGHT_UP), 3) #horizontal line
        #display the health of the tank and the score.
        blit_text("score: " + str(current_score), 25,  (WIDTH/2+100, 0), (255,255,255))
        blit_text("health: " + str(tank.health), 25, (WIDTH/2-200, 0), (255,255,255))
        blit_sound_button()
        #DISPLAY_SCREEN.blit(sound_img, (WIDTH/2, 0))


        tank_bullet = TankBullet(tank.x+62, tank.y+7) #The bullet of the tank should be shooted from the muzzle. That is why: tank.x+62 and tank.y+7.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: #to move the tank upward
                    tank_y_movement = -0.5
                elif event.key == pygame.K_DOWN: #to move the tank downward
                    tank_y_movement = +0.5
                elif event.key == pygame.K_s: #to stop the tank from moving
                    tank_y_movement = 0
                if event.key == pygame.K_SPACE and len(tank.fired_bullets) < tank.max_bullets: # to fire
                    tank.fired_bullets.append(tank_bullet)
                    if blit_sound_button():
                        tank_bullet_sound.play()

        DISPLAY_SCREEN.blit(tank.img, (tank.x, tank.y))
        if len(tank.fired_bullets) > 0:
            for bullet in tank.fired_bullets:
                DISPLAY_SCREEN.blit(bullet.img,(bullet.x, bullet.y))
                if bullet.x < OFFSET_WIDTH:
                    bullet.x += 3
                else: #remove the bullet from fired_bullets list if it passes the screen borders 
                    tank.fired_bullets.remove(bullet)

        if is_tank_fired(tank,enemy_soldiers):# if the tank is fired, decrease the health by 1.
            tank.health -= 1

        for enemy_sol in enemy_soldiers:
            DISPLAY_SCREEN.blit(enemy_sol.img, (enemy_sol.x, enemy_sol.y)) #blit soldiers
            if len(enemy_sol.fired_bullets) < enemy_sol.max_bullets:
                soldier_bullet = SoldierBullet(enemy_sol.x-10, enemy_sol.y+3) #The bullet should be shooted from the muzzle. That is why: enemy_sol.x-10 and enemy_sol.y+3.
                enemy_sol.fired_bullets.append(soldier_bullet)

            for bullet in enemy_sol.fired_bullets:
                if bullet.x > 0:
                    bullet.x -= 1.3
                    DISPLAY_SCREEN.blit(bullet.img, (bullet.x, bullet.y))
                else:
                    enemy_sol.fired_bullets.clear()

            if enemy_sol.x > 200:
                enemy_sol.x -= 0.3
                if is_soldier_fired(tank.fired_bullets, enemy_sol): # if soldier is killed, increase the score by 1 and create a new soldier.
                    enemy_soldiers.remove(enemy_sol)
                    current_score += 1
                    create_enemies(enemy_soldiers, n)
            else:
                enemy_soldiers.remove(enemy_sol)
                create_enemies(enemy_soldiers, n)
        
        if current_score > best_score:
            best_score = current_score

        if tank.health == 0:
            txt_list = [] #list of strings to be displayed on the introduction screen.
            txt_list.append("current score: " + str(current_score))
            txt_list.append("best score: " +  str(best_score))
            start_intro(txt_list)
            
        # check bounds for tank and move it
        if OFFSET_HEIGHT_UP < tank.y + tank_y_movement and  tank.y + tank_y_movement < OFFSET_HEIGHT_DOWN-15:
            tank.y += tank_y_movement
        else:
            tank_y_movement = 0

        pygame.display.update()


def main():
    """ start the introduction of the game
    """
    start_intro()


if __name__ == "__main__":  #to avoid runing the game, if this file is imported
    main()
