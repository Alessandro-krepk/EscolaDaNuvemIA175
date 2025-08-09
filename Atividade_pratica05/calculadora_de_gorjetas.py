"""
Crie uma função que calcule a gorjeta a ser deixada em um restaurante,
baseada no valor total da conta e na porcentagem de gorjeta desejada.

Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
    valor_conta (float): O valor total da conta.
    porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%).
Retorna:
    float: O valor da gorjeta calculada.
"""

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return valor_gorjeta

# Exemplo de uso da função
valor_da_conta = 100.0
porcentagem_da_gorjeta = 15

gorjeta_calculada = calcular_gorjeta(valor_da_conta, porcentagem_da_gorjeta)

print(f"O valor da conta é R$ {valor_da_conta:.2f}")
print(f"A gorjeta é de {porcentagem_da_gorjeta}%")
print(f"O valor da gorjeta a ser pago é R$ {gorjeta_calculada:.2f}")