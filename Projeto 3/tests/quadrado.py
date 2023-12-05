# Importação das bibliotecas da geração de gráficos

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Getting started matplotlib

x = np.linspace(-100, 100, 200)
y = x**2 

# Processamento de dados
fig, ax = plt.subplots()
ax.plot(x, y)

# Saída de dados
plt.show()