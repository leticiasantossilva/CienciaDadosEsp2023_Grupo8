"""
Módulo de Entrada e Saída

Descrição: Este é o módulo com a funções necessárias para a entrada e a saída de dados do Aplicativo de extração de dados em texto.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 07/12/2023

"""

# Função de entrada de dados

def leitor() -> list:
    """ Esta função recebe o link da página, a tag html e a plavra-chave a ser buscada """
    endereco_web = input('Informe o endereço da página (Ex: http://pythonscraping.com/pages/page1.html): ')
    tag = input('Informe o que deseja extrair (Exemplo: title, head, body, etc.): ')
    palavra_chave = input('Informe a palavra-chave que deseja procurar: ')
    return [endereco_web, tag, palavra_chave]


# Função de saída de dados

def saida(soup, tag: str, keyword: str, contagem: int) -> None:
    """ Esta é a função que imprime os resultados do scrapper """
    print(f'O {tag} da página é: \n{soup.find_all(tag)}')
    print(f'A palavra-chave "{keyword}" foi encontrada {contagem} vezes.')