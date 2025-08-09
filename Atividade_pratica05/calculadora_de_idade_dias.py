"""
Crie uma função que calcule a idade de uma pessoa em dias,
baseada no ano de nascimento.
"""

from datetime import date

def calcular_idade_em_dias(ano_nascimento):
    data_hoje = date.today()
    data_nascimento = date(ano_nascimento, 1, 1)
    
    diferenca = data_hoje - data_nascimento
    
    return diferenca.days

# Exemplo de uso do programa
try:
    ano = int(input("Digite o seu ano de nascimento: "))
    
    idade_em_dias = calcular_idade_em_dias(ano)
    
    print(f"\nConsiderando o início do ano de {ano}, você viveu aproximadamente {idade_em_dias} dias.")

except ValueError:
    print("\nErro: Por favor, insira um ano válido com quatro dígitos.")
except Exception as e:
    print(f"\nOcorreu um erro: {e}")