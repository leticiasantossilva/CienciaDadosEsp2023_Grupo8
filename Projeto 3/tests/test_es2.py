import matplotlib.pyplot as plt

def impressora(graf):
    plt.show()


fig = plt.figure()
ax = fig.subplots()
grafico = ax.plot([1, 2, 3, 4], [0, 0.5, 1, 0.2])

# plt.show()

impressora(grafico)