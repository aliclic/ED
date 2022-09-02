class Dog:
  def __init__(self, nome):
    self.nome = nome
    print(f'Seu dog se chama {self.nome}')

  @property
  def latindo(self):
    latir = True
    if latir:
      return f'Seu dog está latindo\n AU AU!!!'

nome_dog = input('Qual o nome do seu dog? ')
d1 = Dog(nome_dog)
print(d1.latindo())
