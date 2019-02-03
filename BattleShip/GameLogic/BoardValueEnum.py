from enum import Enum, auto


class BoardValue(Enum):
    UNOCCUPIED = '-'
    HIT = 'H'
    MISS = 'M'
    CARRIER = 'C'
    BATTLESHIP = 'B'
    DESTROYER = 'D'
    SUBMARINE = 'S'
    PATROL_BOAT = 'P'