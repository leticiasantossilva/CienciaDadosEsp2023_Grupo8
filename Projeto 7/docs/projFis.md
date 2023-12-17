# Projeto Físico

Este documento consiste no código que cria o banco de dados desenvolvido para o software que oferece biblioteca de gerenciamento de dados em uma Agenda de Contatos, em formato de base de dados.

Lembrando que este banco de dados de Agenda de Contatos tem como finalidade ser objeto das funncionalidades de operações CRUD (Create, Read, Update, Delete) de dados.

## Código da tabela do banco de dados Agenda

O código que cria a tabela de contatos no banco de dados Agenda.db através do Python será o seguinte:
 
    conn = sql.connect('agenda.db')
    cursor = conn.cursor()
    
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
    
    conn.close()