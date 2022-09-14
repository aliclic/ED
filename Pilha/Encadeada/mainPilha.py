#Inicialização
from PilhaEncadeada import *

numeros = [4,5,6,90,56,31,42,57]
pilha = Pilha()
for n in numeros:
    pilha.empilha(n)

print(f'Pilha: {pilha}')

#Testando modificação
pilha.modificar(3, 69420)
print(f'Pilha : {pilha}')

#Testando pesquisas
print(pilha.elemento(3))
print(pilha.busca(69420))

#Testando desempilhamento (somente do topo)
print(pilha.desempilha())
print(f'Pilha : {pilha}')


'''

TESTES DO PROF ALEX

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
'''