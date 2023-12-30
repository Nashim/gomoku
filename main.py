import numpy as np
from copy import deepcopy

from game import Game, BLACK, WHITE, NO_END
from player import Player

game = Game()
players = [Player(WHITE), Player(BLACK)]

print(game)
running = True
while running:
    for player in players:
        input()
        move = player.play(game.board)
        game_response = game.move(player.player, move)
        print("Player:", player.player, "Move:", move)
        print(game.board)

        if game_response != NO_END:
            print("Winner:", "Black" if game_response == BLACK else "White" if game_response == WHITE else "Draw")
            running = False
            break