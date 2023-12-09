"""
Módulo de Processamento
Descrição: Este módulo prevê o processamento de dados do Aplicativo de Plotagem de Gráficos.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 04/12/2023

"""

# Importação das bibliotecas da geração de gráficos

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# funções

def quadratica(intervalo: list, coef: list) -> list:
    """ Esta função gera uma lista de atributos para plotagem de uma função quadrática """
    x = np.linspace(intervalo[0], intervalo[1], int((intervalo[1]-intervalo[0])*1000))
    y = float(coef[0])*x**2 + float(coef[1])*x + float(coef[2])
    return [x,  y]

def afim(intervalo: list, coef: list) -> list:
    """ Esta função gera uma lista de atributos para plotagem de uma função afim """
    x = np.linspace(intervalo[0], intervalo[1], int((intervalo[1]-intervalo[0])*1000))
    y = float(coef[0])*x + float(coef[1])
    return [x, y]

def logar(intervalo: list) -> list:
    """ Esta função gera uma lista de atributos para plotagem de uma função logarítmica """
    x = np.linspace(intervalo[0], intervalo[1], int((intervalo[1]-intervalo[0])*1000))
    y = np.log(x)
    return [x, y]

def exp(intervalo: list) -> list:
    """ Esta função gera uma lista de atributos para plotagem de uma função exponencial """
    x = np.linspace(intervalo[0], intervalo[1], int((intervalo[1]-intervalo[0])*1000))
    y = np.exp(x)
    return [x, y]

