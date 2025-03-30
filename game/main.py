import pygame
from screens.Screen_MainGameVsAI import Screen_MainGameVsAI
from constants.constants import *

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic-Tac-Toe Game')

running = True

# screen_home, screen_main_game_vs_ai, screen_winner
current_screen = "main_game_vs_ai" 
# player, ai, plauyer_1, player_2
winner = "" 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(white)
    
    Screen_MainGameVsAI(pygame, screen)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()