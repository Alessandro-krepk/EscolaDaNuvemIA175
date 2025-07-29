# Crie um programa que solicite a idade do usuário e classifique-o
# em uma das seguintes categorias:
# Criança (0-12 anos),
# Adolescente (13-17 anos),
# Adulto (18-59 anos)
# Idoso (60 anos ou mais).

idade = int(input("Digite a sua idade: "))

if 0 <= idade <= 12:
    classificacao = "Criança"
elif 13 <= idade <= 17:
    classificacao = "Adolescente"
elif 18 <= idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"

print(f"A sua classificação é: {classificacao}")