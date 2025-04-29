import pygame
from screens.Screen_MainGameVsAI import Screen_MainGameVsAI
from screens.Screen_MainGamePlayerVsPlayer import Screen_MainGamePlayerVsPlayer
from screens.Screen_Home import Screen_Home
from screens.Screen_Winner import Screen_Winner
from constants.constants import *

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic-Tac-Toe Game')

running = True

# screen_home, screen_main_game_vs_ai, screen_winner
current_screen = "screen_home"
# player, ai, plauyer_1, player_2
winner = ""

game = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def change_screen(new_screen):
    global current_screen
    current_screen = new_screen
    pygame.time.delay(500)

def to_winner_screen(new_winner):
    global winner
    global current_screen
    winner = new_winner
    current_screen = "screen_winner"
    pygame.time.delay(500)

def reset_game():
    global winner
    winner = ""
    global game
    game = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    change_screen("screen_home")



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(white)

    if (current_screen == "screen_main_game_vs_ai"):
        Screen_MainGameVsAI(pygame, screen,game,change_screen,to_winner_screen)
    elif (current_screen == "screen_main_game_player_vs_player"):
        Screen_MainGamePlayerVsPlayer(pygame, screen,change_screen,to_winner_screen)
    elif (current_screen == "screen_home"):
        Screen_Home(pygame, screen,change_screen)
    elif (current_screen == "screen_winner"):
        Screen_Winner(pygame, screen, winner,reset_game)
    
    
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()