import numpy as np
from tensorflow.keras.models import load_model
# Load the trained model once (do this only once to avoid reloading)
import os
model_path = os.path.join(os.path.dirname(__file__), "tictactoe_model.h5")
model = load_model(model_path)


def predict_o_move(game):
    board_string =""

    for i in range(3):
        for j in range(3):
            if(game[i][j]==" "):
                board_string += "-"
            else:
                board_string += game[i][j]
  
    if len(board_string) != 9:
        raise ValueError("Board string must be exactly 9 characters long.")

    
    encoded_board = []
    for cell in board_string:
        if cell == "O":
            encoded_board.append(1)
        elif cell == "X":
            encoded_board.append(-1)
        else:
            encoded_board.append(0)

    encoded_input = np.array(encoded_board).reshape(1, 9)

    # Predict the next move
    predictions = model.predict(encoded_input, verbose=0)[0]

    # Mask illegal moves
    for i, c in enumerate(board_string):
        if c != "-":
            predictions[i] = -1  # ignore taken positions

    # Get the index of the best move
    best_move = int(np.argmax(predictions))
    y = best_move // 3 # 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8
    x = best_move - y * 3 
    return y, x