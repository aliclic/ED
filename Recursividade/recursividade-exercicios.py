def n_numbers(n):
    '''exibe na tela os números de 0 até n'''
    if n < 0:
        return
    n_numbers(n-1)
    print(n,end=' ')

def soma(a,b)->int:
    '''Somar os numeros no intervalo fechado de "a" a "b"'''
    if a == b:
        return a
    else:
        return a +  soma(a+1,b)
    
def strlen(str)->int:
    if len(str)==0:
        return 0
    else:
        return 1 + strlen(str[1:])

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
rating = [4.5,13.2,2.8,4.9,5.0,2.6]
print('Maior: ', maior(rating))
print()
print('strlen(): ', strlen('ifpb'))
print('strlen2(): ', strlen2('ifpb',2))

print()
n = 10
n_numbers(n)
print('Soma: ',soma(2,5))