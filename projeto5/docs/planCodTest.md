# Plano de Codificação e Testes

Tendo em vista o emprego de modelagem funcional no projeto do software, a codificação será feita utilizando o paradigma de programação funcional.

Utilizaremos a linguagem Python para codificação, uma vez que a mesma mostra-se a mais adequada ao desenvolvimento ágil de aplicações de pequena escala com interface de linha de comando.

Empregaremos REPL (Read-Eval-Print Loop) Driven Development (RDD) como método de codificação, utilizando o ambiente de desenvolvimento integrado Jupyter Lab para facilitar sua adoção.

Em um segundo momento, isto é, após a codificação com RDD, procede-se à escrita de testes unitários automatizados, usando a ferramenta pytest, para prover ainda mais segurança a respeito da correção do código.

Para atender ao requisito de baixar uma página web, utilizaremos a biblioteca Python Requests.



## Módulo entrada/saida - es.py

### Requisito 1

Permitir que o usuário entre com o nome de uma página web.

Função leitor_pagina(nome_pagina) -> str



### Requisitos 3

Abrir a página para o usuário.

Função impressora_web(nome_pagina) -> None 



## Módulo de interpolação

### Requisito 2

Baixar a página da web requerida pelo usuário.

Função get_web(nome_pagina) -> file 

