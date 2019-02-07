from BattleShip.GamePieces.ShipType import ShipDirectionEnum
from BattleShip.GameLogic.GameBoard import GameBoard
import re


class Coordinate:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    @staticmethod
    def parse_coordinate(coordinate):

        if not isinstance(coordinate, str):
            return None

        x = re.split(r"([a-z]+)([0-9]+)", coordinate, 1, re.I)
        split_coord = list(filter(None, x))

        if len(split_coord) != 2:
            return None
        if len(split_coord[0]) != 1:
            return None
        if len(split_coord[1]) < 1 or len(split_coord[1]) > 2:
            return None

        # parse the first value
        col_value = ord(split_coord[0].lower()) - ord('a') + 1
        # parse the second value
        row_value = int(split_coord[1])
        # check if within bounds
        if row_value < GameBoard.MIN_ROW or col_value < GameBoard.MIN_COL or \
                row_value > GameBoard.MAX_ROW - 1 or col_value > GameBoard.MAX_COL - 1:
            return None
        return Coordinate(row_value, col_value)

    @staticmethod
    def parse_direction(direction):
        if not isinstance(direction, str):
            return None
        if direction.lower() == "vertical" or direction.lower() == "v":
            return ShipDirectionEnum.VERTICAL
        elif direction.lower() == "horizontal" or direction.lower() == "h":
            return ShipDirectionEnum.HORIZONTAL
        else:
            return None
