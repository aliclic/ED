# Escreva uma função recursiva que retorne a soma dos n primeiros números inteiros. Se n = 3, a soma seria igual a 1 + 2 + 3 = 6

def sum(n)->int:
  if n == 0:
    return 0
  else:
    return n + sum(n-1)

'''
n        return
5        5 + sum(4) => 5 + 10 = 15
4        4 + sum(3) => 4 + 6 =  10 
3        3 + sum(2) => 3 + 3 =  6
2        2 + sum(1) => 2 + 1 =  3
1        1 + sum(0) => 1 + 0 =  1
0        0 => 0 ^
'''

print(sum(5))