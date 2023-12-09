"""
Módulo Entrada e Saída
Descrição: Este módulo prevê funções de entrada e saída de dados para Aplicativo de Ajuste de Curva de Dados.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 05/12/2023

"""

# Importando bibliotecas

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import interpolate


# Definindo a função de entrada de dados: leitora()

def leitora():
    """ Esta função receberá os pontos desejados, precisando estar em ordem crescento pelo X dos pontos (x,y) """
    x = []
    y = []
    pontos = float(input("Digite a quantidade de pontos? "))
    i = 1
    while i <= pontos:
        print('A seguir digite os pontos das coordenadas em ordem crescente de X.')
        x.append(input(f'Digite o ponto X{i}: '))
        y.append(input(f'Digite o ponto Y{i}: '))
        i = i + 1
    return [x, y]


# Definindo a função de saída de dados: plota_curva()

def plota_curva(dados: list) -> None:
    """ Esta função pega os dados em lista de np.ndarray para gerar o gráfico da função de pontos """
    plt.plot(dados[0], dados[1], 'o', dados[2], dados[3], 'b-')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.show()
    