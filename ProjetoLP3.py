#Participantes: Maria Valentina e Juan Pablo

class Categorias:

    def __init__(self, codigo, descricao):
        self.__codigo = codigo
        self.__descricao = descricao 

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao


class Produto:
    
    def __init__(self, codigo, descricao, valor, categoria):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor
        self.__categoria = categoria

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


