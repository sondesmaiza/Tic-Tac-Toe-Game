import json
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load and preprocess the dataset
def load_dataset(filename="games.json"):
    with open(filename, "r") as f:
        games = json.load(f)

    X = []
    y = []

    for game in games:
        for move in game["moves"]:
            state = move["state"]
            action = move["action"]
            player = move["player"]

            # Convert board state to numbers
            # 'X' = 1, 'O' = -1, '-' = 0
            board = []
            for c in state:
                if c == "X":
                    board.append(1 if player == "X" else -1)
                elif c == "O":
                    board.append(1 if player == "O" else -1)
                else:
                    board.append(0)

            X.append(board)
            y.append(action)  # target: the move (0-8)

    X = np.array(X)
    y = to_categorical(y, num_classes=9)  # one-hot encode the action/move
    return X, y

# Build the neural network model
def create_model():
    model = Sequential([
        Dense(64, input_shape=(9,), activation="relu"),
        Dense(64, activation="relu"),
        Dense(9, activation="softmax")  # Output layer: one for each move
    ])
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    return model

# Train and evaluate the model
def train():
    print("🔍 Loading dataset...")
    X, y = load_dataset("games.json")

    # Split into training and testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("🛠️  Building model...")
    model = create_model()
    model.summary()

    print("\n🚀 Training model...")
    model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

    # Evaluate on test set
    print("\n📊 Evaluating model on test data...")
    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
    print(f"\n✅ Final Accuracy: {accuracy * 100:.2f}%")

    # Detailed classification report
    y_pred = model.predict(X_test)
    y_pred_classes = np.argmax(y_pred, axis=1)
    y_true_classes = np.argmax(y_test, axis=1)

    print("\n🧾 Classification Report:")
    print(classification_report(y_true_classes, y_pred_classes))

    # Save model
    model.save("tictactoe_model.h5")
    print("💾 Model saved to 'tictactoe_model.h5'")

if __name__ == "__main__":
    train()