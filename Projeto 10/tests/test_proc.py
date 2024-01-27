"""
Módulo de Processamento

Descrição: Este módulo prevê funções de entrada e saída de dados para o aplicativo que coleta automaticamente dados da web e estime o modelo CAPM para ações na B3 com previsão a partir de apredizado de máquina.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 13/12/2023

"""

# Importando bibliotecas necessárias

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics



# Função de estimação por mínimos quadrados ordinários com machine learning

def estima_modelo(Ri:np.array, Rm:np.array, Rf:np.array) -> list:
    Rf = np.array(Rf[-len(Ri):])
    Rm = np.array(Rm[-len(Ri):])
    Premio = (Rf - Rm)
    

    Ri = Ri.reshape(-1, 1)
    Rm = Rm.reshape(-1, 1)
    Premio = Premio.reshape(-1, 1)
    
    # modelo capm com previsão
    Rm_train, Rm_test, Ri_train, Ri_test = train_test_split(Rm, Ri, test_size=0.2, random_state=0)
    
    # Inicializando o modelo de regressão linear
    modelo = LinearRegression()
    
    # Ajustando o modelo
    results = modelo.fit(Rm_train, Ri_train)
    
    # Utilizando função de projeção
    Ri_pred = modelo.predict(Rm_test)
    
    # Dados alfa, beta, sigma
    alfa = float(modelo.intercept_)
    beta = float(modelo.coef_[0])
    # Resíduos
    residuos = Ri_test - Ri_pred
    # volatilidade estimada
    sigma = np.sqrt(np.var(residuos))

    return [alfa, beta, sigma]


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
