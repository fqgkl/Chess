class MinimaxAI:
    def __init__(self, depth=3):
        self.depth = depth

    def minimax(self, board, depth, maximizing):
        if depth == 0:
            return Evaluation.evaluate(board)

        if maximizing:
            max_eval = float("-inf")
            # Логика поиска лучшего хода (заглушка)
            return max_eval
        else:
            min_eval = float("inf")
            # Логика поиска лучшего хода (заглушка)
            return min_eval
