class Evaluation:
    """
    Класс Evaluation оценивает позицию на шахматной доске.
    """
    piece_values = {"K": 1000, "Q": 9, "R": 5, "B": 3, "N": 3, "P": 1}

    @staticmethod
    def evaluate(board):
        """
        Оценивает текущее состояние шахматной доски.
        
        :param board: Двумерный список, представляющий доску
        :return: Числовая оценка позиции
        """
        score = 0
        for row in board:
            for piece in row:
                if piece.isupper():
                    score += Evaluation.piece_values.get(piece, 0)
                elif piece.islower():
                    score -= Evaluation.piece_values.get(piece.upper(), 0)
        return score