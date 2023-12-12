"""
Módulo Principal

#ALTERAR
Descrição: Este é o módulo com a função principal que integra as fases de entrada, processamento e saída de dados do Aplicativo de Plotagem.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 04/12/2023

"""

# Importação dos módulos
import proc
import es

def main():
    try:
        proc.criar_tabela()
    except:
        pass
    
    funcao = es.funcao()
    while funcao != 'sair':
        if funcao == 'ler':
            proc.ler_dados()
        elif funcao == 'inserir':
            proc.ler_dados()
            proc.inserir_dados()
        elif funcao == 'alterar':
            proc.ler_dados()
            proc.alterar_dados()
        elif funcao == 'excluir':
            proc.ler_dados()
            proc.excluir_dados()

        else:
            print('Função desconhecida.')
        funcao = es.funcao()
    print('Saindo do programa....')
          
if __name__ == "__main__":
    main()
    
    