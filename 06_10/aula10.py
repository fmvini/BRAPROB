#herança:
#1 simples - uma classe herda de uma unica classe base (ancestral)
#2 multipla - uma classe herda de mais de uma classe base, permitindo a agregação dos comportamentos de diferentes origens.

class Animal:
    def __init__(self, apelido):
        print(f'Classe Animal: {apelido}')

class Mamifero(Animal):
    def __init__(self, apelido):
        super().__init__(apelido)
        print(f'Classe Mamifero: {apelido}')

class Naovoadores(Mamifero):
    def __init__(self, apelido):
        super().__init__(apelido)
        print(f'Classe NãoVoadores: {apelido}')

class Naoaquaticos(Mamifero):
    def __init__(self, apelido):
        super().__init__(apelido)
        print(f'Classe NãoAquaticos: {apelido}')

class Dog(Naoaquaticos, Naovoadores):
    def __init__(self, apelido):
        super().__init__(apelido)
        print(f'Classe NãoVoadores e NãoAquaticos: {apelido}')

cachorro = Dog('Apolo')