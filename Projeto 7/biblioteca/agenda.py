"""
Módulo Biblioteca Agenda

Descrição: Este é o módulo com as funções de software que oferece biblioteca de gerenciamento de dados em uma Agenda de Contatos.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 11/12/2023

"""

# Importação da biblioteca SQLite3 
import sqlite3 as sql
from sqlite3 import Cursor


# Função de criar a tabela no banco de dados
def criar_tabela():
    """ Esta função cria uma nova tabela para gravar na base de dados da Agenda de Contatos """
    # Função para conectar banco de dados
    conn = sql.connect('agenda.db')
    # definindo um cursor
    cursor = conn.cursor()
    
    # criando a tabela
    cursor.execute("""
    CREATE TABLE contatos(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    prenome VARCHAR(50) NOT NULL,                           
    nomeMeio VARCHAR(200) NOT NULL,
    sobrenome VARCHAR(200) NOT NULL,
    codArea VARCHAR(2) NOT NULL,
    celular VARCHAR(9) NOT NULL,
    fixo VARCHAR(8),
    estado VARCHAR(2) NOT NULL,
    municipio VARCHAR(30) NOT NULL,
    bairro VARCHAR(30), 
    tipoLogradouro VARCHAR(20) NOT NULL,
    nomeLogradouro VARCHAR(150) NOT NULL,
    numero INTEGER,  
    complemento VARCHAR(100) 
    );
    """)
    
    # fechando conexão com banco de dados
    conn.close()

    
    
# Função para inserir dados no banco de dados da Agenda de Contatos - CREATE
def inserir_dados():
    """ Esta função possibilita inserir novos contatos na Agenda de Contatos """
    # conectando com o banco de dados
    conn = sql.connect('agenda.db')
    cursor = conn.cursor()

    # solicitando os dados ao usuário
    p_prenome = input('Prenome: ')
    p_nomeMeio = input('Nome do Meio: ')
    p_sobrenome = input('Sobrenome: ')
    p_codArea = input('Código de Área: ')
    p_celular = input('Celular: ')
    p_fixo = input('Telefone Fixo: ')
    p_estado = input('Estado: ')
    p_municipio = input('Município: ')
    p_bairro = input('Bairro: ')
    p_tipoLogradouro = input('Tipo de Logradouro: ')
    p_nomeLogradouro = input('Nome de Logradouro: ')
    p_numero = input('Número: ')
    p_complemento = input('Complemento: ')

    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO contatos (prenome, nomeMeio, sobrenome, codArea, celular, fixo, estado, municipio, bairro, tipoLogradouro, nomeLogradouro, numero, complemento)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (p_prenome, p_nomeMeio, p_sobrenome, p_codArea, p_celular, p_fixo, p_estado, p_municipio, p_bairro, p_tipoLogradouro, p_nomeLogradouro, p_numero, p_complemento))
    
    # salvando os dados
    conn.commit()
    
    # confirmação
    print('Dados inseridos com sucesso.')
    
    # fechando a conexão com banco de dados
    conn.close()
       
    


# Função para ler o banco de dados - READ

def ler_dados():
    """ Esta função possibilita ler todos os contatos da Agenda de Contatos """
    # conectando com o banco de dados
    conn = sql.connect('agenda.db')
    cursor = conn.cursor()
    
    # solicitando leitura
    cursor.execute("""
    SELECT * FROM contatos;
    """)

    for linha in cursor.fetchall():
        print(f'ID do contato: {linha[0]} \n Dados: {linha[1:14]}')

    # fechando conexão com banco de dados
    conn.close()


    
#  Função de alterar todos os dados de um contato - UPDATE
def alterar_dados():
    """ Esta função possibilita atualizar todos os dados de algum contato na Agenda de Contatos """
    conn = sql.connect('agenda.db')
    cursor = conn.cursor()

    # solicitando os dados ao usuário
    id_cliente = int(input('id: '))

    p_prenome = input('Prenome: ')
    p_nomeMeio = input('Nome do Meio: ')
    p_sobrenome = input('Sobrenome: ')
    p_codArea = input('Código de Área: ')
    p_celular = input('Celular: ')
    p_fixo = input('Telefone Fixo: ')
    p_estado = input('Estado: ')
    p_municipio = input('Município: ')
    p_bairro = input('Bairro: ')
    p_tipoLogradouro = input('Tipo de Logradouro: ')
    p_nomeLogradouro = input('Nome de Logradouro: ')
    p_numero = input('Número: ')
    p_complemento = input('Complemento: ')

    # executando a alteração
    cursor.execute("""
    UPDATE contatos
    SET prenome = ?, nomeMeio = ?, sobrenome = ?, codArea = ?, celular = ?, fixo = ?, estado = ?, municipio = ?, bairro = ?, tipoLogradouro = ?, nomeLogradouro = ?, numero = ?, complemento = ?
    WHERE id = ?
    """, ((p_prenome, p_nomeMeio, p_sobrenome, p_codArea, p_celular, p_fixo, p_estado, p_municipio, p_bairro, p_tipoLogradouro, p_nomeLogradouro, p_numero, p_complemento, id_cliente)))

    # salvando as alterações
    conn.commit()

    # confirmando a alteração
    print('Dados atualizados com sucesso.')

    # fechando a conexão
    conn.close()

    

    
