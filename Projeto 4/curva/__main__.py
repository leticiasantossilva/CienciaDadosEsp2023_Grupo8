"""
Módulo Principal
Descrição: Este é o módulo com a função principal que integra as fases de entrada, processamento e saída de dados do Aplicativo de Plotagem.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 04/12/2023

"""




# Importação dos módulos

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

import es
import proc

def main():
    dados = es.leitora()
    processamento = proc.interp(dados)
      
if __name__ == "__main__":
    main()
    