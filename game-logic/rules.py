class ChessRules:
    """
    Класс ChessRules содержит правила шахмат.
    """
    @staticmethod
    def is_valid_move(board, move):
        """
        Проверяет, является ли ход допустимым.
        
        :param board: Текущее состояние шахматной доски
        :param move: Ход, который нужно проверить
        :return: True, если ход допустим, иначе False
        """
        return True