"""
Módulo de Processamento
Descrição: Este módulo prevê o processamento de dados do Aplicativo de Coleta de Dados na Web.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 06/12/2023

"""

# Importação das bibliotecas

import requests
import json


# Definindo a função de baixar webpage

def get_web(dados: list):
    """ esta função lê e baixa os dados na página web requerida """
    arquivo = 'pagina.txt'
    if dados[1] == 'json':
        r = requests.get(dados[0])
        page = r.json()
        with open(arquivo, 'w') as f:
            f.write(json.dumps(page))
    elif dados[1] == 'raw':
        r = requests.get(dados[0])
        page = r.content
        with open(arquivo, 'wb') as fd:
            fd.write(page)
    else:
        r = requests.get(dados[0])
        page = r.text
        with open(arquivo, 'w', encoding='utf-8') as f:
            f.write(page)
    return arquivo
