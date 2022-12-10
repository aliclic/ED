def buscaLinearOrdenada(array, chave):
  return busca_linear_ordenada(array, 0, chave)

def busca_linear_ordenada(array, index, chave):
  if index >= len(array):
    return -1

  if chave < array[index]:
    return -1

  if array[index] == chave:
    return index
  
  else:
    return busca_linear_ordenada(array, index+1, chave)




print('Pesquisa Busca Linear Ordenada')
print('*' * 35)
array = [20,5,15,4,2,9,11]
array = sorted(array)
chave = 9
print('Array de busca:', array)
print('Chave', chave)
index = buscaLinearOrdenada(array, chave)
if index > 0:
  print('Chave',chave,'encontrada na posição',index)





'''
def buscaLinearOrdenada(array, chave):
  for i in range(len(array)):
    if ( chave == array[i] ):
      return i              # elemento foi encontrado
    elif (chave < array[i]):
      return -1             # interrompe a busca

  # Se sair do laço é porque percorreu todo o vetor
  # e não encontrou a chave
  return -1
  '''