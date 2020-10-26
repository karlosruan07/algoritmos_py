import sqlite3
from sqlite3 import Error


def conecta(db_file):
    conn = None
    
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        
    except Error as e:
        print(e)
        
    finally: #se o except for executado, a linha finnaly será executada automaticamente.
        if conn is None:
            conn.close()
            print('Conexão fechada.')

if __name__ =="__main__":
    conecta('C:\hospitalar.db')

