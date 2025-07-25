"""
Desenvolva um programa que calcule o preço total de uma compra. 
Use as seguintes informações:
Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 
"""
nome_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3

preco_total = preco_unitario * quantidade

print("Produto:", nome_produto)
print("Preço unitário: R$", preco_unitario)
print("Quantidade:", quantidade)
print("Preço total: R$", round(preco_total, 2))
