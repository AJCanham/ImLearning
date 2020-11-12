import numpy as np
from players import Player


gameBoard = np.zeros([3,3])
ans = input("player 1, what is your name?: ")
player1 = Player(ans)
ans = input("player 2, what is your name?: ")
player2 = Player(ans)
print("board is a 3x3 matrix, with coordinates [0,0] to [2,2]")


def turn(player1,player2,gameboard):
  
  ans = input("Player 1, where is your move? : ")
  

