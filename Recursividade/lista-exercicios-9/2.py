# Faça uma função recursiva chamada printstr() que imprima na tela uma string (caractere a caractere).

def printstr(str):
  if str == '':
    return
  else:
    print(str[0], end='')
    return printstr(str[1:])

'''
str           print          return
'ifpb'       i              printstr('ifpb'[1:])
'fpb'        if             printstr('fpb'[1:])
'pb'         ifp            printstr('pb'[1:])
'b'          ifpb           printstr('b'[1:])
''                          
'''

printstr('ifpb')