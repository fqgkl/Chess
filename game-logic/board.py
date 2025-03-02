class ChessBoard:
    def __init__(self):
        self.board = self.create_initial_board()

    def create_initial_board(self):
        return [
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P"] * 8,
            [" "] * 8,
            [" "] * 8,
            [" "] * 8,
            [" "] * 8,
            ["p"] * 8,
            ["r", "n", "b", "q", "k", "b", "n", "r"]
        ]

    def display(self):
        for row in self.board:
            print(" ".join(row))
        print()
