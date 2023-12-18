"""
Módulo Entrada e Saída

Descrição: Este módulo prevê funções de entrada e saída de dados para o Aplicativo de análise de dados via API.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 12/12/2023

"""
# Importando bibliotecas necessárias

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


# Função de definição da variável
def variavel() -> str:
    """ Esta função recebe do usuário a definição que qual variável financeira a ser analisada """
    variavel = input("""
Qual variável do Balancete de Despesas Orçamentárias dos municípios do RS em 2023 você deseja analisar:
1 - Valor de Dotação Inicial
2 - Valor de Créditos Suplementares
3 - Valor de Créditos Especiais
4 - Valor de Créditos Extraordinários
5 - Valor de Redução de Dotação
6 - Valor de Transferência
7 - Valor de Transposição
8 - Valor de Remanejamento
9 - Valor Empenhado
10 - Valor Liquidado
11 - Valor Pago
12 - Valor Limitado
13 - Valor de Recomposição
14 - Valor de Previsão de Execução
Digite o código da variável: 
""")
    return variavel

# Função para consumir a API e transformar dados csv em DataFrame
def leitor_dados(url: str) -> pd.DataFrame:
    """ Esta função inicia o processamento dos dados em CSV, usando a API de dados abertos """
    return pd.read_csv(url)


# Função de plotagem de gráfico da variável analisada
def plotador(dados: pd.DataFrame) -> None:
    """ Esta função apresenta ao usuário o gráfico dos dados analisados """
    print('O gráfico dos dados é: ')
    dados.plot()
    plt.show()

# Função para imprimir resultado da média e do desvio-padrão
def impressora(resultados: list) -> None:
    """ Esta função imprime para o usuário os resultados da média e do desvio-padrão calculados """
    print(f'A média dos dados é {resultados[0]} e o desvio padrão é {resultados[1]}')
    

    
    
    