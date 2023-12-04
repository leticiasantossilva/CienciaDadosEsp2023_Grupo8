"""
Módulo Principal
Descrição: Este módulo define a função principal do projeto de Calculadora com as 4 operações básicas.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 29/11/2023

"""



# Importação dos módulos

import es
import proc


# Definindo a função de operações matemáticas

def escolhedora(dados: list) -> float:
    """Esta função escolhe a operação de acordo com o usuário"""
    if dados[1] == "+":
        resultado = proc.somadora(dados[0][0], dados[0][1])
    elif dados[1] == "-":
        resultado = proc.diminuidora(dados[0][0], dados[0][1])
    elif dados[1] == "*":
        resultado = proc.mult(dados[0][0], dados[0][1])
    else:
        resultado = proc.div(dados[0][0], dados[0][1])
    return resultado


# Definindo a função principal da calculadora

def main():
    """Esta é a função principal que integra as fases de entrada, processamento e saída de dados"""
    dados = es.leitora()
    resultado = escolhedora(dados)
    es.escritora(resultado)
    
    
# Execução

if __name__ == "__main__":
    main()
    