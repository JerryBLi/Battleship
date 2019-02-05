from BattleShip.GameLogic.BoardValue import BoardValueEnum


class GameBoard:
    """This is the representation for the game board"""
    def __init__(self):
        # declare a 10 x 10 grid for the game, the extra 1 is to display the coordinates
        self.board = [[BoardValueEnum.UNOCCUPIED for i in range(11)] for j in range(11)]
        # Fill the 1st row with numbers
        for i in range(len(self.board) - 1):
            self.board[i + 1][0] = i + 1
        # Fill the 1st column with letters
        for i in range(len(self.board)-1):
            self.board[0][i + 1] = chr(ord('A') + i)
        self.board[0][0] = ''

    def init_board(self):
        pass
