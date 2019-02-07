from BattleShip.GameLogic.GameBoard import GameBoard
from BattleShip.GameLogic.Coordinate import Coordinate
from BattleShip.GamePieces.ShipType import ShipTypeEnum
from BattleShip.GamePieces.ShipType import ShipInformation
from BattleShip.GamePieces.ShipType import ShipDirectionEnum
from BattleShip.GamePieces import Ship
from BattleShip.GameLogic.BoardValue import BoardValueEnum
from BattleShip.GameLogic.BoardValue import AttackValueEnum
import random


class Player:
    """This is the player representation. This will contain the main logic"""

    def __init__(self, is_human):
        self.self_map = GameBoard()
        self.enemy_map = GameBoard()
        self.ships = {}
        self.player_health = 0
        self.is_human = is_human

    def populate_board(self):
        """Populate each ship"""
        for ship in ShipTypeEnum:
            # continue while it's not placed
            while True:
                # get start position of ship
                ship_coord = input("Select initial cell (eg 'A3') to place " +
                                   ShipInformation.displayName.get(ship) +
                                   ": ")
                ship_coord = Coordinate.parse_coordinate(ship_coord)
                # check if valid start position
                if ship_coord is None:
                    print("Invalid Coordinated Entered!")
                    continue
                # get ship direction
                ship_dir = input("Select direction of " +
                                 ShipInformation.displayName.get(ship) +
                                 " (H)orizontal or (V)ertical : ")
                ship_dir = Coordinate.parse_direction(ship_dir)
                # check if valid direction
                if ship_dir is None:
                    print("Invalid Direction Entered!")
                    continue

                # We have the ship's start position and direction, create a new ship
                # and try to place it
                new_ship = Ship.Ship(ship_coord.row, ship_coord.col, ship_dir, ship)

                # place the ship. If successful, it'll return true
                if not self.self_map.place_ship(new_ship):
                    print("Cannot place ship in that location!")
                    continue

                # add our ship to the dictionary
                self.ships[ship] = new_ship

                # add ship length value to player health
                self.player_health += int(ShipInformation.shipLength.get(ship))

                # end the loop, the ship has been placed successfully
                placed = True
                if placed:
                    break

    def auto_populate_board(self):
        ship_directions = (ShipDirectionEnum.VERTICAL, ShipDirectionEnum.HORIZONTAL)
        for ship in ShipTypeEnum:
            while True:
                ship_row = random.randint(GameBoard.MIN_ROW, GameBoard.MAX_ROW)
                ship_col = random.randint(GameBoard.MIN_COL, GameBoard.MAX_COL)
                ship_coord = Coordinate(ship_row, ship_col)
                ship_dir = ship_directions[random.randint(0,1)]
                new_ship = Ship.Ship(ship_coord.row, ship_coord.col, ship_dir, ship)

                if not self.self_map.place_ship(new_ship):
                    continue
                self.ships[ship] = new_ship

                # add ship length value to player health
                self.player_health += int(ShipInformation.shipLength.get(ship))

                # end the loop, the ship has been placed successfully
                placed = True
                if placed:
                    break

    def update_enemy_map(self, coordinate, value):
        if isinstance(coordinate, Coordinate) and isinstance(value, BoardValueEnum):
            self.enemy_map.board[coordinate.row][coordinate.col] = value

    def attack(self, coordinate):
        """Handle enemy attack"""
        # Update self_map
        # update health of ship if hit
        # return value
        if isinstance(coordinate, Coordinate):
            # current ship reference if it's a ship
            if self.self_map.board[coordinate.row][coordinate.col] == BoardValueEnum.UNOCCUPIED:
                self.self_map.board[coordinate.row][coordinate.col] = BoardValueEnum.MISS
                return AttackValueEnum.MISS, ''
            elif self.self_map.board[coordinate.row][coordinate.col] == BoardValueEnum.HIT:
                return AttackValueEnum.EXISTS, ''
            elif self.self_map.board[coordinate.row][coordinate.col] == BoardValueEnum.MISS:
                return AttackValueEnum.EXISTS, ''
            elif self.self_map.board[coordinate.row][coordinate.col] == BoardValueEnum.CARRIER:
                ship = self.ships[ShipTypeEnum.CARRIER]
            elif self.self_map.board[coordinate.row][coordinate.col] == BoardValueEnum.BATTLESHIP:
                ship = self.ships[ShipTypeEnum.BATTLESHIP]
            elif self.self_map.board[coordinate.row][coordinate.col] == BoardValueEnum.DESTROYER:
                ship = self.ships[ShipTypeEnum.DESTROYER]
            elif self.self_map.board[coordinate.row][coordinate.col] == BoardValueEnum.SUBMARINE:
                ship = self.ships[ShipTypeEnum.SUBMARINE]
            elif self.self_map.board[coordinate.row][coordinate.col] == BoardValueEnum.PATROL_BOAT:
                ship = self.ships[ShipTypeEnum.PATROL_BOAT]
            else:
                return AttackValueEnum.INVALID, ''

            # A ship is hit, evaluate if it is destroyed or just hit
            self.player_health -= 1
            ship.ship_health -= 1
            self.self_map.board[coordinate.row][coordinate.col] = BoardValueEnum.HIT
            if ship.ship_health == 0:
                return AttackValueEnum.DESTROYED, ShipInformation.displayName.get(ship.ship_type)
            else:
                return AttackValueEnum.HIT, ShipInformation.displayName.get(ship.ship_type)

        else:
            return AttackValueEnum.INVALID

    def print_board(self, board):
        """Prints the game board with the coordiantes"""
        print('\n'.join(
            [''.join(['{:<4}'.format(item.value if isinstance(item, BoardValueEnum) else item) for item in row]) for row in
             board]))

