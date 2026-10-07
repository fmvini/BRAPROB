class Veiculo:

    def __init__(self, nome):
        self.nome = nome

    def dirigir(self):
        print(f'{self.nome} está dirigindo um Veículo.')

class Voador:
    def voar(self):
        print(f'{self.nome} está voando.')

class Flutuante:
    def flutuar(self):
        print(f'{self.nome} está flutuando.')

class VeiculoAnfibio(Veiculo, Voador, Flutuante):
    def __init___(self, nome):
        super().__init__(nome)

carro_anfibio = VeiculoAnfibio('Carro anfibio aurax 2000')

carro_anfibio.voar()
carro_anfibio.dirigir()
carro_anfibio.flutuar()