import numpy as np
from players import Player
from board import Board
from items import Nought, Cross



def crossTurn():
  while True:
    x = int(input("Where would you like to place? x coord : " ))
    y =  int(input("y coord : "))
    if gameBoard.isSpaceFree(x,y):
      gameBoard.placeItem(Cross(x,y))
      print("cross is placed at:" , x, y)
        
      break
    print("space is unavailable")
  

def noughtTurn():
  while True:
    x = int(input("Where would you like to place? x coord : " ))
    y =  int(input("y coord : "))
    if gameBoard.isSpaceFree(x,y):
      gameBoard.placeItem(Nought(x,y))
      print("nought is placed at:" , x, y)
        
      break
    print("space is unavailable")
  
  





gameBoard = Board()
ans = input("player 1, what is your name?: ")
player1 = Player(ans)
ans = input("player 2, what is your name?: ")
player2 = Player(ans)
print("board is a 3x3 matrix, with coordinates [0,0] to [2,2]")
print("when it's you're turn, be sure to enter an integer input")
ans = input("Player 1, select Os (enter 0) or Xs (enter 1) :")
player1.chooseType(ans)
if player1.itemType == 0:
  player2.chooseType(1)
  print("player 1, you are Os")
  print("player 2 you are Xs")
else:
  player2.chooseType(0)
  print("player 1 you are Xs")
  print("player 2 you are Os")

while True:
  print("player 1 turn: ")
  if player1.itemType == 0:
    noughtTurn()
  else:
    crossTurn()
  if gameBoard.hasNoughtWon() == True or gameBoard.hasCrossWon() == True:
    print("Player 1 wins")
    print(player2.name() , "Can suck a dick")
    break
  print("player 2 turn:")
  if player2.itemType == 0:
    noughtTurn()
  else:
    crossTurn()
  if gameBoard.hasNoughtWon() == True or gameBoard.hasCrossWon() == True:
    print("Player 2 wins")
    print(player1.name() , "Can suck a dick")
    break

  

