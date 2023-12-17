"""
Módulo Principal

Descrição: Este é o módulo com a função principal que integra as fases de entrada, processamento e saída de dados do Aplicativo de extração de dados em texto.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 07/12/2023

"""

# Importando bibliotecas
import es
import proc


# Definindo a função main()
def main():
    """ Esta função integra as fases de entrada, processamento e saída de dados """
    entrada = es.leitor()
    dados = proc.extrator(entrada[0], entrada[1], entrada[2])
    es.saida(dados[0], entrada[1], entrada[2], dados[3])

# Execução do aplicativo
if __name__ == "__main__":
    main()
    
    