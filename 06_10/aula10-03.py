#Modificadores de acesso ou visibilidade:
#Fracamente privado -> _atributo
#Fortemente privado -> __atributo

class Pessoa:

    def __init__(self, nome, idade):
        self.__nome = nome
        self._idade = idade

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self._idade

nova_pessoa = Pessoa('Ana', '20')
print(nova_pessoa._idade)
print(nova_pessoa.get_nome())
print(nova_pessoa.get_idade())
