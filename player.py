import numpy as np
from copy import deepcopy
from game import Game, EMPTY, BOARD_SIZE

class Player(Game):
    def __init__(self, player):
        self.player = player

    def playable(self, board):
        not_empty = np.argwhere(board != EMPTY)
        min = np.min(not_empty, axis=0)
        max = np.max(not_empty, axis=0)
        min_n = np.maximum(min - 2, 0)
        max_n = np.minimum(max + 2, BOARD_SIZE-1)
        return np.argwhere(board[min_n[0]:max_n[0]+1, min_n[1]:max_n[1]+1] == EMPTY) + min_n
    
    def play(self, board):
        self.board = deepcopy(board)
        if np.all(self.board == EMPTY):
            return np.array([7, 8])
        playable = self.playable(self.board)
        print(playable)
        return playable[np.random.randint(len(playable))]