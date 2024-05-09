#  Escreva um programa Python para combinar valores em uma lista de dicionários.
# Dados de amostra: [{'item': 'item1', 'preco': 400}, {'item': 'item2', 'preco': 300}, {'item': 'item1', 'preco': 750}]
# Saída esperada: {'item1': 1150, 'item2': 300}

dados = [{'item': 'item1', 'preço': 200}, {'item': 'item2', 'preço': 300}, {'item': 'item1', 'preço': 200}]

soma_items = {}

for dicionario in dados:
    item = dicionario['item']
    preço = dicionario['preço']
    if item in soma_items:
        soma_items[item] += preço
    else:
        soma_items[item] = preço

print(soma_items)
