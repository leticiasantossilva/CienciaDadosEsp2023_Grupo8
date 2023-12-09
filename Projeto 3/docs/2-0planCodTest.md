# Plano de Codificação e Testes

Tendo em vista o emprego de modelagem funcional no projeto do software, a codificação será feita utilizando o paradigma de programação funcional e orientada a objetos.

Utilizaremos a linguagem Python para codificação, uma vez que a mesma mostra-se a mais adequada ao desenvolvimento ágil de aplicações de pequena escala com interface de linha de comando.

Empregaremos "REPL-driven development" como método de codificação, utilizando o ambiente de desenvolvimento integrado Jupyter Lab para facilitar sua adoção.

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

Caso o usuário escolha a função afim ou função quadrática, na sequência, ele deverá poder informar os coeficientes da função.

função leitor_coeficiente(nome_funcao: string) -> lista
Lê os coeficientes no caso de o usuário escolher plotar uma função afim ou quadrática.


## Módulo de processamento de gráficos (designer)

Este módulo deverá prover uma função para plotar o gráfico da função escolhida pelo usuário.

### 1. Requisito 1a

Determinar o gráfico a ser produzido

Estas funções processam o tipo de função a ser desenhada e a lista de coeficientes (se for necessário):
1. Quadrática:
função quadratica(intervalo: lista, coef: lista) -> lista

2. Afim
função afim(intervalo: lista, coef: lista) -> lista

3. Logarítmica
função logar(intervalo: lista) -> lista

4. Exponencial
função exp(intervalo: lista) -> lista



## Módulo principal

### Integra operações e gráfico

função ope(operacao: str) -> list:
Esta função integra os dados inseridos pelo usuário gerando atributos necessários para a impressora() desenhar o gráfico da função correspondente.


### Função main()

main()
Esta é a função principal que integra as fases de entrada, processamento e saída de dados.
