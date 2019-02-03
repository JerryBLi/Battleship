from enum import Enum, auto


class ShipType(Enum):
    CARRIER = auto()
    BATTLESHIP = auto()
    DESTROYER = auto()
    SUBMARINE = auto()
    PATROL_BOAT = auto()

