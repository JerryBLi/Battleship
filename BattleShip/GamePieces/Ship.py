from BattleShip.GamePieces import ShipTypeEnum


class Ship:
    """ This is the base class representation of a ship. This should not be initialized!"""
    def __init__(self, length, ship_type):
        if isinstance(ship_type, ShipTypeEnum):
            self.length = length
            self.ship_type = ship_type
        else:
            raise(TypeError("ship_type is not recognized"))

