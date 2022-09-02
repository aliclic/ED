notas = [7.0,8.0,9.0,10.0]

try:
    while(True):

        index = int(input("Digite o índice referente a nota:"))

        if index < 0:
            break

        print('Nota: ', notas[index],'\n')

        if index == 1:
            raise FileNotFoundError('Erro na abertura de arquivo')


        print('Nota dividido pelo indice: ', notas[index]/index)
    
    print('Valeu, vamos à proxima iteração.') 

except ValueError as ve:
    print('Indice invalido. Digite um numero inteiro.')
    print('Mensagem embutida:', ve)
except IndexError as ie:
    print(f'Erro: Digite um numero entre 0 e {len(notas)}')
    print('Mensagem embutida:', ie)
except ZeroDivisionError as zde:
    print(f'Erro: A divisao não pode ser realizada com denominador zero')
    print('Mensagem embutida:', zde)
except BaseException as e:
    print('Aconteceu algum problema. Nossa equipe de suporte irá resolver.')
    print('Exceção responsável: ', e.__class__.__name__)
    print('Mensagem da exceção: ',e)
    
print('FIM DO PROGRAMA')