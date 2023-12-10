#Teste es


# Definindo a função de entrada de dados

def leitora() -> list:
    """ Esta função recebe do usuário o endereço da página web e o tipo de dado que deve ser baixado. """
    pagina = input("Digite a página que deseja baixar. Exemplo: https://api.github.com/events \n")
    formato = input("Digite o formato que deseja os dados da webpage ('json', 'raw', 'código fonte')? ")
    return [pagina, formato]


# Definindo a função de saída de dados

def impressora_web(arquivo):
    """ Esta função salva e indica ao usuário o arquivo em que estão armazenados os dados baixados da web. """
    with open(arquivo, encoding='utf-8') as f:
        page = f.readlines()
        print(page)
        print('\n A página da web contém as informações acima e foi salva no arquivo pagina.txt')
    
    