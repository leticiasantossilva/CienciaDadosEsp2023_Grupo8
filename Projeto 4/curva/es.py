"""
Módulo Entrada e Saída
Descrição: Este módulo prevê funções de entrada e saída de dados para Aplicativo de Plotagem.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 04/12/2023

"""

def leitora():
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

