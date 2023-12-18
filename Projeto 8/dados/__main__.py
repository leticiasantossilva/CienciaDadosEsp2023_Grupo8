"""
Módulo Principal

#ALTERAR
Descrição: Este é o módulo com a função principal que integra as fases de entrada, processamento e saída de dados do Aplicativo de Plotagem.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 04/12/2023

"""

# Importação dos módulos

import es
import proc

def main():
    url = "https://dados.tce.rs.gov.br/dados/municipal/balancete-despesa/2023.csv"
    print('Lendo dados da URL: https://dados.tce.rs.gov.br/dados/municipal/balancete-despesa/2023.csv')
    leitor = es.leitor_dados(url)

    variavel = es.variavel()
    
    dados = proc.coleta_dados(leitor, variavel)

    resultados = proc.media_desv(dados)

    es.impressora(resultados)

    es.plotador(dados)



if __name__ == "__main__":
    main()
    