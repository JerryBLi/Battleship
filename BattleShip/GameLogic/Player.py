from BattleShip.GameLogic import GameBoard
from BattleShip.GamePieces.ShipTypeEnum import ShipTypeEnum


class Player:
    """This is the player representation. This will contain the main logic"""

    def __init__(self):
        self.self_map = GameBoard.GameBoard()
        self.enemy_map = GameBoard.GameBoard()

    def populate_board(self):
        """Populate each ship"""
        for ship in ShipTypeEnum:
            # continue while it's not placed
            while True:
                # place ship
                print(ship)
                placed = True
                if placed:
                    break


p = Player()
p.populate_board()