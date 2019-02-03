from enum import Enum, auto


class TurnResult(Enum):
    MISS = auto()
    HIT = auto()
    DESTROYED = auto()
