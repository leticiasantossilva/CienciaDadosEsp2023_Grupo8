"""
Módulo Principal

Descrição: Este é o módulo com a função principal que integra as fases de entrada, processamento e saída de dados do aplicativo que testa o software de Agenda de Contatos.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 11/12/2023

"""


# Importar a biblioteca de Agenda de Contatos
import agenda

# Importação dos módulos
import proc
import es

def main():
    try:
        agenda.criar_tabela()
    except:
        pass
    
        i = 1
        
    while i == 1:
        funcao = es.escolha()
        processo = proc.executar(funcao)
        if funcao == 'Sair':
            break
    print('Saindo do programa....')
          
if __name__ == "__main__":
    main()
    
    