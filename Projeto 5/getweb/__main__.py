"""
Módulo Principal
Descrição: Este é o módulo com a função principal que integra as fases de entrada, processamento e saída de dados do Aplicativo de Coleta de Dados na Web.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 06/12/2023

"""

# Importação dos módulos

import es
import proc

# Definindo a função main do aplicativo de Coleta de Dados na Web

def main():
    """Esta é a função principal que integra as fases de entrada, processamento e saída de dados"""
    # Leitura de dados
    dados = es.leitora()
    # Processamento de dados
    arquivo = proc.get_web(dados)
    # Saída de dados
    pagina = es.impressora_web(arquivo)
    
            
if __name__ == "__main__":
    main()
    