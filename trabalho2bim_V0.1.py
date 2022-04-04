# IMPLEMENTAÇÃO DAS CLASSES
class Cidade:
    def __init__(self, nome, distanciaCapital, *distanciaVizinhos, vizinhos):
        self.nome = nome
        self.distanciaVizinhos = list(distanciaVizinhos)
        self.vizinhos = list(vizinhos)
        self.proximo = None
        self.distanciaCapital = distanciaCapital  # distancia em linha reta da cidade ate a capital, Vitoria


class Fila:
    """Essa classe implementa uma fila utilizando uma lista. Utilizamos
    dois ponteiros, um para indicar o primeiro elemento da fila e outro
    para indicar o último elemento"""

    def __init__(self):
        self.conjunto = []
        self.primeiro = None
        self.ultimo = None

    def inserir_elemento(self, elemento):
        """Insere um elemento na fila.
        Trata os casos da fila estar vazia e da fila ja conter elementos."""
        if len(self.conjunto) == 0:
            self.conjunto.append(elemento)
            self.primeiro = elemento
            self.ultimo = elemento
        else:
            self.conjunto.append(elemento)
            self.ultimo.proximo = elemento
            self.ultimo = elemento

    def remover_elemento(self):
        """Remove o primeiro elemento da fila"""
        if len(self.conjunto) != 0:
            self.primeiro = self.primeiro.proximo
            first = self.conjunto.pop(0)
            return first


def menor_distancia(cidade):
    return cidade.distanciaCapital


def menor_distancia_heuristica(cidade_atual, cities):
    distancia_vizinhos_capital = []
    indice_vizinhos = []
    vizinhos = []
    indice = 0
    for i in cidade_atual.vizinhos:
        vizinhos.append(i)
    for i, nome in enumerate(cities):
        if nome['nome'] in vizinhos:
            indice_vizinhos.append(i)
    for linha in cities:
        if linha['codigo'] in indice_vizinhos:
            distancia_vizinhos_capital.append(cities[linha['codigo']]['cidade'].distanciaCapital)
    distancia_atual_vizinhos = list(cidade_atual.distanciaVizinhos)
    #    distancia_atual_vizinhos = list(cidade_atual.distanciaVizinhos[0])
    soma_distancias = []
    for i in range(len(distancia_vizinhos_capital)):
        soma_distancias.append(distancia_atual_vizinhos[0][i] + distancia_vizinhos_capital[i])

    for j, soma in enumerate(soma_distancias):
        if soma == min(soma_distancias):
            indice = j
    return indice_vizinhos[indice]


