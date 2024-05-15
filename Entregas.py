class Entregador:

    # Define o tamanho padrão do mapa
    linha = 8
    coluna = 8

    # Inicializa um entregador com nome, coordenadas, etc.
    def __init__(self, nome):

        self.nome = nome
        self.caminho = []  # Lista para armazenar o percurso
        self.coordenada_atual = (0,0)  # Coordenada inicial
        self.distancia_percorrida = 0  # Distância percorrida
        self.comecou = False  # Indicador se a entrega já começou

    # Define o ponto de partida para a entrega
    def ponto_de_partida(self, x, y):
        # Verifica se a entrega já começou
        if self.comecou is True:
            print("A entrega já começou, termine a atual para iniciar uma nova entrega")

        # Verifica se as coordenadas estão dentro dos limites do mapa
        elif (x < 0 or x > Entregador.linha-1) and (y < 0 or y > Entregador.coluna-1):
            print(f"X precisa estar entre 0 e {Entregador.linha - 1} e Y precisa estar entre 0 e {Entregador.coluna - 1}")
        elif x < 0 or x > Entregador.linha-1:
             print(f"X precisa estar entre 0 e {Entregador.linha - 1}")
        elif y < 0 or y > Entregador.coluna-1:
             print(f"Y precisa estar entre 0 e {Entregador.coluna - 1}")

        else:
            coordenada = (x,y)
            self.coordenada_atual = coordenada
            self.caminho.append(coordenada)
            self.comecou = True
    
        
    # Encerra a entrega, mostrando o percurso e a distância percorrida
    def termina_entrega(self):

        # Verifica se a entrega não começou

        if self.comecou is False:
            print("É necessário primeiro definir o ponto de partida!")
        # Reinicia as variaveis e mostra o percurso 
        else:
            self.comecou = False 
            self.mostra_percurso()
            distancia_percorrida = self.distancia_percorrida
            self.distancia_percorrida = 0
            self.caminho = []
            return distancia_percorrida
        
    # Mostra o percurso percorrido pelo entregador no mapa
    def mostra_percurso(self):
        for i in range(Entregador.linha):
            for j in range(Entregador.coluna):
                coordenada = (i,j)
                if coordenada in self.caminho:
                    if coordenada == self.caminho[0]:
                        print(" 0 ", end = "")
                    elif coordenada == self.caminho[-1]:
                        print(" 1 ", end = "")
                    else:
                        print(" X ", end = "")
                else:
                    print(" □ ", end="")
            print("") 
        print(f"Coordenada atual: {self.coordenada_atual[0], self.coordenada_atual[1]}")
        print(f"Distância percorrida: {self.distancia_percorrida}")
            
    # Move o entregador para o norte n vezes
    def move_norte_n_vezes(self, n):
        x = self.coordenada_atual[0]

        if self.comecou is False:
            print("É necessário primeiro definir o ponto de partida!")

        if x - n < 0:
            print("Não é possivel realizar o movimento, o entregador ultrapassará o limite do mapa")
        else:
            while(n > 0):
                self.move_norte()
                n = n -1

    # Move o entregador uma casa para o norte
    def move_norte(self):
        x = self.coordenada_atual[0]
        y = self.coordenada_atual[1]       

        if self.comecou is False:
            print("É necessário primeiro definir o ponto de partida!")

        elif x == 0:
            print("Não é possivel realizar o movimento, o entregador está no limite do mapa")
        else:
            x = x - 1
            coordenada = (x,y)
            self.coordenada_atual = coordenada
            self.caminho.append(coordenada)
            self.distancia_percorrida += 1

    # Outros métodos de movimento (sul, leste, oeste) seguem uma lógica semelhante

    def move_sul_n_vezes(self, n):
        x = self.coordenada_atual[0]

        if self.comecou is False:
            print("É necessário primeiro definir o ponto de partida!")

        if x + n > Entregador.linha - 1:
            print("Não é possivel realizar o movimento, o entregadora ultrapassará o limite do mapa")
        else:
            while(n > 0):
                self.move_sul()
                n = n -1
        
    def move_sul(self):
        x = self.coordenada_atual[0]
        y = self.coordenada_atual[1]       

        if self.comecou is False:
            print("É necessário primeiro definir o ponto de partida!")

        elif x == Entregador.linha - 1:
            print("Não é possivel realizar o movimento, o entregador está no limite do mapa")
        else:
            x = x + 1
            coordenada = (x,y)
            self.coordenada_atual = coordenada
            self.caminho.append(coordenada)
            self.distancia_percorrida += 1

    def move_leste_n_vezes(self, n):
        y = self.coordenada_atual[1]

        if self.comecou is False:
            print("É necessário primeiro definir o ponto de partida!")

        if  y + n > Entregador.coluna - 1:
            print("Não é possivel realizar o movimento, o entregadora ultrapassará o limite do mapa")
        else:
           while(n > 0):
                self.move_leste()
                n = n -1


    def move_leste(self):
        x = self.coordenada_atual[0]
        y = self.coordenada_atual[1]       

        if self.comecou is False:
            print("É necessário primeiro definir o ponto de partida!")

        elif y == Entregador.coluna - 1:
            print("Não é possivel realizar o movimento, o entregador está no limite do mapa")
        else:
            y = y + 1
            coordenada = (x,y)
            self.coordenada_atual = coordenada
            self.caminho.append(coordenada)
            self.distancia_percorrida += 1

    def move_oeste_n_vezes(self, n):
        y = self.coordenada_atual[1]

        if self.comecou is False:
            print("É necessário primeiro definir o ponto de partida!")

        if  y - n < 0:
            print("Não é possivel realizar o movimento, o entregadora ultrapassará o limite do mapa")
        else:
            while(n > 0):
                self.move_oeste()
                n = n -1
    
    def move_oeste(self):
        x = self.coordenada_atual[0]
        y = self.coordenada_atual[1]       

        if self.comecou is False:
            print("É necessário primeiro definir o ponto de partida!")

        elif y == 0:
            print("Não é possivel realizar o movimento, o entregador está no limite do mapa")
        else:
            y = y - 1
            coordenada = (x,y)
            self.coordenada_atual = coordenada
            self.caminho.append(coordenada)
            self.distancia_percorrida += 1
    
