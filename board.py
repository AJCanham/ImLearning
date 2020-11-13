from items import Item, Nought, Cross

class Board():
  def __init__(self):
    self.stuff = []

  def isSpaceFree(self,x,y):
    f = True
    xi = int(x)
    yi = int(y)
    if xi > 2 or xi < 0:
      f = False
    if yi >2 or yi <0:
      f = False 
    for i in self.stuff:
      if i.posx == xi and i.posy == yi:
        f =  False
    return f  

<<<<<<< HEAD
  def placeItem(self,item):
    if isinstance(item,Item) == True:
      self.stuff.append(item)


  def hasNoughtWon(self):
    xs = []
    ys = []
    f = False
    for i in self.stuff:
      if isinstance(i,Nought):
        xs.append(i.posx)
        ys.append(i.posy)
    xn = [0 for i in xs]  
    yn = [0  for i in ys]
    print(xn,yn)
    print(xs,ys)
    #For 3 in a row horizontal or vertical
    for i in xs:
      xn[i] += 1
      if xn[i] == 3:
        f = True
    for j in ys:
      yn[j] += 1
      if yn[j] == 3:
        f = True
    ##For the diagonals
    n = 0
    for i in range(0,len(xs)):
      if xs[i] == 2-ys[i]:
        n +=1
    if n == 3:
      f = True
    n = 0
    for j in range(0,len(xs)):
      if xs[j] == ys[j]:
        n +=1
    if n == 3:
      f = True
    return f
  
  def hasCrossWon(self):
    xs = []
    ys = []
    f = False
    for i in self.stuff:
      if isinstance(i,Cross):
        xs.append(i.posx)
        ys.append(i.posy)
    xn = [0 for i in xs]  
    yn = [0  for i in ys]
    print(xn,yn)
    print(xs,ys)
    for i in xs:
      xn[i] += 1
      if xn[i] == 3:
        f = True
    for j in ys:
      yn[j] += 1
      if yn[j] == 3:
        f = True
    n = 0
    for i in range(0,len(xs)):
      if xs[i] == ys[i]:
        n +=1
    if n == 3:
      f = True
    n = 0
    for j in range(0,len(xs)):
      if xs[j] == 2-ys[j]:
        n +=1
    if n == 3:
      f = True
    return f

=======
  def placeItem(item, x, y):
    if isInstance(item,Item) == true:
      self.stuff.append(item)

  def hasWon(itemType):
    xs = []
    ys = []
    f = false
    for i in self.stuff:
      if isinstance(i,itemType):
        xs.append(i.xpos)
        ys.append(i.ypos)
    n1,n2,n3 = 0,0,0
    for j in xs:
      if j == 0:
        n1 +=1
      if j == 1:
        n2 += 1
      else:
        n3 +=1
      if n1 == 3 or n2 == 3 or n3 == 3:
        f = True
    n1,n2,n3 = 0,0,0
    for j in ys:
      if j == 0:
        n1 +=1
      if j == 1:
        n2 += 1
      else:
        n3 +=1
      if n1 == 3 or n2 == 3 or n3 == 3:
        f = True
>>>>>>> origin/main

      

      
<<<<<<< HEAD

=======
game = Board()
print(game.isSpaceFree(0,1))
>>>>>>> origin/main
