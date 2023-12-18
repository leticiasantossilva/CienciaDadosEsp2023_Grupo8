# Plano de Codificação e Testes

Para desenvolver o projeto de aplicativo de análise de dados, utilizaremos a linguagem Python para codificação, uma vez que a mesma mostra-se a mais adequada ao desenvolvimento ágil de aplicações de pequena escala com interface de linha de comando.

Empregaremos REPL (Read-Eval-Print Loop) Driven Development (RDD) como método de codificação, utilizando o ambiente de desenvolvimento integrado Jupyter Lab para facilitar sua adoção.

Para a leitura de dados em CSV e a análise de dados, será utilizada a biblioteca Python Pandas para coletar os dados e produzir as estatísticas, assim como a biblioteca Python MatPlotLib será útil para produzir os gráficos.


## Módulo de Entrada e Saída

### Entrada de dados

Fase para solicitar ao usuário a escolha da variável do Balancete de despesa consolidado 2023 que deve ser analisada.

Função leitor_dados(url: str) -> pd.DataFrame
Esta função inicia o processamento dos dados em CSV, usando a API de dados abertos do TCE-RS

Função variavel() -> str
Esta função recebe do usuário a definição que qual variável financeira a ser analisada.

### Saída de dados

- Requisito 2 (RU2) - Plotar o gráfico dos dados

Função plotador(dados: pd.DataFrame) -> None
Esta função irá apresentar ao usuário o gráfico dos dados analisados.

Função impressora(resultados: list) -> None
Esta função irá imprimir para o usuário os resultados da média e do desvio-padrão calculados.

## Módulo de Processamento

- Requisito 1 (RU1) - Coleta de dados

Função coleta_dados(api_tce: pd.DataFrame, variavel: str) -> pd.DataFrame
Esta função irá realizar a análise dos dados da variável escolhida, usando a API de dados abertos do TCE-RS.

- Requisito 3 (RU3) - Calcular média e desvio-padrão dos dados

Função media_desv(dados: pandas.DataFrame) -> list 
Esta função irá calcular a média e o desvio-padrão da variável financeira dos dados escolhida.

