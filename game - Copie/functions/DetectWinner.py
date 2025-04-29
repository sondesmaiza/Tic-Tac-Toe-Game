
# game_type = "player_vs_ai", "player_vs_player"
# player 1 : X, O
# player 2 : O, X
def DetectWinner(game,game_type,player1,player2,change_screen,to_winner_screen):
    win = ""

    if(game[0][0] == game[0][1] == game[0][2] != " "):
        win = game[0][0]
    elif(game[1][0] == game[1][1] == game[1][2] != " "):
        win = game[1][0]
    elif(game[2][0] == game[2][1] == game[2][2] != " "):
        win = game[2][0]
    elif(game[0][0] == game[1][0] == game[2][0] != " "):
        win = game[0][0]
    elif(game[0][1] == game[1][1] == game[2][1] != " "):
        win = game[0][1]
    elif(game[0][2] == game[1][2] == game[2][2] != " "):
        win = game[0][2]
    elif(game[0][0] == game[1][1] == game[2][2] != " "):
        win = game[0][0]
    elif(game[0][2] == game[1][1] == game[2][0] != " "):
        win = game[0][2]

    final_winner = ""

    
    
    if(win != ""):
        print("Winner is: ", win)
        print(game_type == "player_vs_ai")
        
        if(game_type == "player_vs_ai"):
            if(win == "X"):
                final_winner = "Player X Wins!"
            else:
                final_winner = "AI O Wins!"
        elif(game_type == "player_vs_player"):
            if(win == "X"):
                final_winner = "Player 1 X Wins!"
            else:
                final_winner = "Player 2 O Wins!"
        
        print(final_winner)
        to_winner_screen(final_winner)
        return


        # find if there is a draw
    draw = True
    for i in range(3):
        for j in range(3):
            if game[i][j] == " ":
                draw = False


    if(draw == True):
        print("Draw")
        if(game_type == "player_vs_ai"):
            to_winner_screen("Draw AI vs Player") 
        elif(game_type == "player_vs_player"):
            to_winner_screen("Draw Player 1 vs Player 2")
        return

        
        
        
    