from BattleShip.GameLogic.BoardValueEnum import BoardValue
import numpy as np


class GameBoard:
    """This is the representation for the game board"""
    def __init__(self):
        # declare a 10 x 10 grid for the game
        self.board = [[BoardValue.UNOCCUPIED for i in range(10)] for j in range(10)]

    def print_board(self):
        print('\n'.join([''.join(['{:4}'.format(item.value) for item in row]) for row in self.board]))


