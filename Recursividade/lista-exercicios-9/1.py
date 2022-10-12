# Faça uma função recursiva chamada recursiveLength() que retorne a quantidade de caracteres de um string.

def recursiveLength(str)->int:
  if str == '':
    return 0
  return 1 + recursiveLength(str[1:])

'''
str             return
'aliclic'       1 + recursiveLength('aliclic'[1:]) => 1 + 6 = 7
'liclic'        1 + recursiveLength('liclic'[1:])  => 1 + 5 = 6 ^
'iclic'         1 + recursiveLength('iclic'[1:])   => 1 + 4 = 5 ^
'clic'          1 + recursiveLength('clic'[1:])    => 1 + 3 = 4 ^
'lic'           1 + recursiveLength('lic'[1:])     => 1 + 2 = 3 ^
'ic'            1 + recursiveLength('ic'[1:])      => 1 + 1 = 2 ^
'c'             1 + recursiveLength('c'[1:])       => 1 + 0 = 1 ^
''              0 ^
'''

print(recursiveLength('aliclic'))