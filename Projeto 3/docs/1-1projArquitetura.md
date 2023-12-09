## Projeto de arquitetura

O Aplicativo de Plotagem de Gráficos terá os seguintes módulos:
1. módulo de entrada e saída de dados (requisitos 1b, 2, 3 e 4)
2. módulo de processamento de gráficos (requisito 1a)
3. módulo main


### Módulo de Entrada/Saída (es)
O módulo de entrada/saída (es) deverá prover as seguintes funções:

1. 1b - Plotar o gráfico

função impressora(grafico: objeto gráfico) -> null
Esta função imprime na tela o gráfico da função escolhida pelo usuário. 

2. Menu com as quatro funções a serem plotadas

função leitor_operacao() -> string
Imprime um menu na tela contendo as funções afim, quadrática, logarítmica e exponencial para o usuário escolher qual delas plotar.

3. Inserir coeficientes da função afim e quadrática

função leitor_coeficiente(nome_funcao: string) -> lista 
Lê os coeficientes no caso de o usuário escolher plotar uma função afim ou quadrática.

4. Inserir o intervalo de X no gráfico

função leitora_int() -> list
Lê o intervalo de x a ser apresentado no gráfico.


### Módulo de processamento de gráficos (designer)
Este módulo deverá prover uma função para plotar o gráfico da função escolhida pelo usuário.

1. 1a - Determinar o gráfico

função design(tipo_funcao: str, coeficientes: lista) -> objeto gráfico
Esta função recebe o tipo de função a ser desenhada e a lista de coeficientes (se for necessário) e desenha o gráfico da função correspondente.

### Módulo principal
Este é o módulo com a função principal que integra as fases de entrada, processamento e saída de dados.


## Desenho do projeto

É possível ver o desenho dessa arquitetura em png.:

![Desenho da Arquitetura](arquitetura.png)
