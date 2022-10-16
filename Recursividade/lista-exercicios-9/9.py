# Faça uma função recursiva chamada decToBin() que receba um número inteiro na base decimal e imprima seu correspondente na base binária.

def decToBin( number):
  quoc = number // 2
  resto = number % 2
  if ( number >= 2 ):
    decToBin( quoc )
    print(resto, end='')
  else:
    print(resto, end='')

print(decToBin(5))