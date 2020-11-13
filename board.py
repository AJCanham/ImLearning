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


      

      

