def buscaLinear(array, index, key):
  if index >= len(array):
    return -1

  if array[index] == key:
    return index

  else:
    return buscaLinear(array, index + 1, key)

print('Pesquisa Busca Linear Recursiva')
print('*' * 35)
array = [20,5,15,4,2,9,11]
key = 2
print('Array de busca:', array)
print('Chave:', key)
index = buscaLinear(array, 0, key)
if index >= 0:
  print('Chave',key,'encontrada na posição',index)




'''
def buscaLinear(array, key):
  for i in range(len(array)):
    if array[i] == key:
      return i              # elemento foi encontrado
  # Se sair do laço é porque percorreu todo o vetor
  # e não encontrou a chave
  return -1
  '''