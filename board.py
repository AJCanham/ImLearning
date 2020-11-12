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

      

      
game = Board()
print(game.isSpaceFree(0,1))
