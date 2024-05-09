def bubble_sort(lista):
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(0, tamanho-i-1):
            if lista[j] > lista[j+1]:
                print("Antes da mudança", lista[j], lista[j+1])
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print("Depois da mudança", lista[j], lista[j+1])
            print("lista", lista)
    return lista

# Exemplo de uso:
minha_lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", minha_lista)
print("Lista ordenada:", bubble_sort(minha_lista))
