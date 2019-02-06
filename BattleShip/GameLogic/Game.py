from BattleShip.GameLogic import Player
from BattleShip.GameLogic.BoardValue import BoardValueEnum
from BattleShip.GameLogic.Coordinate import Coordinate


class Game:

    def __init__(self):
        self.players = (Player(), Player())

    def game_won(self):
        """Check if the game is won if any of the players have 0 health left"""
        for player in self.players:
            if player.player_health == 0:
                return True
        else:
            return False

    def play(self):
        pass
        while not self.game_won():
            pass

    def player_turn(self, player):
        current_player = self.players[player]


    def attack(self):
        """Select a cell to attack"""
        while True:
            # get start position of ship
            ship_coord = input("Select cell (eg 'A3') to attack: ")
            ship_coord = Coordinate.parse_coordinate(ship_coord)
            # check if valid start position
            if ship_coord is None:
                print("Invalid Coordinated Entered!")
                continue
            if self.enemy_map[ship_coord.row][ship_coord.col] != BoardValueEnum.UNOCCUPIED:
                print("Coordinate already attacked!")
                continue
            return ship_coord

    def print_board(self, board):
        """Prints the game board with the coordiantes"""
        print('\n'.join(
            [''.join(['{:<4}'.format(item.value if isinstance(item, BoardValueEnum) else item) for item in row]) for row in
             board]))
