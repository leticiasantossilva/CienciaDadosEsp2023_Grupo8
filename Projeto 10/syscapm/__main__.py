"""
Módulo Principal

Descrição: Este é o módulo com a função principal que integra as fases de entrada, processamento e saída de dados do aplicativo que coleta automaticamente dados da web e estime o modelo CAPM para ações na B3 com previsão a partir de apredizado de máquina.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 13/12/2023

"""

# Bibliotecas
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import requests

# Importação dos módulos

import es
import proc


# Função principal
   
def main():
    """ Esta é a função que integra as fases de entrada, processamento e saída de dados  """
    
    # Dados do ativo livre de risco
    cdi = es.leitor_taxa()
    
    # Dados de mercado
    ibov = es.leitor_indice()
    
    # Leitura de local de gravação
    pasta = es.leitor_pasta()

    # Dados das ações
    acoes = es.leitor_acoes()
    
    # Dataframe para resultados das estimações
    dados = pd.DataFrame(columns=['Nome da Ação', 'Data', 'Alfa', 'Beta', 'Sigma'])
    
    for item in acoes:
        acao = es.leitor_precos(item)   
    # Estimando modelo
        results = proc.estima_modelo(acao, ibov, cdi)
    # saída de dados
        alfa = results[0]
        beta = results[1]
        sigma = results[2]    
        
        resultado = pd.DataFrame({
        'Nome da Ação': [item],
        'Data': [datetime.now().strftime('%Y-%m-%d')],
        'Alfa': [alfa],
        'Beta': [beta],
        'Sigma': [sigma]
    })
        dados = pd.concat([dados, resultado], ignore_index=True)

    es.grava_csv(pasta, dados)
    
# Executando a função do aplicativo
if __name__ == "__main__":
    main()
    