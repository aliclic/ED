def n_numbers(n):
    '''exibe na tela os números de 0 até n'''
    if n < 0:
        return
    n_numbers(n-1)
    print(n,end=' ')

'''
n      return             print
5      n_numbers(4)       0 1 2 3 4 5
4      n_numbers(3)       0 1 2 3 4 ^
3      n_numbers(2)       0 1 2 3 ^
2      n_numbers(1)       0 1 2 ^
1      n_numbers(0)       0 1 ^
0      n_numbers(-1)      0 ^
-1       ------
'''

def soma(a,b)->int:
    '''Somar os numeros no intervalo fechado de "a" a "b" '''
    if a == b:
        return a
    else:
        return a + soma(a+1,b)

'''
a    b     return
2    5     2 + soma(3, 5) => 2 + 13 = 14
3    5     3 + soma(4, 5) => 3 + 10 = 12 ^
4    5     4 + soma(5, 5) => 5 + 5 = 9 ^
5    5     5 ^
'''
    
def strlen(str)->int:
    if len(str)==0:
        return 0
    else:
        return 1 + strlen(str[1:])

'''
str         return
'ifpb'      1 + strlen('ifpb'[1:]) => 1 + 3 = 4
'fpb'       1 + strlen('fpb'[1:])  => 1 + 2 = 3 ^
'pb'        1 + strlen('pb'[1:])   => 1 + 1 = 2 ^
'b'         1 + strlen('b'[1:])    => 1 + 0 = 1 ^
''          0 ^
'''

def strlenaux(str)->int:
    return strlen2(str,0)

def strlen2(str,i=0)->int:
    if i == len(str):
        return 0
    else:
        return 1 + strlen2(str,i+1)

def maior(array)->float:
    if len(array)==0:
        raise Exception('Array vazio.')
    if len(array) == 1:
        return array[0]
    return max(array[0],maior(array[1:]))
    '''
    retorno = maior(array[1:])
    if array[0] > retorno:
        return array[0]
    else:
        return retorno
    '''

# programa principal
n = 5
n_numbers(n)
print()
print('Soma: ',soma(2,5))

print()

rating = [4.5,13.2,2.8,4.9,5.0,2.6]
print('Maior: ', maior(rating))

print()

print('strlen(): ', strlen('ifpb'))
print('strlen2(): ', strlen2('ifpb',2))
