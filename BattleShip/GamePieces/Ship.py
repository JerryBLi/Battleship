from BattleShip.GamePieces.ShipType import ShipTypeEnum
from BattleShip.GamePieces.ShipType import ShipInformation

class Ship:
    """ This is the base class representation of a ship. This should not be initialized!"""
    def __init__(self, row, col, direction, ship_type):
        if isinstance(ship_type, ShipTypeEnum):
            self.length = ShipInformation.shipLength.get(ship_type)
            self.ship_type = ship_type
            self.row_placed = row
            self.col_placed = col
            self.ship_direction = direction
        else:
            raise(TypeError("ship_type is not recognized"))

