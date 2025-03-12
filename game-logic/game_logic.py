from board import ChessBoard
from rules import ChessRules

class ChessGame:
    """
    Класс ChessGame управляет логикой шахматной игры.
    """
    def __init__(self):
        """
        Инициализация шахматной игры.
        """
        self.board = ChessBoard()
        self.current_turn = "white"

    def make_move(self, move):
        """
        Обрабатывает ход игрока.
        
        :param move: Ход в шахматной нотации (например, "e2-e4")
        """
        if ChessRules.is_valid_move(self.board, move):
            print(f"Ход {move} выполнен.")
            # Обновить доску (будет добавлено позже)
        else:
            print("Некорректный ход!")