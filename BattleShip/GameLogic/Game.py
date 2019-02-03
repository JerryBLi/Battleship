from BattleShip.GameLogic import Player


class Game:

    def __init__(self):
        self.players = (Player(), Player())

    def game_won(self):
        return False

    def play(self):
        while not self.game_won():
            pass
