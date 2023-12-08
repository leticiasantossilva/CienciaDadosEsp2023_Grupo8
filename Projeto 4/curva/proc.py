"""
Módulo de Processamento
Descrição: Este módulo prevê o processamento de dados do Aplicativo de Interpolacao.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 05/12/2023

"""
# Importação das bibliotecas da geração de gráficos

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

def interp(dados):
    x1 = [float(i) for i in dados[0]]
    y1 = [float(i) for i in dados[1]]
    
    x = np.array(x1)
    y = np.array(y1)
    
    f = interpolate.interp1d(x, y)
    
    xnew = np.arange(min(x), max(x), 0.1)
    ynew = f(xnew)   # use interpolation function returned by `interp1d`
    plt.plot(x, y, 'o', xnew, ynew, '-')
    plt.show()