# A classe Carro herda de Entregador
class Carro(Entregador):

    consumo_medio = 5.50  # Define o consumo médio do carro

    # Inicializa um carro chamando o construtor da classe Entregador
    def __init__(self, nome):
        super().__init__(nome) 
    
    # Calcula o consumo total de combustível
    def consumo_total(self):
        if self.comecou is False:
            print("É necessário primeiro definir o ponto de partida!")
        else:
            return self.distancia_percorrida * Carro.consumo_medio
    
    # Sobrescreve o método termina_entrega() para imprimir o consumo total antes de retornar a distância percorrida
    def termina_entrega(self):
        distancia_percorrida = super().termina_entrega()
        print(f"Consumo Total: {distancia_percorrida * Carro.consumo_medio}")
        return distancia_percorrida

# A classe Drone herda de Entregador
class Drone(Entregador):
    
    # Inicializa um drone chamando o construtor da classe Entregador
    def __init__(self, nome):
        super().__init__(nome)
    
    # Inicializa um drone chamando o construtor da classe Entregador
    def move_direto(self, x, y):
        # Verifica se a entrega já começou e se as coordenadas estão dentro dos limites do mapa
        if self.comecou is False:
            print("É necessário primeiro definir o ponto de partida!")
        elif (x < 0 or x > Entregador.linha-1) and (y < 0 or y > Entregador.coluna-1):
            print(f"X precisa estar entre 0 e {Entregador.linha - 1} e Y precisa estar entre 0 e {Entregador.coluna - 1}")
        elif x < 0 or x > Entregador.linha-1:
             print(f"X precisa estar entre 0 e {Entregador.linha - 1}")
        elif y < 0 or y > Entregador.coluna-1:
             print(f"Y precisa estar entre 0 e {Entregador.coluna - 1}")

        else:
            # Move o drone diagonalmente até alcançar a linha ou coluna desejada
            x_atual = self.coordenada_atual[0]
            y_atual = self.coordenada_atual[1]

            while x != x_atual and y != y_atual:

                if x < x_atual and y < y_atual:
                    self.move_diagonal_sup_esq()

                elif x < x_atual and y > y_atual:
                    self.move_diagonal_sup_dir()

                elif x > x_atual and y < y_atual:
                    self.move_diagonal_inf_esq()

                elif x > x_atual and y > y_atual:
                    self.move_diagonal_inf_dir()


                x_atual = self.coordenada_atual[0]
                y_atual = self.coordenada_atual[1]

            # Após mover diagonalmente, move-se horizontalmente ou verticalmente conforme necessário
            if not (y == y_atual and x == x_atual):

                if x == x_atual:

                    while(y != y_atual):
                        if y < y_atual:
                            self.move_oeste()
                            
                        else:
                            self.move_leste()
                            
                        y_atual = self.coordenada_atual[1]

                else:
                    while(x != x_atual):
                        if x < x_atual:
                            self.move_norte()
                            
                        else:
                            self.move_sul()

                        x_atual = self.coordenada_atual[0]

    # Outros métodos de movimento diagonal (sup_esq, sup_dir, inf_esq, inf_dir) foram criados para servir de auxiliar para o mover direto
    #mas também podem ser utilizadas separadamente

    def move_diagonal_sup_dir(self):   
        x = self.coordenada_atual[0]
        y = self.coordenada_atual[1]       

        if self.comecou is False:
            print("É necessário primeiro definir o ponto de partida!")
        elif x == 0 or y == Entregador.coluna - 1:
            print("Não é possivel realizar o movimento, o entregador está no limite do mapa")
        else:
            x = x - 1
            y = y + 1
            coordenada = (x,y)
            self.coordenada_atual = coordenada
            self.caminho.append(coordenada)
            self.distancia_percorrida += 1
            


    def move_diagonal_inf_dir(self): 
        x = self.coordenada_atual[0]
        y = self.coordenada_atual[1]       

        if self.comecou is False:
            print("É necessário primeiro definir o ponto de partida!")
        elif x == Entregador.linha - 1 or y == Entregador.coluna - 1:
            print("Não é possivel realizar o movimento, o entregador está no limite do mapa")
        else:
            x = x + 1
            y = y + 1
            coordenada = (x,y)
            self.coordenada_atual = coordenada
            self.caminho.append(coordenada)
            self.distancia_percorrida += 1


    def move_diagonal_sup_esq(self):
        x = self.coordenada_atual[0]
        y = self.coordenada_atual[1]       

        if self.comecou is False:
            print("É necessário primeiro definir o ponto de partida!")
        elif x == 0 or y == 0:
            print("Não é possivel realizar o movimento, o entregador está no limite do mapa")
        else:
            x = x - 1
            y = y - 1
            coordenada = (x,y)
            self.coordenada_atual = coordenada
            self.caminho.append(coordenada)
            self.distancia_percorrida += 1

    def move_diagonal_inf_esq(self):
        x = self.coordenada_atual[0]
        y = self.coordenada_atual[1]       

        if self.comecou is False:
            print("É necessário primeiro definir o ponto de partida!")
        elif x == Entregador.linha - 1 or y == 0:
            print("Não é possivel realizar o movimento, o entregador está no limite do mapa")
        else:
            x = x + 1
            y = y - 1
            coordenada = (x,y)
            self.coordenada_atual = coordenada
            self.caminho.append(coordenada)
            self.distancia_percorrida += 1

