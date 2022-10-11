from email.errors import MultipartConversionError
from platform import java_ver

'''
1. Há uma regra/padrão que seja geral para a maioria da entrada de dados 
   do problema?
   2 ^ 1 = 1
   2 ^ 2 = 2 x 2
   2 ^ 3 = 2 x 2 x 2
   2 ^ 4 = 2 x 2 x 2 x 2 

   base (2) multiplicada n vezes pelo expoente
   se expoente >= 1 
   ...
2. Identificar os casos bases
   2 ^ 0  = 1
   O caso base é quem vai determinar a quebra do ciclo de chamadas recursivas

3. Ao começar a desenvolver a solução recursiva, certifique-se que um
   dos argumentos de controle de recursividade está sendo alterado
   a cada chamada recursiva, até que atinja o caso base
'''

"""
def potenciaYago(base, exp) -> int:
    return potenciaAuxiliar(base,1,exp)

def potenciaAuxiliar(base, exp,limite):
    if exp > limite:
        return 1
    else:
        return base * potenciaAuxiliar(base,exp+1,limite)
"""

#       POTÊNCIA

def potenciaIterativa(base, exp)->int:
    resultado = 1
    for i in range(exp):
        resultado *= base
    return resultado

def potenciaRecursiva(base, exp, n)->int:
    print(f'Chamada {n}: base {base}, expoente {exp}')
    if exp == 0:
        return 1
    else:
        return base * potenciaRecursiva(base,exp-1,n+1)

'''
base     exp    return
2        3      2 * potenciaRecursiva(2, 2) => 2 * 4 = 8
2        2      2 * potenciaRecursiva(2, 1) => 2 * 2 = 4 ^
2        1      2 * potenciaRecursiva(2, 0) => 2 * 1 = 2 ^
2        0                1                 =>         1 ^
'''

#       FATORIAL

def fatorialIterativa(n)->int:
    if (n == 0):
        return 1
    fat = 1
    for i in range(n, 0, -1):
        fat *= i
    return fat
print('Fatorial Iterativa: ', fatorialIterativa(4))

def fatorialRecursiva(n)->int:
    if (n < 0):
        return -1
    if (n == 0):
        return 1
    else:
        return (n * fatorialRecursiva(n-1))
print('Fatorial Recursiva: ', fatorialRecursiva(4))

'''
n        return
4        4 * fatorialRecursiva(3) => 4 * 6 = 24
3        3 * fatorialRecursiva(2) => 3 * 2 = 6 ^
2        2 * fatorialRecursiva(1) => 2 * 1 = 2 ^
1        1 * fatorialRecursiva(0) => 1 * 1 = 1 ^
0        1 ^
'''


def frec(i,j)->int:
    if i == j:
        return 0
    else:
        return i + frec(i+1,j)
print(frec(2,6)) # o que será exibido


#       ORDEM CRESCENTE E DECRESCENTE

def printNumbersDescending(n):    # Decrescente
    if n == 0:
        return
    print(n,end=' ')
    printNumbersDescending(n-1)
printNumbersDescending(5)

'''
n        print                            return
5        5                                printNumbersDescending(4)
4        5, 4                             printNumbersDescending(3)
3        5, 4, 3                          printNumbersDescending(2)
2        5, 4, 3, 2                       printNumbersDescending(1)
1        5, 4, 3, 2, 1                    printNumbersDescending(0)
0                                         0 ^
'''

def printNumbersAscending(n):    # Crescente
    if n == 0:
        return
    printNumbersAscending(n-1)
    print(n,end=' ')
print()
printNumbersAscending(5)

'''
n        return                        print
5        printNumbersAscending(4)      1, 2, 3, 4
4        printNumbersAscending(3)      1, 2, 3
3        printNumbersAscending(2)      1, 2
2        printNumbersAscending(1)      1
1        printNumbersAscending(0)      
0        0 ^
'''      


# main
# 2 ^ 3 = 2 x 2 x 2
print()
print('Potencia Iterativa: ', potenciaIterativa(2,10))
print('Potencia Recursiva: ', potenciaRecursiva(2,3,0))
#print(potenciaYago(2,3))