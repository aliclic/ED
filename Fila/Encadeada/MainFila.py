from FilaEncadeada import *

fila = Fila()

print(fila)
print(fila.estaVazia())
print(fila.tamanho())

fila.enfileira('Alic')
fila.enfileira('Victor')
fila.enfileira(True)
fila.enfileira(48)
fila.desenfileira()
fila.desenfileira()
print(fila.tamanho())
fila.modificar(1, 'Alic')
fila.modificar(2, 'Alic')
fila.enfileira(47)
print(fila.busca(47))
print(fila.primeiro())

print(fila)