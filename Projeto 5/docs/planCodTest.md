# Plano de Codificação e Testes

Tendo em vista o emprego de modelagem funcional no projeto do Aplicativo de Coleta de Dados na Web, a codificação será feita utilizando o paradigma de programação funcional.

Utilizaremos a linguagem Python para codificação, uma vez que a mesma mostra-se a mais adequada ao desenvolvimento ágil de aplicações de pequena escala com interface de linha de comando.

Empregaremos REPL (Read-Eval-Print Loop) Driven Development (RDD) como método de codificação, utilizando o ambiente de desenvolvimento integrado Jupyter Lab para facilitar sua adoção.

Para atender ao requisito de baixar dados de página web, utilizaremos a biblioteca Python Requests.



## Módulo entrada/saida - es.py

### Função de entrada

Permitir que o usuário entre com o nome de uma página web.

Função leitora() -> list[pagina, dado]

Esta função receberá do usuário o endereço da página web e o tipo de dado que deve ser baixado.


### Função de saída

Abrir a página para o usuário.

Função impressora_web(arquivo_web) -> None 

Esta função deve indicar ao usuário o arquivo que armazena os dados baixados na web.


## Módulo de get web - proc.py

### Função de processamento

Baixar a página da web requerida pelo usuário.

Função get_web(pagina, dado) -> file 

Esta função que deve ler e baixar os dados na página web requerida.


## Módulo principal - __main__.py

### Função main()

main()
Esta é a função principal que integra as fases de entrada, processamento e saída de dados.

