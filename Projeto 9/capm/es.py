"""
Módulo Entrada e Saída

Descrição: Este módulo prevê funções de entrada e saída de dados para o aplicativo que coleta automaticamente dados da web e estima o modelo CAPM para ações na B3.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 13/12/2023

"""

# ENTRADA DE DADOS

# Importando bibliotecas necessárias

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os


# Imput acoes

def leitor_acoes() -> list:
    acoes = []
    i = 1
    while i < 10:
        acoes.append(input(f'Digite o Ticker da ação que deseja avaliar {i} de 10: '))
    
    return acoes

# Leitura do CDI

def leitor_cdi(mercado) -> np.array:
    #CDI tem que estar na mesma base do mercado (mensal, diario, semanal)
    #CDI DIARIO
    cdi = pd.read_json('https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados?formato=json')
    #CDI MES
    cdi = pd.read_json('https://api.bcb.gov.br/dados/serie/bcdata.sgs.4390/dados?formato=json')['valor']
    cdi1 = np.array(cdi[-len(mercado):])
    return cdi1

# Leitura de retornos de preços de ações

def leitor_precos(ticker:str) -> np.array:
    """" Esta função realiza a leitura de preço de fechamento de ações nas quarta-feiras de todas as últimas 260 semanas e calcula seus retornos """
    end_date = datetime.now()
    start_date = end_date - timedelta(weeks=263)
    dado = yf.download(ticker, start=start_date, end=end_date, progress=False, interval='1d')
    data_day = dado[dado.index.weekday == 2]
    fechamento = data_day['Adj Close'].pct_change().dropna()
    return np.array(fechamento)


# Leitura de retornos da carteira de mercado (IBOVESPA)

def leitor_indice() -> np.array:
    """" Esta função realiza a leitura de fechamento do Bovespa nas quartas-feiras de todas as últimas 260 semanas e calcula seus retornos """
    end_date = datetime.now()
    start_date = end_date - timedelta(weeks=263)
    bov = yf.download("^BVSP", start=start_date, end=end_date, progress=False, interval='1d')
    retorno = bov['Adj Close'].pct_change().dropna()
    mercado = retorno[retorno.index.weekday == 2]
    return np.array(mercado)    


# Escolha de pasta para gravação de dados do CAPM

def leitor_pasta() -> str:
    """ Esta função executa a leitura do teclado para a escolha da pasta de gravação dos arquivos """
    pasta_destino = input("""Digite o caminho da pasta de gravação de arquivos: """)
    return pasta_destino


# SAÍDA DE DADOS

# bibliotecas
import os
import csv

#Função de gravação de dados CAPM em novo arquivo .csv
def grava_arquivo():
    """ Esta função cria um novo arquivo CSV com os resultados a cada estimação CAPM realizada """
    pass
