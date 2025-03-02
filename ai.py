import random

class ChessAI:
    def __init__(self, level=1):
        self.level = level

    def get_best_move(self):
        moves = ["e2e4", "d2d4", "g1f3", "c2c4"]
        return random.choice(moves)

if __name__ == "__main__":
    ai = ChessAI(level=10)
    print(f"AI move: {ai.get_best_move()}")
