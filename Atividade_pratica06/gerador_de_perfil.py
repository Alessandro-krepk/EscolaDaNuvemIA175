"""
Crie um programa que gera um perfil de usuário aleatório usando a
API 'Random User Generator'. O programa deve exibir o nome, email
e país do usuário gerado.
"""

import requests

def gerar_perfil_aleatorio():
    url_api = "https://randomuser.me/api/"
    
    try:
        resposta = requests.get(url_api)
        resposta.raise_for_status()
        
        dados = resposta.json()
        usuario = dados["results"][0]
        
        titulo = usuario["name"]["title"]
        primeiro_nome = usuario["name"]["first"]
        ultimo_nome = usuario["name"]["last"]
        nome_completo = f"{titulo} {primeiro_nome} {ultimo_nome}"
        
        email = usuario["email"]
        pais = usuario["location"]["country"]
        
        print("Perfil de Usuário Gerado:")
        print(f"  Nome: {nome_completo}")
        print(f"  Email: {email}")
        print(f"  País: {pais}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao se conectar com a API: {e}")
    except (KeyError, IndexError):
        print("Erro: Não foi possível processar os dados recebidos da API.")


gerar_perfil_aleatorio()