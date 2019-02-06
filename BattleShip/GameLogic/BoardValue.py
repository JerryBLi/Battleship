from enum import Enum, auto


class BoardValueEnum(Enum):
    UNOCCUPIED = '-',
    HIT = 'H',
    MISS = 'M',
    CARRIER = 'C',
    BATTLESHIP = 'B',
    DESTROYER = 'D',
    SUBMARINE = 'S',
    PATROL_BOAT = 'P'


class AttackValueEnum(Enum):
    HIT = auto(),
    MISS = auto(),
    DESTROYED = auto(),
    INVALID = auto(),
    EXISTS = auto()
