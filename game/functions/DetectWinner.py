
# game_type = "player_vs_ai", "player_vs_player"
# player 1 : X, O
# player 2 : O, X
def DetectWinner(game,game_type,player1,player2,change_screen):
    winner = ""

    if(game[0][0] == game[0][1] == game[0][2] != " "):
        winner = game[0][0]
    elif(game[1][0] == game[1][1] == game[1][2] != " "):
        winner = game[1][0]
    elif(game[2][0] == game[2][1] == game[2][2] != " "):
        winner = game[2][0]
    elif(game[0][0] == game[1][0] == game[2][0] != " "):
        winner = game[0][0]
    elif(game[0][1] == game[1][1] == game[2][1] != " "):
        winner = game[0][1]
    elif(game[0][2] == game[1][2] == game[2][2] != " "):
        winner = game[0][2]
    elif(game[0][0] == game[1][1] == game[2][2] != " "):
        winner = game[0][0]
    elif(game[0][2] == game[1][1] == game[2][0] != " "):
        winner = game[0][2]
    
    if(winner != ""):
        print("Winner is: ", winner)
        change_screen("screen_winner")
        
        
        
    