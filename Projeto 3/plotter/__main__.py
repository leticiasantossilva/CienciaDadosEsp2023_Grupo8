"""
Módulo Principal
Descrição: Este é o módulo com a função principal que integra as fases de entrada, processamento e saída de dados do Aplicativo de Plotagem.
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

def main():
    """Esta é a função principal que integra as fases de entrada, processamento e saída de dados"""
    # Leitura de dados
    operacao = es.leitora_operacao()
    dados = proc.ope(operacao)
    es.impressora(dados[0], dados[1])
        
if __name__ == "__main__":
    main()
    