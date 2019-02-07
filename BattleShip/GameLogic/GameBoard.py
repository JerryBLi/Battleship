from BattleShip.GameLogic.BoardValue import BoardValueEnum
from BattleShip.GamePieces.ShipType import ShipDirectionEnum
from BattleShip.GamePieces.ShipType import ShipInformation


class GameBoard:
    MAX_ROW = 11
    MIN_ROW = 1
    MAX_COL = 11
    MIN_COL = 1
    """This is the representation for the game board"""
    def __init__(self):
        # declare a 10 x 10 grid for the game, the extra 1 is to display the coordinates
        self.board = [[BoardValueEnum.UNOCCUPIED for i in range(GameBoard.MAX_ROW)] for j in range(GameBoard.MAX_COL)]
        # Fill the 1st row with numbers
        for i in range(len(self.board) - 1):
            self.board[i + 1][0] = i + 1
        # Fill the 1st column with letters
        for i in range(len(self.board)-1):
            self.board[0][i + 1] = chr(ord('A') + i)
        self.board[0][0] = ''

    def place_ship(self, ship):
        current_row = ship.row_placed
        current_col = ship.col_placed
        # check if the ship can be placed
        for i in range(int(ship.length)):
            if current_col < GameBoard.MIN_COL or current_row < GameBoard.MIN_ROW or \
                    current_row > GameBoard.MAX_ROW - 1 or current_col > GameBoard.MAX_COL - 1 or \
                    self.board[current_row][current_col] != BoardValueEnum.UNOCCUPIED:
                return False
            if ship.ship_direction == ShipDirectionEnum.HORIZONTAL:
                current_col += 1
            else:
                current_row += 1

        # reset column and row
        current_row = ship.row_placed
        current_col = ship.col_placed

        # it can be placed, so place it
        for i in range(int(ship.length)):
            self.board[current_row][current_col] = ShipInformation.boardValue.get(ship.ship_type)
            if ship.ship_direction == ShipDirectionEnum.HORIZONTAL:
                current_col += 1
            else:
                current_row += 1

        return True
