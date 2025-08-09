"""
Crie um programa que receba o preço original de um produto e um
percentual de desconto, realizando o cálculo do preço final após a
aplicação do desconto.

Requisitos:
- Permitir que o usuário informe o preço do produto e o percentual de desconto.
- Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
- Exibir o preço final com duas casas decimais para garantir precisão.

Entrada esperada:
preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).
"""

def calcular_preco_final(preco_original, percentual_desconto):
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_com_desconto = preco_original - valor_desconto
    return preco_com_desconto

try:
    preco_produto = float(input("Digite o preço original do produto: R$ "))
    desconto_percentual = float(input("Digite o percentual de desconto (%): "))

    preco_final = calcular_preco_final(preco_produto, desconto_percentual)
    
    print(f"\nO preço final do produto com {desconto_percentual}% de desconto é: R$ {preco_final:.2f}")

except ValueError:
    print("\nErro: Por favor, insira valores numéricos válidos.")