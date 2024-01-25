"""
Módulo de Processamento

Descrição: Este módulo prevê o processamento de dados do Aplicativo de análise de dados via API.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 12/12/2023

"""
# Importando bibliotecas necessárias

import requests
import json

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

import es

def modelo(acoes):
    mercado = es.leitor_indice()
    for item in acoes:
        acao = es.leitor_precos(item)
        df = pd.DataFrame({'Ativo':acao, 'Mercado':mercado})
        model = smf.ols('Ativo ~ Mercado', data=df).fit()
        resultado = model.summary()

        print(f'Ativo: {item}')
        print(resultado, '\n')


def alfa(acoes):
    mercado = es.leitor_indice()
    cdi1 = es.leitor_cdi()

    for item in acoes:
        acao = es.leitor_precos(item)
        y = acao - cdi1
        x = mercado - cdi1
        df = pd.DataFrame({'Rativo': y, 'Rmercado': x})
        model = smf.ols('Rativo ~ Rmercado', data=df).fit()

        #Alfa Jensen é o intercepto, teste t do intercepto
        print(f'Ativo: {item}')
        print(f'Alfa de Jensen: {item}')
        print(model.summary(), '\n')

