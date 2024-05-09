def selection_sort(lista):
    tamanho = len(lista)
    for i in range(tamanho-1):
        indice_menor = i
        for j in range(i+1, tamanho):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        if indice_menor != i:
            lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
           


    return lista

# Exemplo de uso:
minha_lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", minha_lista)
print("Lista ordenada:", selection_sort(minha_lista))
