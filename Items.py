class Item:
  def _init_(self, player):
    self.player = player

class Nought(Item):
  def _init_(self,player):
    super()._init_(self,player)

class Cross(Item):
  def _init_(self,player):
    super()._init_(self,player)