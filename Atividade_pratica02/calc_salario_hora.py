# 6- Calculadora de salário por horas trabalhadas
# Leia o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora.
# Calcule o salário do funcionário e exiba o resultado formatado corretamente.
# Entrada:
# O programa recebe 2 números inteiros e 1 número com duas casas decimais.
# Saída:
# Imprima o número do funcionário e o salário calculado com duas casas decimais.

print("\n Exercício 6: Calculadora de Salário")
# Para usar com entrada do usuário, descomente as três linhas abaixo e remova as três seguintes:
# numero_funcionario = int(input("Digite o número do funcionário: "))
# horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
# valor_por_hora = float(input("Digite o valor recebido por hora: "))
numero_funcionario = 25
horas_trabalhadas = 100
valor_por_hora = 5.50

salario = horas_trabalhadas * valor_por_hora

print(f"Número do funcionário: {numero_funcionario}")
print(f"Horas trabalhadas: {horas_trabalhadas}")
print(f"Valor por hora: R$ {valor_por_hora:.2f}")
print(f"NÚMERO = {numero_funcionario}")
print(f"SALÁRIO = R$ {salario:.2f}")