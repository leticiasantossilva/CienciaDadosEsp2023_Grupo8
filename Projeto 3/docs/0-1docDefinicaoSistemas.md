# Documento de Definição de Sistemas

Este documento organiza as definições de sistemas baseadas nos requisitos de desenvolvimento do projeto de Aplicativo.


### Módulo de Entrada/Saída (es)
O módulo de entrada/saída (es) deverá prover as seguintes funções:

1. Requisito 1b
Plotar o gráfico

função impressora(grafico: objeto gráfico) -> null
Esta função imprime na tela o gráfico da função escolhida pelo usuário. 

2. Requisito 2
Deve haver um menu com as quatro funções capazes de serem plotadas pelo aplicativo.

função leitor_funcao() -> string
Imprime um menu na tela contendo as funções afim, quadrática, logarítmica e exponencial para o usuário escolher qual delas plotar.

3. Requisito 3

Caso o usuário escolha a função afim, na sequência, ele deverá poder informar os coeficientes da função.


função leitor_coeficiente(nome_funcao: string) -> lista 
Lê os coeficientes no caso de o usuário escolher plotar uma função afim ou quadrática.

3. Requisito 4

Idêntico ao requisito 2, mas sendo válido para função quadrática.

função leitor_coeficiente(nome_funcao: string) -> lista 
Lê os coeficientes no caso de o usuário escolher plotar uma função afim ou quadrática.



### Módulo de processamento de gráficos (designer)
Este módulo deverá prover uma função para plotar o gráfico da função escolhida pelo usuário.

1. Requisito 1a

Determinar o gráfico

função design(tipo_funcao: str, coeficientes: lista) -> objeto gráfico
Esta função recebe o tipo de função a ser desenhada e a lista de coeficientes (se for necessário) e desenha o gráfico da função correspondente.