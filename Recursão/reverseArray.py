def reverse_array(A, i, j):
    if i < j:
        A[i], A[j] = A[j], A[i]  # Inverte os elementos A[i] e A[j]
        reverse_array(A, i + 1, j - 1)

# Exemplo de uso:
arranjo = [1, 2, 3, 4, 5]
reverse_array(arranjo, 0, len(arranjo) - 1)
print(arranjo)  # Saída: [5, 4, 3, 2, 1]
