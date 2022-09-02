class Carro:
  def __init__(self, cor, placa, pecas = []):
    self.__cor = cor
    self.__placa = placa
    self.__pecas = pecas

  def get_pecas(self):
    return self.__pecas
  
  def set_pecas(self, novas_pecas):
    self.__pecas = novas_pecas

  def add_peca(self, nova_peca):
    self.__pecas.append(nova_peca)

  def __str__(self):
    saida = ''

    for i in range(len(self.__pecas)):
      saida = saida + f'{self.__pecas[i]}' + ' '

    return f'Cor: {self.__cor}, Placa: {self.__placa}, Peças => {saida}'