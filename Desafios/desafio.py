def maximo_da_lista(lista):
    if not lista:
        return None
    maximo = lista[0]
    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
    return maximo

# Exemplo de uso
minha_lista = [10, 30, 20, 50, 40]
resultado = maximo_da_lista(minha_lista)
print(resultado)  # Saída: 50
