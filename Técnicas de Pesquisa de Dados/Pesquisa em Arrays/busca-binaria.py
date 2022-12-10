def buscaBinaria(array, chave):
  return busca_binaria(array, chave, 0, len(array)-1)

def busca_binaria(array, chave, inicio, fim):
  if inicio > fim:
    return -1
  else:
    meio = (inicio + fim)//2
    if chave == array[meio]:
      return meio            # elemento foi encontrado
    elif chave < array[meio]:
      return busca_binaria(array, chave, inicio, meio-1)
    else:
      return busca_binaria(array, chave, meio+1, fim)





print('Pesquisa Busca Linear Ordenada')
print('*' * 35)
array = [20,5,15,4,2,9,11]
array = sorted(array)
chave = 5
print('Array de busca:', array)
print('Chave', chave)
index = buscaBinaria(array, chave)
if index > 0:
  print('Chave',chave,'encontrada na posição',index)
else:
  print('Chave', chave, 'não encontrada no Array')






'''
def buscaBinaria(array, chave):
  inicio = 0
  fim = len(array)-1 
  # Enquanto houver distância entre inicio e fim
  while (inicio <= fim ):
    meio = (inicio + fim)//2
    if ( chave < array[meio] ):
      fim = meio - 1            # Ajusta a pos. final
    elif ( chave > array[meio] ):
      inicio = meio + 1         # Ajusta a pos. inicial
    else:
      return meio               # elemento foi encontrado!

  # Se finalizar o laço, percorreu todo o array e
  # não encontrou
  return -1

array = [1,2,3,4,5,6,7,8,9,10]
print(buscaBinaria(array, 3))
'''