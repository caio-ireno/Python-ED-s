def algoritmo_a(n):
    s = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            s = s + 1
    return s

resultado = algoritmo_a(10)
print("A soma dos 10 primeiros números inteiros é ", resultado)