####################################################
####################################################
####################################################
####################################################
####################################################
####################################################
# SOCKET DECLARATION
import socketio
import time
room = 'room1'
sio = socketio.Client()
my_symbol = None
my_turn = False
board = ['' for _ in range(9)]

def resetRoom():
    time.sleep(2)
    sio.emit('resetroom', {
            'room': room,
            })

@sio.event
def connect():
    print("Connected to server")
    sio.emit('join', {'room': room})

@sio.event
def start(data):
    global my_symbol, board, my_turn
    my_symbol = data['symbol']
    board = data['board']
    my_turn = (data['turn'] == my_symbol)
    print(my_symbol, board, my_turn)
    print("Game started. You are", my_symbol)


@sio.event
def update(data):
    global board, my_turn
    board = data['board']
    my_turn = (data['turn'] == my_symbol)

    if data['winner']:
        resetRoom()
        if data['winner'] == my_symbol:
            print("You win!")
        else:
            print("You lose!")
            time.sleep(2)

    elif data['isDraw']:
        resetRoom()
        print("It's a draw.")



@sio.event
def waiting():
    print("Waiting for opponent...")


@sio.event
def room_full():
    print("Room is full")

@sio.event
def opponent_left():
    print("Opponent disconnected")

#sio.connect('http://20.185.226.148')
sio.connect('http://localhost:5000')
####################################################
####################################################
####################################################
####################################################
####################################################
####################################################


from constants.constants import *
from components.BoxTitle import BoxTitle
from components.Background import Background
from components.Field import draw_Field
from components.ExitGame import draw_ExitGame
from functions.DetectWinner import DetectWinner
from model.AI_Move import predict_o_move
import random



turn = "X"

def makeGameFromBoard():
    global board
    local_game = [[" "," "," "],[" "," "," "],[" "," "," "]]
    for i in range(9):
        character =" "
        if(board[i] == ''):
            character = " "
        elif(board[i] == 'X'):
            character = "X"
        elif(board[i] == 'O'):
            character = "O"
        x,y = i%3,i//3
        local_game[y][x] = character
    return local_game


def game_over(game):
    isGameOver = True
    for i in range(3):
        for j in range(3):
            if game[i][j] == " ":
                isGameOver = False
                break
    if(isGameOver):
        print("Game Over")
    return isGameOver


def PlaceMove(i,j,change_screen,to_winner_screen,game):
    global my_symbol, my_turn
    not_selected = game[i][j] == " "
    print("I WILL PLAY" ,i,j, "BUT : ", my_symbol,my_turn)
    if not_selected:
        if(my_turn and not(game_over(game))):
            print("I WILL PLAY",i,j)
            sio.emit('move', {
            'room': room,
            'index': i*3 + j,
            'symbol': my_symbol
            })
            


def Screen_MainGamePlayerVsPlayer(pygame,screen,change_screen,to_winner_screen):
    game = makeGameFromBoard()
    Background(pygame, screen)
    BoxTitle(pygame, screen)
    draw_Field(pygame, screen, screen_width,game,PlaceMove,change_screen,to_winner_screen) 
    draw_ExitGame(pygame, screen, screen_width,change_screen)
    DetectWinner(game, "player_vs_player","X","O",change_screen,to_winner_screen)

    