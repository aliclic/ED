class Data:
  def __init__(self, dia:int, mes:int, ano:int):
    self.__dia = dia
    self.__mes = mes
    self.__ano = ano

  @property
  def dia(self)->int:
    return self.__dia
  
  @dia.setter
  def dia(self, novo_dia)->int:
    self.__dia = novo_dia

  @property
  def mes(self)->int:
    return self.__mes

  @mes.setter
  def mes(self, novo_mes)->int:
    self.__mes = novo_mes
  
  @property
  def ano(self)->int:
    return self.__ano
  
  @ano.setter
  def ano(self, novo_ano)->int:
    self.__ano = novo_ano

  def __str__(self):
    return f'{self.__dia} / {self.__mes} / {self.__ano}'