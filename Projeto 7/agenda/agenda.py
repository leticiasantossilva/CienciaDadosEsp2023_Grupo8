"""
Cabeçalho
"""



import sqlite3 as sql
from sqlite3 import Cursor

def inserir(registro: list) -> sql.Cursor:
    """ Esta função aceita a inserção de novos registros no banco Agenda.db - atende ao RS2 """
    conn = sql.connect('agenda.db')
    conn.cursor()
    conn.execute("""
    INSERT INTO contato VALUES registro; """)