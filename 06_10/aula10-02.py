#polimorfismo: refere-se a capacidade de diferentes objetos responderem à mesma chamada de método ou função de maneiras específicas para seus tipos individuais.

class Pato:

    def nadar(self):
        return 'O Pato está nadando'
    def voar(self):
        return 'O Pato está voando'

class Aviao:

    def voar(self):
        return 'O Avião está voando'

class Fodase:
    def __init__(self):
        pass

def teste_voar(objeto):
    print(objeto.voar())

patinho = Pato()
tecoteco = Aviao()

teste_voar(patinho)
teste_voar(tecoteco)