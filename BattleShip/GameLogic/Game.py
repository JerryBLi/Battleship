from BattleShip.GameLogic import Player
from BattleShip.GameLogic import BoardValueEnum


class Game:

    def __init__(self):
        self.players = (Player(), Player())

    def game_won(self):
        return False

    def play(self):
        pass
        while not self.game_won():
            pass

    def print_board(self, board):
        """Prints the game board with the coordiantes"""
        print('\n'.join(
            [''.join(['{:<4}'.format(item.value if isinstance(item, BoardValueEnum) else item) for item in row]) for row in
             board]))
