
import requests
from bs4 import BeautifulSoup

def leitor_web(endereco_web: str) -> str:
    pagina = requests.get(endereco_web)
    return pagina.text

def extrator(pagina_web: str) -> str:
    soup = BeautifulSoup(pagina_web, 'html.parser')
    return soup