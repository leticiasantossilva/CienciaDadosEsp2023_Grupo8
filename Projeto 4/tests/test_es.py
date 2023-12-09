
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
    """Função para plotagem da função"""
    plt.plot(dados[0], dados[1], 'o', dados[2], dados[3], 'b-')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.show()