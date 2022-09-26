class FilaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class NoCabeca:
    def __init__(self):
        self.inicio = None
        self.final  = None
        self.tamanho = 0

class No:
    def __init__(self, carga):
        self.carga = carga
        self.prox = None

    def __str__(self):
        return f'{self.carga}'

class Fila:
    def __init__(self):
        self.__head = NoCabeca()

    def estaVazia(self)->bool:
        return self.__head.tamanho == 0

    def tamanho(self)->int:
        return self.__head.tamanho

    def __len__(self)->int:
        return self.__head.tamanho

    def elemento(self, posicao:int)->any:
        try:
            assert posicao > 0 and posicao <= self.__head.tamanho

            cursor = self.__head.inicio
            count = 1
            while(count < posicao):
                cursor = cursor.prox
                count += 1
            return cursor.carga
        except AssertionError:
            raise FilaException(f'Posicao inválida para a fila atual com {self.__head.tamanho} elementos')


    def busca(self, chave:any) -> int:  # retornar a posicao de "chave" na fila
        cursor = self.__head.inicio
        count = 0

        while (cursor is not None):
            count += 1
            if cursor.carga == chave:
                return count
            cursor = cursor.prox

        raise FilaException(f'A chave {chave} não está na Fila.')


    def modificar(self, posicao:int, conteudo:any):
        try:
            assert posicao > 0 and posicao <= self.__head.tamanho

            cursor = self.__head.inicio
            cont = 1
            while (cont < posicao):
                cursor = cursor.prox
                cont += 1
            cursor.carga = conteudo
        except AssertionError:
            raise FilaException(f'Posicao inválida para a fila atual com {self.__head.tamanho} elementos')


    def enfileira(self, conteudo:any):
        novo = No(conteudo)

        if self.estaVazia():
            self.__head.inicio = novo
            self.__head.final = novo
        else:
            self.__head.final.prox = novo
            self.__head.final = novo

        self.__head.tamanho += 1


    def desenfileira(self)->any:
        if self.estaVazia():
            raise FilaException(f'Fila vazia. Não é possível a remoção')

        carga = self.__head.inicio.carga
        self.__head.inicio = self.__head.inicio.prox
        self.__head.tamanho -= 1
        return carga


    def primeiro(self)->any:
        if self.estaVazia():
            raise FilaException(f'Fila vazia. Não é possível a remoção')

        carga = self.__head.inicio.carga
        return carga
        

    def __str__(self)->str:
        s = '[ '
        cursor = self.__head.inicio

        while (cursor is not None):
            s += f'{cursor.carga} '
            cursor = cursor.prox

        s += ']'

        return s

    def esvazia(self)->None:
        while(not self.estaVazia()):
            self.desenfileira()