class ChessBoard:
    """
    Класс ChessBoard представляет шахматную доску.
    """
    def __init__(self):
        """
        Инициализация доски с начальными позициями фигур.
        """
        self.board = self.create_initial_board()

    def create_initial_board(self):
        """
        Создает и возвращает начальное расположение фигур на шахматной доске.
        
        :return: Двумерный список с начальными позициями фигур
        """
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
        """
        Выводит шахматную доску в консоль.
        """
        for row in self.board:
            print(" ".join(row))
        print()