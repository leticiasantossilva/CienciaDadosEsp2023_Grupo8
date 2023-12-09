# Plano de Codificação e Testes

Tendo em vista o emprego de modelagem funcional no projeto do software, a codificação será feita utilizando o paradigma de programação funcional e orientada a objetos.

Utilizaremos a linguagem Python para codificação, uma vez que a mesma mostra-se a mais adequada ao desenvolvimento ágil de aplicações de pequena escala com interface de linha de comando.

Empregaremos REPL (Read-Eval-Print Loop) Driven Development (RDD) como método de codificação, utilizando o ambiente de desenvolvimento integrado Jupyter Lab para facilitar sua adoção.

A fim de representar os pontos dentro de um sistema de eixos cartesianos necessários à plotagem de gráficos de funções, utilizaremos a biblioteca Python NumPy, Python Scipy e, para plotagem dos gráficos, a biblioteca Python MatPlotLib.


## Módulo entrada/saida - es.py

### Entrada de dados

Função leitora() -> lista com pontos

Esta função receberá do usuário os pontos desejados, estando ordenados pela coordenada X de ponto (x,y).


### 3. Saída do gráfico da curva ajustada

Função plota_curva(lista com pontos) e imprimir o gráfico

Esta função gera o gráfico com o resultado do ajuste de curva dos pontos inseridos pelo usuário. 



## Módulo de Processamento - proc.py

### Interpolação da lista de pontos

Função interp(lista com pontos) -> funções

Esta função será responsável por processar os pontos, através de interpolação, e encontrar a função que ajusta a curva.



## Módulo principal - __main__.py

### Função main()

main()
Esta é a função principal que integra as fases de entrada, processamento e saída de dados.
