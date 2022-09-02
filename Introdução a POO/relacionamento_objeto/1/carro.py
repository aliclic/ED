from motor import Motor

class Carro:
  def __init__(self, cor, placa, motor):
    self.__cor = cor
    self.__placa = placa
    self.__motor = motor

  @property
  def cor(self):
    return self.__cor

  @cor.setter
  def cor(self, nova_cor):
    self.__cor = nova_cor

  @property
  def placa(self):
    return self.__placa

  @placa.setter
  def placa(self, nova_placa):
    self.__placa = nova_placa

  @property
  def motor(self):
    return self.__motor

  @motor.setter
  def motor(self, novo_motor):
    self.__motor = novo_motor

  def __str__(self):
    return f'Cor: {self.__cor}, Placa {self.__placa}, Motor: {self.__motor}'

if __name__ == "__main__":
  motor = Motor(1.8, 'gasolina')
  carro = Carro('preto', 'ABC-1234', motor)

  motor.motorizacao = 4.0

  print(carro)