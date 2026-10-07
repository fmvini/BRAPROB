from database import cursor, conn

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = int(ano)
    def insert(self):
        cursor.execute('INSERT INTO carro (marca, modelo, ano) VALUES (?, ?, ?)', (self.marca, self.modelo, self.ano))
        conn.commit()
        return cursor.lastrowid
    
    def update(self, id):
        cursor.execute('UPDATE carro SET marca=?, modelo=?, ano=? WHERE id=?', (self.marca, self.modelo, self.ano, id))
        conn.commit()

    @staticmethod
    def consulta():
        cursor.execute('SELECT * FROM carro')
        resultado = cursor.fetchall()
        if resultado:
            print('ID\tMarca\tModelo\tAno')
            for item in resultado:
                print(f'{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}')
        else:
            print('Nenhum carro encontrado.')