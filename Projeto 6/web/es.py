

def leitor_web():
    endereco_web = input('Informe o endereço da página (Ex: http://pythonscraping.com/pages/page1.html): ')
    tag = input('Informe o que deseja extrair (Exemplo: title, head, body, etc.): ')
    return [endereco_web, tag]

def saida(soup, tag):
    print(f'O {tag} da página é: \n{soup.find_all(tag)}')