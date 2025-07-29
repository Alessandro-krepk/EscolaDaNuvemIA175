# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Digite a unidade de origem (Celsius, Fahrenheit, Kelvin): ").upper()
unidade_destino = input("Digite a unidade de destino (Celsius, Fahrenheit, Kelvin): ").upper()

# Converter para Celsius primeiro
if unidade_origem == "FAHRENHEIT":
    temp_celsius = (temperatura - 32) * 5/9
elif unidade_origem == "KELVIN":
    temp_celsius = temperatura - 273.15
else: # se for Celsius, não faz nada
    temp_celsius = temperatura

# Converter de Celsius para a unidade de destino
if unidade_destino == "FAHRENHEIT":
    resultado = (temp_celsius * 9/5) + 32
elif unidade_destino == "KELVIN":
    resultado = temp_celsius + 273.15
else: # se o destino for Celsius
    resultado = temp_celsius

print(f"{temperatura:.2f} {unidade_origem} é igual a {resultado:.2f} {unidade_destino}")