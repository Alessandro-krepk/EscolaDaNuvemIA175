"""
Crie um programa que consulte a cotação atual de uma moeda estrangeira em
relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda
desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo
e mínimo da cotação, além da data e hora da última atualização.
Utilize a API da AwesomeAPI para obter os dados de cotação.
"""

import requests
from datetime import datetime

def consultar_cotacao(codigo_moeda):
    par_de_moedas = f"{codigo_moeda}-BRL"
    url_api = f"https://economia.awesomeapi.com.br/json/last/{par_de_moedas}"
    
    try:
        resposta = requests.get(url_api)
        resposta.raise_for_status()
        dados = resposta.json()
        
        chave_cotacao = par_de_moedas.replace('-', '')
        return dados.get(chave_cotacao)
        
    except requests.exceptions.RequestException:
        return None

# Bloco principal do programa
codigo_usuario = input("Digite o código da moeda para consulta (ex: USD, EUR, BTC): ").upper().strip()

if not codigo_usuario:
    print("\nErro: Nenhum código de moeda foi inserido.")
else:
    dados_cotacao = consultar_cotacao(codigo_usuario)

    if dados_cotacao:
        valor_atual = float(dados_cotacao['bid'])
        valor_maximo = float(dados_cotacao['high'])
        valor_minimo = float(dados_cotacao['low'])
        data_hora_str = dados_cotacao['create_date']
        
        data_hora_obj = datetime.strptime(data_hora_str, '%Y-%m-%d %H:%M:%S')
        data_formatada = data_hora_obj.strftime('%d/%m/%Y às %H:%M:%S')

        print(f"\n--- Cotação da Moeda: {dados_cotacao['name']} ---")
        print(f"Valor atual (compra): R$ {valor_atual:.4f}")
        print(f"Máximo do dia: R$ {valor_maximo:.4f}")
        print(f"Mínimo do dia: R$ {valor_minimo:.4f}")
        print(f"\nÚltima atualização: {data_formatada}")
    else:
        print(f"\nNão foi possível obter a cotação para '{codigo_usuario}'.")
        print("Verifique se o código da moeda está correto ou tente novamente mais tarde.")