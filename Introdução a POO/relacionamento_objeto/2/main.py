from novo_carro import Carro
from pecas import Peca

if __name__ == "__main__":
  pecas = []

  p1 = Peca('1', 'chassi')
  p2 = Peca('2', 'volante')
  p3 = Peca('3', 'disco de freio')

  pecas.append(p1)
  pecas.append(p2)
  pecas.append(p3)

  carro = Carro('verde', 'ABC-1234', pecas)

  carro.add_peca(Peca('4', 'filtro de ar'))

  print(carro)