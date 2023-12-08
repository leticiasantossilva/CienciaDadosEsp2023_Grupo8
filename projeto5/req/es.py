"""
Módulo Entrada e Saída
Descrição: Este módulo prevê funções de entrada e saída de dados para Aplicativo de Plotagem.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 04/12/2023

"""

def leitora():
    pagina = input("Digite a página que deseja ler. Exemplo: https://api.github.com/events \n")
    formato = input("Digite o formato que deseja ler os dados da webpage ('json', 'raw', 'código fonte')? ")
    return [pagina, formato]

def impressora_web(arquivo):
    with open(arquivo) as f:
        page = f.readlines()
    return page
    
    
    
    