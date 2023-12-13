"""
Módulo Principal

#ALTERAR
Descrição: Este é o módulo com a função principal que integra as fases de entrada, processamento e saída de dados do Aplicativo de Plotagem.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 04/12/2023

"""

import es
import proc

def main():
    endereco_web = es.leitor_web()
    pagina_web = proc.leitor_web(endereco_web[0])
    dados = proc.extrator(pagina_web)
    es.saida(dados, endereco_web[1])
    
if __name__ == "__main__":
    main()
    
    