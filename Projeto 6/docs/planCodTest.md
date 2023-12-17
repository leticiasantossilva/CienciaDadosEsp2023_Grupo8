# Plano de Codificação e Testes


Para desenvolver o projeto de aplicativo de extração de dados em texto, utilizaremos a linguagem Python para codificação, uma vez que a mesma mostra-se a mais adequada ao desenvolvimento ágil de aplicações de pequena escala com interface de linha de comando.

Empregaremos REPL (Read-Eval-Print Loop) Driven Development (RDD) como método de codificação, utilizando o ambiente de desenvolvimento integrado Jupyter Lab para facilitar sua adoção.

Para atender ao requisito de baixar uma página web, utilizaremos a biblioteca Python Requests, já para extrair o texto, será usada a biblioteca Python BeautifulSoup4.


## Módulo de Entrada e Saída

### Entrada de dados

Fase para solicitar ao usuário os dados necessários para atender aos requisito 1, 2 e 3:

Função leitor() -> list
Esta função receberá o link da página, a tag html e a plavra-chave a ser buscada

### Saída de dados

Fase para imprimir ao usuário os resultados do scraping da página.

Função saida(soup, tag: str, palavra_chave: str, contagem: int) -> None
Esta função irá imprimir na tela do usuário o resultado da tag buscada e o resultado de quantas vezes a palavra-chave foi encontrada.

## Módulo de Processamento de dados

#### Requisito 1

Baixar a página web em html

Função leitor_web(endereco_web: str) -> str
Esta função utiliza a biblioteca Requests para baixar a página html escolhida pelo usuário.

#### Requisito 2
Buscar no html a tag desejada (como o título)

Será utilizada a bibliteca BeautifulSoup4 para rastrear a presença da tag no html.

#### Requisito 3
Informar quantas vezes uma palavra-chave foi encontrada

Também será utilizada a bibliteca BeautifulSoup4 para rastrear a palavra-chave e contabilizar quantas vezes ela aparece na página.


Juntando os três processos que atendem aos requisitos, apresenta-se a função de extração dos dados em html:

Função extrator(pagina_web: str, tag: str, palavra_chave: str) -> list
Esta função irá extrair da pagina html a tag e a palavra-chave desejada.
  

