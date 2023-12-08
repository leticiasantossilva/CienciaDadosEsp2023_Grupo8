# Plano de Codificação e Testes

Tendo em vista o emprego de modelagem funcional no projeto do software, a codificação será feita utilizando o paradigma de programação funcional e orientada a objetos.

Utilizaremos a linguagem Python para codificação, uma vez que a mesma mostra-se a mais adequada ao desenvolvimento ágil de aplicações de pequena escala com interface de linha de comando.

Empregaremos "REPL-driven development" como método de codificação, utilizando o ambiente de desenvolvimento integrado Jupyter Lab para facilitar sua adoção.

Em um segundo momento, isto é, após a codificação com RDD, procede-se à escrita de testes unitários automatizados, usando a ferramenta pytest, para prover ainda mais segurança a respeito da correção do código.

A fim de representar os pontos dentro de um sistema de eixos cartesianos necessários à plotagem de gráficos de funções, utilizaremos a biblioteca Python NumPy e, para plotagem dos gráficos propriamente dita, a biblioteca Python MatPlotLib.

## Módulo entrada/saida - es.py

### 1. Requisito 1b

Plotar o gráfico

função impressora(grafico: objeto gráfico) -> null
Esta função imprime na tela o gráfico da função escolhida pelo usuário.

### 2. Requisito 2

Deve haver um menu com as quatro funções capazes de serem plotadas pelo aplicativo.

função leitor_funcao() -> string
Imprime um menu na tela contendo as funções afim, quadrática, logarítmica e exponencial para o usuário escolher qual delas plotar.

### 3. Requisitos 3 e 4

 Caso o usuário escolha a função afim, na sequência, ele deverá poder informar os coeficientes da função.

- Idêntico ao requisito 2, mas sendo válido para função quadrática.

função leitor_coeficiente(nome_funcao: string) -> lista
Lê os coeficientes no caso de o usuário escolher plotar uma função afim ou quadrática.

## Módulo de processamento de gráficos (designer)

Este módulo deverá prover uma função para plotar o gráfico da função escolhida pelo usuário.

### 1. Requisito 1a

Determinar o gráfico

função design(tipo_funcao: str, coeficientes: lista) -> objeto gráfico
Esta função recebe o tipo de função a ser desenhada e a lista de coeficientes (se for necessário) e desenha o gráfico da função correspondente.
