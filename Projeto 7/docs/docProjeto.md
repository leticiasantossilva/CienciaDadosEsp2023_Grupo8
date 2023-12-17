# Documento de Projeto de Software

## Introdução
O software se constitui em uma biblioteca de código escrito na linguagem Python, utilizando o pacote de gerenciamento de banco de dados Python SQLite3.


## Projeto de estrutura de dados

Os dados utilizados pela biblioteca desenvolvida serão armazenados por processo de SQLite3 em um banco de dados, em formatos de tabelas. 


## Projeto de arquitetura

O projeto de arquitetura do software contem as funncionalidades de operações CRUD (Create, Read, Update, Delete) de banco de dados:

### Criar

- Função criar_tabela()
Esta função cria uma nova tabela para gravar contatos na base de dados da Agenda de Contatos.


### Inserir

- Função inserir_dados()
Esta função possibilita inserir novos contatos na Agenda de Contatos.


### Ler

- Função ler_dados()
Esta função possibilita ler os contatos da Agenda de Contatos.


### Alterar e Atualizar

- Função alterar_dados()
Esta função possibilita atualizar todos os dados de algum contato na Agenda de Contatos.

- Função atualizar_dado()
Esta função possibilita atualizar isoladamente um dado de algum contato na Agenda de Contatos.


### Excluir

- Função excluir_dados()
Esta função possibilita a exclusão de algum contato registrado no banco Agenda.db.


## Projeto de algoritmos
Fica a critério do desenvolvedor a escolha do algoritmo ótimo.


## Projeto de banco de dados

As fases do projeto do banco de dados incluem:

1. ![Projeto Conceitual](projConc.md)

2. ![Projeto Lógico](projLog.md)

3. ![Projeto Físico](projFis.md)
