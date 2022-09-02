from Pais import Pais

if __name__ == "__main__":
  p1 = Pais('Brasil', 'Brasília', 8516)
  p2 = Pais('Estados Unidos', 'Washington', 9834)
  print(p1)
  print(p2)
  print(p1.vizinhos)
  print(p2.capital)
  p1.addPaisDeFronteira('Argentina')
  p1.addPaisDeFronteira('Bolívia')
  p1.addPaisDeFronteira('Argentina')
  p1.addPaisDeFronteira('Colômbia')
  print(p1.vizinhos)