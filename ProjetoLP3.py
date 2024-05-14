#Participantes: Maria Valentina e Juan Pablo

class Categoria:

    # Contador para os códigos de categoria
    id = 1

    def __init__(self, descricao):
        self.__codigo = Categoria.id
        Categoria.id+=1
        self.__descricao = descricao 


    #Retorna uma representação em string da categoria no formato "codigo descricao"
    def __str__(self):
        return f"{self.__codigo} {self.__descricao}"

    
    # Retorna o código da categoria.
    def get_codigo(self):
        return self.__codigo

    # Define um novo código para a categoria.
    def set_codigo(self, codigo):
        self.__codigo = codigo

    # Retorna a descrição da categoria.
    def get_descricao(self):
        return self.__descricao

    # Define uma nova descrição para a categoria.
    def set_descricao(self, descricao):
        self.__descricao = descricao


class Produto:
    
    # Contador do código do produto
    id = 1

    def __init__(self, descricao, valor, categoria):
        self.__codigo = Produto.id
        Produto.id += 1
        self.__descricao = descricao
        self.__valor = valor
        self.__categoria = categoria

    #Retorna uma representação em string do produto no formato "codigo descricao valor categoria"
    def __str__(self):

       return f"{self.__codigo} {self.__descricao} {self.__valor} {self.__categoria}"
    
    # Retorna o código do produto.
    def get_codigo(self):
        return self.__codigo

    # Define um novo código para o produto.
    def set_codigo(self, codigo):
        self.__codigo = codigo

    # Retorna a descrição do produto.
    def get_descricao(self):
        return self.__descricao

    # Define uma nova descrição para o produto.
    def set_descricao(self, descricao):
        self.__descricao = descricao

    # Retorna o valor do produto.
    def get_valor(self):
        return self.__valor

    #Define um novo valor para o produto.
    def set_valor(self, valor):
        self.__valor = valor

    # Retorna a categoria do produto.
    def get_categoria(self):
        return self.__categoria

    # Define uma nova categoria para o produto.
    def set_categoria(self, categoria):
        self.__categoria = categoria


# Imprime a lista de produtos com suas informações detalhadas.
def print_produtos(produtos):

    print("============CARDAPIO============")
    for produto in produtos:
        print("ID:", produto.get_codigo())
        print("Descrição:", produto.get_descricao())
        print("Valor:", produto.get_valor())
        print("Categoria:", produto.get_categoria().get_descricao())
        print("--------------------------------")


# Imprime a lista de categorias com suas informações detalhadas.
def print_categorias(categorias):

    print("---------------CATEGORIAS---------------")
    for categoria in categorias:
        print("ID:", categoria.get_codigo())
        print("Descrição:", categoria.get_descricao())
        print("--------------------------------")


# Adiciona uma nova categoria à lista de categorias e retorna a instância da nova categoria adicionada
def add_categoria(categoria):

    c = Categoria(input("Digite a descricao da categoria:"))
    categoria.append(c)
    print("Categoria cadastrada!")

    return c


# Adiciona um novo produto à lista de produtos de uma categoria específica (funcao criada pois foi especificado que para cada categoria criada é preciso atrelar pelo menos 3 produtos)
def add_produto_de_categoria(produtos, categoria):

    descricao = input("Digite a descrição do produto: ")
    valor = float(input("Digite o valor do produto: "))

    p = Produto(descricao, valor, categoria)
    produtos.append(p)
    print("Produto adicionado com sucesso!")



# Adiciona um novo produto à lista de produtos, permitindo a seleção de uma categoria existente.
def add_produtos_isolados(produto, categorias):

    descricao = (input("Digite a descricao do produto: "))
    valor = float(input("Digite o valor do produto: "))

    print("Categorias disponiveis:")
    for categoria in categorias:
        print(categoria.get_codigo(),"-",categoria.get_descricao())

    while True:

        categoria_codigo = int(input("Digite o código da categoria do produto: "))

        for categoria in categorias:
            if categoria.get_codigo() == categoria_codigo:
                categoria_produto = categoria
                break
        else:
            print("Categoria não encontrada. Por favor, digite um código de categoria válido.") # Continua pedindo a categoria enquanto nao fornecer uma valida
            continue

        break
        

        

    p = Produto(descricao, valor, categoria_produto)
    produto.append(p) 
    print("Produto cadastrado!")



if __name__ == "__main__":
    Categorias = []  # Lista para armazenar categorias
    Produtos = []   # Lista para armazenar produtos


    # Adiciona duas categorias e três produtos para cada categoria 
    for _ in range(2):
        nova_categoria = add_categoria(Categorias)
        add_produto_de_categoria(Produtos, nova_categoria)
        add_produto_de_categoria(Produtos, nova_categoria)
        add_produto_de_categoria(Produtos, nova_categoria)
    answer = 1

    # Pergunta se quer adicionar mais categorias. Enquanto a resposta for sim, adiciona mais uma categoria e mais tres produtos para cada uma
    while(answer == 1):
        answer = int(input("Deseja inserir mais categorias? 1 para sim e 0 para nao: "))
        if(answer == 1):
            nova_categoria = add_categoria(Categorias)
            add_produto_de_categoria(Produtos, nova_categoria)
            add_produto_de_categoria(Produtos, nova_categoria)
            add_produto_de_categoria(Produtos, nova_categoria)
            answer = int(input("Deseja inserir mais categorias? 1 para sim e 0 para nao: "))

    opcao = 1


    while(opcao):

        print("\n========MENU DE OPERAÇÕES========")
        print("1 - Adicionar categoria")
        print("2 - Adicionar produto")
        print("3 - Imprimir cardápio")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))
    
        if opcao == 1:
            nova_categoria = add_categoria(Categorias)
            add_produto_de_categoria(Produtos, nova_categoria)
            add_produto_de_categoria(Produtos, nova_categoria)
            add_produto_de_categoria(Produtos, nova_categoria)
            opcao = 1

        elif opcao == 2:
            add_produtos_isolados(Produtos, Categorias)
            opcao = 1

        elif opcao == 3:
            print_produtos(Produtos)

        elif opcao > 3 and opcao < 0:
            print("Opcao nao encontrada! Favor, escolher alguma dentre as apresentadas no menu.")
            opcao = 1
            
    
                



