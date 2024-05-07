class Entregador:

    linha = 8
    coluna = 8

    def __init__(self, nome):

        self.nome = nome
        self.caminho = []
        self.coordenada_atual = (0,0)
        self.distancia_percorrida = 0
        self.comecou = False


    def ponto_de_partida(self, x, y):
       

        if (x < 0 or x > Entregador.linha-1) and (y < 0 or y > Entregador.coluna-1):
            print(f"X precisa estar entre 0 e {Entregador.linha - 1} e Y precisa estar entre 0 e {Entregador.coluna - 1}")
        elif x < 0 or x > Entregador.linha-1:
             print(f"X precisa estar entre 0 e {Entregador.linha - 1}")
        elif y < 0 or y > Entregador.coluna-1:
             print(f"Y precisa estar entre 0 e {Entregador.coluna - 1}")
        elif self.comecou is True:
            print("A entrega já começou, termine a atual para iniciar uma nova entrega")

        else:
            coordenada = (x,y)
            self.coordenada_atual = coordenada
            self.caminho.append(coordenada)
            self.comecou = True
    
    def termina_entrega(self):

        if self.comecou is False:
            print("É necessário primeiro definir o ponto de partida!")
        else:
            self.comecou = False
            self.mostra_percurso()
            distancia_percorrida = self.distancia_percorrida
            self.distancia_percorrida = 0
            self.caminho = []
            return distancia_percorrida

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
        print(f"Distância percorrida: {self.distancia_percorrida}")
            

    def move_norte_n_vezes(self, n):
        x = self.coordenada_atual[0]

        if x - n < 0:
            print("Não é possivel realizar o movimento, o entregadora ultrapassará o limite do mapa")
        else:
            while(n > 0):
                self.move_norte()
                n = n -1
        
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

    def move_sul_n_vezes(self, n):
        x = self.coordenada_atual[0]

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
    
class Carro(Entregador):

    consumo_medio = 5.50

    def __init__(self, nome):
        super().__init__(nome) 
    
    def consumo_total(self):
        if self.comecou is False:
            print("É necessário primeiro definir o ponto de partida!")
        else:
            return self.distancia_percorrida * Carro.consumo_medio
    

    def termina_entrega(self):
        distancia_percorrida = super().termina_entrega()
        print(f"Consumo Total: {distancia_percorrida * Carro.consumo_medio}")
        return distancia_percorrida
    
class Drone(Entregador):
    
    def __init__(self, nome):
        super().__init__(nome)
    
    def move_direto(self, x, y):
        if self.comecou is False:
            print("É necessário primeiro definir o ponto de partida!")
        elif (x < 0 or x > Entregador.linha-1) and (y < 0 or y > Entregador.coluna-1):
            print(f"X precisa estar entre 0 e {Entregador.linha - 1} e Y precisa estar entre 0 e {Entregador.coluna - 1}")
        elif x < 0 or x > Entregador.linha-1:
             print(f"X precisa estar entre 0 e {Entregador.linha - 1}")
        elif y < 0 or y > Entregador.coluna-1:
             print(f"Y precisa estar entre 0 e {Entregador.coluna - 1}")

        else:
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

""""
def menu():

    opc = 1

    while(opc != 0):
        print("====Menu====")
        print("1- Cadastrar Entrega")
        print("0- Sair")
        print("")
        opc = int(input("Digite uma opção: "))
    

        if opc == 1:
            nome = input("Digite o nome do entregador: ")
            while(opc != 0):
                print("===Opcoes===")
                print("1- A Pé")
                print("2- Carro")
                print("3- Drone")
                print("0- Voltar")
                print("")
                opc = int(input("Digite uma opção: "))
                if opc == 1:
                    menu_entregador(nome)

                elif opc == 2:
                    entregador = Carro(nome)

                elif opc == 3:
                    entregador = Drone(nome)

                elif opc != 0:
                    print("Opção Inválida, digite novamente!")

        elif opc != 0:
            print("Opção Inválida, digite novamente!")
        

def menu_entregador(nome):

    entregador = Entregador(nome)

    opc = 1

    while(opc != 0):
        print("====Menu====")
        print("1- Ponto de Partida")
        print("2- Terminar Entrega")
        print("3- Mover Norte")
        print("4- Mover Norte")
        print("5- Mover Norte")
        print("6- Mover Norte")
        print("0- Sair")
        print("")
        opc = int(input("Digite uma opção: "))

        if opc == 1:
            coordenadas = input("Digite o x e y: ")
            coordenadas = coordenadas.split()
            x = coordenadas[0]
            y = coordenadas[1]
            entregador.ponto_de_partida(x,y)
        if opc == 2:
            entregador.termina_entrega()
        if opc == 3:
            entregador.move_norte()
""" 
    
j = Drone("Juan")
print(j.nome)
j.ponto_de_partida(0,0)
j.move_direto(7,2)

j.termina_entrega()
    
