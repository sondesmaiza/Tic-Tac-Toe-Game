import random
import json

# Constants
EMPTY = "-"
PLAYER_X = "X"
PLAYER_O = "O"

# Winning combinations on a 3x3 board
WIN_COMBOS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]              # diagonals
]

def check_winner(board):
    """Check if there's a winner or draw."""
    for combo in WIN_COMBOS:
        a, b, c = combo
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    if EMPTY not in board:
        return "draw"
    return None

def available_moves(board):
    """Return list of available move indices."""
    return [i for i, spot in enumerate(board) if spot == EMPTY]

def play_random_game():
    """Simulate a game with random moves."""
    board = [EMPTY] * 9
    moves = []
    current_player = PLAYER_X

    while True:
        move = random.choice(available_moves(board))
        board_before = "".join(board)
        board[move] = current_player

        moves.append({
            "state": board_before,
            "action": move,
            "player": current_player
        })

        result = check_winner(board)
        if result:
            return {
                "moves": moves,
                "result": result
            }

        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

def generate_dataset(num_games=1000, filename="games.json"):
    """Generate unique Tic Tac Toe games and save to JSON."""
    data = []
    seen_games = set()

    print(f"Generating {num_games} unique games...")

    while len(data) < num_games:
        game = play_random_game()
        # Use action sequence as signature to avoid duplicates
        signature = tuple(m["action"] for m in game["moves"])

        if signature not in seen_games:
            seen_games.add(signature)
            data.append(game)

            if len(data) % 100 == 0 or len(data) == num_games:
                print(f"Generated {len(data)} unique games...")

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

    print(f"\n✅ Done! {num_games} games saved to '{filename}'")

# Run the script
if __name__ == "__main__":
    generate_dataset(num_games=1000)

# Tic-Tac-Toe-Game