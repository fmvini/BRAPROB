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
    
    @staticmethod
    def consulta():
        cursor.execute('SELECT * FROM carro')
        return cursor.fetchall()