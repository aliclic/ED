from No import No

def preordem(no_inicial):
    if no_inicial is None:
        return
    print(f'{no_inicial.carga}', end=' ')
    preordem(no_inicial.esq)
    preordem(no_inicial.dir)
# 10 32 12 5 40 23 30 60 22

def emordem(no_inicial):
    if no_inicial is None:
        return
    emordem(no_inicial.esq)
    print(f'{no_inicial.carga}', end=' ')
    emordem(no_inicial.dir)
# 5 12 32 40 10 23 60 22 30

def posordem(no_inicial):
    if no_inicial is None:
        return
    posordem(no_inicial.esq)
    posordem(no_inicial.dir)
    print(f'{no_inicial.carga}', end=' ')
# 5 12 40 32 22 60 30 23 10

def busca(chave, no_inicial)->bool:
    if no_inicial is None:
        return False
    if no_inicial.carga == chave:
        return True
    if ( busca(chave, no_inicial.esq)):
        return True
    else:
        return busca(chave, no_inicial.dir)

raiz = No(10)
raiz.esq = No(32)
raiz.dir = No(23)
cursor = raiz.esq # cursor desce para o nó 32
cursor.esq = No(12)
cursor.dir = No(40)
cursor = cursor.esq # cursor desce para o nó 12
cursor.esq = No(5)
cursor = raiz.dir # cursor desce para o nó 23, a partir do raiz
cursor.dir = No(30)
cursor = cursor.dir # cursor desce para o nó 30
cursor.esq = No(60)
cursor = cursor.esq # cursor desce par ao nó 60
cursor.dir = No(22)

preordem(raiz) # em Pré Ordem
print()
emordem(raiz)  # em Ordem
print()
posordem(raiz) # em Pós Ordem

print(busca(22, raiz))



