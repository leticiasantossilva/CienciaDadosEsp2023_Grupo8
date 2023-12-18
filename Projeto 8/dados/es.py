"""
Módulo Entrada e Saída
Descrição: Este módulo prevê funções de entrada e saída de dados para Aplicativo de Plotagem.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 04/12/2023

"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

def variavel() -> str:
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

def leitor_dados(url: str) -> pd.DataFrame:
    return pd.read_csv(url)

def plotador(dados: pd.DataFrame) -> None:
    print('O gráfico dos dados é: ')
    dados.plot()

def impressora(resultados):
    print(f'A média dos dados é {resultados[0]} e o desvio padrão é {resultados[1]}')
    

    
    
    