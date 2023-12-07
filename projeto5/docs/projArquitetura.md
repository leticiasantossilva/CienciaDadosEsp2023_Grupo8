# Projeto de arquitetura


O projeto de desenvolvimento do aplicativo capaz de ler e abrir uma página web, contará com os seguintes módulos:

### Módulo de entrada e saida

Este módulo oferece duas funções, sendo uma para atender ao requisito 1 e outra para o requisito 3. 

Na entrada, deve haver uma função que solicita ao usuário a inserção do nome da página web desejada. A função terá a seguinte assinatura:

1. função leitor_pagina(nome_pagina) -> str


Na fase de saída, deve haver uma função que imprime para o usuário a página web requerida. A função terá a seguinte assinatura:
2. função impressora_web(nome_pagina) -> None


### Módulo de baixar página web

Para atender ao requisito 2, o módulo prevê uma função capaz de baixar página web com a seguinte assinatura:

função get_web(nome_pagina) -> file


## Desenho do projeto

É possível ver o desenho dessa arquitetura em png.:

![Desenho da Arquitetura](arquitetura.png) <!--- Imagem ainda não foi alterada!! --->



