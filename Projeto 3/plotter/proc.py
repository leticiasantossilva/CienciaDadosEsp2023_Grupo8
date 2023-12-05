"""
Módulo de Processamento
Descrição: Este módulo prevê o processamento de dados do Aplicativo de Plotagem.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 04/12/2023

"""
# Importação das bibliotecas da geração de gráficos

import numpy as np
import es

def ope(operacao) -> list:
    """Função para definição do array para posterior plotagem da função"""
    if operacao == 'quad':
        coef = es.leitora_coeficientes(operacao)
        intervalo = es.leitora_int()
        x = np.linspace(intervalo[0], intervalo[1], int((intervalo[1]-intervalo[0])*1000))
        y = float(coef[0])*x**2 + float(coef[1])*x + float(coef[2])
        return [x,  y]
    elif operacao == 'afim':
        coef = es.leitora_coeficientes(operacao)
        intervalo = es.leitora_int()
        x = np.linspace(intervalo[0], intervalo[1], int((intervalo[1]-intervalo[0])*1000))
        y = float(coef[0])*x + float(coef[1])
        return [x,  y]              
    elif operacao == 'log':
        intervalo = es.leitora_int()
        x = np.linspace(intervalo[0], intervalo[1], int((intervalo[1]-intervalo[0])*1000))
        y = np.log(x)
        return [x, y]
    else:
        intervalo = es.leitora_int()
        x = np.linspace(intervalo[0], intervalo[1], int((intervalo[1]-intervalo[0])*1000))
        y = np.exp(x)
        return [x, y]
