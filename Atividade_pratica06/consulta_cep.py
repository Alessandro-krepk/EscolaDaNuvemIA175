"""
Desenvolva um programa que consulte informações de endereço a partir de um
CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir
o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
"""

import requests

def consultar_endereco(cep):
    url_api = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        resposta = requests.get(url_api)
        resposta.raise_for_status()
        
        dados_endereco = resposta.json()
        
        if "erro" in dados_endereco:
            return None
        
        return dados_endereco
        
    except requests.exceptions.RequestException:
        return "erro_conexao"
    except ValueError:
        return None

# Bloco principal do programa
cep_usuario = input("Digite o CEP que deseja consultar (apenas números): ").strip()

if len(cep_usuario) == 8 and cep_usuario.isdigit():
    endereco = consultar_endereco(cep_usuario)
    
    if endereco == "erro_conexao":
        print("\nFalha ao se conectar com o serviço. Verifique sua internet.")
    elif endereco:
        print("\nEndereço encontrado:")
        print(f"  Logradouro: {endereco.get('logradouro', 'N/A')}")
        print(f"  Bairro: {endereco.get('bairro', 'N/A')}")
        print(f"  Cidade: {endereco.get('localidade', 'N/A')}")
        print(f"  Estado: {endereco.get('uf', 'N/A')}")
    else:
        print("\nCEP não encontrado ou inválido.")
else:
    print("\nFormato de CEP inválido. Por favor, digite 8 números.")