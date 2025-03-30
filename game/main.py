import pygame
from screens.Screen_MainGameVsAI import Screen_MainGameVsAI
from screens.Screen_Home import Screen_Home
from screens.Screen_Winner import Screen_Winner
from constants.constants import *

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic-Tac-Toe Game')

running = True

# screen_home, screen_main_game_vs_ai, screen_winner
current_screen = "screen_main_game_vs_ai"
# player, ai, plauyer_1, player_2
winner = "" 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(white)

    if (current_screen == "screen_main_game_vs_ai"):
        Screen_MainGameVsAI(pygame, screen)
    elif (current_screen == "screen_home"):
        Screen_Home(pygame, screen)
    elif (current_screen == "screen_winner"):
        Screen_Winner(pygame, screen, winner)
    
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()