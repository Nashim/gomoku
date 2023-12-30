import numpy as np
from copy import deepcopy
from game import Game, EMPTY

class Player(Game):
    def __init__(self, player):
        self.player = player

    def play(self, board):
        self.board = deepcopy(board)
        while True:
            move = np.random.randint(15, size=2)
            if self.board[tuple(move)] == EMPTY:
                break
        return move