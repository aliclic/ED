class Motor:
  def __init__(self, motorizacao, combustivel = 'flex'):
    self.__motorizacao = motorizacao
    self.__combustivel = combustivel
  
  @property
  def motorizacao(self):
    return self.__motorizacao
  
  @motorizacao.setter
  def motorizacao(self, nova_motorizacao):
    self.__motorizacao = nova_motorizacao

  def __str__(self):
    return f'Motor: {self.motorizacao}L, Combustível: {self.__combustivel}'

if __name__ == "__main__":
  motor = Motor(2.0)
  print(motor)