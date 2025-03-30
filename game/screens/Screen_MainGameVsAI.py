from constants.constants import *
from components.BoxTitle import BoxTitle
from components.Background import Background
from components.Field import draw_Field
from components.ExitGame import draw_ExitGame
import random

game = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

turn = "X"

def game_over():
    isGameOver = True
    for i in range(3):
        for j in range(3):
            if game[i][j] == " ":
                isGameOver = False
                break
    if(isGameOver):
        print("Game Over")
    return isGameOver

def AisMove():
    if game_over():
        return
    # AI's move
    global turn
    while True:
        random_i = random.randint(0, 2)
        random_j = random.randint(0, 2)
        if game[random_i][random_j] == " ":
            game[random_i][random_j] = "O"
            turn = "X"
            break
    # If no empty spaces, change turn back


def PlaceMove(i,j):
    not_selected = game[i][j] == " "
    if not_selected:
        if(turn == "X" and not(game_over())):
            game[i][j] = "X"
            AisMove()

    else:
        print("Already selected")



def Screen_MainGameVsAI(pygame,screen):
    Background(pygame, screen)
    BoxTitle(pygame, screen)
    draw_Field(pygame, screen, screen_width,game,PlaceMove) 
    draw_ExitGame(pygame, screen, screen_width)

    