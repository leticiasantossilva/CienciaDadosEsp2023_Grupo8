# Documento de Definição de Sistemas

Este documento organiza as definições de sistemas baseadas nos requisitos de desenvolvimento do projeto de Aplicativo de Plotagem de Gráficos.


### Módulo de Entrada/Saída (es)
O módulo de entrada/saída (es) deverá prover as seguintes funções:

1. Requisito 1b
Plotar o gráfico

Função para imprimir na tela o gráfico da função escolhida pelo usuário. 

2. Requisito 2
Deve haver um menu com as quatro funções capazes de serem plotadas pelo aplicativo.

Função para imprimir um menu na tela contendo as funções afim, quadrática, logarítmica e exponencial para o usuário escolher qual delas plotar.

3. Requisito 3

Caso o usuário escolha a função afim, na sequência, ele deverá poder informar os coeficientes da função.

Função para ler os coeficientes no caso de o usuário escolher plotar uma função afim ou quadrática.

3. Requisito 4

Idêntico ao requisito 3, mas sendo válido para função quadrática.

Função para ler coeficientes no caso de o usuário escolher plotar uma função afim ou quadrática.


### Módulo de processamento de gráficos (designer)
Este módulo deverá prover uma função para plotar o gráfico da função escolhida pelo usuário.

1. Requisito 1a

Determinar o gráfico

Função para receber o tipo de função a ser desenhada e a lista de coeficientes (se for necessário) e desenha o gráfico da função correspondente.