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

def escritora(dados):
    arquivo = 'pagina.txt'
    if dados[1] == 'json':
        r = requests.get(dados[0])
        page = r.json()
        with open(arquivo, 'w') as f:
            f.write(json.dumps(page))
    elif dados[1] == 'raw':
        r = requests.get(dados[0], stream=True)
        with open(arquivo, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)
    else:
        r = requests.get(dados[0])
        page = r.text
        with open(arquivo, 'w') as f:
            f.write(page)
    return arquivo