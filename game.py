import numpy as np
from copy import deepcopy

BLACK = -1
WHITE = 1
EMPTY = 0
NO_END = 0
DRAW = 2
BOARD_SIZE = 15

class Game():
    def __init__(self):
        self.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=np.int8)
        self.current_player = WHITE

    def __str__(self):
        return str(self.board)
    
    def move(self, player, move):
        if player != self.current_player:
            print("Wrong player")
            return player
        self.current_player = -self.current_player
        if self.board[tuple(move)] != 0:
            print("Wrong move: illegal move")
            return player
        self.board[tuple(move)] = player

        winner = self.check_win(move)
        if winner != NO_END:
            return winner
        return self.draw()
    
    def check_win(self, move):
        player = self.board[tuple(move)]
        vectors = np.array([[1, 0], [0, 1], [1, 1], [1, -1]])
        for vec in vectors:
            count = 0
            for dir in [-1, 1]:
                for i in range(1, 5):
                    next_move = tuple(move + i * dir * vec)
                    if next_move in np.ndindex(self.board.shape):
                        if self.board[next_move] == player:
                            count += 1
                        else:
                            break
            if count >= 5:
                return player
            
        return NO_END
    
    def draw(self):
        if not np.any(self.board == EMPTY):
            return DRAW
        return NO_END