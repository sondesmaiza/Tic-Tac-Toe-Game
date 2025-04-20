import socketio
import eventlet
from collections import defaultdict

# Create a Socket.IO server
sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

# Store game state and players per room
games = {}  # room_id -> Game instance
players = defaultdict(list)  # room_id -> list of player sids

class Game:
    def __init__(self):
        self.board = ['' for _ in range(9)]
        self.turn = 'X'
        self.winner = None

    def make_move(self, index, symbol):
        if self.board[index] != '' or symbol != self.turn or self.winner:
            return False
        self.board[index] = symbol
        if self.check_winner(symbol):
            self.winner = symbol
        else:
            self.turn = 'O' if self.turn == 'X' else 'X'
        return True

    def check_winner(self, symbol):
        win_combos = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        return any(all(self.board[i] == symbol for i in combo) for combo in win_combos)

    def is_full(self):
        return all(cell != '' for cell in self.board)

@sio.event
def connect(sid, environ):
    print(f"Client connected: {sid}")

@sio.event
def join(sid, data):
    room = data['room']
    sio.enter_room(sid, room)
    players[room].append(sid)

    if room not in games:
        games[room] = Game()

    if len(players[room]) == 1:
        sio.emit('waiting', to=sid)
    elif len(players[room]) == 2:
        # First player gets X, second gets O
        p1, p2 = players[room]
        sio.emit('start', {'symbol': 'X', 'board': games[room].board, 'turn': 'X'}, to=p1)
        sio.emit('start', {'symbol': 'O', 'board': games[room].board, 'turn': 'X'}, to=p2)
    else:
        sio.emit('room_full', to=sid)

@sio.event
def move(sid, data):
    room = data['room']
    index = data['index']
    symbol = data['symbol']
    game = games.get(room)

    if not game:
        return

    if not game.make_move(index, symbol):
        return

    sio.emit('update', {
        'board': game.board,
        'turn': game.turn,
        'winner': game.winner,
        'isDraw': game.is_full() and not game.winner
    }, room=room)

@sio.event
def resetroom(sid, data):
    room = data['room']
    game = games.get(room)

    if not game:
        return

    game.board = ['' for _ in range(9)]
    game.turn = 'X'
    game.winner = None

    sio.emit('update', {
        'board': game.board,
        'turn': game.turn,
        'winner': game.winner,
        'isDraw': game.is_full() and not game.winner
    }, room=room)

@sio.event
def disconnect(sid):
    print(f"Client disconnected: {sid}")
    for room, sids in list(players.items()):
        if sid in sids:
            sids.remove(sid)
            sio.emit('opponent_left', room=room)
            if not sids:
                players.pop(room)
                games.pop(room, None)

if __name__ == '__main__':
    print("Server running on http://localhost:5000")
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)