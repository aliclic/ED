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
    
        cursor = self.__topo #Armazene o nó atual numa variável 'cursor'
        while (CONDIÇÃO): #EX: cursor != None
            cursor = cursor.prox #Atualize o valor do cursor para ser o próximo nó


        ==================================================================================

        deve ter mais formas de mexer com encadeamento ...
        fazer a topo apontar pro tail e o tail apontar pro topo faz uma estrutura circular
        cabecinha com bundinha & bundinha com cabecinha  :)

    '''

    def __init__(self):
        self.__topo = None
        self.__tamanho = 0

    def estaVazia(self)->bool:
        # verifica se a Pilha está vazia, retornando True or False
        return self.__topo == None

    def tamanho(self)->int:
        # retorna o tamanho da Pilha
        return self.__tamanho

    def __len__(self)->int:
        # retorna o tamanho da Pilha
        return self.__tamanho

    def elemento(self, posicao:int)->any:
        # retorna a carga armazenada no nó na 'posição'
        try:
            assert posicao > 0 and posicao <= self.__tamanho
            cont = self.__tamanho
            atual = self.__topo
            while cont != posicao:
                atual = atual.prox
                cont -= 1
            return atual.conteudo
        except AssertionError:
            raise PilhaException(f'Posicao inválida para a pilha atual com {self.__tamanho} elementos')
    
    def busca(self, conteudo:any)->int: 
        # retorna a posição do nó cuja conteúdo corresponde à consulta
        cont = 0
        atual = self.__topo
        while atual != None:
            if atual.conteudo == conteudo:
                return self.__tamanho - cont # 30 - 3  = 27
            atual = atual.prox
            cont += 1
        raise  PilhaException(f'Valor {conteudo} não está na pilha')

    def modificar(self, posicao:int, conteudo: any):
        # substitui o conteúdo do elemento na posição N
        try:
            assert posicao > 0 and posicao <= self.__tamanho
            cont = self.__tamanho
            atual = self.__topo
            while cont != posicao:
                atual = atual.prox
                cont -= 1
            atual.conteudo = conteudo
        
        except AssertionError:
            raise PilhaException(f'Posicao inválida para a pilha atual com {self.__tamanho} elementos')

    def empilha(self, conteudo:any):
        # Empilha um novo nó "newno"
        newno = No(conteudo)
        newno.prox = self.__topo
        self.__topo = newno
        self.__tamanho += 1
 
    def desempilha(self)->any:
        # Desempilha o nó topo atual
        if self.estaVazia():
            raise PilhaException(f'Pilha vazia!!!.')
        topo = self.__topo
        self.__topo = self.__topo.prox
        self.__tamanho -= 1
        return topo

    def __str__(self):
        s = '['
        atual = self.__topo
        while atual != None:
            s += f'{atual}, '
            atual = atual.prox
        s = f'{s[:len(s)-2]}]' #Isso daqui é só pra cortar a vírgula e espaço do último loop do while sem precisar fazer nenhum if chatinho(preguiça)
        return s

    def esvazia(self):
        self.__topo = None
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
    def concatena(self, outraPilha:'Pilha'):
        #Inverter a pilha "outraPilha"
        paux = Pilha()
        while(not outraPilha.estaVazia()):
            paux.empilha( outraPilha.desempilha())
        # descarregando paux na pilha que recebeu a chamada
        while(not paux.estaVazia()):
            self.empilha( paux.desempilha())