# Função de atualização de apenas uma parte do contato - UPDATE
def atualizar_dado():
    """ Esta função possibilita atualizar isoladamente um dado de algum contato na Agenda de Contatos """
    # conectando com o banco de dados
    conn = sql.connect('agenda.db')
    cursor = conn.cursor()

    # solicitando os dados ao usuário
    id_contato = input('ID do contato a ser atualizado: ')
    dado = input("""
    Qual o código do dado será atualizado:
    1 - Prenome
    2 - Nome do Meio
    3 - Sobrenome
    4 - Código de Área
    5 - Celular
    6 - Telefone Fixo
    7 - Estado
    8 - Município
    9 - Bairro
    10 - Tipo de Logradouro
    11 - Nome de Logradouro
    12 - Número
    13 - Complemento
    """)
    
    # Solicita atualização e executa
    if dado == '1':
        novo_dado = input('Novo Prenome: ')
        cursor.execute("""
        UPDATE contatos SET prenome = ? WHERE id = ?
        """, (novo_dado, id_contato))
    elif dado == '2':
        novo_dado = input('Novo Nome do Meio: ')
        cursor.execute("""
        UPDATE contatos SET nomeMeio = ? WHERE id = ?
        """, (novo_dado, id_contato))
    elif dado == '3':
        novo_dado = input('Novo Sobrenome: ')
        cursor.execute("""
        UPDATE contatos SET sobrenome = ? WHERE id = ?
        """, (novo_dado, id_contato))
    elif dado == '4':
        novo_dado = input('Novo Código de Área: ')
        cursor.execute("""
        UPDATE contatos SET codArea = ? WHERE id = ?
        """, (novo_dado, id_contato))
    elif dado == '5':
        novo_dado = input('Novo Celular: ')
        cursor.execute("""
        UPDATE contatos SET celular = ? WHERE id = ?
        """, (novo_dado, id_contato))
    elif dado == '6':
        novo_dado = input('Novo Telefone Fixo: ')
        cursor.execute("""
        UPDATE contatos SET fixo = ? WHERE id = ?
        """, (novo_dado, id_contato))
    elif dado == '7':
        novo_dado = input('Novo Estado: ')
        cursor.execute("""
        UPDATE contatos SET estado = ? WHERE id = ?
        """, (novo_dado, id_contato))
    elif dado == '8':
        novo_dado = input('Novo Município: ')
        cursor.execute("""
        UPDATE contatos SET municipio = ? WHERE id = ?
        """, (novo_dado, id_contato))
    elif dado == '9':
        novo_dado = input('Novo Bairro: ')
        cursor.execute("""
        UPDATE contatos SET bairro = ? WHERE id = ?
        """, (novo_dado, id_contato))
    elif dado == '10':
        novo_dado = input('Novo Tipo de Logradouro: ')
        cursor.execute("""
        UPDATE contatos SET tipoLogradouro = ? WHERE id = ?
        """, (novo_dado, id_contato))
    elif dado == '11':
        novo_dado = input('Novo Nome do Logradouro: ')
        cursor.execute("""
        UPDATE contatos SET nomeLogradouro = ? WHERE id = ?
        """, (novo_dado, id_contato))
    elif dado == '12':
        novo_dado = input('Novo Número: ')
        cursor.execute("""
        UPDATE contatos SET numero = ? WHERE id = ?
        """, (novo_dado, id_contato))
    else:
        novo_dado = input('Novo Complemento: ')
        cursor.execute("""
        UPDATE contatos SET complemento = ? WHERE id = ?
        """, (novo_dado, id_contato))
    
    # salvando os dados
    conn.commit()
    
    # confirmndo da atualização
    print(f'O dado do contato de ID {id_contato} foi atualizado com sucesso.')
    
    # fechando a conexão
    conn.close()
    
    

    
# Função para excluir dados no banco de dados da Agenda de Contatos - DELETE
def excluir_dados():
    """ Esta função possibilita a exclusão de algum contato registrado no banco Agenda.db """
    conn = sql.connect('agenda.db')
    cursor = conn.cursor()
    
    # solicita o ID do contato
    id_contato = input('Digite o ID do contato que deseja excluir: ')

    # excluindo um registro da tabela
    cursor.execute("""
    DELETE FROM contatos
    WHERE id = ?
    """, (id_contato))

    # salvando os dados
    conn.commit()

    # confirmação da atualização
    print('Contato excluído com sucesso.')

    # fechando a conexão
    conn.close()

