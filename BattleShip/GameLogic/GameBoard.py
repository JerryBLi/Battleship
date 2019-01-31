from BattleShip.GameLogic.BoardValueEnum import BoardValue


class GameBoard:
    """This is the representation for the game board"""
    def __init__(self):
        # declare a 10 x 10 grid for the game
        self.board = [[BoardValue.UNVISITED for i in range(10)] for j in range(10)]


