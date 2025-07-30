"""
================================================================================
Exercício: Contador Interativo de Números Pares e Ímpares
================================================================================
Crie um programa que solicite ao usuário a inserção de números inteiros.

Especificações:
1. O programa deve continuar solicitando números até que o usuário digite 'fim'.
2. Para cada número inteiro inserido, o programa deve informar se ele é
   par ou ímpar.
3. Se o usuário inserir algo que não seja um número inteiro (ex: texto ou
   número decimal), o programa deve informar o erro e continuar para a
   próxima solicitação sem travar.
4. Ao final (quando o usuário digitar 'fim'), o programa deve exibir a
   quantidade total de números pares e ímpares que foram inseridos.
================================================================================
"""
contador_pares = 0
contador_impares = 0

print("--- Contador de Pares e Ímpares ---")
print("Digite números inteiros. Para finalizar, digite 'fim'.")

while True:
    entrada = input("\nDigite um número inteiro: ")

    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print(f"O número {numero} é PAR.")
            contador_pares += 1
        else:
            print(f"O número {numero} é ÍMPAR.")
            contador_impares += 1

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um NÚMERO INTEIRO ou 'fim'.")

print("\n======================================")
print("Programa finalizado. Resumo:")
print(f"Total de números pares inseridos: {contador_pares}")
print(f"Total de números ímpares inseridos: {contador_impares}")
print("======================================")