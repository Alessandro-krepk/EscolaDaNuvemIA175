"""
Crie um programa que gera uma senha aleatória com o módulo random,
utilizando caracteres especiais, possibilitando o usuário a informar
a quantidade de caracteres dessa senha aleatória.
"""

import random
import string

def gerar_senha(tamanho):
    letras = string.ascii_letters
    numeros = string.digits
    caracteres_especiais = string.punctuation
    
    todos_os_caracteres = letras + numeros + caracteres_especiais
    
    senha_gerada = "".join(random.choices(todos_os_caracteres, k=tamanho))
    
    return senha_gerada

# Exemplo de uso do programa
try:
    quantidade_caracteres = int(input("Digite a quantidade de caracteres para a senha: "))

    if quantidade_caracteres > 0:
        senha_aleatoria = gerar_senha(quantidade_caracteres)
        print(f"\nSua senha aleatória é: {senha_aleatoria}")
    else:
        print("\nPor favor, insira um número maior que zero.")

except ValueError:
    print("\nErro: Por favor, insira um número inteiro válido.")