def linear_sum(A, n):
    if n == 1:
        return A[0]
    else:
        return linear_sum(A, n - 1) + A[n - 1]

# Exemplo de uso:
arranjo = [1, 2, 3, 4, 5]
n = 3
print(linear_sum(arranjo, n))  # Saída: 1 + 2 + 3 = 6
