"""
================================================================================
Exercício: Sistema de Registro de Notas e Cálculo de Média
================================================================================
Crie um programa que permita a um professor registrar as notas de uma turma.

Especificações:
1. O programa deve solicitar notas continuamente.
2. O loop de solicitação deve parar quando o professor digitar 'fim'.
3. As notas válidas devem estar no intervalo de 0 a 10.
4. O programa deve ignorar notas inválidas (fora do intervalo 0-10 ou
   entradas não numéricas) e continuar solicitando a próxima nota.
5. Ao final, o programa deve exibir a média das notas válidas da turma,
   formatada com duas casas decimais.
================================================================================
"""
notas_validas = []

print("--- Sistema de Registro de Notas ---")
print("Digite as notas dos alunos. Digite 'fim' para encerrar e calcular a média.")

while True:
    entrada = input("Digite uma nota (ou 'fim'): ")

    if entrada.lower() == 'fim':
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas_validas.append(nota)
            print(f"Nota {nota:.1f} registrada com sucesso.")
        else:
            print("Erro: A nota deve estar entre 0 e 10. Tente novamente.")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número ou 'fim'.")

if len(notas_validas) > 0:
    media = sum(notas_validas) / len(notas_validas)
    print("\n-------------------------------------")
    print(f"Total de notas válidas inseridas: {len(notas_validas)}")
    print(f"A média da turma é: {media:.2f}")
    print("-------------------------------------")
else:
    print("\nNenhuma nota válida foi inserida. O cálculo da média não pôde ser realizado.")