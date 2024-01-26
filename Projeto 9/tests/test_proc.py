"""
Módulo de Processamento

Descrição: Este módulo prevê o processamento de dados do  aplicativo que coleta automaticamente dados da web e estima o modelo CAPM para ações na B3.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 13/12/2023

"""

# Importando bibliotecas necessárias

import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import requests



# Função de estimação por mínimos quadrados ordinários

def estima_modelo(Ri:np.array, Rm:np.array, Rf:np.array):
    Rf = np.array(Rf[-len(Ri):])
    Rm = np.array(Rm[-len(Ri):])
    Premio = (Rf - Rm)
    
    # Adicionando uma constante à variável independente
    X = sm.add_constant(Premio)
    
    # Estimando regressão
    results = sm.OLS(Ri, X, missing = 'drop').fit()
    return results


# Função de teste de nulidade do Alfa de Jensen e do risco específico

def test_nulidade_t_parametro(results):
    """ Esta função realiza teste t de nulidade do Alfa de Jensen e do risco específico """
    teste_t = results.t_test('const = 0')
    return teste_t

# Função de teste de nulidade do Alfa de Jensen e do risco específico

def test_nulidade_F_parametros(results):
    """ Função que avalia a nulidade conjunta dos parâmetros da regressão (usando o teste F) """
    hipotese = "const = 0, x1 = 0"
    teste_f = results.f_test(hipotese)
    return teste_f

# Função de teste correlograma

def testa_corr(results):
    """ Esta função que testa a correlação serial do modelo (usando o correlograma) """
    residuos = results.resid
    sm.graphics.tsa.plot_acf(residuos, lags=250)
    plt.title("Correlograma dos Resíduos do CAPM")
    plt.show()