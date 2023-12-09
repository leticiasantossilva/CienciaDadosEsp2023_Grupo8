
# Importando bibliotecas

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import interpolate



# função de interpolação

def interp(dados: list) -> list:
    """ Esta função aplica interpolação na lista de pontos inserida pelo usuário, gerando uma lista com elementos np.ndarray """
    x1 = [float(i) for i in dados[0]]
    y1 = [float(i) for i in dados[1]]
    
    x = np.array(x1)
    y = np.array(y1)
    
    f = interpolate.interp1d(x, y)
    
    xnew = np.arange(min(x), max(x), 0.0001)
    ynew = f(xnew)   # use interpolation function returned by `interp1d`
    
    return (x, y, xnew, ynew)
