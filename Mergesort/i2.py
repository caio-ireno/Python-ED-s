def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Dividir a lista ao meio
    meio = len(arr) // 2
    metade_esquerda = arr[:meio]
    metade_direita = arr[meio:]
    
    # Ordenar recursivamente cada metade
    metade_esquerda = merge_sort(metade_esquerda)
    metade_direita = merge_sort(metade_direita)
    
    # Combinação das metades ordenadas
    return merge(metade_esquerda, metade_direita)

def merge(left, right):
    merged = []
    index_esquerdo, index_direito = 0, 0
    
    while index_esquerdo < len(left) and index_direito < len(right):
        if left[index_esquerdo] < right[index_direito]:
            merged.append(left[index_esquerdo])
            index_esquerdo += 1
        else:
            merged.append(right[index_direito])
            index_direito += 1
    
    # Adiciona os elementos restantes de left e right
    merged.extend(left[index_esquerdo:])
    merged.extend(right[index_direito:])
    
    return merged

def concat(arr1,arr2):
    for i in arr1:
        arr2.append(i)
    return arr2

# Sequência inicial
arr1 = [3, 4, 9, 2, 5, 1, 8]
arr2 = [88,0,2,55,40,100]
arrConcat = concat(arr1,arr2)
print(arrConcat)

print("Sequência inicial:", arrConcat)

# Ordenar a sequência utilizando Merge Sort
sorted_arr = merge_sort(arrConcat)
print("Sequência ordenada:", sorted_arr)
