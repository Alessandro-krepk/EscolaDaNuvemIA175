"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo
(lê-se igual de trás para frente, ignorando espaços e pontuação).
Se o resultado é True, responda “Sim”, se o resultado for False,
responda “Não”.
"""

def eh_palindromo(frase):
    texto_limpo = "".join(caractere.lower() for caractere in frase if caractere.isalnum())
    
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

# Exemplo de uso da função
frase1 = "Anotaram a data da maratona"
frase2 = "python"
palavra1 = "radar"
palavra2 = "reviver"

print(f"'{frase1}' é um palíndromo? {eh_palindromo(frase1)}")
print(f"'{frase2}' é um palíndromo? {eh_palindromo(frase2)}")
print(f"'{palavra1}' é um palíndromo? {eh_palindromo(palavra1)}")
print(f"'{palavra2}' é um palíndromo? {eh_palindromo(palavra2)}")