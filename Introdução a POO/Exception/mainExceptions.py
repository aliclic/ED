notas = [7.0,8.0,9.0,10.0]

while(True):
    index = int(input("Digite o índice referente a nota:"))

    if index < 0:
        break

    if index >= (len(notas)):
        continue

    print('Nota: ', notas[index],'\n')

    if index == 0:
        print('Não é possivel dividir a nota por zero')
    else:
        print('Nota dividido pelo indice: ', notas[index]/index)

print('FIM DO PROGRAMA')