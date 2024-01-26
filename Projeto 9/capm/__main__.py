"""
Módulo Principal

Descrição: Este é o módulo com a função principal que integra as fases de entrada, processamento e saída de dados do  aplicativo que coleta automaticamente dados da web e estima o modelo CAPM para ações na B3.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 13/12/2023

"""


# Importação dos módulos

import es
import proc


# Função principal
   
def main():
    """ Esta é a função que integra as fases de entrada, processamento e saída de dados  """
    
    # Dados do ativo livre de risco
    cdi = es.leitor_taxa()
    
    # Dados de mercado
    ibov = es.leitor_indice()
    
    # Leitura de local de gravação
    pasta = es.leitor_pasta()

    # Dados das ações
    acoes = es.leitor_acoes()
    
    for item in acoes:
        acao = es.leitor_precos(item)   
    # Estimando modelo
        results = proc.estima_modelo(acao, ibov, cdi)
    # saída de dados
        alfa = float(results.params[0])
        beta = float(results.params[1])
        sigma = float(results.resid.std())    
        es.grava_csv(pasta, item, alfa, beta, sigma)
    

    
# Executando a função do aplicativo
if __name__ == "__main__":
    main()
    