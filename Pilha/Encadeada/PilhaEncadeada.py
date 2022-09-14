class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class No:
    def __init__(self, conteudo: any):
        self.conteudo = conteudo
        self.prox = None

    def __str__(self):
        return str(self.conteudo)


class Pilha:

    '''
            ~ RECEITA DE BOLO PARA PERCORRER UMA PILHA/LISTA ENCADEADA ~
    
        cursor = self.__head #Armazene o nó atual numa variável 'cursor'
        while (CONDIÇÃO): #EX: cursor != None
            cursor = cursor.prox #Atualize o valor do cursor para ser o próximo nó


        ==================================================================================

        deve ter mais formas de mexer com encadeamento ...
        fazer a head apontar pro tail e o tail apontar pro head faz uma estrutura circular
        cabecinha com bundinha & bundinha com cabecinha  :)

    '''

    def __init__(self):
        self.__head = None
        self.__tamanho = 0

    def estaVazia(self)->bool:
        return self.__head == None

    def tamanho(self)->int:
        return self.__tamanho

    def __len__(self)->int:
        return self.__tamanho

    def elemento(self, posicao:int)->any:
        #Retorna a carga armazenada no nó na posição N
        try:
            assert posicao > 0 and posicao <= self.__tamanho
            cont = self.__tamanho
            atual = self.__head
            while cont != posicao:
                atual = atual.prox
                cont -= 1
            return atual.conteudo
        except AssertionError:
            raise PilhaException(f'Posicao inválida para a pilha atual com {self.__tamanho} elementos')
    
    def busca(self, conteudo:any)->int: 
        #Retorna a posição do nó cuja conteúdo corresponde à consulta
        cont = 0
        atual = self.__head
        while atual != None:
            if atual.conteudo == conteudo:
                return self.__tamanho - cont
            atual = atual.prox
            cont += 1
        raise  PilhaException(f'Valor {conteudo} não está na pilha')

    def modificar(self, posicao:int, conteudo: any):
        #Substitui o conteúdo do elemento na posição N
        try:
            assert posicao > 0 and posicao <= self.__tamanho
            cont = self.__tamanho
            atual = self.__head
            while cont != posicao:
                atual = atual.prox
                cont -= 1
            atual.conteudo = conteudo

        except AssertionError:
            raise PilhaException(f'Posicao inválida para a pilha atual com {self.__tamanho} elementos')

    def empilha(self, conteudo:any):
        #Empilha um novo nó "newno"
        newno = No(conteudo)
        newno.prox = self.__head
        self.__head = newno
        self.__tamanho += 1

    def desempilha(self)->any:
        #Desempilha o nó head atual
        if self.estaVazia():
            raise PilhaException(f'Pilha vazia.')
        head = self.__head.conteudo
        self.__head = self.__head.prox  
        self.__tamanho -= 1
        return head
        

    def __str__(self):
        s = '['
        atual = self.__head
        while atual != None:
            s+=f'{atual}, '
            atual = atual.prox
        s = f'{s[:len(s)-2]}]' #Isso daqui é só pra cortar a vírgula e espaço do último loop do while sem precisar fazer nenhum if chatinho(preguiça)
        return s

    def esvazia(self):
        self.__head = None
        self.__tamanho = 0

        '''
            ~ SOLUÇÕES PARA LÍNGUAS ALÉM DE PYTHON ~
        1.
        while not self.estaVazia():
            self.desempilha()

        2.
        try:
            while self.desempilha():
                pass
        except:
            pass
        '''