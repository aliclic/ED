class Aluno:
  def __init__(self, matricula:int, nome:str, notas:list):
    self.__matricula = matricula
    self.__nome = nome
    self.__notas = notas

  @property
  def nome(self)->str:
    return self.__nome

  @nome.setter
  def nome(self, novo_nome)->str:
    self.__nome = novo_nome
  
  @property
  def matricula(self)->str:
    return self.__matricula

  @property
  def notas(self)->list:
    return self.__notas

  def media(self):
    m = sum(self.__notas) / len(self.__notas)
    return f'{m:.1f}'

  def adiciona_nota(self, nota):
    self.__notas.append(nota)