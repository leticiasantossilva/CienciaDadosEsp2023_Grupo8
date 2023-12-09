"""
Módulo Principal
Descrição: Este é o módulo com a função principal que integra as fases de entrada, processamento e saída de dados do Aplicativo de Plotagem de Gráficos.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 04/12/2023

"""

# Importação dos módulos

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

import es
import proc


# Definindo a função ope(operacao: str) -> list

def ope(operacao: str) -> list:
    """Esta função escolhe a operação de acordo com o usuário"""
    if operacao == 'quad':
        coef = es.leitora_coeficientes(operacao)
        intervalo = es.leitora_int()
        resultado = proc.quadratica(intervalo, coef)
    elif operacao == 'afim':
        coef = es.leitora_coeficientes(operacao)
        intervalo = es.leitora_int()
        resultado = proc.afim(intervalo, coef)
    elif operacao == 'log':
        intervalo = es.leitora_int()
        resultado = proc.logar(intervalo)
    else:
        intervalo = es.leitora_int()
        resultado = proc.exp(intervalo)
    return resultado

# Definindo função main

def main():
    """Esta é a função principal que integra as fases de entrada, processamento e saída de dados"""
    # Leitura de dados
    operacao = es.leitora_operacao()
    # Processamento de dados
    dados = ope(operacao)
    # Saída de dados
    es.impressora(dados[0], dados[1])
        
if __name__ == "__main__":
    main()