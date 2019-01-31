from enum import Enum, auto


class BoardValue(Enum):
    UNVISITED = auto()
    HIT = auto()
    MISS = auto()