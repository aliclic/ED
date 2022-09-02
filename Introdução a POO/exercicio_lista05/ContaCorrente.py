class ContaBloqueadaException(Exception):
  def __init__(self, msg):
    super().__init__(msg)

class ContaCorrente:
  def __init__(self, numero:int, saldo:int, nome:str):
    self.__numero = numero
    self.__saldo = saldo
    self.__nome = nome
    self.bloqueado = False

  @property
  def numero(self):
    return self.__numero

  @property
  def saldo(self):
    return self.__saldo

  @property
  def nome(self):
    return self.__nome
  
  def depositar(self, valor_depositado:int):
    self.__saldo += valor_depositado

  def sacar(self, valor_sacado:int)->bool:
    if self.bloqueado == True:
      raise ContaBloqueadaException('Não é possível sacar, pois a conta do cliente está bloqueada')
    assert self.__saldo - valor_sacado >= 0, 'Saldo insuficiente para saque'
    self.__saldo -= valor_sacado
  
  def __str__(self):
    return f'Conta: {self.__nome}, Saldo: {self.__saldo}'


p1 = ContaCorrente(1, 500, 'Alic')
p2 = ContaCorrente(2, 100, 'Victor')
try:
  print(p1)
  p1.bloqueado = True
  p1.sacar(100)
  print(p1)
except AssertionError as ae:
  print(ae)
except ContaBloqueadaException as cbe:
  print(cbe)