def algoritmo_b(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s

resultado = algoritmo_b(10)
print("A soma dos 10 primeiros números inteiros é ", resultado)
