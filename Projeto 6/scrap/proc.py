"""
Módulo de Processamento

Descrição: Este é o módulo com a funções necessárias para o processamento de dados do Aplicativo de extração de dados em texto.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 07/12/2023

"""

# Importando bibliotecas

import requests
from bs4 import BeautifulSoup


# Função de baixar pagina html

def leitor_web(endereco_web: str) -> str:
    """ Esta função baixa página html escolhida """
    pagina = requests.get(endereco_web)
    return pagina.text

# Função de scrapper

def extrator(pagina_web: str, tag: str, palavra_chave: str) -> list:
    """ Esta função extrai da pagina html a tag e a palavra-chave desejada """
    pagina = leitor_web(pagina_web)
    soup = BeautifulSoup(pagina, 'html.parser')
    dado_web = soup.find_all(tag)
    busca = soup.find_all(string=lambda text: palavra_chave.lower() in text.lower())
    contagem = len(busca)
    return [soup, dado_web, busca, contagem]