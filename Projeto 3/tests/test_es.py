import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


dados = [[1,2,3,4], [1,4,2,3]]

fig, ax = plt.subplots()
#ax.plot(dados[0], dados[1])

# plt.show()



def impressora(grafico, x, y) -> None:
    grafico.plot(x,y)
    plt.show()


impressora(ax, dados[0], dados[1])