# Função para exibir o menu e interagir com o usuário
def menu():
    while True:
        print("==== Menu ====")
        print("1- Cadastrar Entrega")
        print("0- Sair")
        opc = int(input("Digite uma opção: "))

        if opc == 1:
            nome = input("Digite o nome do entregador: ")
            print("Escolha o tipo de entregador: ")
            print("1- A Pé")
            print("2- Carro")
            print("3- Drone")
            print("0- Voltar")
            tipo_entregador = int(input("Digite uma opção: "))

            # Cria o entregador correspondente com base na escolha do usuário
            if tipo_entregador == 1:
                entregador = Entregador(nome)
                menu_entregador(entregador, "A Pé")
            elif tipo_entregador == 2:
                entregador = Carro(nome)
                menu_entregador(entregador, "Carro")
            elif tipo_entregador == 3:
                entregador = Drone(nome)
                menu_drone(entregador)
            elif tipo_entregador == 0:
                continue
            else:
                print("Opção inválida!")
                continue


        elif opc == 0:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!")            

        
# Função para exibir o menu do entregador e interagir com o usuário
def menu_entregador(entregador, string):
    
    while True:
        print(f"==== Menu {string} ====")
        print("1- Definir Ponto de Partida")
        print("2- Terminar Entrega")
        print("3- Mover para o Norte")
        print("4- Mover para o Sul")
        print("5- Mover para o Leste")
        print("6- Mover para o Oeste")
        print("7- Mostra percurso")
        print("8- Coordenada Atual")
        print("0- Voltar ao Menu Principal")

        opc_entregador = int(input("Digite uma opção: "))

        # Realiza a ação correspondente com base na escolha do usuário
        if opc_entregador == 1:
            if entregador.comecou is True:
                print("A entrega já começou, termine a atual para iniciar uma nova entrega")
            else:
                x = int(input("Digite a coordenada X: "))
                y = int(input("Digite a coordenada Y: "))
                entregador.ponto_de_partida(x, y)
        elif opc_entregador == 2:
            if entregador.comecou is False:
                print("É necessário primeiro definir o ponto de partida!")
            else:
                entregador.termina_entrega()
        elif opc_entregador == 3:
            if entregador.comecou is False:
                print("É necessário primeiro definir o ponto de partida!")
            else:
                n = int(input("Digite quantas casas quer mover para o Norte: "))
                entregador.move_norte_n_vezes(n)
        elif opc_entregador == 4:
            if entregador.comecou is False:
                print("É necessário primeiro definir o ponto de partida!")
            else:
                n = int(input("Digite quantas casas quer mover para o Sul: "))
                entregador.move_sul_n_vezes(n)
        elif opc_entregador == 5:
            if entregador.comecou is False:
                print("É necessário primeiro definir o ponto de partida!")
            else:    
                n = int(input("Digite quantas casas quer mover para o Leste: "))
                entregador.move_leste_n_vezes(n)
        elif opc_entregador == 6:
            if entregador.comecou is False:
                print("É necessário primeiro definir o ponto de partida!")
            else:
                n = int(input("Digite quantas casas quer mover para o Oeste: "))
                entregador.move_oeste_n_vezes(n)
        elif opc_entregador == 7:
            if entregador.comecou is False:
                print("É necessário primeiro definir o ponto de partida!")
            else:
                entregador.mostra_percurso()
        elif opc_entregador == 8:
            if entregador.comecou is False:
                print("É necessário primeiro definir o ponto de partida!")
            else:
                print(f"X: {entregador.coordenada_atual[0]}, Y: {entregador.coordenada_atual[1]}")


        elif opc_entregador == 0:
            input("Pressione Enter para continuar...")
            break
        else:
            print("Opção inválida!")

        input("Pressione Enter para continuar...")


