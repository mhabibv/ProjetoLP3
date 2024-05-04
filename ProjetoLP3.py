#Participantes: Maria Valentina e Juan Pablo

class Categoria:
    id = 1

    def __init__(self, descricao):
        self.__codigo = Categoria.id
        Categoria.id+=1
        self.__descricao = descricao 

    def __str__(self):
        return f"{self.__codigo} {self.__descricao}"

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao


class Produto:
    
    #Atributo que serve para contar o código do produto
    id = 1

    def __init__(self, descricao, valor, categoria):
        self.__codigo = Produto.id
        Produto.id += 1
        self.__descricao = descricao
        self.__valor = valor
        self.__categoria = categoria

    def __str__(self):

       return f"{self.__codigo} {self.__descricao} {self.__valor} {self.__categoria}"
    

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        self.__valor = valor

    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, categoria):
        self.__categoria = categoria


Categorias = []
Produtos = []

c = Categoria("Comida")
Categorias.append(c)

p = Produto("Biscoito", 7.50, c)

print(p)




