# Importação das bibliotecas da geração de gráficos

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Getting started matplotlib

# Atribuição de variáveis
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

# Processamento de dados
fig, ax = plt.subplots()
ax.plot(x, y)

# Saída de dados
plt.show()