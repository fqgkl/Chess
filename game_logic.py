class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()

    def initialize_board(self):
        return [
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P"] * 8,
            [" "] * 8,
            [" "] * 8,
            [" "] * 8,
            [" "] * 8,
            ["p"] * 8,
            ["r", "n", "b", "q", "k", "b", "n", "r"],
        ]

    def make_move(self, move):
        print(f"Move: {move}")

if __name__ == "__main__":
    game = ChessGame()
    game.make_move("e2e4")
