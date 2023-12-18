"""
Módulo de Processamento
Descrição: Este módulo prevê o processamento de dados do Aplicativo de Interpolacao.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 05/12/2023

"""
# Importação das bibliotecas da geração de gráficos

import requests
import json

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

def coleta_dados(api_tce, variavel):
    coluna = ['', 'VL_DOTACAO_INICIAL', 'VL_CREDITOS_SUPLEMENTARES', 'VL_CREDITOS_ESPECIAIS', 'VL_CREDITOS_EXTRAORDINARIOS', 'VL_REDUCAO_DOTACAO', 'VL_TRANSFERENCIA', 'VL_TRANSPOSICAO', 'VL_REMANEJAMENTO', 'VL_EMPENHADO', 'VL_LIQUIDADO', 'VL_PAGO', 'VL_LIMITADO', 'VL_RECOMPOSICAO', 'VL_PREVISAO_EXECUCAO']

    resultado = api_tce[coluna[int(variavel)]]
    
    return resultado

def media_desv(dados):
    resultado_media = np.average(dados)
    resultado_desv = np.std(dados)
    return [resultado_media, resultado_desv]