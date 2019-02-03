from BattleShip.GameLogic import GameBoard


class Player:
    """This is the player representation. This will contain the main logic"""

    def __init__(self):
        self.self_map = GameBoard()
        self.enemy_map = GameBoard()

    def populate_board(self):
        pass

