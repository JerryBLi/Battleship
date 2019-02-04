from BattleShip.GameLogic.BoardValueEnum import BoardValueEnum
import string
import numpy as np


class GameBoard:
    """This is the representation for the game board"""
    def __init__(self):
        # declare a 10 x 10 grid for the game, the extra 1 is to display the coordinates
        self.board = [[BoardValueEnum.UNOCCUPIED for i in range(11)] for j in range(11)]
        for i in range(len(self.board) - 1):
            self.board[0][i + 1] = chr(ord('A') + i)
        for i in range(len(self.board)-1):
            self.board[i+1][0] = i+1
        self.board[0][0] = ''

    def init_board(self):
        pass

    def print_board(self):
        """Prints the game board with the coordiantes"""
        print('\n'.join([''.join(['{:<4}'.format(item.value if isinstance(item,BoardValueEnum) else item) for item in row]) for row in self.board]))


#x = GameBoard()
#x.print_board()