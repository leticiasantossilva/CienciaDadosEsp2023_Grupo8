
import sqlite3 as sql

def criar_tabela():
    # Função para criar banco de dados
    conn = sql.connect('agenda.db')
    # definindo um cursor
    cursor = conn.cursor()
    # criando a tabela
    cursor.execute("""
    CREATE TABLE contato(
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
    conn.close()

def excluir_dados():
    #EXCLUIR DADOS

    conn = sql.connect('agenda.db')
    cursor = conn.cursor()
    
    id_cliente = int(input('Digite o ID que deseja excluir: '))

    # excluindo um registro da tabela
    cursor.execute("""
    DELETE FROM contato
    WHERE id = ?
    """, (id_cliente,))

    conn.commit()

    print('Registro excluido com sucesso.')

    conn.close()
    
def alterar_dados():
    #ALTERAR DADOS
    conn = sql.connect('agenda.db')
    cursor = conn.cursor()

    id_cliente = int(input('id: '))

    p_prenome = input('prenome: ')
    p_nomeMeio = input('nomeMeio: ')
    p_sobrenome = input('sobrenome: ')
    p_codArea = input('codArea: ')
    p_celular = input('celular: ')
    p_fixo = input('fixo: ')
    p_estado = input('estado: ')
    p_municipio = input('municipio: ')
    p_bairro = input('bairro: ')
    p_tipoLogradouro = input('tipoLogradouro: ')
    p_nomeLogradouro = input('nomeLogradouro: ')
    p_numero = input('numero: ')
    p_complemento = input('complemento: ')

    cursor.execute("""
    UPDATE contato
    SET prenome = ?, nomeMeio = ?, sobrenome = ?, codArea = ?, celular = ?, fixo = ?, estado = ?, municipio = ?, bairro = ?, tipoLogradouro = ?, nomeLogradouro = ?, numero = ?, complemento = ?
    WHERE id = ?
    """, ((p_prenome, p_nomeMeio, p_sobrenome, p_codArea, p_celular, p_fixo, p_estado, p_municipio, p_bairro, p_tipoLogradouro, p_nomeLogradouro, p_numero, p_complemento, id_cliente)))

    conn.commit()

    print('Dados atualizados com sucesso.')

    conn.close()

def ler_dados():
    # LER DADOS
    conn = sql.connect('agenda.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM contato;
    """)

    for linha in cursor.fetchall():
        print(f'ID: {linha[0]} - Dados {linha}')

    conn.close()
    
def inserir_dados():
    ############## Inserir dados
    conn = sql.connect('agenda.db')
    cursor = conn.cursor()

    # solicitando os dados ao usuário
    p_prenome = input('prenome: ')
    p_nomeMeio = input('nomeMeio: ')
    p_sobrenome = input('sobrenome: ')
    p_codArea = input('codArea: ')
    p_celular = input('celular: ')
    p_fixo = input('fixo: ')
    p_estado = input('estado: ')
    p_municipio = input('municipio: ')
    p_bairro = input('bairro: ')
    p_tipoLogradouro = input('tipoLogradouro: ')
    p_nomeLogradouro = input('nomeLogradouro: ')
    p_numero = input('numero: ')
    p_complemento = input('complemento: ')

    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO contato (prenome, nomeMeio, sobrenome, codArea, celular, fixo, estado, municipio, bairro, tipoLogradouro, nomeLogradouro, numero, complemento)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (p_prenome, p_nomeMeio, p_sobrenome, p_codArea, p_celular, p_fixo, p_estado, p_municipio, p_bairro, p_tipoLogradouro, p_nomeLogradouro, p_numero, p_complemento))

    conn.commit()

    print('Dados inseridos com sucesso.')

    conn.close()