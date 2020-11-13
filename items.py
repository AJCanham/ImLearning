class Item():
  def __init__(self, posx,posy):
    self.posx = posx
    self.posy = posy

class Nought(Item):
  def __init__(self, posx,posy):
    super().__init__(posx,posy)

class Cross(Item):
  def __init__(self,posx,posy):
    super().__init__(posx,posy)