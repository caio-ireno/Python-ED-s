def merge(lst, inicio, meio, fim):
    aux = []
    i = inicio
    j = meio + 1
    while (i <= meio and j <= fim):
        if (lst[i] <= lst[j]):
            aux.append(lst[i])
            i += 1
        else:
            aux.append(lst[j])
            j += 1
    while (i <= meio):
        aux.append(lst[i])
        i += 1
    while (j <= fim):
        aux.append(lst[j])
        j += 1
    i = inicio
    for elemento in aux:
        lst[i] = elemento
        i += 1


def mergeSort(lst, inicio, fim):
    if (inicio < fim):
        meio = (inicio + fim) // 2
        mergeSort(lst, inicio, meio)
        mergeSort(lst, meio + 1, fim)
        merge(lst, inicio, meio, fim)
    return lst

lista = [8, 7, 6, 5, 4, 3, 2, 1]
final = len(lista) - 1
resultado = mergeSort(lista, 0, final)
print(resultado)
