def BinarySum(A, i, n):
    if n == 1:
        return A[i]
    else:
        meio = n // 2 # meio = 3
        print("meio:", meio, "indice:",i, "n:",n)
        return BinarySum(A, i, meio) + BinarySum(A, i + meio, n - meio)

# Exemplo de uso:
arranjo = [1, 2, 3, 4, 5, 6,7]
indice_inicial = 0
numero_elementos = len(arranjo)
print(BinarySum(arranjo, indice_inicial, numero_elementos))  # Saída: soma de todos os elementos do arranjo

