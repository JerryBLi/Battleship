from enum import Enum, auto
from BattleShip.GameLogic.BoardValue import BoardValueEnum


class ShipTypeEnum(Enum):
    CARRIER = auto()
    BATTLESHIP = auto()
    DESTROYER = auto()
    SUBMARINE = auto()
    PATROL_BOAT = auto()


class ShipDirectionEnum(Enum):
    VERTICAL = auto()
    HORIZONTAL = auto()


class ShipInformation:
    """Information about each ship including length and display name"""
    shipLength = {
        ShipTypeEnum.CARRIER: 5,
        ShipTypeEnum.BATTLESHIP: 4,
        ShipTypeEnum.DESTROYER: 3,
        ShipTypeEnum.SUBMARINE: 3,
        ShipTypeEnum.PATROL_BOAT: 2
        }

    displayName = {
        ShipTypeEnum.CARRIER: "Carrier",
        ShipTypeEnum.BATTLESHIP: "Battleship",
        ShipTypeEnum.DESTROYER: "Destroyer",
        ShipTypeEnum.SUBMARINE: "Submarine",
        ShipTypeEnum.PATROL_BOAT: "Patrol Boat"
        }

    boardValue = {

        ShipTypeEnum.CARRIER: BoardValueEnum.CARRIER,
        ShipTypeEnum.BATTLESHIP: BoardValueEnum.BATTLESHIP,
        ShipTypeEnum.DESTROYER: BoardValueEnum.DESTROYER,
        ShipTypeEnum.SUBMARINE: BoardValueEnum.SUBMARINE,
        ShipTypeEnum.PATROL_BOAT: BoardValueEnum.PATROL_BOAT
    }
