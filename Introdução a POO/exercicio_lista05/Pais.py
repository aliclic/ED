from typing import List

class Pais: 
  def __init__(self, nome:str, capital:str, dimensao:int):
    self.__nome = nome
    self.__capital = capital
    self.__dimensao = dimensao
    self.__vizinhos = list()

  @property
  def nome(self)->str:
    return self.__nome

  @property
  def capital(self)->str:
    return self.__capital

  @property
  def dimensao(self)->int:
    return self.__dimensao

  @property
  def vizinhos(self)->list[str]:
    return self.__vizinhos

  def addPaisDeFronteira(self, nome_do_pais:str):
    if nome_do_pais not in self.__vizinhos:
      self.__vizinhos.append(nome_do_pais)
    
  def __str__(self):
    return f'{self.__nome}, capital {self.__capital}, {self.__dimensao} Km²'