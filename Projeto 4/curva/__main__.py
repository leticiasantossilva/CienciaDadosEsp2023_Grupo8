"""
Módulo Principal
Descrição: Este é o módulo com a função principal que integra as fases de entrada, processamento e saída de dados do Aplicativo de Ajuste de Curva de Dados.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 05/12/2023

"""



# Importação de bibliotecas e módulos

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

import es
import proc


# Definindo a função main do aplicativo

def main():
    """Esta é a função principal que integra as fases de entrada, processamento e saída de dados"""
    # Leitura de dados
    pontos = es.leitora()
    # Processamento de dados
    dados = proc.interp(pontos)
    # Saída de dados
    es.plota_curva(dados)
    
        
if __name__ == "__main__":
    main()
    