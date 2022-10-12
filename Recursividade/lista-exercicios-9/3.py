# Faça uma função recursiva chamada invertString() que retorne a sequência de caracteres de uma string passada como argumento na ordem inversa

def invertString(str):
  if str == "":
    return str
  else:
    return invertString(str[1:]) + str[0]

'''
str         return
'ifpb'      invertString('ifpb'[1:]) + 'i' => 'bpf' + 'i' = 'bpfi'
'fpb'       invertString('fpb'[1:]) + 'f'  => 'bp' + 'f' = 'bpf'
'pb'        invertString('pb'[1:]) + 'p'   => 'b' + 'p' = 'bp'
'b'         invertString('b'[1:]) + 'b'    => '' + 'b' = 'b' 
''          '' ^
'''

print(invertString('ifpb'))