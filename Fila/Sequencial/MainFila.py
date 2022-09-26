from FilaSequencialCircular import *

fila = Fila()

fila.enfileira('Alic')
fila.enfileira('Victor')
fila.enfileira(42)
fila.enfileira(10)
fila.enfileira(True)
fila.enfileira(52.2)
fila.enfileira(False)
fila.enfileira('Gabriel')
fila.enfileira(89)
fila.enfileira(100)

print(fila)

print(fila.desenfileira())

print(fila)

print(fila.elemento(1))

print(fila.busca('Victor'))

fila.modificar(2, 70)

print(fila)

fila.esvazia()
print(fila)