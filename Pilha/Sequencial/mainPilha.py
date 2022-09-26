from PilhaSequencial import *

numeros = [4,5,6,90,56,31,42,57]
numeros2 = [58, 59, 60]
pilha = Pilha()
pilha2 = Pilha()


for n in numeros:
    pilha.empilha(n)

for n in numeros2:
    pilha2.empilha(n)

# pilha.concatena(pilha2) 
# print(pilha)  4, 5, 6, 90, 56, 31, 42, 57, 58, 59, 60

print('Array: ',numeros)
print('Pilha: ', pilha)

string = 'Instituto Federal da Paraiba'
pilha.esvazia()
print(string)
for s in string:
    pilha.empilha(s)
print()

while(not pilha.estaVazia()):
    print(pilha.desempilha(),end='')

try:
    print
    print(pilha.busca(90))
except PilhaException as pe:
    print(pe)

