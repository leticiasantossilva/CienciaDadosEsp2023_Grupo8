"""
Módulo Entrada e Saída
Descrição: Este módulo prevê funções de entrada e saída de dados para o projeto de Calculadora com as 4 operações básicas.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 29/11/2023

"""

# Funções para o processo de entrada de dados

def leitora_numeros() -> list:
    """ Esta função recebe os dois números que fazem parte do cálculo """
    i = 0
    numeros = []
    while i < 2:
        numeros.append(float(input(f"Digite o número {i+1} que deseja operar: ")))
        i+=1
    return numeros


def leitora_operacao() -> str:
    """ Esta função recebe a definição da operação a ser executada no cálculo """
    operacao = input("""Digite a operação que deseja realizar.
Pressione + para adição;
- para subtração;
* para multiplicação;
/ para divisão """)
    return operacao


def leitora() -> list:
    """ Esta função define a operação de entrada de dados """
    lista_numeros = leitora_numeros()
    operacao = leitora_operacao()
    return [lista_numeros, operacao]


# Processo de saída de dados

def escritora(resultado: float) -> None:
    """ Esta função coloca o resultado na tela """
    print(f"O resultado da operação é igual a {resultado}")
    