class Player:
  def __init__ (self, name):
    self.name = name
  
  def chooseType(self,item):
    if int(item) == 0 or int(item) == 1:
      self.itemType = int(item)
    else: 
      self.itemType = 0
  
  
  