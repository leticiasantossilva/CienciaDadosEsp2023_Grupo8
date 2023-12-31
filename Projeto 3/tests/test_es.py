import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def leitora_operacao() -> str:
    """Esta funcao le a função a ser realizada."""
    operacao = input("""Digite o tipo de função que deseja plotar. 
Digite quad para quadratica (a*x2 + b*x + c); 
afim para afim (a*x + b); 
log para logarítmica (log(x)); 
exp para exponencial (exp(x)): \n""")
    return operacao

def leitora_coeficientes(operacao: str) -> list:
    """Função para inserir o coeficientes da função"""
    a = input("Qual o coeficiente a? ")
    b = input('Qual o coeficiente b? ')
    if operacao == 'quad':
        c = input('Qual o coeficiente c? ')
        return [a, b, c]
    else:
        return [a, b]

def leitora_int() -> list:
    """Função para inserir o intervalo de x da função"""
    inicio = float(input('Qual o valor de x inicio da funcao? '))
    fim = float(input('Qual o valor de x final da função? '))
    return [inicio, fim]
                
# Saída de dados

def impressora(x, y) -> None:
    """Função para plotagem da função"""
    fig, grafico = plt.subplots()
    grafico.plot(x,y)
    plt.show()

