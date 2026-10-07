import sqlite3

conn = sqlite3.connect('carros.db')
cursor = conn.cursor()

def inicializar_banco():
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS carro(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        ano INTEGER NOT NULL)
        '''
    )
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS bateria (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        capacidade INTEGER NOT NULL,
        nivel INTEGER NOT NULL
        )
        '''
    )
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS carroeletrico(
        id INTEGER PRIMARY KEY,
        bateria_id INTEGER NOT NULL, 
        FOREIGN KEY (id) REFERENCES carro (id),
        FOREIGN KEY (bateria_id) REFERENCES bateria (id)
        )
        '''
    )

    conn.commit()