"""
================================================================================
Exercício: Calculadora Robusta com Tratamento de Erros
================================================================================
Desenvolva uma calculadora em Python que realize as quatro operações básicas
(adição, subtração, multiplicação e divisão) entre dois números.

A calculadora deve ser capaz de lidar com diversos tipos de erros de
entrada e operação.

Especificações:
1. Solicitar ao usuário que insira dois números e uma operação.
2. As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
3. O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
4. Tratar os seguintes erros com try/except:
   - Entrada inválida (não numérica) para os números.
   - Divisão por zero.
   - Operação inválida.
5. Após cada erro, o programa deve informar o usuário sobre o problema e
   solicitar a entrada novamente.
6. Quando uma operação é concluída com sucesso, o programa deve exibir o
   resultado e encerrar.
================================================================================
"""
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))

        operacao = input("Digite a operação (+, -, *, /): ")

        num2 = float(input("Digite o segundo número: "))

        resultado = 0

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida. Use apenas +, -, * ou /.")

        print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")
        break

    except ValueError as e:
        print(f"\nErro de entrada: {e}. Por favor, tente novamente.\n")

    except ZeroDivisionError:
        print("\nErro: Não é possível dividir por zero. Por favor, tente novamente.\n")

    except Exception as e:
        print(f"\nOcorreu um erro: {e}. Por favor, tente novamente.\n")