def trabalho():
    # cadastro das cidades e seus vizinhos
    cities = [{"codigo": 0, "nome": "Vila Velha", "cidade": Cidade('Vila Velha', 5.18, (5.18, 11.54, 30.57), vizinhos=('Vitória', 'Cariacica', 'Guarapari'))},
              {'codigo': 1, 'nome': 'Vitoria', 'cidade': Cidade('Vitoria', 0.0, (4.76, 6.73, 19.87), vizinhos=('Vila Velha', 'Cariacica', 'Serra'))},
              {'codigo': 2, 'nome': 'Serra', 'cidade': Cidade('Serra', 19.87, (19.87, 21.47, 25.47), vizinhos=('Vitoria', 'Cariacica', 'Fundao'))},
              {'codigo': 3, 'nome': 'Cariacica','cidade': Cidade('Cariacica', 6.73, (6.73, 9.39, 11.54, 21.47,  25.51), vizinhos=('Vitoria', 'Viana', 'Vila Velha', 'Serra', 'Santa Leopoldina'))},
              {'codigo': 4, 'nome': 'Viana', 'cidade': Cidade('Viana', 11.42, (9.39, 22.64, 24.20), vizinhos=('Cariacica', 'Guarapari', 'Domingos Martins'))},
              {'codigo': 5, 'nome': 'Guarapari', 'cidade': Cidade('Guarapari', 31.98, (22.64, 30.57, 33.06, 76.86), vizinhos=('Viana', 'Vila Velha', 'Anchieta', 'Cachoeiro do Itapemirim'))},##erro
              {'codigo': 6, 'nome': 'Fundao', 'cidade': Cidade('Fundao', 41.22, (25.47, 18.76, 20.25, 20.26), vizinhos=('Serra', 'Aracruz', 'Santa Teresa', 'Joao Neiva'), )},
              {'codigo': 7, 'nome': 'Domingos Martins', 'cidade': Cidade('Domingos Martins', 35.10, (24.20, 5.68), vizinhos=('Viana', 'Marechal Floriano'))},
              {'codigo': 8, 'nome': 'Marechal Floriano', 'cidade': Cidade('Marechal Floriano', 38.40, (5.68, 36.98), vizinhos=('Domingos Martins', 'Pedra Azul'))},
              {'codigo': 9, 'nome': 'Pedra Azul', 'cidade': Cidade('Pedra Azul', 73.59, (36.98, 12.58), vizinhos=('Marechal Floriano', 'Venda Nova do Imigrante'))},
              {'codigo': 10, 'nome': 'Venda Nova do Imigrante', 'cidade': Cidade('Venda Nova do Imigrante', 83.84, (12.58, 33.17), vizinhos=('Pedra Azul', 'Castelo'))},
              {'codigo': 11, 'nome': 'Castelo', 'cidade': Cidade('Castelo', 97.71, (33.17, 27.01), vizinhos=('Venda Nova do Imigrante', 'Cachoeiro do Itapemirim'))},
              {'codigo': 12, 'nome': 'Santa Leopoldina', 'cidade': Cidade('Santa Leopoldina', 30.76, (25.51,), vizinhos=('Cariacica',))},
              {'codigo': 13, 'nome': 'Anchieta', 'cidade': Cidade('Anchieta', 64.28, (33.06,), vizinhos=('Guarapari',))},
              {'codigo': 14, 'nome': 'Cachoeiro do Itapemirim', 'cidade': Cidade('Cachoeiro do Itapemirim', 101.92, (76.86, 27.01), vizinhos=('Guarapari', 'Castelo'))},
              {'codigo': 15, 'nome': 'Aracruz', 'cidade': Cidade('Aracruz', 53.59, (18.76,), vizinhos=('Fundao',))},
              {'codigo': 16, 'nome': 'Santa Teresa', 'cidade': Cidade('Santa Teresa', 49.23, (20.25,), vizinhos=('Fundao',))},
              {'codigo': 17, 'nome': 'Joao Neiva', 'cidade': Cidade('Joao Neiva', 60.88, (20.26,), vizinhos=('Fundao',))}]

    """ CONSIDERAMOS QUE CADA CIDADE FAZ FRONTEIRA COM AS OUTRAS CUJO VALOR NA MATRIZ EH IGUAL A 1.
    CONSIDERAMOS QUE UMA CIDADE NAO FAZ FRONTEIRA COM ELA MESMA (DIAGONAL PRINCIPAL = 0)"""
    fronteiras = [[0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # vila velha 0
                  [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # vitoria 1
                  [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # serra 2
                  [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # cariacica 3
                  [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # viana 4
                  [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],  # guarapari 5
                  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],  # fundao 6
                  [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # domingos martins 7
                  [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # marechal floriano 8
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # pedra azul 9
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # venda nova 10
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],  # castelo 11
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # sta leopoldina 12
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # anchieta 13
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # cachoeiro 14
                  [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # aracruz 15
                  [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # sta teresa 16
                  [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # joao neiva 17

    # estrutura para guardar as cidades visitadas no percurso
    visitadas = []

    # destino é fixado como a capital, Vitória
    destino = 1

    # menu para o usuario escolher o tipo de busca
    while True:
        print('Opcao 1: Busca gulosa \n'
              'Opcao 2: Busca A* \n')
        try:
            tipo_busca = int(input('Digite a opcao desejada: '))
            break
        except ValueError:
            print('O valor digitado deve ser um numero inteiro.\n')

    # exibir as opções de cidades para o usuário
    for i, cidade in enumerate(cities):
        print(i, cidade['cidade'].nome)

    while True:
        try:
            origem = int(input("Digite o codigo da cidade de origem: "))
            break
        except ValueError:
            print('Codigo da origem deve ser um numero inteiro.\n')
    if tipo_busca == 1:
        indice = origem
        fila = Fila()
        fila.inserir_elemento(cities[indice]['cidade'])  # adiciona o objeto CIDADE de origem na fila
        while True:
            if indice == destino:
                visitadas.append(cities[indice]['cidade'].nome)
                print(f'O caminho percorrido foi: {[nome for nome in visitadas]}')
                break
            else:
                filhos = [i for i, fronteiras[indice][i] in enumerate(fronteiras[indice]) if fronteiras[indice][i] == 1]
                # ENFILEIRANDO OS FILHOS
                for filho in filhos:
                    if cities[filho]['nome'] in visitadas or cities[filho]['cidade'] in fila.conjunto:
                        continue
                    else:
                        fila.inserir_elemento(cities[filho]['cidade'])
                if len(fila.conjunto) > 0:
                    removido = fila.remover_elemento()
                    visitadas.append(removido.nome)
                    fila.conjunto.sort(key=menor_distancia)
                    fila.primeiro = fila.conjunto[0]
                    fila.ultimo = fila.conjunto[-1]
                else:
                    print('Nao foi possivel chegar ao destino')
                    break
                for cidade in cities:
                    if cidade['nome'] == fila.primeiro.nome:
                        indice = cidade['codigo']
                        break
    if tipo_busca == 2:
        indice = origem
        fila = Fila()
        fila.inserir_elemento(cities[indice]['cidade'])  # adiciona o objeto CIDADE de origem na fila
        while True:
            if indice == destino:
                visitadas.append(cities[indice]['cidade'].nome)
                print(f'O caminho percorrido foi: {[nome for nome in visitadas]}')
                break
            else:
                filhos = [i for i, fronteiras[indice][i] in enumerate(fronteiras[indice]) if fronteiras[indice][i] == 1]
                # ENFILEIRANDO OS FILHOS
                for filho in filhos:
                    if cities[filho]['nome'] in visitadas or cities[filho]['cidade'] in fila.conjunto:
                        continue
                    else:
                        fila.inserir_elemento(cities[filho]['cidade'])  # adicionou os vizinhos na fila
                if len(fila.conjunto) > 0:
                    removido = fila.remover_elemento()
                    visitadas.append(removido.nome)
                    melhor = menor_distancia_heuristica(removido, cities)
                    fila.conjunto.clear()
                    fila.primeiro = None
                    fila.ultimo = None
                    fila.inserir_elemento(cities[melhor]['cidade'])
                #                    fila.conjunto.sort(key=lambda x: menor_distancia_heuristica(removido, cities))
                else:
                    print('Nao foi possivel chegar ao destino')
                    break
                for cidade in cities:
                    if cidade['nome'] == fila.primeiro.nome:
                        indice = cidade['codigo']
                        break


trabalho()
