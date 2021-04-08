
import sqlite3

conn = sqlite3.connect('C:\\Users\Ruan\Documents\curso_ifto\Banco de dados\hospitalar.sqlite3')

cursor = conn.execute('select * from hospital')
linhas = cursor.fetchall()

for linha in linhas:
    print(linha)
    







