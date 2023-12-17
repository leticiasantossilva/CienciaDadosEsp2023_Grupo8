"""
Módulo de Processamento

Descrição: Este é o módulo com as funções de processamento de dados do aplicativo que testa o software de Agenda de Contatos.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 11/12/2023

"""

# Importar a biblioteca de Agenda de Contatos
import agenda


def executar(funcao: str):
    if funcao == 'Ler':
        agenda.ler_dados()
    elif funcao == 'Inserir':
        agenda.inserir_dados()
    elif funcao == 'Alterar':
        agenda.ler_dados()
        agenda.alterar_dados()
    elif funcao == 'Atualizar':
        agenda.ler_dados()
        agenda.atualizar_dado()
    elif funcao == 'Excluir':
        agenda.ler_dados()
        agenda.excluir_dados()
    elif funcao == 'Sair':
        pass
    
    else:
        print('Função desconhecida.')
        