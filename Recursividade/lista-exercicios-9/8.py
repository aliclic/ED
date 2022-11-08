# Faça uma função recursiva chamada menores_rec() que receba como parâmetro um list de valores
# numéricos e um número inteiro key. A função deve retornar quantos elementos da lista possuem valor
# inferior a key. O protótipo da função é definido por:

def menores_rec( lista, key ):
  if lista == []:
    return 0
  if lista[0] >= key:
    return 0
  else:
    return 1 + menores_rec(lista[1:], key)
 

print(menores_rec([1,2,3,4,5], 4))