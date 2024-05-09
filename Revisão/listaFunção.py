def busca1(item, lista):
    for i in lista:
        if i == item:
            return i
    return None

# Exemplo de uso
lista = [1, 2, 3, 4, 5]
item_busca = 2
resultado = busca1(item_busca, lista)

if resultado is not None:
    print("Item encontrado:", resultado)
else:
    print("Item", item_busca, "não encontrado na lista.")


# MODIFICADO vERSÃO 2

def busca2(item, lista):
    for indice, valor in enumerate(lista):
        if valor == item:
            return indice
    return None

# Exemplo de uso
lista = [1, 2, 3, 4, 5]
item_busca = 5
indice_encontrado = busca2(item_busca, lista)

if indice_encontrado is not None:
    print("Item", item_busca, "encontrado no índice:", indice_encontrado)
else:
    print("Item", item_busca, "não encontrado na lista.")

    
