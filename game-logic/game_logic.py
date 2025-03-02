from board import ChessBoard
from rules import ChessRules

class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.current_turn = "white"

    def make_move(self, move):
        if ChessRules.is_valid_move(self.board, move):
            print(f"Ход {move} выполнен.")
            # Обновить доску (будет добавлено позже)
        else:
            print("Некорректный ход!")

game = ChessGame()
game.board.display()
game.make_move("e2-e4")
