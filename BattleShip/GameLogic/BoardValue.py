from enum import Enum


class BoardValueEnum(Enum):
    UNOCCUPIED = '-'
    HIT = 'H'
    MISS = 'M'
    CARRIER = 'C'
    BATTLESHIP = 'B'
    DESTROYER = 'D'
    SUBMARINE = 'S'
    PATROL_BOAT = 'P'
