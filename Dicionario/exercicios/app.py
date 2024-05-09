# Escreva um programa que leia uma frase e calcula a frequência relativa de cada letra em uma frase, usando dicionários. Ignore caracteres brancos e pontuação.

# Modifique o programa abaixo para que a frase seja digitada pelo usuário e para que imprima apenas as letras com frequência maior que 2.

IGNORE = ' .,;:?!\t\n'

def main1():
    frase = "the quick brown fox jumps over the lazy dog"
    letra = {}

    for c in frase:
        if c not in IGNORE:
            if c in letra:
                letra[c] += 1
            else:
                letra[c] = 1

    print(letra)

#main1()


IGNORE = ' .,;:?!\t\n'

def main2():
    frase = input("Digite uma frase: ")
    letra = {}
    for c in frase:
        if c not in IGNORE:
            if c in letra:
                letra[c] += 1
            else:
                letra[c] = 1

    for chave, valor in letra.items():
        if valor > 2:
            print(f"A letra '{chave}' aparece {valor} vezes na frase.")
        else:
            print("nenhuma letra maior do que 2")

main2()
