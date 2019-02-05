from BattleShip.GameLogic.GameBoard import GameBoard
from BattleShip.GameLogic.Coordinate import Coordinate
from BattleShip.GamePieces.ShipType import ShipTypeEnum
from BattleShip.GamePieces.ShipType import ShipInformation
from BattleShip.GamePieces import Ship


class Player:
    """This is the player representation. This will contain the main logic"""

    def __init__(self):
        self.self_map = GameBoard()
        self.enemy_map = GameBoard()
        self.ships = []

    def populate_board(self):
        """Populate each ship"""
        for ship in ShipTypeEnum:
            # continue while it's not placed
            while True:
                # place ship
                ship_coord = input("Select initial cell (eg 'A3') to place " +
                                   ShipInformation.displayName.get(ship) +
                                   ": ")
                ship_coord = Coordinate.parse_coordinate(ship_coord)

                if ship_coord is None:
                    print("Invalid Coordinated Entered!")
                    continue

                ship_dir = input("Select direction of " +
                                 ShipInformation.displayName.get(ship) +
                                 " (H)orizontal or (V)ertical : ")
                ship_dir = Coordinate.parse_direction(ship_dir)

                if ship_dir is None:
                    print("Invalid Direction Entered!")
                    continue

                self.ships.append(Ship.Ship(ship_coord.row, ship_coord.col, ship_dir, ship))
                
                placed = True
                if placed:
                    break
        for ship in self.ships:

            print("{} placed at ({},{}) in the {} direction".format(ShipInformation.displayName.get(ship.ship_type),
                  ship.row_placed, ship.col_placed, ship.ship_direction))
            print()


p = Player()
p.populate_board()