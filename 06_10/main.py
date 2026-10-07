from database import inicializar_banco
from carro import Carro

def main():
    inicializar_banco()
    marca=input('marca: ')
    modelo=input('modelo: ')
    ano=int(input('Ano: '))
    novo_carro = Carro(marca, modelo, ano)
    print(f'Registro inserido: {novo_carro.insert()}')
    novo_carro.consulta()

if __name__ == '__main__':
    main()