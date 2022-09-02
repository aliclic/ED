class Cubo:
  def __init__ (self, x):
    self.x = x
  
  def calcula_cubo(self):
    cubo = self.x ** 3
    return f'o cubo (**3) de {self.x} é {cubo}'


c1 = Cubo(10)
print(c1.calcula_cubo())