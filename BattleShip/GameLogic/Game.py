from BattleShip.GameLogic.Player import Player
from BattleShip.GameLogic.BoardValue import BoardValueEnum
from BattleShip.GameLogic.BoardValue import AttackValueEnum
from BattleShip.GameLogic.Coordinate import Coordinate
from BattleShip.GameLogic.GameBoard import GameBoard
import random
import os


class Game:

    def __init__(self):
        self.players = (Player(True), Player(False))

    def game_won(self):
        """Check if the game is won if any of the players have 0 health left"""
        for player in self.players:
            if player.player_health == 0:
                return True
        else:
            return False

    def play(self):
        self.players[0].populate_board()
        self.players[1].auto_populate_board()
        current_player = 0

        while not self.game_won():
            Game.player_turn(self, current_player)
            current_player = (current_player + 1) % 2

        if self.players[0].player_health == 0:
            print("Player 1 Won!")
        else:
            print("Player 2 Won!")

    def player_turn(self, player_num):
        current_player = self.players[player_num]
        enemy_player = self.players[(player_num + 1) % 2]
        if current_player.is_human is True:
            Game.human_move(current_player, enemy_player)
        else:
            Game.computer_move(current_player, enemy_player)

    @staticmethod
    def human_move(self_player, enemy_player):

        #clear the screen
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        """Select a cell to attack"""
        # Print the maps
        print("--------------------- HUMAN ENEMY MAP ---------------------")
        Game.print_board(self_player.enemy_map.board)
        print("--------------------- HUMAN OWN MAP ---------------------")
        Game.print_board(self_player.self_map.board)

        while True:
            # get start position of ship
            attack_coord = input("Select cell (eg 'A3') to attack: ")
            attack_coord = Coordinate.parse_coordinate(attack_coord)
            # check if valid start position
            if attack_coord is None:
                print("Invalid Coordinated Entered!")
                continue
            else:
                attack_result, ship_disp_name = enemy_player.attack(attack_coord)
                if attack_result == AttackValueEnum.EXISTS or attack_result == AttackValueEnum.INVALID:
                    print("Invalid Attack")
                else:
                    Game.update_enemy_map(self_player, attack_coord, attack_result)

                    if attack_result == AttackValueEnum.HIT:
                        print("HIT!")
                    elif attack_result == AttackValueEnum.MISS:
                        print("MISS!")
                    elif attack_result == AttackValueEnum.DESTROYED:
                        print("You sunk my " + ship_disp_name)
                    break

    @staticmethod
    def computer_move(self_player, enemy_player):
        if isinstance(enemy_player, Player):
            while True:
                attack_row = random.randint(GameBoard.MIN_ROW, GameBoard.MAX_ROW - 1)
                attack_col = random.randint(GameBoard.MIN_COL, GameBoard.MAX_COL - 1)
                attack_coord = Coordinate(attack_row, attack_col)
                attack_result, ship_disp_name = enemy_player.attack(attack_coord)
                if attack_result == AttackValueEnum.EXISTS or attack_result == AttackValueEnum.INVALID:
                    continue
                else:
                    Game.update_enemy_map(self_player, attack_coord, attack_result)
                    print("Attacking {}{}".format(chr((ord('A') + attack_col)), attack_row))
                    break

    @staticmethod
    def update_enemy_map(player, coordinate, attack_value):
        if isinstance(attack_value, AttackValueEnum) and isinstance(player, Player):
            if attack_value == AttackValueEnum.HIT or attack_value == AttackValueEnum.DESTROYED:
                player.update_enemy_map(coordinate, BoardValueEnum.HIT)
            elif attack_value == AttackValueEnum.MISS:
                player.update_enemy_map(coordinate, BoardValueEnum.MISS)

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

    @staticmethod
    def print_board(board):
        """Prints the game board with the coordiantes"""
        print('\n'.join([''.join(['{:<4}'.format(item.value if isinstance(item, BoardValueEnum) else item) for item in row]) for row in board]))

