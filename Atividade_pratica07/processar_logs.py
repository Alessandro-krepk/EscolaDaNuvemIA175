"""
Leia um arquivo que contenha dados de log de treinamento de modelos de
Machine Learning. Calcule a média e o desvio padrão do tempo de
execução constantes.
"""
import pandas as pd

def processar_logs_treinamento(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        media_tempo = df['tempo_execucao'].mean()
        desvio_padrao_tempo = df['tempo_execucao'].std()
        print(f"Média do tempo de execução: {media_tempo:.2f} segundos.")
        print(f"Desvio Padrão do tempo de execução: {desvio_padrao_tempo:.2f} segundos.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print("Erro ao processar o arquivo: {e}")

nome_arquivo = input("Digite o nome do arquivo de log: ")

processar_logs_treinamento(nome_arquivo)