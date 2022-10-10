# print recursivo printstr()

def printstr(str):
  if (str == ''):
    return
  print(str[0], end='')
  printstr(str[1:])


def printstrInvertida(str):
  if (str == ''):
    return
  printstrInvertida(str[1:])
  print(str[0], end='')

def tamanhostr(str):
  if (str == ''):
    return 0
  else:
    return 1 + tamanhostr(str[1:])



str = 'ifpb'
printstr(str)
print()
printstrInvertida(str)
print()
print(tamanhostr(str))