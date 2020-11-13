class Player:
  def __init__ (self, name):
    self.name = name
  
  def chooseType(self,item):
    if item == 0 or item == 1:
      self.itemType = int(item)
    else: 
      self.itemType = 0
  
  
  