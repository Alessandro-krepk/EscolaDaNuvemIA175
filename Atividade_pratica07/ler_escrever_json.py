"""
Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.
"""
import json

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
            print(dados)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def escrever_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json)
        print(f"Dados salvos em {nome_arquivo}.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo {e}.")

dados = { 
    "nome": "João",
    "idade": 25,
    "Cidade": "Recife"
}        
if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo JSON: ").strip()
    escrever_json(nome_arquivo, dados)
    ler_json(nome_arquivo)