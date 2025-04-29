# Tic-Tac-Toe-Game
Here's a complete `README.md` file for your GitHub project, written to explain your Tic-Tac-Toe game structure, setup, and functionality clearly and professionally:

---

````markdown
# 🧠🎮 Tic-Tac-Toe Game with AI and Online Multiplayer

A complete Python-based Tic-Tac-Toe game built using **Pygame**, featuring two gameplay modes:

- **Player vs Player** over sockets (online multiplayer)
- **Player vs AI** using a trained machine learning model

---

## 📦 Installation

To install all necessary dependencies, run:

```bash
pip install numpy
pip install tensorflow
pip install scikit-learn
pip install pygame
pip install python-socketio eventlet
pip install "python-socketio[client]"
```
````

---

## 🗂️ Project Structure

```bash
Tic-Tac-Toe-Game/
│
├── dataset-generator/          # Random game simulator to generate training data
│   ├── dataset-generator.py
│   └── games.json
│
├── design/                     # Game UI assets
│   └── *.jpg
│
├── machine-learning/           # AI model creation and training
│   ├── ai.py
│   ├── game.json
│   └── tictactoe_model.h5
│
├── server/                     # Socket.IO server for multiplayer
│   └── server.py
│
├── game/                       # Main game app built with Pygame
│   ├── components/
│   ├── constants/
│   ├── functions/
│   ├── images/
│   ├── model/
│   ├── screens/
│   ├── main.py
│   └── README.md
```

---

## 🤖 AI Model

The AI opponent is trained using a feedforward neural network built with **TensorFlow** and **Keras**. The dataset is generated using simulated random games.

### Dataset Generation

`dataset-generator/dataset-generator.py` simulates Tic-Tac-Toe games and stores them in a JSON format.

```python
generate_dataset(num_games=1000)  # Simulate 1000 games by default
```

This creates a `games.json` file with board states and optimal moves.

### Model Training

Located in `machine-learning/ai.py`, the training script:

- Loads and encodes the dataset.
- Builds a neural network with two hidden layers.
- Trains the model to predict the next best move based on current board state.
- Evaluates performance with a classification report.
- Saves the trained model as `tictactoe_model.h5`.

---

## 🌐 Multiplayer Server

The `server/server.py` is a **Python Socket.IO** server that handles:

- Room-based player assignment
- Turn-taking and board updates
- Win/draw detection
- Real-time game reset and disconnect handling

To run the server:

```bash
python server/server.py
```

Server runs at: `http://localhost:5000`

---

## 🎮 Game UI (Pygame)

Located in the `game/` directory, the GUI supports:

- A home screen to choose game mode
- Multiplayer game screen
- AI game screen
- Winner display screen

To launch the game:

```bash
cd game
python main.py
```

Screens are modularized under `screens/`, and assets like buttons, background, and game field are found in `components/`.

---

## 🧩 Features

- ✅ Trained AI using simulated games
- ✅ Online multiplayer via sockets
- ✅ Visual interface with Pygame
- ✅ Dataset generation for custom model training
- ✅ Game reset and winner detection

---

## 🛠️ Future Enhancements

- Match history or leaderboard
- Improved AI through reinforcement learning
- Web version using a frontend framework

---

## 📜 License

This project is open-source under the MIT License.

---

## 🙌 Credits

Developed using:

- Python
- Pygame
- TensorFlow / Keras
- Scikit-learn
- Python Socket.IO
