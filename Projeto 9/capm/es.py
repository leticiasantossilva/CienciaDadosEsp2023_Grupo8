"""
Módulo Entrada e Saída

Descrição: Este módulo prevê funções de entrada e saída de dados para o aplicativo que coleta automaticamente dados da web e estima o modelo CAPM para ações na B3.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 13/12/2023

"""


# Importando bibliotecas necessárias

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


# Defininido a função de leitura de preços de ações

def leitor_precos(ticker:str):
    """" Esta função realiza a leitura de preço de fechamento de ações nas quarta-feiras de todas as últimas 260 semanas """
    end_date = datetime.now()
    start_date = end_date - timedelta(weeks=262)
    dado = yf.download(ticker, start=start_date, end=end_date, progress=False, interval='1d')
    data_day = dado[dado.index.weekday == 2]
    fechamento = data_day['Adj Close'].dropna()
    return fechamento


# Defininido a função de leitura da carteira de mercado (IBOVESPA)

def leitor_indice():
    """" Esta função realiza a leitura de fechamento do Bovespa nas quartas-feiras de todas as últimas 260 semanas """
    end_date = datetime.now()
    start_date = end_date - timedelta(weeks=262)
    bov = yf.download("^BVSP", start=start_date, end=end_date, progress=False, interval='1d')
    fechamento = bov['Adj Close']
    mercado = fechamento[fechamento.index.weekday == 2]
    return mercado    
    

    
