from minimax import MinimaxAI

class ChessAI:
    def __init__(self, difficulty=10):
        self.engine = MinimaxAI(depth=difficulty)

    def make_best_move(self, board):
        print("ИИ анализирует позицию...")
        # Заглушка: в будущем ИИ предложит ход

ai = ChessAI()
ai.make_best_move(None)  # Пока передаем None вместо доски
