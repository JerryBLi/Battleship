from BattleShip.GamePieces.ShipType import ShipDirectionEnum


class Coordinate:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    @staticmethod
    def parse_coordinate(coordinate):

        if not isinstance(coordinate, str):
            return None

        split_coord = list(coordinate)

        if len(split_coord) != 2:
            return None
        if len(split_coord[0]) != 1:
            return None
        if len(split_coord[1]) != 1:
            return None

        # parse the first value
        row_value = ord(split_coord[0].lower()) - ord('a') + 1
        # parse the second value
        col_value = ord(split_coord[1]) - ord('1') + 1
        # check if within bounds
        if row_value <= 0 or col_value <= 0 or row_value >= 11 or col_value >= 11:
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
