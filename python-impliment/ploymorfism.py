class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.moedel = model

  def move(self):
   print("The cat is moving")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
   print("The boat is moving")


class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
   print("The Plane is flying")

car = Car("Toyota", "g4")
boat = Boat("Titanic", "Titanic")
plane = Plane("Boeing", "747")

for x in (car, boat, plane):
  x.move()

  print("o------------o------------o")
  print(" ||||||||        ||||||| ")