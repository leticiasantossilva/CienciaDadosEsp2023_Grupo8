"""
Módulo Entrada

Descrição: Este é o módulo com a função de entrada de dados do aplicativo que testa o software de Agenda de Contatos.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 11/12/2023

"""

import sqlite3 as sql

def escolha():
    funcao = input("""
    Informe a ação que deseja executar com seus contatos na Agenda de Contatos:
    "Inserir" contato
    "Ler" contatos
    "Alterar" todo um contato
    "Atualizar" parte de um contato
    "Excluir" contato
    "Sair" do programa
    """)
    return funcao