# Função para exibir o menu do drone e interagir com o usuário
def menu_drone(entregador):
    while True:
        print(f"==== Menu Drone ====")
        print("1- Definir Ponto de Partida")
        print("2- Terminar Entrega")
        print("3- Mover para o Norte")
        print("4- Mover para o Sul")
        print("5- Mover para o Leste")
        print("6- Mover para o Oeste")
        print("7- Mostra percurso")
        print("8- Move Direto")
        print("9- Coordenada Atual")
        print("0- Voltar ao Menu Principal")

        opc_entregador = int(input("Digite uma opção: "))

        # Realiza a ação correspondente com base na escolha do usuário
        if opc_entregador == 1:
            if entregador.comecou is True:
                print("A entrega já começou, termine a atual para iniciar uma nova entrega")
            else:
                x = int(input("Digite a coordenada X: "))
                y = int(input("Digite a coordenada Y: "))
                entregador.ponto_de_partida(x, y)
        elif opc_entregador == 2:
            if entregador.comecou is False:
                print("É necessário primeiro definir o ponto de partida!")
                
            else:
                entregador.termina_entrega()
        elif opc_entregador == 3:
            if entregador.comecou is False:
                print("É necessário primeiro definir o ponto de partida!")
            else:
                n = int(input("Digite quantas casas quer mover para o Norte: "))
                entregador.move_norte_n_vezes(n)
        elif opc_entregador == 4:
            if entregador.comecou is False:
                print("É necessário primeiro definir o ponto de partida!")
            else:
                n = int(input("Digite quantas casas quer mover para o Sul: "))
                entregador.move_sul_n_vezes(n)
        elif opc_entregador == 5:
            if entregador.comecou is False:
                print("É necessário primeiro definir o ponto de partida!")
            else:    
                n = int(input("Digite quantas casas quer mover para o Leste: "))
                entregador.move_leste_n_vezes(n)
        elif opc_entregador == 6:
            if entregador.comecou is False:
                print("É necessário primeiro definir o ponto de partida!")
            else:
                n = int(input("Digite quantas casas quer mover para o Oeste: "))
                entregador.move_oeste_n_vezes(n)
        elif opc_entregador == 7:
            if entregador.comecou is False:
                print("É necessário primeiro definir o ponto de partida!")
            else:
                entregador.mostra_percurso()
        elif opc_entregador == 8:
            if entregador.comecou is False:
                print("É necessário primeiro definir o ponto de partida!")
            else:
                x = int(input("Digite a coordenada X: "))
                y = int(input("Digite a coordenada Y: "))
                entregador.move_direto(x,y)
        elif opc_entregador == 9:
            if entregador.comecou is False:
                print("É necessário primeiro definir o ponto de partida!")
            else:
                print(f"X: {entregador.coordenada_atual[0]}, Y: {entregador.coordenada_atual[1]}")


        elif opc_entregador == 0:
            input("Pressione Enter para continuar...")
            break
        else:
            print("Opção inválida!")

        input("Pressione Enter para continuar...")


# Chamada da função principal para iniciar o programa
menu()
    


    
