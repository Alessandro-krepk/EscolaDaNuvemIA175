"""
================================================================================
Exercício: Verificador de Força de Senha
================================================================================
Crie um programa que verifique se uma senha fornecida pelo usuário é forte.

Especificações:
1. Uma senha forte deve atender aos seguintes critérios:
   - Ter no mínimo 8 caracteres de comprimento.
   - Conter pelo menos um número.
2. O programa deve continuar pedindo uma senha até que uma válida seja
   inserida pelo usuário.
3. O usuário pode digitar 'sair' a qualquer momento para encerrar o programa.
4. O programa deve informar ao usuário o motivo pelo qual a senha é fraca.
5. Ao inserir uma senha forte, o programa deve confirmar e encerrar.
================================================================================
"""
while True:
    senha = input("Crie uma senha (ou digite 'sair' para encerrar): ")

    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break

    if len(senha) < 8:
        print("Senha fraca: A senha deve ter no mínimo 8 caracteres.")
        continue

    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
            break

    if not tem_numero:
        print("Senha fraca: A senha deve conter pelo menos um número.")
        continue

    print("\nSenha forte criada com sucesso!")
    break
